#!/bin/bash
# Check whether the installed PHP 5.x packages carry the php2shell-eol-backport
# fixes (EL6 / EL7): CVE-2026-109618 / CVE-2026-109619 since .php2shell.1,
# CVE-2026-126714 (phpAfterShell) since .php2shell.2, the other applicable issues of
# 19 Nov 2026 (CVE-2026-129496, -128064, -128090, -129292, -129538, -15353) since .php2shell.3.
#
# Exit status: 0 = fixed (or no PHP 5.x installed), 1 = vulnerable package found,
#              2 = fixed, but a running process still uses the old code,
#              3 = an older .php2shell.N release is installed: some fixes are missing.
status=0
outdated=0
# CVEs fixed after release 1, in release order
later_fixes="CVE-2026-126714:phpAfterShell CVE-2026-129496:timezone-cache CVE-2026-128064:https-case
CVE-2026-128090:phar-signature CVE-2026-129292:fpm-status-xss CVE-2026-129538:cgi-path-info CVE-2026-15353:soap-array"

pkgs=$(rpm -qa --qf '%{NAME} %{VERSION}-%{RELEASE} %{SOURCERPM}\n' | awk '$3 ~ /^php-5\./')
if [ -z "$pkgs" ]; then
    echo "No PHP 5.x packages installed."
    exit 0
fi

while read -r name vr _; do
    changelog=$(rpm -q --changelog "$name")
    if echo "$changelog" | grep -q 'CVE-2026-109618'; then
        missing=""
        for f in $later_fixes; do
            echo "$changelog" | grep -q "${f%%:*}" || missing="$missing, ${f#*:} (${f%%:*})"
        done
        if [ -z "$missing" ]; then
            echo "FIXED       $name-$vr"
        else
            echo "OUTDATED    $name-$vr: not fixed: ${missing#, }; update to the latest .php2shell.N"
            outdated=1
        fi
    else
        echo "VULNERABLE  $name-$vr"
        status=1
    fi
done <<EOF
$pkgs
EOF

# The fix adds a new php.ini directive, which the CLI can report.
if command -v php >/dev/null 2>&1; then
    if php -n -r 'exit(ini_get("max_multipart_body_parts") === false ? 1 : 0);'; then
        echo "php CLI:    fixed code is loaded (max_multipart_body_parts is known)"
    else
        echo "php CLI:    old code (max_multipart_body_parts is unknown)"
        status=1
    fi
fi

# Long-running processes keep the code they started with: a process that still
# maps a replaced (deleted) PHP file runs the old code. This finds every such
# process (mod_php in any httpd instance, php-fpm, php-cgi, PHP CLI daemons),
# but reading the memory maps of other users' processes needs root.
# rpm renames a replaced file before it removes it, so the map shows a suffix,
# for example "/usr/lib64/httpd/modules/libphp5.so;6adb7398 (deleted)".
if [ "$status" -eq 0 ]; then
    if [ "$(id -u)" -ne 0 ]; then
        echo "NOTE        run as root to check running processes (httpd, php-fpm, ...)"
    else
        pids=$(grep -lE '(/libphp5[^ ]*|/usr/lib(64)?/php/[^ ]*|/usr/bin/php[^ /]*|/usr/sbin/php-fpm[^ /]*) \(deleted\)$' \
               /proc/[0-9]*/maps 2>/dev/null | cut -d/ -f3 | sort -n)
        if [ -n "$pids" ]; then
            # shellcheck disable=SC2086
            ps -o comm= -p "$(echo $pids | tr ' ' ',')" | sort | uniq -c | while read -r n comm; do
                echo "RESTART     $comm: $n process(es) still run the replaced PHP code, restart the service"
            done
            status=2
        fi
    fi
fi

if [ "$status" -eq 0 ] && [ "$outdated" -eq 1 ]; then
    status=3
fi
exit $status

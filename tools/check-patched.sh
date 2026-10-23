#!/bin/bash
# Check whether the installed PHP 5.x packages carry the php2shell-eol-backport
# fix for CVE-2026-109618 / CVE-2026-109619 (EL6 / EL7).
#
# Exit status: 0 = fixed (or no PHP 5.x installed), 1 = vulnerable package found,
#              2 = fixed, but a running process still uses the old code.
status=0

pkgs=$(rpm -qa --qf '%{NAME} %{VERSION}-%{RELEASE} %{SOURCERPM}\n' | awk '$3 ~ /^php-5\./')
if [ -z "$pkgs" ]; then
    echo "No PHP 5.x packages installed."
    exit 0
fi

while read -r name vr _; do
    if rpm -q --changelog "$name" | grep -q 'CVE-2026-109618'; then
        echo "FIXED       $name-$vr"
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
if [ "$status" -eq 0 ]; then
    if [ "$(id -u)" -ne 0 ]; then
        echo "NOTE        run as root to check running processes (httpd, php-fpm, ...)"
    else
        pids=$(grep -lE '(libphp5[^ ]*\.so|/usr/lib(64)?/php/|/usr/bin/php[^ /]*|/usr/sbin/php-fpm) \(deleted\)$' \
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

exit $status

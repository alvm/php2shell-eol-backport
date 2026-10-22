#!/bin/bash
# Check whether the installed PHP 5.x packages carry the php2shell-eol-backport
# fix for CVE-2026-109618 / CVE-2026-109619 (EL6 / EL7).
#
# Exit status: 0 = fixed (or no PHP 5.x installed), 1 = vulnerable package found,
#              2 = fixed, but a running httpd / php-fpm still uses the old code.
status=0

pkgs=$(rpm -qa --qf '%{NAME} %{VERSION}-%{RELEASE} %{SOURCERPM} %{INSTALLTIME}\n' | awk '$3 ~ /^php-5\./')
if [ -z "$pkgs" ]; then
    echo "No PHP 5.x packages installed."
    exit 0
fi

newest_install=0
while read -r name vr _ installtime; do
    if rpm -q --changelog "$name" | grep -q 'CVE-2026-109618'; then
        echo "FIXED       $name-$vr"
    else
        echo "VULNERABLE  $name-$vr"
        status=1
    fi
    [ "$installtime" -gt "$newest_install" ] && newest_install=$installtime
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

# Long-running processes keep the code they started with.
if [ "$status" -eq 0 ]; then
    for proc in httpd php-fpm; do
        for pid in $(pidof "$proc" 2>/dev/null); do
            started=$(date -d "$(ps -o lstart= -p "$pid")" +%s 2>/dev/null) || continue
            if [ "$started" -lt "$newest_install" ]; then
                echo "RESTART     $proc (pid $pid) was started before the update: restart it"
                status=2
                break
            fi
        done
    done
fi

exit $status

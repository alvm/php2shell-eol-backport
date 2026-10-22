# Security policy

## Supported versions

Only the latest release of each package receives fixes.

| Package | Distribution |
|---|---|
| `php-5.4.16-48.el7.php2shell.N` | RHEL / CentOS / Oracle Linux / Scientific Linux 7 |
| `php-5.3.3-50.el6_10.php2shell.N` | RHEL / CentOS / Oracle Linux 6 |

## Reporting a vulnerability

Report security problems in this project privately through GitHub:
[Security → Report a vulnerability](https://github.com/alvm/php2shell-eol-backport/security/advisories/new).
Please do not open a public issue for them.

In scope: the patches, the spec file changes, the build scripts and `tools/check-patched.sh`. For example, a way
around the fix in the patched packages, or a regression that the patch introduced.

This is a volunteer project. You can expect an acknowledgement within 7 days. A fix is released as a new
`.php2shell.N` package release, with a GitHub security advisory when that is useful.

## Out of scope

- Other vulnerabilities of PHP 5.3 / 5.4 that this project does not claim to fix. PHP 5 is end-of-life, and this
  project fixes only CVE-2026-109618 and CVE-2026-109619. Report new PHP vulnerabilities to the
  [PHP project](https://github.com/php/php-src/security) and to your OS vendor.
- The general risk of running an end-of-life PHP version.

## Verifying releases

Packages and release tags are signed with this key (`RPM-GPG-KEY-php2shell-eol-backport` in this repository, also on
`keyserver.ubuntu.com`):

```
2757 B60F D23D ED25 021B  BE37 8079 7C97 A561 BC94
```

# Alternatives and how this project compares

Status as of 23 October 2026. If something here is out of date or wrong, please open an issue.

## Vendors: the stock EL6 / EL7 packages

| Vendor | EL7 `php-5.4.16` | EL6 `php-5.3.3` | Notes |
|---|---|---|---|
| Red Hat | no update | no update | [RHSB-2026-013](https://access.redhat.com/security/vulnerabilities/RHSB-2026-013) (22 Oct): RHEL 7 is "Only affected by CVE-2026-109619 — In a default configuration, the version of PHP in use is vulnerable"; the CVE-2026-109618 code is not present. The older [CSAF VEX](https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2026-109619.json) data still lists RHEL 7 as not affected by CVE-2026-109619; for RHEL 6 it lists CVE-2026-109619 as *not affected* and CVE-2026-109618 as *under investigation* |
| Oracle | no update | no update | [errata](https://linux.oracle.com/cve/CVE-2026-109618.html) only for Oracle Linux 8, 9 and 10 |
| TuxCare ELS (commercial) | fixed on 21 Oct 2026, `php-5.4.16-48.el7.tuxcare.els21` ([CLSA-2026:1792611997](https://errata.tuxcare.com/els_os/rhel7els/CLSA-2026-1792611997.html)) | fixed on 21 Oct 2026, `php-5.3.3-50.el6_10.tuxcare.ol.els27` ([CLSA-2026:1792611737](https://errata.tuxcare.com/els_os/oraclelinux6els/CLSA-2026-1792611737.html)) | subscription; builds for CentOS, RHEL and Oracle Linux |
| CIQ Bridge (commercial, CentOS 7) | no fix planned | — | [KB article](https://kb.ciq.com/article/security-advisories/cve-php2shell-mitigation): "No patched PHP package will be available for Bridge" |

If you already have a TuxCare subscription, use their packages: they come with vendor support and cover other
vulnerabilities too. TuxCare describes the same design as this project ("disable the session upload progress
handler and harden request state after bailout", "memory_limit and allocation overflow fatals now print to stderr
and terminate the process"). Their source was not compared.

## Free community patches for PHP 5.3 / 5.4

Most community ports target the last upstream releases (5.4.45, 5.3.29), the version used by PHP installers,
control panels and Docker images. The EL6 / EL7 packages are a different source tree: PHP 5.4.16 / 5.3.3 with
many fixes backported by the vendor.

| Project | Target | Provides |
|---|---|---|
| this project | vendor `php-5.4.16-48.el7` (RHEL / CentOS / Oracle Linux / Scientific Linux 7), `php-5.3.3-50.el6_10` (EL6) | patches against the vendor trees, vendor spec files, container build, CI with the PHP test suite |
| [leonlai-tw/php-eol-cve-2026-109618-109619](https://github.com/leonlai-tw/php-eol-cve-2026-109618-109619) | Amazon Linux 2 `php-5.4.16-46.amzn2.0.7` (derived from the RHEL 7 package), Amazon Linux 1 `php-5.3.29`, Remi `php73` on EL7 | patches, build scripts |
| [vperetti/php-cve-2026-109618-109619-backports](https://github.com/vperetti/php-cve-2026-109618-109619-backports) | upstream 5.4.45 … 7.3.33 | source patches |
| [nft-syou/php-5.4.45-php2shell-patch](https://github.com/nft-syou/php-5.4.45-php2shell-patch) | upstream 5.4.45 | source patch |
| [valentin-marquez/php](https://github.com/valentin-marquez/php) | upstream 5.4.45 … 8.1 | source patches, build script |
| [waksboy/fixed-fpm-cve-2026-109618-and-109619-images](https://github.com/waksboy/fixed-fpm-cve-2026-109618-and-109619-images) | upstream 5.0 … 8.1 | source patches, Docker images |
| [Qsnh/php2shell-fixed](https://github.com/Qsnh/php2shell-fixed) | BT Panel builds of 5.4 … 8.1 | patched source packages, install scripts |
| [linuxeye/lnmp](https://github.com/linuxeye/lnmp) | the LNMP installer's 5.3 … 5.6 builds | source patches |

There are many more for PHP 5.6 and 7.x. Mitigations that do not change PHP itself, such as
[HOSTED-POWER/php_uploadprogress_guard](https://github.com/HOSTED-POWER/php_uploadprogress_guard), are not listed.

## The two PHP 5.4.16 ports compared

This project and leonlai-tw's Amazon Linux 2 port both start from the RHEL 7 `php-5.4.16` code and were made
independently. The table compares them with the official PHP 7.4 backport
([712e60f9ed](https://github.com/php/php-src/commit/712e60f9edfd03f0960fc4fc3c2c375f42b90aa2)); leonlai-tw
state as of commit `cb40b1c`.

| Change in the official fix | this project | leonlai-tw (AL2) |
|---|---|---|
| Allocation failures (`zend_mm_safe_error()` and the four "Possible integer overflow" checks in `zend_alloc.c`) print the error and `_exit(1)` instead of `zend_bailout()` | yes | yes, same code |
| `zend_mm_panic()`: `exit()` → `_exit()` | yes | no |
| `Balloc()` errors in `zend_strtod.c` take the same exit path | yes | no |
| String concatenation size overflow takes the same exit path (upstream: `ZEND_CONCAT` / `ZEND_FAST_CONCAT` handlers; PHP 5.4: `concat_function()`, which also gets the missing size check in its second branch) | yes | no (listed as not ported) |
| Session upload progress disabled | yes | yes, same code |
| SAPI request fields set to `NULL` after `efree()` | yes | yes, same code |
| `zend_llist_destroy()` resets `head` / `tail` | yes | yes, same code |
| `shutdown_executor()` resets `EG(error_handling)` / `EG(exception)` | yes | yes, same code |
| `PG(http_globals)` cleared and `PG(modules_activated)` reset at request shutdown | yes, in `php_request_shutdown()` | yes, in `php_request_shutdown()` and also in `php_request_shutdown_for_hook()`, which no SAPI of the RHEL build calls |
| Multipart parts: keep only `Content-Disposition` / `Content-Type`, ignore duplicates | yes | yes, same code |
| `max_multipart_body_parts` limit | yes | no |
| Hash table, VM and other PHP 7 engine changes | not applicable | not applicable |

The core of the fix is the same line for line in both ports. This project also ports the remaining fatal error
paths and the multipart part limit of the official fix. For comparison, Red Hat's own PHP 7.4 update for RHEL 8
(`php-7.4.33-8`) carries the whole official patch except the `max_multipart_body_parts` part, because that
package already had the limit from an earlier fix (CVE-2023-0662).

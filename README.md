# php2shell-eol-backport

Unofficial fix for **CVE-2026-109618** and **CVE-2026-109619** ("php2shell") for the end-of-life PHP packages
of **Enterprise Linux 6 and 7**: `php-5.3.3` (RHEL / CentOS / Oracle Linux 6) and `php-5.4.16`
(RHEL / CentOS / Oracle Linux / Scientific Linux 7).

PHP fixed both vulnerabilities on 21 Oct 2026 in 8.2.35, 8.3.36, 8.4.27 and 8.5.12, and published source
backports for 7.4, 8.0 and 8.1. Nothing was released for PHP 5, and the EL6 / EL7 vendors have not shipped
a fix. If you have to keep such a system running, this project gives you rebuilt vendor packages with a
port of the official minimal fix.

> **This is not an official fix from PHP, Red Hat or Oracle.** It reduces the risk until you can move to a
> supported PHP version — do that as soon as you can.
> On EL8 / EL9 / EL10, install your vendor's updates instead (for example ELSA/RHSA-2026:87080, 87151, 87079).

## What is fixed

- [CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) and
  [CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp), CVSS 4.0 9.2.
- The patch is a port of php-src commit
  [712e60f9ed](https://github.com/php/php-src/commit/712e60f9edfd03f0960fc4fc3c2c375f42b90aa2)
  ("Avoid state corruption via bailout"), the official minimal backport for PHP 7.4, to the PHP 5.3 / 5.4
  code base. It is applied on top of the vendor package with all its existing security patches.
- The patches are made against the vendor source trees. They do not apply to the plain `php-5.4.16` /
  `php-5.3.3` release tarballs, which lack the vendor's later security fixes in the same code
  (for example CVE-2015-4024 in multipart header parsing).

| Distribution | Vendor package | Fixed package from this project |
|---|---|---|
| RHEL / CentOS / Oracle Linux / Scientific Linux 7 | `php-5.4.16-48.el7` | `php-5.4.16-48.el7.php2shell.1` |
| RHEL / CentOS / Oracle Linux 6 | `php-5.3.3-50.el6_10` | `php-5.3.3-50.el6_10.php2shell.1` |

The release suffix sorts above the vendor package, and below any future vendor erratum
(for example `48.el7_9.1`), so an official fix, if one ever appears, replaces this one with a normal update.

### How serious is this on PHP 5?

Probably less than on PHP 7 and 8, but there is no definite answer yet:

- Red Hat rates the RHEL 6 / 7 `php` packages as not affected by CVE-2026-109619 ("vulnerable code not present")
  and lists CVE-2026-109618 as under investigation
  ([CSAF VEX](https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2026-109618.json)).
- An [independent analysis of PHP 5.3](https://github.com/euriconicacio/blog/blob/main/all_collections/_posts/2026-10-22-evaluating-php2shell-reachability-and-corruptibility-in-php-5-3-15.md)
  found that the out-of-memory fault can be reached, but the published memory corruption step relies on
  PHP 7 engine internals, so on PHP 5 the known attack ends in a denial of service. PHP 5.4–5.6 were assessed by
  comparing the code, not tested, and other attack paths are not ruled out.

This project applies the official mitigation anyway: it removes the unsafe error path itself, not only the
known way to reach it.

## Install

From the signed yum repository on GitHub Pages:

```bash
# EL7
curl -o /etc/yum.repos.d/php2shell-eol-backport.repo \
  https://alvm.github.io/php2shell-eol-backport/php2shell-eol-backport-el7.repo
# EL6
curl -o /etc/yum.repos.d/php2shell-eol-backport.repo \
  https://alvm.github.io/php2shell-eol-backport/php2shell-eol-backport-el6.repo

yum update 'php*'            # confirm the signing key: fingerprint under "Signing key" below
service httpd restart        # and php-fpm, if you use it
```

The repository contains only the PHP packages of this project, and both the packages and the repository
metadata are signed (`gpgcheck=1`, `repo_gpgcheck=1`). The RPMs and source RPMs are also attached to each
[release](https://github.com/alvm/php2shell-eol-backport/releases), with a signed `SHA256SUMS`; install them
with `yum localinstall`.

## Check a system

```bash
./tools/check-patched.sh
```

It lists every installed PHP 5 package as `FIXED` or `VULNERABLE`, checks that the PHP CLI runs the fixed
code, and warns if `httpd` or `php-fpm` was started before the update and still runs the old code.

## Behaviour changes and known limitations

The fix follows the official minimal backport, which favours safety over graceful error handling:

- **Memory exhaustion ends the PHP process.** When a request exceeds `memory_limit` (or an allocation size
  overflows), PHP prints `Fatal error: ...` to stderr (the web server error log) and the process exits at once.
  Apache / php-fpm start a new worker. Shutdown functions do not run, and temporary files of uploads in that
  request are not removed — `tmpwatch` (EL6) and `systemd-tmpfiles` (EL7) clean them from `/tmp` over time.
- **Session upload progress is disabled** (PHP 5.4; PHP 5.3 does not have it).
- **Multipart requests:** only the `Content-Disposition` and `Content-Type` headers of each part are kept
  (the only ones PHP uses), and the new `php.ini` directive `max_multipart_body_parts` limits the number of
  parts (default `-1` = `max_input_vars` + `max_file_uploads`).
- The patch adds one exported function (`zend_mm_safe_error_ex`) and changes no existing API or ABI, so
  extensions built for the vendor package keep working.

This is a minimal mitigation of the published attack paths, not a full security update of PHP 5.

## How it was verified

- Built from the vendor source RPMs (pinned SHA-256 in `build/build.sh`); the spec change is 8 lines
  (`spec/*/php.spec.diff`).
- The PHP test suite (`make test`, run during the RPM build) was compared with an unmodified rebuild of the
  same vendor package. The only new failures are expected:
  the session upload progress tests (feature disabled) and `tests/lang/bug45392.phpt` (the fatal error
  message now starts with an empty line, as in the official 7.4 patch).

  | | tests | failed: vendor | failed: patched |
  |---|---|---|---|
  | EL7, PHP 5.4.16 | 12373 | 14 | 23 (8 upload progress + bug45392) |
  | EL6, PHP 5.3.3 | 11213 | 55 | 56 (bug45392) |

  The exact counts vary slightly between build environments: on GitHub runners two SPL file-owner tests
  (`DirectoryIterator_getOwner/getGroup_basic`) also fail, and `time_sleep_until_basic` is timing-sensitive.
  None of them touches code changed by the patch.

- The PHP 5.4 patch was compared with an independent port of the same fix for Amazon Linux 2's `php-5.4.16`:
  the core changes are identical. The differences are listed in [docs/ALTERNATIVES.md](docs/ALTERNATIVES.md).
- No exploit code was written or used. Please review the patch against the upstream commit yourself.

## Alternatives

- **Commercial:** TuxCare Extended Lifecycle Support shipped fixed packages for EL6 and EL7 on 21 Oct 2026.
- **Other free patches:** mostly for the upstream 5.4.45 / 5.3.29 sources, and one for Amazon Linux.

See [docs/ALTERNATIVES.md](docs/ALTERNATIVES.md) for the vendor status, a list of projects and a comparison.

## Build it yourself

Requires Docker and about 3 GB of free disk space per build.

```bash
build/build.sh el7      # results in _build/el7/RPMS
build/build.sh el6      # results in _build/el6/RPMS
```

The script downloads the vendor source RPM, checks its SHA-256, and rebuilds it in a pinned Oracle Linux
container with the spec file and patch from this repository.

## Signing key

Packages and release tags are signed with:

```
pub   rsa4096/80797C97A561BC94 2026-10-22 [SC] [expires: 2029-10-21]
      2757 B60F D23D ED25 021B  BE37 8079 7C97 A561 BC94
uid   Oleksii Molchanov (php2shell-eol-backport signing key) <2106429+alvm@users.noreply.github.com>
```

The key is in this repository (`RPM-GPG-KEY-php2shell-eol-backport`) and on `keyserver.ubuntu.com`.

## Repository layout

```
patches/el7, patches/el6   the fix, as a patch against the vendor source tree
spec/el7, spec/el6         vendor spec files with the patch added, and their diffs
build/                     reproducible container build
tools/check-patched.sh     check an installed system
docs/ALTERNATIVES.md       vendor status, other projects, comparison
SECURITY.md                how to report a security problem
```

## Reporting problems

Open an issue for bugs. For a security problem in the patch itself, see [SECURITY.md](SECURITY.md).

## Credits and license

- The fix is by the PHP security team; this project only ports it. See the GitHub advisories for the
  reporters.
- Patches: PHP License 3.01 (`LICENSE.PHP`), like the code they change. Build scripts and tools: MIT
  (`LICENSE`). Spec files are derived from the Red Hat / Fedora packaging (MIT).

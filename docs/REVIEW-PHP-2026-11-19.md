# PHP security releases of 19 November 2026: review for PHP 5.4 and 5.3

On 19 November 2026 PHP released 8.2.36, 8.3.37, 8.4.28 and 8.5.13 and published 17 security advisories. This page
lists every one of them and says, for the two packages of this project, whether it applies and what we did:

- EL7: `php-5.4.16-48.el7` (RHEL / CentOS / Oracle Linux / Scientific Linux 7)
- EL6: `php-5.3.3-50.el6_10` (RHEL / CentOS / Oracle Linux 6)

**In short:** 8 of the 17 issues affect these packages, and a 9th (CVE-2026-129506) has its defect only in a path
that PHP does not count as a security issue. All 9 are fixed: phpAfterShell (CVE-2026-126714) in release 2, 6 in
release 3, and CVE-2026-129291 and CVE-2026-129506 in release 4 (see
[Correction in release 4](#correction-in-release-4)). One more, CVE-2026-115560, is already closed by release 1. The
other 7 do not apply, because the code they fix does not exist in PHP 5.3 / 5.4.

## How we checked

For each advisory we read PHP's statement of the affected versions, took the upstream fix commit from the PHP-8.2
branch, and compared the code it changes with the vendor source trees of both packages: the PHP release with all
security patches of Red Hat applied, which is the code that the packages are built from. "Affected" means the vendor
code has the same defect as the code before the fix. "Not affected" means the code is not there, or the path to it
does not exist; the reason is given for each issue.

This is a review of the code, not an exploit test. No exploit code was written or used. Ports follow the upstream
commit, changed only where the PHP 5 API differs, and each port is a separate patch in `patches/el7` and `patches/el6`.

## Results

| CVE | Advisory | Severity | Issue | EL7 5.4.16 | EL6 5.3.3 | Result |
|---|---|---|---|---|---|---|
| CVE-2026-126714 | [GHSA-fm2m-fjf5-v3cp](https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp) | critical | phpAfterShell: partially overwritten session files | affected | affected | **fixed in release 2** |
| CVE-2026-129496 | [GHSA-gr4f-wgx5-jpfv](https://github.com/php/php-src/security/advisories/GHSA-gr4f-wgx5-jpfv) | critical | timezone cache use-after-free | affected | affected | **fixed in release 3** |
| CVE-2026-115560 | [GHSA-658j-r8rw-q6mx](https://github.com/php/php-src/security/advisories/GHSA-658j-r8rw-q6mx) | critical | session serializer mismatch (upload progress) | closed by release 1 | not affected | no new change |
| CVE-2026-129289 | [GHSA-qc49-hpvq-g2w6](https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6) | critical | PHP-FPM request smuggling through an unread body | not affected | not affected | not applicable |
| CVE-2026-129481 | [GHSA-g3vh-838c-65v7](https://github.com/php/php-src/security/advisories/GHSA-g3vh-838c-65v7) | critical | use-after-free after interrupted session shutdown | not affected | not affected | not applicable |
| CVE-2026-129182 | [GHSA-2fjv-p558-g82m](https://github.com/php/php-src/security/advisories/GHSA-2fjv-p558-g82m) | critical | fatal error backtrace after shutdown | not affected | not affected | not applicable |
| CVE-2026-129474 | [GHSA-8mjj-2r7p-4hg2](https://github.com/php/php-src/security/advisories/GHSA-8mjj-2r7p-4hg2) | critical | magic method backtraces | not affected | not affected | not applicable |
| CVE-2026-128064 | [GHSA-f6gg-rchx-xw8j](https://github.com/php/php-src/security/advisories/GHSA-f6gg-rchx-xw8j) | high | mixed-case HTTPS / FTPS URLs sent in plaintext | affected | affected | **fixed in release 3** |
| CVE-2026-128090 | [GHSA-68fq-fh7h-f8gr](https://github.com/php/php-src/security/advisories/GHSA-68fq-fh7h-f8gr) | high | PHAR OpenSSL signature downgrade | affected | affected | **fixed in release 3** |
| CVE-2026-127960 | [GHSA-mmf9-xm3v-hg2x](https://github.com/php/php-src/security/advisories/GHSA-mmf9-xm3v-hg2x) | high | slow parsing of folded HTTP response headers | not affected | not affected | not applicable |
| CVE-2026-129291 | [GHSA-jm4m-qfqx-967m](https://github.com/php/php-src/security/advisories/GHSA-jm4m-qfqx-967m) | high | PHP-FPM epoll use-after-free | affected | affected | **fixed in release 4** |
| CVE-2026-129292 | [GHSA-3mg3-cr28-46gc](https://github.com/php/php-src/security/advisories/GHSA-3mg3-cr28-46gc) | medium | PHP-FPM status page XSS | affected | affected | **fixed in release 3** |
| CVE-2026-129538 | [GHSA-5j3f-64r7-f564](https://github.com/php/php-src/security/advisories/GHSA-5j3f-64r7-f564) | medium | php-cgi `PATH_INFO` out-of-bounds read and write | affected | affected | **fixed in release 3** |
| CVE-2026-15353 | [GHSA-q23r-hr55-xmpg](https://github.com/php/php-src/security/advisories/GHSA-q23r-hr55-xmpg) | medium | SOAP out-of-bounds read on an empty array size | affected | affected | **fixed in release 3** |
| CVE-2026-129506 | [GHSA-4646-p932-gw34](https://github.com/php/php-src/security/advisories/GHSA-4646-p932-gw34) | medium | SOAP use-after-free with DTD entity references | WSDL / schema loading only | WSDL / schema loading only | **fixed in release 4** |
| CVE-2026-129438 | [GHSA-mg3p-mxj9-g2mm](https://github.com/php/php-src/security/advisories/GHSA-mg3p-mxj9-g2mm) | medium | RFC 3986 URI serialization | not affected | not affected | not applicable |
| CVE-2026-129501 | [GHSA-x8r7-mg3g-74hg](https://github.com/php/php-src/security/advisories/GHSA-x8r7-mg3g-74hg) | medium | double free in DOM XML serialization | not affected | not affected | not applicable |

## Fixed

| CVE | Upstream commit | Patch | What the port does |
|---|---|---|---|
| CVE-2026-126714 | [41c0941ae27](https://github.com/php/php-src/commit/41c0941ae27d1033129e0e09ce3af034ffee86ba) | Patch9002 | The `files` session handler always truncates the session file before it writes it. |
| CVE-2026-129496 | [cb20015e045](https://github.com/php/php-src/commit/cb20015e045508ed6642ab7d72858270f9224d64) | Patch9003 | Outside a started request, the timestamp of the file-based error log is in UTC, so no timezone cache is created in startup memory. |
| CVE-2026-128064 | [9c0b44ffd66](https://github.com/php/php-src/commit/9c0b44ffd6631cea9906db32deca945bcbc93361) | Patch9004 | The http and ftp stream wrappers choose TLS by a case-insensitive comparison of the whole scheme. Before, only a lowercase `s` enabled TLS. |
| CVE-2026-128090 | [db90b7ba0db](https://github.com/php/php-src/commit/db90b7ba0db7f6568c61c4eb1c4c22968bfab575) | Patch9005 | When `<phar>.pubkey` exists, a phar signature that does not use OpenSSL is rejected. |
| CVE-2026-129292 | [37abd0a7f7b](https://github.com/php/php-src/commit/37abd0a7f7b444ad8f9fb1b5c7993488b1cf5fb3) | Patch9006 | The HTML and XML full status of PHP-FPM escapes the request method, URI, query string, user and script name. |
| CVE-2026-129538 | [1e109bfbd2f](https://github.com/php/php-src/commit/1e109bfbd2f80367882f9866dbc6aa8088f0551f) | Patch9007 | php-cgi rewrites `PATH_INFO` only when it is longer than the suffix it strips. |
| CVE-2026-15353 | [382d2494805](https://github.com/php/php-src/commit/382d24948058d1d586ea48c549a65eb41ac531c6) | Patch9008 | An empty SOAP array size counts as one dimension. |
| CVE-2026-129291 | [13c4db29870](https://github.com/php/php-src/commit/13c4db2987098737278ef78849bb791866021c3c) | Patch9009 | When a worker exits, the PHP-FPM master removes the events of its stdout / stderr pipes before it closes them, and invalidates the descriptors. |
| CVE-2026-129506 | [13a0f8c8c16](https://github.com/php/php-src/commit/13a0f8c8c1634d80de1a42016390b1bc3bd6e470) | Patch9010 | The SOAP extension keeps the DTD node while it cleans up a parsed WSDL or schema document. |

Notes on the ports:

- **CVE-2026-129496.** PHP: the affected code "has been present since PHP 5.3.18 and 5.4.8", and "an earlier form of it
  was present in" 5.3.0 to 5.3.8. Both vendor trees have the full sequence: the log timestamp is formatted in local
  time during startup, the startup memory is released, and request input is processed before the date extension
  resets its reference to the cache. We also checked that no other code creates the cache during startup in PHP 5:
  cookie dates are formatted in UTC, and the `date.timezone` setting only validates the name.
- **CVE-2026-128090.** PHP 5 knows only one OpenSSL signature type, so the check is "not OpenSSL" instead of the
  three types of PHP 8.
- **CVE-2026-129292.** The PHP 5 code escaped only the query string, with flags that left double quotes as they were.
  The port escapes all five fields with the flags of the upstream fix. This also covers the earlier advisory
  [GHSA-7qg2-v9fj-4mwv](https://github.com/php/php-src/security/advisories/GHSA-7qg2-v9fj-4mwv) (CVE-2026-6735, May
  2026, unescaped request URI), which was never fixed in PHP 5. The JSON output is unchanged; it is served as `application/json`.
  The status page exists only when a pool sets `pm.status_path`.
- **CVE-2026-129538.** The same defect in PHP-FPM was fixed by the vendor update for CVE-2019-11043 long ago; php-cgi
  had kept it. php-cgi is in the `php-cli` package and is used when a web server runs PHP through CGI or FastCGI with
  `php-cgi`.

## Correction in release 4

The first version of this review (release 3) listed CVE-2026-129291 and CVE-2026-129506 as not applicable. On 22 Nov
2026 Red Hat fixed both in its RHEL 7 update (`php-5.4.16-48.el7_9.2`, RHSA-2026:101337), so we checked the code
again.

- **CVE-2026-129291 was a mistake on our side.** PHP dates the issue to 8.1.20, because in PHP 8 before 8.1.20 the
  stdout / stderr events of a worker carried its process ID, and the handler looked the worker up and did nothing
  when it was gone. The PHP 5.3 / 5.4 vendor code is different: the event carries a pointer to the worker record, as
  in 8.1.20 and later. When a worker exits, `fpm_child_close()` closes its pipes without removing their epoll events
  and frees the record at once, and a new worker switches to the pool user before it closes the pipes that it
  inherited from the master. So the use-after-free of the advisory exists in both packages. It requires local code
  execution in a PHP-FPM worker and `catch_workers_output = yes`, which the vendor `php-fpm.d/www.conf` leaves
  commented out (off). Release 4 ports the upstream fix.

  Why we got it wrong: the first review relied on PHP's statement that the affected delayed-cleanup path was
  introduced in 8.1.20, saw that PHP-FPM 5.3 / 5.4 has no delayed cleanup, and stopped there. It did not compare how
  the event handler finds the worker, which is the part that decides whether freed memory is used.
- **CVE-2026-129506 stays as described for SOAP server requests:** PHP 5.3 / 5.4 parse them without the cleanup that
  removes the DTD, and reject them when they have one. The same cleanup does run when PHP loads a WSDL or schema
  document, so the defect exists there. PHP does not count untrusted WSDL or schema documents as a security issue,
  but Red Hat fixed it for RHEL 7 (rated Low), and release 4 ports the fix for the same coverage.
- **A counting error:** the summary of the first version said that 8 issues affect the packages (1 fixed in release 2,
  7 in release 3) and that 8 do not apply. By the results table of that version, 7 were affected (1 in release 2, 6 in
  release 3) and 9 did not apply; the two errors cancelled out in the total of 17. The summary above has the corrected
  numbers for release 4.

## Closed earlier: CVE-2026-115560

The issue is in session upload progress, which "was introduced in PHP 5.4.0". Release 1 disables session upload
progress in the PHP 5.4 code, and PHP 5.3 does not have it. Red Hat states the same for its own updates: they
"unconditionally disabled the Session Upload Progress functionality", which "provides a mitigation for this issue as
well".

## Not applicable, and why

| CVE | Why PHP 5.3 / 5.4 are not affected |
|---|---|
| CVE-2026-129289 | PHP: the affected code "has been present since PHP 5.6.0", which made reading `php://input` lazy. In PHP 5.3 / 5.4, request shutdown always reads and discards a request body that was not read in full, and a body that is read is read to its `Content-Length`, so no unread bytes stay on a FastCGI connection. Red Hat's VEX data lists RHEL 6 and 7 as affected, and its RHEL 7 update of 22 Nov 2026 does not fix it either; the code does not support that it applies. |
| CVE-2026-129481 | PHP: "The affected field was introduced in PHP 8.3.0" (the file and line where a session was started). PHP 5 does not have it. |
| CVE-2026-129182 | PHP: "The affected global was introduced in PHP 8.5.0 by fatal error backtraces." PHP 5 has neither. |
| CVE-2026-129474 | PHP: the attack path "was introduced in PHP 8.5.0 by fatal error backtraces". The underlying error is in how PHP 7 and later enter a method handled by `__call()`; PHP 5 handles these calls differently and has no fatal error backtraces. With release 1, a `memory_limit` error also ends the process at once. |
| CVE-2026-127960 | PHP: "The affected code was introduced by the fix for GHSA-v8xr-gpvj-cx9g, first released in PHP 8.1.32". The http wrapper of PHP 5 does not have this header folding code. Red Hat's VEX data listed RHEL 6 and 7 as affected on 20 Nov 2026; since 22 Nov it lists RHEL 7 as not affected. |
| CVE-2026-129438 | Affects the `Uri\Rfc3986\Uri` class of PHP 8.5. PHP 5 has no URI extension. |
| CVE-2026-129501 | Affects the `Dom\XMLDocument` and `Dom\HTMLDocument` classes of PHP 8.4. PHP 5 has only the legacy `DOMDocument`, which "does not use this serializer". |

## Limits

- The review covers the 17 advisories of 19 November 2026. PHP 5 is end-of-life and has many older, unfixed
  vulnerabilities; this project fixes only the ones listed in the README.
- "Not affected" is based on PHP's statements and on our reading of the code. If you find a path we missed, please
  report it as described in [SECURITY.md](../SECURITY.md).
- How the fixes were tested is described in the README under
  [How it was verified](../README.md#how-it-was-verified).

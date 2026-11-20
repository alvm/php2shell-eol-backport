# PHP security releases of 19 November 2026: review for PHP 5.4 and 5.3

On 19 November 2026 PHP released 8.2.36, 8.3.37, 8.4.28 and 8.5.13 and published 17 security advisories. This page
lists every one of them and says, for the two packages of this project, whether it applies and what we did:

- EL7: `php-5.4.16-48.el7` (RHEL / CentOS / Oracle Linux / Scientific Linux 7)
- EL6: `php-5.3.3-50.el6_10` (RHEL / CentOS / Oracle Linux 6)

**In short:** 8 of the 17 issues affect these packages. All 8 are fixed: phpAfterShell (CVE-2026-126714) in release 2,
the other 7 in release 3. One more, CVE-2026-115560, is already closed by release 1. The other 8 do not apply,
because the code they fix does not exist in PHP 5.3 / 5.4.

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
| CVE-2026-129291 | [GHSA-jm4m-qfqx-967m](https://github.com/php/php-src/security/advisories/GHSA-jm4m-qfqx-967m) | high | PHP-FPM epoll use-after-free | not affected | not affected | not applicable |
| CVE-2026-129292 | [GHSA-3mg3-cr28-46gc](https://github.com/php/php-src/security/advisories/GHSA-3mg3-cr28-46gc) | medium | PHP-FPM status page XSS | affected | affected | **fixed in release 3** |
| CVE-2026-129538 | [GHSA-5j3f-64r7-f564](https://github.com/php/php-src/security/advisories/GHSA-5j3f-64r7-f564) | medium | php-cgi `PATH_INFO` out-of-bounds read and write | affected | affected | **fixed in release 3** |
| CVE-2026-15353 | [GHSA-q23r-hr55-xmpg](https://github.com/php/php-src/security/advisories/GHSA-q23r-hr55-xmpg) | medium | SOAP out-of-bounds read on an empty array size | affected | affected | **fixed in release 3** |
| CVE-2026-129506 | [GHSA-4646-p932-gw34](https://github.com/php/php-src/security/advisories/GHSA-4646-p932-gw34) | medium | SOAP use-after-free with DTD entity references | not affected | not affected | not applicable |
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

## Closed earlier: CVE-2026-115560

The issue is in session upload progress, which "was introduced in PHP 5.4.0". Release 1 disables session upload
progress in the PHP 5.4 code, and PHP 5.3 does not have it. Red Hat states the same for its own updates: they
"unconditionally disabled the Session Upload Progress functionality", which "provides a mitigation for this issue as
well".

## Not applicable, and why

| CVE | Why PHP 5.3 / 5.4 are not affected |
|---|---|
| CVE-2026-129289 | PHP: the affected code "has been present since PHP 5.6.0", which made reading `php://input` lazy. In PHP 5.3 / 5.4, request shutdown always reads and discards a request body that was not read in full, and a body that is read is read to its `Content-Length`, so no unread bytes stay on a FastCGI connection. Red Hat's VEX data lists RHEL 6 and 7 as affected; the code does not support that. |
| CVE-2026-129481 | PHP: "The affected field was introduced in PHP 8.3.0" (the file and line where a session was started). PHP 5 does not have it. |
| CVE-2026-129182 | PHP: "The affected global was introduced in PHP 8.5.0 by fatal error backtraces." PHP 5 has neither. |
| CVE-2026-129474 | PHP: the attack path "was introduced in PHP 8.5.0 by fatal error backtraces". The underlying error is in how PHP 7 and later enter a method handled by `__call()`; PHP 5 handles these calls differently and has no fatal error backtraces. With release 1, a `memory_limit` error also ends the process at once. |
| CVE-2026-127960 | PHP: "The affected code was introduced by the fix for GHSA-v8xr-gpvj-cx9g, first released in PHP 8.1.32". The http wrapper of PHP 5 does not have this header folding code. Red Hat's VEX data (20 Nov 2026) lists RHEL 6 and 7 as affected; the vendor code of both packages does not support that. |
| CVE-2026-129291 | PHP: "The affected delayed-cleanup path was introduced by the fix for GH-10461, first released in PHP 8.1.20 and 8.2.7." PHP-FPM 5.3 / 5.4 frees a worker at once and has no delayed cleanup. Red Hat's VEX data (20 Nov 2026) lists RHEL 6 and 7 as affected; the vendor code of both packages does not support that. |
| CVE-2026-129506 | PHP: "SOAP server requests have been affected since PHP 5.6.0". From 5.6 the SOAP server reads the request through a parser path that also runs a cleanup which removes the DTD. PHP 5.3 / 5.4 parse the request without that cleanup, so the DTD stays and the server rejects the request with "DTD are not supported by SOAP". The cleanup runs only when PHP loads a WSDL or schema document, and PHP states that "loading an untrusted WSDL or schema is not considered a security issue". Red Hat's VEX data (20 Nov 2026) lists RHEL 6 and 7 as affected; for SOAP server requests the vendor code of both packages does not support that. |
| CVE-2026-129438 | Affects the `Uri\Rfc3986\Uri` class of PHP 8.5. PHP 5 has no URI extension. |
| CVE-2026-129501 | Affects the `Dom\XMLDocument` and `Dom\HTMLDocument` classes of PHP 8.4. PHP 5 has only the legacy `DOMDocument`, which "does not use this serializer". |

## Limits

- The review covers the 17 advisories of 19 November 2026. PHP 5 is end-of-life and has many older, unfixed
  vulnerabilities; this project fixes only the ones listed in the README.
- "Not affected" is based on PHP's statements and on our reading of the code. If you find a path we missed, please
  report it as described in [SECURITY.md](../SECURITY.md).
- How the fixes were tested is described in the README under
  [How it was verified](../README.md#how-it-was-verified).

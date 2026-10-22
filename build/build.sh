#!/bin/bash
# Build the patched PHP RPMs for one EL release in a pinned Oracle Linux container.
#
#   build/build.sh el7|el6 [WORKDIR]
#
# The official vendor source RPM is downloaded and checked against a pinned
# SHA-256, then rebuilt with the spec file and patch from this repository.
# Results: WORKDIR/RPMS, WORKDIR/SRPMS, WORKDIR/build.log (default WORKDIR: ./_build/<el>).
set -euo pipefail

EL=${1:?usage: build/build.sh el7|el6 [WORKDIR]}
REPO=$(cd "$(dirname "$0")/.." && pwd)
WORKDIR=${2:-$REPO/_build/$EL}

case $EL in
  el7)
    SRPM_URL=https://oss.oracle.com/ol7/SRPMS-updates/php-5.4.16-48.el7.src.rpm
    SRPM_SHA256=14273a817f15748ec591a0d88288a3828423493f83da8a6fa7a5c962c0dcc60d
    IMAGE=oraclelinux@sha256:767c93c07b1fa621ae56d1f5f090e8c0dce7eb452e7dda1e74bbe7546504d63f  # oraclelinux:7
    ;;
  el6)
    SRPM_URL=https://oss.oracle.com/ol6/SRPMS-updates/php-5.3.3-50.el6_10.src.rpm
    SRPM_SHA256=d39acc71fc5c984b42466e940b031ea195866d785378307d3af52890da466223
    IMAGE=oraclelinux@sha256:f4f7375d3a220de1158f57719eb1df7a7438cad9e33c3a8b8ce88907684b656b  # oraclelinux:6
    ;;
  *) echo "unknown release: $EL" >&2; exit 2 ;;
esac

mkdir -p "$WORKDIR/topdir"
SRPM=$WORKDIR/$(basename "$SRPM_URL")
if [ ! -f "$SRPM" ]; then
  curl -fsSL -o "$SRPM.tmp" "$SRPM_URL"
  mv "$SRPM.tmp" "$SRPM"
fi
echo "$SRPM_SHA256  $SRPM" | sha256sum -c -

# The build tree lives on the host (WORKDIR), not in the container layer.
# Its path inside the container must be longer than /usr/src/debug, otherwise
# debugedit refuses to rewrite debug info paths.
docker run --rm \
  -v "$REPO:/src:ro" \
  -v "$SRPM:/srpm/$(basename "$SRPM"):ro" \
  -v "$WORKDIR/topdir:/root/rpmbuild-php2shell-eol-backport" \
  "$IMAGE" /src/build/in-container.sh "$EL" "/srpm/$(basename "$SRPM")" \
  | tee "$WORKDIR/build.log"

mkdir -p "$WORKDIR/RPMS" "$WORKDIR/SRPMS"
cp -a "$WORKDIR"/topdir/RPMS/x86_64/*.rpm "$WORKDIR/RPMS/"
cp -a "$WORKDIR"/topdir/SRPMS/*.rpm "$WORKDIR/SRPMS/"
(cd "$WORKDIR/RPMS" && sha256sum -- *.rpm > SHA256SUMS)
echo "Done: $WORKDIR/RPMS"

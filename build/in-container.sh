#!/bin/bash
# Runs inside the Oracle Linux build container; called by build/build.sh.
#   in-container.sh el7|el6 /path/to/vendor.src.rpm
set -euo pipefail

EL=$1
SRPM=$2
TOPDIR=/root/rpmbuild-php2shell-eol-backport

# The build tree is a host directory: hand it back to its owner on exit,
# so that it can be removed without root.
OWNER=$(stat -c %u:%g "$TOPDIR")
trap 'chown -R "$OWNER" "$TOPDIR"' EXIT

case $EL in
  el7) DIST=.el7;    OPTIONAL_REPO=ol7_optional_latest ;;
  el6) DIST=.el6_10; OPTIONAL_REPO=ol6_optional_latest ;;
esac

# The spec file does not list the basic toolchain (a mock buildroot has it).
yum -q -y install yum-utils rpm-build make gcc gcc-c++ redhat-rpm-config tar patch bzip2 cpio
yum-config-manager -q --enable "$OPTIONAL_REPO" >/dev/null

rpm -i --define "_topdir $TOPDIR" "$SRPM"
cp "/src/spec/$EL/php.spec" "$TOPDIR/SPECS/php.spec"
cp /src/patches/"$EL"/*.patch "$TOPDIR/SOURCES/"
# rpm 4.8 (EL6) rejects source files owned by uids unknown in the container.
chown -R root:root "$TOPDIR/SOURCES" "$TOPDIR/SPECS"

yum-builddep -y "$TOPDIR/SPECS/php.spec"
# %check runs the PHP test suite; failures are reported in the log, not fatal.
rpmbuild -ba \
  --define "_topdir $TOPDIR" \
  --define "dist $DIST" \
  --define "_smp_mflags -j$(nproc)" \
  "$TOPDIR/SPECS/php.spec"

%global contentdir  /var/www
# API/ABI check
%global apiver      20090626
%global zendver     20090626
%global pdover      20080721
# Extension version
%global fileinfover 1.0.5-dev
%global pharver     2.0.1
%global zipver      1.9.1
%global jsonver     1.2.1

%define httpd_mmn %(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)

# Use the arch-specific mysql_config binary to avoid mismatch with the
# arch detection heuristic used by bindir/mysql_config.
%define mysql_config %{_libdir}/mysql/mysql_config

Summary: PHP scripting language for creating dynamic web sites
Name: php
Version: 5.3.3
Release: 50%{?dist}.php2shell.1
License: PHP
Group: Development/Languages
URL: http://www.php.net/

Source0: http://www.php.net/distributions/php-%{version}.tar.bz2
Source1: php.conf
Source2: php.ini
Source3: macros.php
# php-fpm files
Source4: php-fpm.conf
Source5: php-fpm-www.conf
Source7: php-fpm.logrotate
Source8: php-fpm.sysconfig
Source9: php-fpm.init
# sapi/fpm sources from php-5.3.18
Source10: php-fpm-5.3.18.tar.bz2

# Build fixes
Patch1: php-5.3.3-gnusrc.patch
Patch2: php-5.3.0-install.patch
Patch3: php-5.2.4-norpath.patch
Patch4: php-5.3.0-phpize64.patch
Patch5: php-5.2.0-includedir.patch
Patch6: php-5.2.4-embed.patch
Patch7: php-5.3.0-recode.patch
Patch8: php-5.3.3-aconf26x.patch

# Fixes for extensions
Patch20: php-4.3.11-shutdown.patch
Patch21: php-5.3.3-zipmemset.patch
Patch22: php-5.3.3-pdo-overflow.patch
Patch23: php-5.3.3-pdo-53551.patch
Patch24: php-5.3.3-fileinfo.patch
Patch25: php-5.3.3-imap.patch
Patch26: php-5.3.3-odbc.patch
Patch27: php-5.3.3-bug53592.patch

# Functional changes
Patch40: php-5.0.4-dlopen.patch
Patch41: php-5.3.0-easter.patch
Patch42: php-5.3.1-systzdata-v7.patch
Patch43: php-5.3.3-getmodinit.patch

# Fixes for tests
Patch61: php-5.0.4-tests-wddx.patch

# Bug fixes
Patch100: php-5.3.3-extrglob.patch
Patch101: php-5.3.3-varnegidx.patch
Patch102: php-5.3.3-setdate.patch
Patch103: php-5.3.18-fpmcovscan.patch
Patch104: php-5.3.3-zendgc.patch
Patch106: php-5.3.3-copy.patch
Patch107: php-5.3.3-errorhandler.patch
Patch108: php-5.3.3-bug54268.patch
Patch109: php-5.3.3-pdopgsql.patch
Patch110: php-5.3.3-bug66762.patch
Patch111: php-5.3.3-bug52636.patch
Patch112: php-5.3.3-rfc2616.patch
Patch113: php-5.3.3-r305043.patch
Patch114: php-5.3.3-bug53141.patch
Patch115: php-5.3.3-openssl.patch
Patch116: php-5.3.3-bug54609.patch
Patch117: php-5.3.3-curltls.patch
Patch118: php-5.3.3-bug63635.patch

# Fixes for security bugs
Patch200: php-5.3.3-CVE-2010-3709.patch
Patch201: php-5.3.2-CVE-2010-3870.patch
Patch202: php-5.3.3-CVE-2010-3710.patch
Patch203: php-5.3.2-CVE-2010-4645.patch
Patch204: php-5.3.3-CVE-2010-4156.patch
Patch205: php-5.3.3-CVE-2011-0708.patch
Patch206: php-5.3.3-CVE-2011-1148.patch
Patch207: php-5.3.3-CVE-2011-1466.patch
Patch208: php-5.3.3-CVE-2011-1468.patch
Patch209: php-5.3.3-CVE-2011-1469.patch
Patch210: php-5.3.3-CVE-2011-1470.patch
Patch211: php-5.3.3-CVE-2011-1471.patch
Patch212: php-5.3.3-CVE-2011-1938.patch
Patch213: php-5.3.3-CVE-2011-2202.patch
Patch214: php-5.3.3-CVE-2011-2483.patch
Patch215: php-5.3.3-CVE-2011-4885.patch
Patch216: php-5.3.3-CVE-2011-4566.patch
Patch217: php-5.3.3-CVE-2012-0830.patch
Patch218: php-5.3.3-CVE-2012-1823.patch
Patch219: php-5.3.3-CVE-2012-2336.patch
Patch220: php-5.3.3-CVE-2011-4153.patch
Patch221: php-5.3.3-CVE-2012-0781.patch
Patch222: php-5.3.3-CVE-2012-1172.patch
Patch223: php-5.3.3-CVE-2012-2143.patch
Patch224: php-5.3.3-CVE-2012-2386.patch
Patch225: php-5.3.3-CVE-2012-0057.patch
Patch226: php-5.3.3-CVE-2012-0789.patch
Patch227: php-5.3.3-CVE-2010-2950.patch
Patch228: php-5.3.3-CVE-2012-2688.patch
Patch229: php-5.3.3-CVE-2012-0831.patch
Patch230: php-5.3.3-CVE-2011-1398.patch
Patch231: php-5.3.3-CVE-2013-1643.patch
Patch232: php-5.3.3-CVE-2006-7243.patch
Patch233: php-5.3.3-CVE-2013-4113.patch
Patch234: php-5.3.3-CVE-2013-4248.patch
Patch235: php-5.3.3-CVE-2013-6420.patch
Patch236: php-5.3.3-CVE-2014-0237.patch
Patch237: php-5.3.3-CVE-2014-0238.patch
Patch238: php-5.3.3-CVE-2014-2270.patch
Patch239: php-5.3.3-CVE-2014-1943.patch
Patch240: php-5.3.3-CVE-2014-3479.patch
Patch241: php-5.3.3-CVE-2012-1571.patch
Patch242: php-5.3.3-CVE-2014-3480.patch
Patch243: php-5.3.3-CVE-2014-4721.patch
Patch244: php-5.3.3-CVE-2013-6712.patch
Patch245: php-5.3.3-CVE-2014-4049.patch
Patch246: php-5.3.3-CVE-2014-3515.patch
Patch247: php-5.3.3-CVE-2014-2497.patch
Patch248: php-5.3.3-CVE-2014-3587.patch
Patch249: php-5.3.3-CVE-2014-3597.patch
Patch250: php-5.3.3-CVE-2014-4698.patch
Patch251: php-5.3.3-CVE-2014-4670.patch
Patch252: php-5.3.3-CVE-2014-3668.patch
Patch253: php-5.3.3-CVE-2014-3669.patch
Patch254: php-5.3.3-CVE-2014-3670.patch
Patch255: php-5.3.3-CVE-2014-3710.patch
Patch256: php-5.3.3-CVE-2014-9425.patch
Patch257: php-5.3.3-CVE-2015-0232.patch
Patch258: php-5.3.3-CVE-2014-9709.patch
Patch259: php-5.3.3-CVE-2015-0273.patch
Patch260: php-5.3.3-CVE-2014-9705.patch
Patch261: php-5.3.3-CVE-2015-2301.patch
Patch262: php-5.3.3-CVE-2015-2787.patch
Patch263: php-5.3.3-bug69085.patch
Patch264: php-5.3.3-CVE-2015-2783.patch
Patch265: php-5.3.3-CVE-2015-3329.patch
Patch266: php-5.3.3-CVE-2015-4021.patch
Patch267: php-5.3.3-CVE-2015-4022.patch
Patch268: php-5.3.3-CVE-2015-4024.patch
Patch269: php-5.3.3-CVE-2015-4026.patch
Patch270: php-5.3.3-bug69353.patch
Patch271: php-5.3.3-bug69152.patch
Patch272: php-5.3.3-CVE-2015-4644.patch
Patch273: php-5.3.3-CVE-2016-5385.patch
Patch274: php-5.3.3-CVE-2019-11043.patch
# php2shell-eol-backport: minimal fix for CVE-2026-109618 / CVE-2026-109619,
# ported from php-src 712e60f9ed (official PHP 7.4 backport)
Patch9001: php-5.3.3-50.el6_10-cve-2026-109618.patch


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: bzip2-devel, curl-devel >= 7.9, db4-devel, gmp-devel
BuildRequires: httpd-devel >= 2.0.46-1, pam-devel
BuildRequires: libstdc++-devel, openssl-devel, sqlite-devel >= 3.6.0
BuildRequires: zlib-devel, pcre-devel >= 6.6, smtpdaemon, libedit-devel
BuildRequires: bzip2, perl, libtool >= 1.4.3, gcc-c++
Obsoletes: php-dbg, php3, phpfi, stronghold-php
Requires: httpd-mmn = %{httpd_mmn}
Provides: mod_php = %{version}-%{release}
Requires: php-common%{?_isa} = %{version}-%{release}
# For backwards-compatibility, require php-cli for the time being:
Requires: php-cli%{?_isa} = %{version}-%{release}
# To ensure correct /var/lib/php/session ownership:
Requires(pre): httpd

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated webpages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. 

The php package contains the module which adds support for the PHP
language to Apache HTTP Server.

%package cli
Group: Development/Languages
Summary: Command-line interface for PHP
Requires: php-common%{?_isa} = %{version}-%{release}
Provides: php-cgi = %{version}-%{release}
Provides: php-pcntl, php-readline

%description cli
The php-cli package contains the command-line interface 
executing PHP scripts, /usr/bin/php, and the CGI interface.

%package zts
Group: Development/Languages
Summary: Thread-safe PHP interpreter for use with the Apache HTTP Server
Requires: php-common%{?_isa} = %{version}-%{release}
Requires: httpd-mmn = %{httpd_mmn}
BuildRequires: libtool-ltdl-devel

%description zts
The php-zts package contains a module for use with the Apache HTTP
Server which can operate under a threaded server processing model.

%package fpm
Group: Development/Languages
Summary: PHP FastCGI Process Manager
Requires: php-common%{?_isa} = %{version}-%{release}
Requires(pre): /usr/sbin/useradd
Requires(preun): initscripts
Requires(postun): initscripts

%description fpm
PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI
implementation with some additional features useful for sites of
any size, especially busier sites.

%package common
Group: Development/Languages
Summary: Common files for PHP
# ABI/API/Version check
Provides: php-api = %{apiver}, php-zend-abi = %{zendver}
Provides: php(api) = %{apiver}, php(zend-abi) = %{zendver}
Provides: php(language) = %{version}
# Provides for all builtin modules:
Provides: php-bz2, php-calendar, php-ctype, php-curl, php-date, php-exif
Provides: php-ftp, php-gettext, php-gmp, php-hash, php-iconv, php-libxml
Provides: php-reflection, php-session, php-shmop, php-simplexml, php-sockets
Provides: php-spl, php-tokenizer, php-openssl, php-pcre
Provides: php-zlib, php-json, php-zip, php-fileinfo
Provides: php-core, php-ereg, php-filter, php-phar, php-standard
Obsoletes: php-openssl, php-pecl-zip, php-pecl-json, php-json, php-pecl-phar, php-pecl-Fileinfo
# For obsoleted pecl extension
Provides: php-pecl-json = %{jsonver}, php-pecl(json) = %{jsonver}
Provides: php-pecl-zip = %{zipver}, php-pecl(zip) = %{zipver}
Provides: php-pecl-phar = %{pharver}, php-pecl(phar) = %{pharver}
Provides: php-pecl-Fileinfo = %{fileinfover}, php-pecl(Fileinfo) = %{fileinfover}

%description common
The php-common package contains files used by both the php
package and the php-cli package.

%package devel
Group: Development/Libraries
Summary: Files needed for building PHP extensions
Requires: php%{?_isa} = %{version}-%{release}, autoconf, automake
Obsoletes: php-pecl-pdo-devel

%description devel
The php-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%package imap
Summary: A module for PHP applications that use IMAP
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
Obsoletes: mod_php3-imap, stronghold-php-imap
BuildRequires: krb5-devel, openssl-devel, libc-client-devel

%description imap
The php-imap package contains a dynamic shared object that will
add support for the IMAP protocol to PHP.

%package ldap
Summary: A module for PHP applications that use LDAP
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
Obsoletes: mod_php3-ldap, stronghold-php-ldap
BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel

%description ldap
The php-ldap package is a dynamic shared object (DSO) for the Apache
Web server that adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language. If you need LDAP support for PHP applications, you will
need to install this package in addition to the php package.

%package pdo
Summary: A database access abstraction module for PHP applications
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
Obsoletes: php-pecl-pdo-sqlite, php-pecl-pdo
Provides: php-pdo-abi = %{pdover}
Provides: php-sqlite3, php-pdo_sqlite

%description pdo
The php-pdo package contains a dynamic shared object that will add
a database access abstraction layer to PHP.  This module provides
a common interface for accessing MySQL, PostgreSQL or other 
databases.

%package mysql
Summary: A module for PHP applications that use MySQL databases
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}, php-pdo%{?_isa}
Provides: php_database, php-mysqli, php-pdo_mysql
Obsoletes: mod_php3-mysql, stronghold-php-mysql
BuildRequires: mysql-devel >= 4.1.0

%description mysql
The php-mysql package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php package.

%package pgsql
Summary: A PostgreSQL database module for PHP
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}, php-pdo%{?_isa}
Provides: php_database, php-pdo_pgsql
Obsoletes: mod_php3-pgsql, stronghold-php-pgsql
BuildRequires: krb5-devel, openssl-devel, postgresql-devel

%description pgsql
The php-pgsql package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL database
support to PHP. PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.

%package process
Summary: Modules for PHP script using system process interfaces
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
Provides: php-posix, php-sysvsem, php-sysvshm, php-sysvmsg

%description process
The php-process package contains dynamic shared objects which add
support to PHP using system interfaces for inter-process
communication.

%package odbc
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}, php-pdo%{?_isa}
Summary: A module for PHP applications that use ODBC databases
Provides: php_database, php-pdo_odbc
Obsoletes: stronghold-php-odbc
BuildRequires: unixODBC-devel

%description odbc
The php-odbc package contains a dynamic shared object that will add
database support through ODBC to PHP. ODBC is an open specification
which provides a consistent API for developers to use for accessing
data sources (which are often, but not always, databases). PHP is an
HTML-embeddable scripting language. If you need ODBC support for PHP
applications, you will need to install this package and the php
package.

%package soap
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
Summary: A module for PHP applications that use the SOAP protocol
BuildRequires: libxml2-devel

%description soap
The php-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%package snmp
Summary: A module for PHP applications that query SNMP-managed devices
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}, net-snmp
BuildRequires: net-snmp-devel

%description snmp
The php-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package xml
Summary: A module for PHP applications which use XML
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
Obsoletes: php-domxml, php-dom
Provides: php-dom, php-xsl, php-domxml, php-wddx
Provides: php-xmlreader, php-xmlwriter
BuildRequires: libxslt-devel >= 1.0.18-1, libxml2-devel >= 2.4.14-1

%description xml
The php-xml package contains dynamic shared objects which add support
to PHP for manipulating XML documents using the DOM tree,
and performing XSL transformations on XML documents.

%package xmlrpc
Summary: A module for PHP applications which use the XML-RPC protocol
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}

%description xmlrpc
The php-xmlrpc package contains a dynamic shared object that will add
support for the XML-RPC protocol to PHP.

%package mbstring
Summary: A module for PHP applications which need multi-byte string handling
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}

%description mbstring
The php-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package gd
Summary: A module for PHP applications for using the gd graphics library
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
# Required to build the bundled GD library
BuildRequires: libXpm-devel, libjpeg-devel, libpng-devel, freetype-devel

%description gd
The php-gd package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%package bcmath
Summary: A module for PHP applications for using the bcmath library
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}

%description bcmath
The php-bcmath package contains a dynamic shared object that will add
support for using the bcmath library to PHP.

%package dba
Summary: A database abstraction layer module for PHP applications
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}

%description dba
The php-dba package contains a dynamic shared object that will add
support for using the DBA database abstraction layer to PHP.

%package tidy
Summary: Standard PHP module provides tidy library support
Group: Development/Languages
Requires: php-common%{?_isa} = %{version}-%{release}
BuildRequires: libtidy-devel

%description tidy
The php-tidy package contains a dynamic shared object that will add
support for using the tidy library to PHP.

%package embedded
Summary: PHP library for embedding in applications
Group: System Environment/Libraries
Requires: php-common%{?_isa} = %{version}-%{release}
# doing a real -devel package for just the .so symlink is a bit overkill
Provides: php-embedded-devel = %{version}-%{release}

%description embedded
The php-embedded package contains a library which can be embedded
into applications to provide PHP scripting language support.

%package pspell
Summary: A module for PHP applications for using pspell interfaces
Group: System Environment/Libraries
Requires: php-common%{?_isa} = %{version}-%{release}
BuildRequires: aspell-devel >= 0.50.0

%description pspell
The php-pspell package contains a dynamic shared object that will add
support for using the pspell library to PHP.

%package recode
Summary: A module for PHP applications for using the recode library
Group: System Environment/Libraries
Requires: php-common%{?_isa} = %{version}-%{release}
BuildRequires: recode-devel

%description recode
The php-recode package contains a dynamic shared object that will add
support for using the recode library to PHP.

%package intl
Summary: Internationalization extension for PHP applications
Group: System Environment/Libraries
Requires: php-common%{?_isa} = %{version}-%{release}
BuildRequires: libicu-devel >= 3.6

%description intl
The php-intl package contains a dynamic shared object that will add
support for using the ICU library to PHP.

%package enchant
Summary: Human Language and Character Encoding Support
Group: System Environment/Libraries
Requires: php-common%{?_isa} = %{version}-%{release}
BuildRequires: enchant-devel >= 1.2.4

%description enchant
The php-intl package contains a dynamic shared object that will add
support for using the enchant library to PHP.


%prep
%setup -q -a 10

%patch1 -p1 -b .gnusrc
%patch2 -p1 -b .install
%patch3 -p1 -b .norpath
%patch4 -p1 -b .phpize64
%patch5 -p1 -b .includedir
%patch6 -p1 -b .embed
%patch7 -p1 -b .recode
%patch8 -p1 -b .aconf26x

%patch20 -p1 -b .shutdown
%patch21 -p1 -b .zipmemset
%patch22 -p1 -b .pdooverflow
%patch23 -p1 -b .pdo53551
%patch24 -p1 -b .streams
%patch25 -p1 -b .imapauth
%patch26 -p1 -b .pdoodbc
%patch27 -p1 -b .bug53592

%patch40 -p1 -b .dlopen
%patch41 -p1 -b .easter
%patch42 -p1 -b .systzdata
%patch43 -p1 -b .getmodinit

%patch61 -p1 -b .tests-wddx

%patch100 -p1 -b .extrglob
%patch101 -p1 -b .varnegidx
%patch102 -p1 -b .setdate
%patch103 -p1 -b .fpmcovscan
%patch104 -p1 -b .zendgc
%patch106 -p1 -b .copy
%patch107 -p1 -b .errorhandler
%patch108 -p1 -b .bug54268
%patch109 -p1 -b .pdopgsql
%patch110 -p0 -b .bug66762
%patch111 -p1 -b .bug52636
%patch112 -p1 -b .rfc2616
%patch113 -p1 -b .r305043
%patch114 -p1 -b .bug53141
%patch115 -p1 -b .ivlength
%patch116 -p1 -b .bug54609
%patch117 -p1 -b .curltls
%patch118 -p1 -b .bug63635

%patch200 -p1 -b .cve3709
%patch201 -p1 -b .cve3870
%patch202 -p1 -b .cve3710

%patch203 -p1 -b .cve4645
%patch204 -p1 -b .cve4156

%patch205 -p1 -b .cve0708
%patch206 -p1 -b .cve1148
%patch207 -p1 -b .cve1466
%patch208 -p1 -b .cve1468
%patch209 -p1 -b .cve1469
%patch210 -p1 -b .cve1470
%patch211 -p1 -b .cve1471
%patch212 -p1 -b .cve1938
%patch213 -p1 -b .cve2202
%patch214 -p1 -b .cve2483

%patch215 -p1 -b .cve4885
%patch216 -p1 -b .cve4566
%patch217 -p1 -b .cve0830
%patch218 -p1 -b .cve1823
%patch219 -p1 -b .cve2336

%patch220 -p1 -b .cve4153
%patch221 -p1 -b .cve0781
%patch222 -p1 -b .cve1172
%patch223 -p1 -b .cve2143
%patch224 -p1 -b .cve2386
%patch225 -p1 -b .cve0057
%patch226 -p1 -b .cve0789
%patch227 -p1 -b .cve2950
%patch228 -p1 -b .cve2688
%patch229 -p1 -b .cve0831
%patch230 -p1 -b .cve1398
%patch231 -p1 -b .cve1643
%patch232 -p1 -b .cve7243
%patch233 -p1 -b .cve4113
%patch234 -p1 -b .cve4248
%patch235 -p1 -b .cve6420
%patch236 -p1 -b .cve0237
%patch237 -p1 -b .cve0238
%patch238 -p1 -b .cve2270
%patch239 -p1 -b .cve1943
%patch240 -p1 -b .cve3479
%patch241 -p1 -b .cve1571
%patch242 -p1 -b .cve3480
%patch243 -p1 -b .cve4721
%patch244 -p1 -b .cve6712
%patch245 -p1 -b .cve4049
%patch246 -p1 -b .cve3515
%patch247 -p1 -b .cve2497
%patch248 -p1 -b .cve3587
%patch249 -p1 -b .cve3597
%patch250 -p1 -b .cve4698
%patch251 -p1 -b .cve4670
%patch252 -p1 -b .cve3668
%patch253 -p1 -b .cve3669
%patch254 -p1 -b .cve3670
%patch255 -p1 -b .cve3710
%patch256 -p1 -b .cve9425
%patch257 -p1 -b .cve0232
%patch258 -p1 -b .cve9709
%patch259 -p1 -b .cve0273
%patch260 -p1 -b .cve9705
%patch261 -p1 -b .cve2301
%patch262 -p1 -b .cve2787
%patch263 -p1 -b .bug69085
%patch264 -p1 -b .cve2783
%patch265 -p1 -b .cve3329
%patch266 -p1 -b .cve4021
%patch267 -p1 -b .cve4022
%patch268 -p1 -b .cve4024
%patch269 -p1 -b .cve4026
%patch270 -p1 -b .bug69353
%patch271 -p1 -b .bug69152
%patch272 -p1 -b .cve4644
%patch273 -p1 -b .cve5385
%patch274 -p1 -b .cve11043
%patch9001 -p1 -b .php2shell

# Prevent %%doc confusion over LICENSE files
cp Zend/LICENSE Zend/ZEND_LICENSE
cp TSRM/LICENSE TSRM_LICENSE
cp ext/ereg/regex/COPYRIGHT regex_COPYRIGHT
cp ext/gd/libgd/README gd_README

# Multiple builds for multiple SAPIs
mkdir build-cgi build-apache build-embedded build-zts build-fpm

# Remove bogus test; position of read position after fopen(, "a+")
# is not defined by C standard, so don't presume anything.
rm -f ext/standard/tests/file/bug21131.phpt

# Tests that fail.
rm -f ext/standard/tests/file/bug22414.phpt \
      ext/iconv/tests/bug16069.phpt

# Safety check for API version change.
vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
   : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
   : Update the zendver macro and rebuild.
   exit 1
fi

# Safety check for PDO ABI version change
vpdo=`sed -n '/#define PDO_DRIVER_API/{s/.*[ 	]//;p}' ext/pdo/php_pdo_driver.h`
if test "x${vpdo}" != "x%{pdover}"; then
   : Error: Upstream PDO ABI version is now ${vpdo}, expecting %{pdover}.
   : Update the pdover macro and rebuild.
   exit 1
fi

# Check for some extension version
ver=$(sed -n '/#define PHP_FILEINFO_VERSION /{s/.* "//;s/".*$//;p}' ext/fileinfo/php_fileinfo.h)
if test "$ver" != "%{fileinfover}"; then
   : Error: Upstream FILEINFO version is now ${ver}, expecting %{fileinfover}.
   : Update the fileinfover macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_PHAR_VERSION /{s/.* "//;s/".*$//;p}' ext/phar/php_phar.h)
if test "$ver" != "%{pharver}"; then
   : Error: Upstream PHAR version is now ${ver}, expecting %{pharver}.
   : Update the pharver macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_ZIP_VERSION_STRING /{s/.* "//;s/".*$//;p}' ext/zip/php_zip.h)
if test "$ver" != "%{zipver}"; then
   : Error: Upstream ZIP version is now ${ver}, expecting %{zipver}.
   : Update the zipver macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_JSON_VERSION /{s/.* "//;s/".*$//;p}' ext/json/php_json.h)
if test "$ver" != "%{jsonver}"; then
   : Error: Upstream JSON version is now ${ver}, expecting %{jsonver}.
   : Update the jsonver macro and rebuild.
   exit 1
fi

# Fix some bogus permissions
find . -name \*.[ch] -exec chmod 644 {} \;
find . -name \*.cpp  -exec chmod 644 {} \;
chmod 644 README.*

%build
# aclocal workaround - to be improved
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >>aclocal.m4

# Force use of system libtool:
libtoolize --force --copy
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4

# Regenerate configure scripts (patches change config.m4's)
touch configure.in
./buildconf --force

CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
export CFLAGS

# Install extension modules in %{_libdir}/php/modules.
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{_datadir}/pear; export PEAR_INSTALLDIR

# Shell function to configure and build a PHP tree.
build() {
# bison-1.875-2 seems to produce a broken parser; workaround.
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
ln -sf ../configure
%configure \
	--cache-file=../config.cache \
        --with-libdir=%{_lib} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/php.d \
	--disable-debug \
	--with-pic \
	--disable-rpath \
	--without-pear \
	--with-bz2 \
	--with-exec-dir=%{_bindir} \
	--with-freetype-dir=%{_prefix} \
	--with-png-dir=%{_prefix} \
	--with-xpm-dir=%{_prefix} \
	--enable-gd-native-ttf \
	--without-gdbm \
	--with-gettext \
	--with-gmp \
	--with-iconv \
	--with-jpeg-dir=%{_prefix} \
	--with-openssl \
        --with-pcre-regex=%{_prefix} \
	--with-zlib \
	--with-layout=GNU \
	--enable-exif \
	--enable-ftp \
	--enable-magic-quotes \
	--enable-sockets \
	--enable-sysvsem --enable-sysvshm --enable-sysvmsg \
	--with-kerberos \
	--enable-ucd-snmp-hack \
	--enable-shmop \
	--enable-calendar \
        --without-sqlite \
        --with-libxml-dir=%{_prefix} \
	--enable-xml \
        --with-system-tzdata \
	$* 
if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi

make %{?_smp_mflags}
}

# Build /usr/bin/php-cgi with the CGI SAPI, and all the shared extensions
pushd build-cgi
build --enable-force-cgi-redirect \
      --enable-pcntl \
      --with-imap=shared --with-imap-ssl \
      --enable-mbstring=shared \
      --enable-mbregex \
      --with-gd=shared \
      --enable-bcmath=shared \
      --enable-dba=shared --with-db4=%{_prefix} \
      --with-xmlrpc=shared \
      --with-ldap=shared --with-ldap-sasl \
      --with-mysql=shared,%{_prefix} \
      --with-mysqli=shared,%{mysql_config} \
      --enable-dom=shared \
      --with-pgsql=shared \
      --enable-wddx=shared \
      --with-snmp=shared,%{_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --with-curl=shared,%{_prefix} \
      --enable-fastcgi \
      --enable-pdo=shared \
      --with-pdo-odbc=shared,unixODBC,%{_prefix} \
      --with-pdo-mysql=shared,%{mysql_config} \
      --with-pdo-pgsql=shared,%{_prefix} \
      --with-pdo-sqlite=shared,%{_prefix} \
      --with-sqlite3=shared,%{_prefix} \
      --enable-json=shared \
      --enable-zip=shared \
      --without-readline \
      --with-libedit \
      --with-pspell=shared \
      --enable-phar=shared \
      --with-tidy=shared,%{_prefix} \
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-posix=shared \
      --with-unixODBC=shared,%{_prefix} \
      --enable-fileinfo=shared \
      --enable-intl=shared \
      --with-icu-dir=%{_prefix} \
      --with-enchant=shared,%{_prefix} \
      --with-recode=shared,%{_prefix}
popd

without_shared="--without-mysql --without-gd \
      --disable-dom --disable-dba --without-unixODBC \
      --disable-pdo --disable-xmlreader --disable-xmlwriter \
      --without-sqlite3 --disable-phar --disable-fileinfo \
      --disable-json --without-pspell --disable-wddx \
      --without-curl --disable-posix \
      --disable-sysvmsg --disable-sysvshm --disable-sysvsem"

# Build Apache module, and the CLI SAPI, /usr/bin/php
pushd build-apache
build --with-apxs2=%{_sbindir}/apxs ${without_shared}
popd

# Build php-fpm
pushd build-fpm
build --enable-fpm ${without_shared}
popd

# Build for inclusion as embedded script language into applications,
# /usr/lib[64]/libphp5.so
pushd build-embedded
build --enable-embed ${without_shared}
popd

# Build a special thread-safe Apache SAPI
pushd build-zts
EXTENSION_DIR=%{_libdir}/php/modules-zts
build --with-apxs2=%{_sbindir}/apxs ${without_shared} \
      --enable-maintainer-zts \
      --with-config-file-scan-dir=%{_sysconfdir}/php-zts.d
popd

### NOTE!!! EXTENSION_DIR was changed for the -zts build, so it must remain
### the last SAPI to be built.

%check
cd build-apache
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
unset TZ LANG LC_ALL
if ! make test; then
  set +x
  for f in `find .. -name \*.diff -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
  done
  set -x
  #exit 1
fi
unset NO_INTERACTION REPORT_EXIT_STATUS MALLOC_CHECK_

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Install the version for embedded script language in applications + php_embed.h
make -C build-embedded install-sapi install-headers INSTALL_ROOT=$RPM_BUILD_ROOT

# Install the php-fpm binary
make -C build-fpm install-fpm INSTALL_ROOT=$RPM_BUILD_ROOT

# Install everything from the CGI SAPI build
make -C build-cgi install INSTALL_ROOT=$RPM_BUILD_ROOT 

# Install the default configuration file and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
install -m 644    *.gif $RPM_BUILD_ROOT%{contentdir}/icons/

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/php/pear \
                  $RPM_BUILD_ROOT%{_datadir}/php

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules

# install the ZTS DSO
install -m 755 build-zts/libs/libphp5.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/libphp5-zts.so

# Apache config fragment
install -m 755 -d $RPM_BUILD_ROOT/etc/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/php.conf $RPM_BUILD_ROOT/etc/httpd/conf.d

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
#install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php/session

# PHP-FPM stuff
# Log
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/php-fpm
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/php-fpm
# Config
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/www.conf
mv $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf.default .
# Service
install -m 755 -d $RPM_BUILD_ROOT%{_initddir}
install -m 755 %{SOURCE9} $RPM_BUILD_ROOT%{_initddir}/php-fpm
# LogRotate
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/php-fpm
# Environment file
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/php-fpm

# Fix the link
(cd $RPM_BUILD_ROOT%{_bindir}; ln -sfn phar.phar phar)

# Generate files lists and stub .ini files for each subpackage
for mod in pgsql mysql mysqli odbc ldap snmp xmlrpc imap \
    mbstring gd dom xsl soap bcmath dba xmlreader xmlwriter \
    pdo pdo_mysql pdo_pgsql pdo_odbc pdo_sqlite json zip \
    sqlite3 enchant phar fileinfo intl \
    tidy pspell curl wddx \
    posix sysvshm sysvsem sysvmsg recode; do
    cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
    cat > files.${mod} <<EOF
%attr(755,root,root) %{_libdir}/php/modules/${mod}.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/${mod}.ini
EOF
done

# The dom, xsl and xml* modules are all packaged in php-xml
cat files.dom files.xsl files.xml{reader,writer} files.wddx > files.xml

# The mysql and mysqli modules are both packaged in php-mysql
cat files.mysqli >> files.mysql

# Split out the PDO modules
cat files.pdo_mysql >> files.mysql
cat files.pdo_pgsql >> files.pgsql
cat files.pdo_odbc >> files.odbc

# sysv* and posix in packaged in php-process
cat files.sysv* files.posix > files.process

# Package sqlite3 and pdo_sqlite with pdo; isolating the sqlite dependency
# isn't useful at this time since rpm itself requires sqlite.
cat files.pdo_sqlite >> files.pdo
cat files.sqlite3 >> files.pdo

# Package json, zip, curl, phar and fileinfo in -common.
cat files.json files.zip files.curl files.phar files.fileinfo > files.common

# Install the macros file:
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rpm
sed -e "s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/;s/@PHP_PDOVER@/%{pdover}/" \
    -e "s/@PHP_VERSION@/%{version}/" \
    < $RPM_SOURCE_DIR/macros.php > macros.php
install -m 644 -c macros.php \
           $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.php

# Remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/php/modules/*.a \
       $RPM_BUILD_ROOT%{_bindir}/{phptar} \
       $RPM_BUILD_ROOT%{_datadir}/pear \
       $RPM_BUILD_ROOT%{_libdir}/libphp5.la

# Remove irrelevant docs
rm -f README.{Zeus,QNX,CVS-RULES}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
rm files.* macros.php

%post embedded -p /sbin/ldconfig
%postun embedded -p /sbin/ldconfig

%pre fpm
# Add the "apache" user
getent group  apache >/dev/null || \
  groupadd -g 48 -r apache
getent passwd apache >/dev/null || \
  useradd -r -u 48 -g apache -s /sbin/nologin \
    -d %{contentdir} -c "Apache" apache
exit 0

%post fpm
if [ $1 = 1 ]; then
    # Initial installation
    /sbin/chkconfig --add php-fpm
fi

%preun fpm
if [ $1 = 0 ]; then
    # Package removal, not upgrade
    /sbin/service php-fpm stop >/dev/null 2>&1
    /sbin/chkconfig --del php-fpm
fi

%postun fpm
if [ $1 -ge 1 ]; then
    /sbin/service php-fpm condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root)
%{_libdir}/httpd/modules/libphp5.so
%attr(0770,root,apache) %dir %{_localstatedir}/lib/php/session
%config(noreplace) %{_sysconfdir}/httpd/conf.d/php.conf
%{contentdir}/icons/php.gif

%files common -f files.common
%defattr(-,root,root)
%doc CODING_STANDARDS CREDITS EXTENSIONS INSTALL LICENSE NEWS README*
%doc Zend/ZEND_* TSRM_LICENSE regex_COPYRIGHT
%doc php.ini-production php.ini-development
%config(noreplace) %{_sysconfdir}/php.ini
%dir %{_sysconfdir}/php.d
#dir %{_sysconfdir}/php-zts.d
%dir %{_libdir}/php
%dir %{_libdir}/php/modules
#dir %{_libdir}/php/modules-zts
%dir %{_localstatedir}/lib/php
%dir %{_libdir}/php/pear
%dir %{_datadir}/php

%files cli
%defattr(-,root,root)
%{_bindir}/php
%{_bindir}/php-cgi
%{_bindir}/phar.phar
%{_bindir}/phar
%{_mandir}/man1/php.1*
%doc sapi/cgi/README* sapi/cli/README

%files zts
%defattr(-,root,root)
%{_libdir}/httpd/modules/libphp5-zts.so

%files fpm
%defattr(-,root,root)
%doc php-fpm.conf.default
%doc sapi/fpm/LICENSE
%config(noreplace) %{_sysconfdir}/php-fpm.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/www.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/php-fpm
%config(noreplace) %{_sysconfdir}/sysconfig/php-fpm
%{_initddir}/php-fpm
%{_sbindir}/php-fpm
%dir %{_sysconfdir}/php-fpm.d
# log owned by apache for log
%attr(770,apache,root) %dir %{_localstatedir}/log/php-fpm
%dir %{_localstatedir}/run/php-fpm
%{_mandir}/man8/php-fpm.8*
%{_datadir}/fpm/status.html

%files devel
%defattr(-,root,root)
%{_bindir}/php-config
%{_bindir}/phpize
%{_includedir}/php
%{_libdir}/php/build
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*
%config %{_sysconfdir}/rpm/macros.php

%files embedded
%defattr(-,root,root,-)
%{_libdir}/libphp5.so
%{_libdir}/libphp5-%{version}.so

%files pgsql -f files.pgsql
%files mysql -f files.mysql
%files odbc -f files.odbc
%files imap -f files.imap
%files ldap -f files.ldap
%files snmp -f files.snmp
%files xml -f files.xml
%files xmlrpc -f files.xmlrpc
%files mbstring -f files.mbstring
%files gd -f files.gd
%defattr(-,root,root)
%doc gd_README
%files soap -f files.soap
%files bcmath -f files.bcmath
%files dba -f files.dba
%files pdo -f files.pdo
%files tidy -f files.tidy
%files pspell -f files.pspell
%files intl -f files.intl
%files process -f files.process
%files recode -f files.recode
%files enchant -f files.enchant


%changelog
* Thu Oct 22 2026 Oleksii Molchanov <2106429+alvm@users.noreply.github.com> - 5.3.3-50.php2shell.1
- Fix CVE-2026-109618 and CVE-2026-109619 (php2shell): port of the minimal
  upstream fix "Avoid state corruption via bailout" (php-src 712e60f9ed)

* Tue Oct 29 2019 Remi Collet <rcollet@redhat.com> - 5.3.3-50
- fix underflow in env_path_info in fpm_main.c CVE-2019-11043

* Mon Nov  7 2016 Remi Collet <rcollet@redhat.com> - 5.3.3-49
- fix php-soap fails to connect to HTTPS web service sporadically
  as stream_socket_enable_crypto() uses NONBLOCK #1283153

* Mon Jul 25 2016 Remi Collet <rcollet@redhat.com> - 5.3.3-48
- don't set environmental variable based on user supplied Proxy
  request header CVE-2016-5385

* Wed Dec  9 2015 Remi Collet <rcollet@redhat.com> - 5.3.3-47
- fix wrong warning in openssl_encrypt() for missing IV
  when IV is not required #1260315
- fix segfault's when you try and allocate an SplFixedArray
  with size >= 9999 #1071344
- segfault in php_pgsql_meta_data CVE-2015-4644  #1234434
- add options to enable TLS in curl #1255920
- fix segfault in gc_collect_cycles #1122681

* Fri Jul  3 2015 Remi Collet <rcollet@redhat.com> - 5.3.3-46
- fix gzfile accept paths with NUL character #1213407
- fix patch for CVE-2015-4024

* Wed Jun 10 2015 Remi Collet <rcollet@redhat.com> - 5.3.3-45
- fix more functions accept paths with NUL character #1213407

* Mon Jun  8 2015 Remi Collet <rcollet@redhat.com> - 5.3.3-44
- soap: missing fix for #1222538 and #1204868

* Fri Jun  5 2015 Remi Collet <rcollet@redhat.com> - 5.3.3-43
- core: fix multipart/form-data request can use excessive
  amount of CPU usage CVE-2015-4024
- fix various functions accept paths with NUL character
  CVE-2015-4026, #1213407
- ftp: fix integer overflow leading to heap overflow when
  reading FTP file listing CVE-2015-4022
- phar: fix buffer over-read in metadata parsing CVE-2015-2783
- phar: invalid pointer free() in phar_tar_process_metadata()
  CVE-2015-3307
- phar: fix buffer overflow in phar_set_inode() CVE-2015-3329
- phar: fix memory corruption in phar_parse_tarfile caused by
  empty entry file name CVE-2015-4021
- soap: more fix type confusion through unserialize #1222538

* Mon Apr 13 2015 Remi Collet <rcollet@redhat.com> - 5.3.3-42
- soap: more fix type confusion through unserialize #1204868

* Thu Apr  9 2015 Remi Collet <rcollet@redhat.com> - 5.3.3-41
- core: fix double in zend_ts_hash_graceful_destroy CVE-2014-9425
- core: fix use-after-free in unserialize CVE-2015-2787
- exif: fix free on unitialized pointer CVE-2015-0232
- gd: fix buffer read overflow in gd_gif.c CVE-2014-9709
- date: fix use after free vulnerability in unserialize CVE-2015-0273
- enchant: fix heap buffer overflow in enchant_broker_request_dict
  CVE-2014-9705
- phar: use after free in phar_object.c CVE-2015-2301
- soap: fix type confusion through unserialize

* Thu Oct 23 2014 Jan Kaluza <jkaluza@redhat.com> - 5.3.3-40
- fileinfo: fix out-of-bounds read in elf note headers. CVE-2014-3710

* Tue Oct 21 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-39
- xmlrpc: fix out-of-bounds read flaw in mkgmtime() CVE-2014-3668
- core: fix integer overflow in unserialize() CVE-2014-3669
- exif: fix heap corruption issue in exif_thumbnail() CVE-2014-3670

* Wed Sep 10 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-38
- spl: fix use-after-free in ArrayIterator due to object
  change during sorting. CVE-2014-4698
- spl: fix use-after-free in SPL Iterators. CVE-2014-4670

* Thu Aug 14 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-37
- gd: fix NULL pointer dereference in gdImageCreateFromXpm.
  CVE-2014-2497
- fileinfo: fix incomplete fix for CVE-2012-1571 in
  cdf_read_property_info. CVE-2014-3587
- core: fix incomplete fix for CVE-2014-4049 DNS TXT
  record parsing. CVE-2014-3597

* Tue Jul 15 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-36
- core: type confusion issue in phpinfo(). CVE-2014-4721
- date: fix heap-based buffer over-read in DateInterval. CVE-2013-6712
- core: fix heap-based buffer overflow in DNS TXT record parsing.
  CVE-2014-4049
- core: unserialize() SPL ArrayObject / SPLObjectStorage type
  confusion flaw. CVE-2014-3515

* Tue Jul  1 2014 Jan Kaluza <jkaluza@redhat.com> - 5.3.3-35
- fileinfo: out-of-bounds memory access in fileinfo. CVE-2014-2270
- fileinfo: unrestricted recursion in handling of indirect type
  rules. CVE-2014-1943
- fileinfo: out of bounds read in CDF parser. CVE-2012-1571
- fileinfo: cdf_check_stream_offset boundary check. CVE-2014-3479
- fileinfo: cdf_count_chain insufficient boundary check. CVE-2014-3480

* Fri Jun 13 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-34
- fileinfo: cdf_unpack_summary_info() excessive looping
  DoS. CVE-2014-0237
- fileinfo: CDF property info parsing nelements infinite
  loop. CVE-2014-0238

* Wed Jun  4 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-33
- add php_get_module_initialized internal function (#1053301)

* Tue May 27 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-31
- soap: fixRFC2616 transgression (#1045019)
- fix static calling in non-static method (#953786)
- fix autoload called from closing session (#954027)

* Mon May 12 2014 Remi Collet <rcollet@redhat.com> - 5.3.3-29
- drop unneeded part of CVE-2006-724.patch and fileinfo.patch
  extension not provided or git binary patches (#1064027)
- odbc: fix incompatible pointer type (#1053982)
- mysqli: fix possible segfault in mysqli_stmt::bind_result
  php bug 66762 (#1069167)
- mysql: fix php_mysql_fetch_hash writes long value into int
  php bug 52636 (#1054953)

* Thu Dec  5 2013 Remi Collet <rcollet@redhat.com> - 5.3.3-27
- add security fix for CVE-2013-6420

* Mon Aug 19 2013 Remi Collet <rcollet@redhat.com> - 5.3.3-26
- add security fix for CVE-2013-4248

* Fri Jul 26 2013 Remi Collet <rcollet@redhat.com> - 5.3.3-25
- rename patch to math CVE-2010-3709 name
- add security fixes for CVE-2006-7243, CVE-2013-1643

* Mon Jul 22 2013 Remi Collet <rcollet@redhat.com> - 5.3.3-24
- fix buffer overflow in _pdo_pgsql_error (#969110)
- fix double free when destroy_zend_class fails (#910466)
- fix segfault in error_handler with
  allow_call_time_pass_reference = Off (#892158)
- fix copy doesn't report failure on partial copy (#947428)
- add rpm macros for packagers: %%php_inidir,
  %%php_incldir and %%__php (#953814)

* Fri Jul 12 2013 Remi Collet <rcollet@redhat.com> - 5.3.3-23
- add security fix for CVE-2013-4113

* Thu Nov 29 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-22
- php-xml provides php-xmlreader and php-xmlwriter (#874987)
- fix possible NULL derefence and buffer overflow (#879179)
- fix zend garbage collector (#848186, #868375)

* Tue Oct 23 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-21
- fix CVE reference in previous changelog entry

* Fri Oct 19 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-20
- remove reproducer from security fix for CVE-2012-0781

* Thu Oct 18 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-19
- add FastCGI Process Manager (php-fpm) SAPI (#806132, #824293)

* Wed Oct 17 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-18
- php script hangs when it exceeds max_execution_time
  when inside an ODBC call (#864951)

* Tue Oct 16 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-17
- add security fixes for CVE-2012-2688, CVE-2012-0831, CVE-2011-1398

* Tue Oct  9 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-16
- fix stream support in fileinfo (#858653)
- fix imap_open DISABLE_AUTHENTICATOR param ignores array (#859371)

* Thu Oct  4 2012 Remi Collet <rcollet@redhat.com> - 5.3.3-15
- fix permission on source files (#676364)
- fix negative keys with var_export (#771738)
- fix setDate when DateTime created from timestamp (#812819)
- add php(language) and missing provides (#837042)
- use arch-specific requires (#833545)
- fix possible buffer overflow in pdo_odbc (#836264)
- fix possible segfault in pdo_mysql (#824199)

* Mon Jun 25 2012 Joe Orton <jorton@redhat.com> - 5.3.3-14
- add security fix for CVE-2010-2950

* Wed Jun 13 2012 Joe Orton <jorton@redhat.com> - 5.3.3-13
- fix tests for CVE-2012-2143, CVE-2012-0789

* Tue Jun 12 2012 Joe Orton <jorton@redhat.com> - 5.3.3-12
- add fix for CVE-2012-2336

* Mon Jun 11 2012 Joe Orton <jorton@redhat.com> - 5.3.3-11
- add security fixes for CVE-2012-0781, CVE-2011-4153, CVE-2012-0057,
  CVE-2012-0789, CVE-2012-1172, CVE-2012-2143, CVE-2012-2386

* Thu May  3 2012 Joe Orton <jorton@redhat.com> - 5.3.3-9
- correct detection of = in CVE-2012-1823 fix (#818607)

* Thu May  3 2012 Joe Orton <jorton@redhat.com> - 5.3.3-8
- add security fix for CVE-2012-1823 (#818607)

* Thu Feb  2 2012 Joe Orton <jorton@redhat.com> - 5.3.3-7
- add security fix for CVE-2012-0830 (#786744)

* Thu Jan 05 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 5.3.3-6
- merge Joe's changes:
- improve CVE-2011-1466 fix to cover CAL_GREGORIAN, CAL_JEWISH
- add security fixes for CVE-2011-2483, CVE-2011-0708, CVE-2011-1148,
  CVE-2011-1466, CVE-2011-1468, CVE-2011-1469, CVE-2011-1470,
  CVE-2011-1471, CVE-2011-1938, and CVE-2011-2202 (#740732)

* Wed Jan 04 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 5.3.3-5
- remove extra php.ini-prod/devel files caused by %%patch -b

* Mon Jan 02 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 5.3.3-4
- add security fixes for CVE-2011-4885, CVE-2011-4566 (#769755)

* Fri Jan 21 2011 Joe Orton <jorton@redhat.com> - 5.3.3-3
- add security fixes for CVE-2010-4645, CVE-2010-4156 (#670439)

* Fri Jan 14 2011 Joe Orton <jorton@redhat.com> - 5.3.3-2
- fix transposed memset arguments in libzip

* Wed Jan 12 2011 Joe Orton <jorton@redhat.com> - 5.3.3-1
- update to 5.3.3 (#645591)
- add security fixes for CVE-2010-3709, CVE-2010-3710,
  CVE-2010-3870, CVE-2009-5016 (#651953)
- prevent extract() cloberring $GLOBALS (#655118)
- ensure correct mysql_config is used in biarch builds

* Tue Aug 17 2010 Joe Orton <jorton@redhat.com> - 5.3.2-6
- add security fixes for CVE-2010-1866, CVE-2010-2094, CVE-2010-1917,
  CVE-2010-2531, MOPS-2010-060 (#624469)

* Fri Aug 13 2010 Joe Orton <jorton@redhat.com> - 5.3.2-5
- add security fix for CVE-2010-0397 (#575712)

* Thu Jun 24 2010 Joe Orton <jorton@redhat.com> - 5.3.2-4
- add security fix for CVE-2010-2225 (#605644)

* Wed May  5 2010 Joe Orton <jorton@redhat.com> - 5.3.2-3
- restore -imap (#586050)

* Fri Mar 26 2010 Joe Orton <jorton@redhat.com> - 5.3.2-2
- remove mcrypt support (#459804, #577257)

* Wed Mar 24 2010 Joe Orton <jorton@redhat.com> - 5.3.2-1
- update to 5.3.2 (#575158, #575712)

* Sat Mar 06 2010 Remi Collet <Fedora@famillecollet.com>
- PHP 5.3.2 Released!
- remove mime_magic option (now provided by fileinfo, by emu)
- add patch for http://bugs.php.net/50578
- remove patch for libedit (upstream)

* Fri Jan 15 2010 Joe Orton <jorton@redhat.com> - 5.3.1-7
- add security fix for CVE-2009-4142 (#552268)

* Fri Dec 18 2009 Joe Orton <jorton@redhat.com> - 5.3.1-6
- drop mssql, pdo_dblib

* Fri Dec 11 2009 Joe Orton <jorton@redhat.com> - 5.3.1-5
- drop imap

* Fri Dec 11 2009 Joe Orton <jorton@redhat.com> - 5.3.1-4
- drop t1lib, interbase/firebird support

* Fri Nov 27 2009 Joe Orton <jorton@redhat.com> - 5.3.1-3
- update to v7 of systzdata patch

* Wed Nov 25 2009 Joe Orton <jorton@redhat.com> - 5.3.1-2
- fix build with autoconf 2.6x

* Fri Nov 20 2009 Remi Collet <Fedora@famillecollet.com> 5.3.1-1
- update to 5.3.1
- remove openssl patch (merged upstream)
- add provides for php-pecl-json
- add prod/devel php.ini in doc

* Tue Nov 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 5.3.0-7
- use libedit instead of readline to resolve licensing issues

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 5.3.0-6
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Joe Orton <jorton@redhat.com> 5.3.0-4
- rediff systzdata patch

* Thu Jul 16 2009 Joe Orton <jorton@redhat.com> 5.3.0-3
- update to v6 of systzdata patch; various fixes

* Tue Jul 14 2009 Joe Orton <jorton@redhat.com> 5.3.0-2
- update to v5 of systzdata patch; parses zone.tab and extracts
  timezone->{country-code,long/lat,comment} mapping table

* Sun Jul 12 2009 Remi Collet <Fedora@famillecollet.com> 5.3.0-1
- update to 5.3.0
- remove ncurses, dbase, mhash extensions
- add enchant, sqlite3, intl, phar, fileinfo extensions
- raise sqlite version to 3.6.0 (for sqlite3, build with --enable-load-extension)
- sync with upstream "production" php.ini

* Sat Jun 21 2009 Remi Collet <Fedora@famillecollet.com> 5.2.10-1
- update to 5.2.10
- add interbase sub-package

* Sat Feb 28 2009 Remi Collet <Fedora@FamilleCollet.com> - 5.2.9-1
- update to 5.2.9

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  5 2009 Joe Orton <jorton@redhat.com> 5.2.8-9
- add recode support, -recode subpackage (#106755)
- add -zts subpackage with ZTS-enabled build of httpd SAPI
- adjust php.conf to use -zts SAPI build for worker MPM

* Wed Feb  4 2009 Joe Orton <jorton@redhat.com> 5.2.8-8
- fix patch fuzz, renumber patches

* Wed Feb  4 2009 Joe Orton <jorton@redhat.com> 5.2.8-7
- drop obsolete configure args
- drop -odbc patch (#483690)

* Mon Jan 26 2009 Joe Orton <jorton@redhat.com> 5.2.8-5
- split out sysvshm, sysvsem, sysvmsg, posix into php-process

* Sun Jan 25 2009 Joe Orton <jorton@redhat.com> 5.2.8-4
- move wddx to php-xml, build curl shared in -common
- remove BR for expat-devel, bogus configure option

* Fri Jan 23 2009 Joe Orton <jorton@redhat.com> 5.2.8-3
- rebuild for new MySQL

* Sat Dec 13 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.8-2
- libtool 2 workaround for phpize (#476004)
- add missing php_embed.h (#457777)

* Tue Dec 09 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.8-1
- update to 5.2.8

* Sat Dec 06 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.7-1.1
- libtool 2 workaround

* Fri Dec 05 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.7-1
- update to 5.2.7
- enable pdo_dblib driver in php-mssql

* Mon Nov 24 2008 Joe Orton <jorton@redhat.com> 5.2.6-7
- tweak Summary, thanks to Richard Hughes

* Tue Nov  4 2008 Joe Orton <jorton@redhat.com> 5.2.6-6
- move gd_README to php-gd
- update to r4 of systzdata patch; introduces a default timezone
  name of "System/Localtime", which uses /etc/localtime (#469532)

* Sat Sep 13 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.6-5
- enable XPM support in php-gd
- Fix BR for php-gd

* Sun Jul 20 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.6-4
- enable T1lib support in php-gd

* Mon Jul 14 2008 Joe Orton <jorton@redhat.com> 5.2.6-3
- update to 5.2.6
- sync default php.ini with upstream
- drop extension_dir from default php.ini, rely on hard-coded
  default, to make php-common multilib-safe (#455091)
- update to r3 of systzdata patch

* Thu Apr 24 2008 Joe Orton <jorton@redhat.com> 5.2.5-7
- split pspell extension out into php-spell (#443857)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.2.5-6
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Joe Orton <jorton@redhat.com> 5.2.5-5
- ext/date: use system timezone database

* Fri Dec 28 2007 Joe Orton <jorton@redhat.com> 5.2.5-4
- rebuild for libc-client bump

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 5.2.5-3
- Rebuild for openssl bump

* Wed Dec  5 2007 Joe Orton <jorton@redhat.com> 5.2.5-2
- update to 5.2.5

* Mon Oct 15 2007 Joe Orton <jorton@redhat.com> 5.2.4-3
- correct pcre BR version (#333021)
- restore metaphone fix (#205714)
- add READMEs to php-cli

* Sun Sep 16 2007 Joe Orton <jorton@redhat.com> 5.2.4-2
- update to 5.2.4

* Sun Sep  2 2007 Joe Orton <jorton@redhat.com> 5.2.3-9
- rebuild for fixed APR

* Tue Aug 28 2007 Joe Orton <jorton@redhat.com> 5.2.3-8
- add ldconfig post/postun for -embedded (Hans de Goede)

* Fri Aug 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 5.2.3-7
- add php-embedded sub-package

* Fri Aug 10 2007 Joe Orton <jorton@redhat.com> 5.2.3-6
- fix build with new glibc
- fix License

* Mon Jul 16 2007 Joe Orton <jorton@redhat.com> 5.2.3-5
- define php_extdir in macros.php

* Mon Jul  2 2007 Joe Orton <jorton@redhat.com> 5.2.3-4
- obsolete php-dbase

* Tue Jun 19 2007 Joe Orton <jorton@redhat.com> 5.2.3-3
- add mcrypt, mhash, tidy, mssql subpackages (Dmitry Butskoy)
- enable dbase extension and package in -common

* Fri Jun  8 2007 Joe Orton <jorton@redhat.com> 5.2.3-2
- update to 5.2.3 (thanks to Jeff Sheltren)

* Wed May  9 2007 Joe Orton <jorton@redhat.com> 5.2.2-4
- fix php-pdo *_arg_force_ref global symbol abuse (#216125)

* Tue May  8 2007 Joe Orton <jorton@redhat.com> 5.2.2-3
- rebuild against uw-imap-devel

* Fri May  4 2007 Joe Orton <jorton@redhat.com> 5.2.2-2
- update to 5.2.2
- synch changes from upstream recommended php.ini

* Thu Mar 29 2007 Joe Orton <jorton@redhat.com> 5.2.1-5
- enable SASL support in LDAP extension (#205772)

* Wed Mar 21 2007 Joe Orton <jorton@redhat.com> 5.2.1-4
- drop mime_magic extension (deprecated by php-pecl-Fileinfo)

* Mon Feb 19 2007 Joe Orton <jorton@redhat.com> 5.2.1-3
- fix regression in str_{i,}replace (from upstream)

* Thu Feb 15 2007 Joe Orton <jorton@redhat.com> 5.2.1-2
- update to 5.2.1
- add Requires(pre) for httpd
- trim %%changelog to versions >= 5.0.0

* Thu Feb  8 2007 Joe Orton <jorton@redhat.com> 5.2.0-10
- bump default memory_limit to 32M (#220821)
- mark config files noreplace again (#174251)
- drop trailing dots from Summary fields
- use standard BuildRoot
- drop libtool15 patch (#226294)

* Tue Jan 30 2007 Joe Orton <jorton@redhat.com> 5.2.0-9
- add php(api), php(zend-abi) provides (#221302)
- package /usr/share/php and append to default include_path (#225434)

* Tue Dec  5 2006 Joe Orton <jorton@redhat.com> 5.2.0-8
- fix filter.h installation path
- fix php-zend-abi version (Remi Collet, #212804)

* Tue Nov 28 2006 Joe Orton <jorton@redhat.com> 5.2.0-7
- rebuild again

* Tue Nov 28 2006 Joe Orton <jorton@redhat.com> 5.2.0-6
- rebuild for net-snmp soname bump

* Mon Nov 27 2006 Joe Orton <jorton@redhat.com> 5.2.0-5
- build json and zip shared, in -common (Remi Collet, #215966)
- obsolete php-json and php-pecl-zip
- build readline extension into /usr/bin/php* (#210585)
- change module subpackages to require php-common not php (#177821)

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 5.2.0-4
- provide php-zend-abi (#212804)
- add /etc/rpm/macros.php exporting interface versions
- synch with upstream recommended php.ini

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 5.2.0-3
- update to 5.2.0 (#213837)
- php-xml provides php-domxml (#215656)
- fix php-pdo-abi provide (#214281)

* Tue Oct 31 2006 Joseph Orton <jorton@redhat.com> 5.1.6-4
- rebuild for curl soname bump
- add build fix for curl 7.16 API

* Wed Oct  4 2006 Joe Orton <jorton@redhat.com> 5.1.6-3
- from upstream: add safety checks against integer overflow in _ecalloc

* Tue Aug 29 2006 Joe Orton <jorton@redhat.com> 5.1.6-2
- update to 5.1.6 (security fixes)
- bump default memory_limit to 16M (#196802)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.1.4-8.1
- rebuild

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-8
- Provide php-posix (#194583)
- only provide php-pcntl from -cli subpackage
- add missing defattr's (thanks to Matthias Saou)

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-7
- move Obsoletes for php-openssl to -common (#194501)
- Provide: php-cgi from -cli subpackage

* Fri Jun  2 2006 Joe Orton <jorton@redhat.com> 5.1.4-6
- split out php-cli, php-common subpackages (#177821)
- add php-pdo-abi version export (#193202)

* Wed May 24 2006 Radek Vokal <rvokal@redhat.com> 5.1.4-5.1
- rebuilt for new libnetsnmp

* Thu May 18 2006 Joe Orton <jorton@redhat.com> 5.1.4-5
- provide mod_php (#187891)
- provide php-cli (#192196)
- use correct LDAP fix (#181518)
- define _GNU_SOURCE in php_config.h and leave it defined
- drop (circular) dependency on php-pear

* Mon May  8 2006 Joe Orton <jorton@redhat.com> 5.1.4-3
- update to 5.1.4

* Wed May  3 2006 Joe Orton <jorton@redhat.com> 5.1.3-3
- update to 5.1.3

* Tue Feb 28 2006 Joe Orton <jorton@redhat.com> 5.1.2-5
- provide php-api (#183227)
- add provides for all builtin modules (Tim Jackson, #173804)
- own %%{_libdir}/php/pear for PEAR packages (per #176733)
- add obsoletes to allow upgrade from FE4 PDO packages (#181863)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 5.1.2-4
- rebuild for new libc-client soname

* Mon Jan 16 2006 Joe Orton <jorton@redhat.com> 5.1.2-3
- only build xmlreader and xmlwriter shared (#177810)

* Fri Jan 13 2006 Joe Orton <jorton@redhat.com> 5.1.2-2
- update to 5.1.2

* Thu Jan  5 2006 Joe Orton <jorton@redhat.com> 5.1.1-8
- rebuild again

* Mon Jan  2 2006 Joe Orton <jorton@redhat.com> 5.1.1-7
- rebuild for new net-snmp

* Mon Dec 12 2005 Joe Orton <jorton@redhat.com> 5.1.1-6
- enable short_open_tag in default php.ini again (#175381)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  8 2005 Joe Orton <jorton@redhat.com> 5.1.1-5
- require net-snmp for php-snmp (#174800)

* Sun Dec  4 2005 Joe Orton <jorton@redhat.com> 5.1.1-4
- add /usr/share/pear back to hard-coded include_path (#174885)

* Fri Dec  2 2005 Joe Orton <jorton@redhat.com> 5.1.1-3
- rebuild for httpd 2.2

* Mon Nov 28 2005 Joe Orton <jorton@redhat.com> 5.1.1-2
- update to 5.1.1
- remove pear subpackage
- enable pdo extensions (php-pdo subpackage)
- remove non-standard conditional module builds
- enable xmlreader extension

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 5.0.5-6
- rebuilt against new openssl

* Mon Nov  7 2005 Joe Orton <jorton@redhat.com> 5.0.5-5
- pear: update to XML_RPC 1.4.4, XML_Parser 1.2.7, Mail 1.1.9 (#172528)

* Tue Nov  1 2005 Joe Orton <jorton@redhat.com> 5.0.5-4
- rebuild for new libnetsnmp

* Wed Sep 14 2005 Joe Orton <jorton@redhat.com> 5.0.5-3
- update to 5.0.5
- add fix for upstream #34435
- devel: require autoconf, automake (#159283)
- pear: update to HTTP-1.3.6, Mail-1.1.8, Net_SMTP-1.2.7, XML_RPC-1.4.1
- fix imagettftext et al (upstream, #161001)

* Thu Jun 16 2005 Joe Orton <jorton@redhat.com> 5.0.4-11
- ldap: restore ldap_start_tls() function

* Fri May  6 2005 Joe Orton <jorton@redhat.com> 5.0.4-10
- disable RPATHs in shared extensions (#156974)

* Tue May  3 2005 Joe Orton <jorton@redhat.com> 5.0.4-9
- build simplexml_import_dom even with shared dom (#156434)
- prevent truncation of copied files to ~2Mb (#155916)
- install /usr/bin/php from CLI build alongside CGI
- enable sysvmsg extension (#142988)

* Mon Apr 25 2005 Joe Orton <jorton@redhat.com> 5.0.4-8
- prevent build of builtin dba as well as shared extension

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-7
- split out dba and bcmath extensions into subpackages
- BuildRequire gcc-c++ to avoid AC_PROG_CXX{,CPP} failure (#155221)
- pear: update to DB-1.7.6
- enable FastCGI support in /usr/bin/php-cgi (#149596)

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-6
- build /usr/bin/php with the CLI SAPI, and add /usr/bin/php-cgi,
  built with the CGI SAPI (thanks to Edward Rudd, #137704)
- add php(1) man page for CLI
- fix more test cases to use -n when invoking php

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-5
- rebuild for new libpq soname

* Tue Apr 12 2005 Joe Orton <jorton@redhat.com> 5.0.4-4
- bundle from PEAR: HTTP, Mail, XML_Parser, Net_Socket, Net_SMTP
- snmp: disable MSHUTDOWN function to prevent error_log noise (#153988)
- mysqli: add fix for crash on x86_64 (Georg Richter, upstream #32282)

* Mon Apr 11 2005 Joe Orton <jorton@redhat.com> 5.0.4-3
- build shared objects as PIC (#154195)

* Mon Apr  4 2005 Joe Orton <jorton@redhat.com> 5.0.4-2
- fix PEAR installation and bundle PEAR DB-1.7.5 package

* Fri Apr  1 2005 Joe Orton <jorton@redhat.com> 5.0.4-1
- update to 5.0.4 (#153068)
- add .phps AddType to php.conf (#152973)
- better gcc4 fix for libxmlrpc

* Wed Mar 30 2005 Joe Orton <jorton@redhat.com> 5.0.3-5
- BuildRequire mysql-devel >= 4.1
- don't mark php.ini as noreplace to make upgrades work (#152171)
- fix subpackage descriptions (#152628)
- fix memset(,,0) in Zend (thanks to Dave Jones)
- fix various compiler warnings in Zend

* Thu Mar 24 2005 Joe Orton <jorton@redhat.com> 5.0.3-4
- package mysqli extension in php-mysql
- really enable pcntl (#142903)
- don't build with --enable-safe-mode (#148969)
- use "Instant Client" libraries for oci8 module (Kai Bolay, #149873)

* Fri Feb 18 2005 Joe Orton <jorton@redhat.com> 5.0.3-3
- fix build with GCC 4

* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 5.0.3-2
- install the ext/gd headers (#145891)
- enable pcntl extension in /usr/bin/php (#142903)
- add libmbfl array arithmetic fix (dcb314@hotmail.com, #143795)
- add BuildRequire for recent pcre-devel (#147448)

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 5.0.3-1
- update to 5.0.3 (thanks to Robert Scheck et al, #143101)
- enable xsl extension (#142174)
- package both the xsl and dom extensions in php-xml
- enable soap extension, shared (php-soap package) (#142901)
- add patches from upstream 5.0 branch:
 * Zend_strtod.c compile fixes
 * correct php_sprintf return value usage

* Mon Nov 22 2004 Joe Orton <jorton@redhat.com> 5.0.2-8
- update for db4-4.3 (Robert Scheck, #140167)
- build against mysql-devel
- run tests in %%check

* Wed Nov 10 2004 Joe Orton <jorton@redhat.com> 5.0.2-7
- truncate changelog at 4.3.1-1
- merge from 4.3.x package:
 - enable mime_magic extension and Require: file (#130276)

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-6
- fix dom/sqlite enable/without confusion

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-5
- fix phpize installation for lib64 platforms
- add fix for segfault in variable parsing introduced in 5.0.2

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-4
- update to 5.0.2 (#127980)
- build against mysqlclient10-devel
- use new RTLD_DEEPBIND to load extension modules
- drop explicit requirement for elfutils-devel
- use AddHandler in default conf.d/php.conf (#135664)
- "fix" round() fudging for recent gcc on x86
- disable sqlite pending audit of warnings and subpackage split

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-4
- don't build dom extension into 2.0 SAPI

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-3
- ExclusiveArch: x86 ppc x86_64 for the moment

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-2
- fix default extension_dir and conf.d/php.conf

* Thu Sep  9 2004 Joe Orton <jorton@redhat.com> 5.0.1-1
- update to 5.0.1
- only build shared modules once
- put dom extension in php-dom subpackage again
- move extension modules into %%{_libdir}/php/modules
- don't use --with-regex=system, it's ignored for the apache* SAPIs

* Wed Aug 11 2004 Tom Callaway <tcallawa@redhat.com>
- Merge in some spec file changes from Jeff Stern (jastern@uci.edu)

* Mon Aug 09 2004 Tom Callaway <tcallawa@redhat.com>
- bump to 5.0.0
- add patch to prevent clobbering struct re_registers from regex.h
- remove domxml references, replaced with dom now built-in
- fix php.ini to refer to php5 not php4

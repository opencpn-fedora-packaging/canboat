%global commit 870a9231cd451b24d876097166e95ab4a55122ce
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner canboat
%global project canboat

Name: %{project}
Summary: NMEA 2000 and NMEA 0183 utilities
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv3+
Source: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: libxslt

%description
A small but effective set of command-line utilities to work with CAN
networks on BOATs. Guess you now know where the name comes from.

The most common version of CAN networks on board, and in fact at the
moment the only ones that this suite can analyze, are NMEA 2000 PGNs.

The NMEA 2000 database and implementation is copyrighted by the NMEA
(National Marine Electronics Association). Access is restricted to
members and parties that pay for it. If they do so they are not able
to divulge the content of the database, thus making it impossible for
open source developers to get access to it.

For this reason we have reverse engineered the NMEA 2000 database by
network observation and assembling data from public sources.

To use the programs included in this project you will need the
excellent Actisense NGT-1 PC gateway if you run Microsoft Windows or
OS X. On Linux you can use the NGT-1 or the built in Linux
''socketcan'' driver.

This code uses reverse engineered knowledge to access the NGT-1
directly. It does not use the Actisense DLL or SDK.

%prep
%autosetup -n %{project}-%{commit}
sed -i -e 's/-g $(ROOT_GID) -o $(ROOT_UID) -m $(ROOT_MOD)//' Makefile

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{optflags}"

%install
%make_install PREFIX="" EXEC_PREFIX="/usr"

%files
%{_sysconfdir}/default/n2kd
%{_sysconfdir}/default/n2kd_nmea
%{_bindir}/analyzer
%{_bindir}/actisense-serial
%{_bindir}/candump2analyzer
%{_bindir}/command-group-function
%{_bindir}/iptee
%{_bindir}/list-product-information
%{_bindir}/n2kd
%{_bindir}/n2kd_monitor
%{_bindir}/n2kd_nmea_monitor
%{_bindir}/nmea0183-serial
%{_bindir}/request-group-function
%{_bindir}/socketcan-writer

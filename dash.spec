Name:		dash
Version:	0.5.12
Release:	1%{?dist}
Summary: 	Debian Almquist shell (dash)
Provides:	/bin/sh
Provides:	/bin/dash
License:	BSD
URL:		https://gondor.apana.org.au/~herbert/dash
Source0:	https://git.kernel.org/pub/scm/utils/dash/dash.git/snapshot/%{name}-%{version}.tar.gz

%description
The Debian Almquist shell (dash) is a POSIX compliant shell that aims to be
as small as possible.

%prep
%autosetup
autoreconf -if

%build
%configure
%make_build

%install
%make_install
ln -sf dash %{buildroot}%{_bindir}/sh

%files
%{_bindir}/dash
%{_bindir}/sh
%{_mandir}/man1/*


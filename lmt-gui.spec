Name: 
Version: 
Release: 

License: GPL
Group: Applications/System
Summary: Lustre Montitoring Tools Client
URL: http://code.google.com/p/lmt
Packager: Jim Garlick <garlick@llnl.gov>
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ant, ant-nodeps
BuildRequires: ncurses
BuildRequires: jre >= 1.4.2, java-devel >= 1.4.2
Requires: jre >= 1.4.2
Obsoletes: lmt-client < 3.0
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%define lmtlibdir %{_datadir}/%{name}

%description
Lustre Monitoring Tools (LMT) GUI Client

%prep
%setup

%build
%configure
make

%install
rm -rf   $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{lmtlibdir}

cp scripts/lwatch   $RPM_BUILD_ROOT%{_bindir}
cp lmt-complete.jar $RPM_BUILD_ROOT%{lmtlibdir}/lmt-complete.jar
cp etc/lmtrc        $RPM_BUILD_ROOT%{lmtlibdir}/sample.lmtrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS DISCLAIMER COPYING
%{_bindir}/lwatch
%dir %{lmtlibdir}
%{lmtlibdir}/sample.lmtrc
%attr(0644,root,root) %{lmtlibdir}/lmt-complete.jar

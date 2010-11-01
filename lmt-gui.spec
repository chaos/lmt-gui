Name:  lmt-gui
Version: 3.0.0
Release:  1

License: GPL
Group: Applications/System
Summary: Lustre Montitoring Tools Client
URL: http://code.google.com/p/lmt
Packager: Jim Garlick <garlick@llnl.gov>
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%if 0%{?ch4}
BuildRequires: jre = 1.4.2, java-devel = 1.4.2
%else
BuildRequires: jre >= 1.4.2, java-devel >= 1.4.2
%endif
Requires: jre >= 1.4.2
Obsoletes: lmt-client < 3.0
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

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
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp scripts/lwatch   $RPM_BUILD_ROOT%{_bindir}
cp scripts/lstat $RPM_BUILD_ROOT%{_bindir}
cp lmt.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS DISCLAIMER COPYING sample.lmtrc
%{_bindir}/lwatch
%{_bindir}/lstat
%attr(0644,root,root) %{_javadir}/%{name}-%{version}.jar

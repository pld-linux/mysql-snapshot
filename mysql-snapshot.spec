%include	/usr/lib/rpm/macros.perl
Summary:	Tool for taking LVM snapshots of MySQL data and mounting them
Name:		mysql-snapshot
Version:	0.1.0
Release:	0.2
License:	LGPL
Group:		Applications/Databases
Source0:	http://mirror.provenscaling.com/extras/provenscaling/%{name}-%{version}-0.noarch.rpm
# Source0-md5:	ac6856b7fbe12d8f4c4db9c0d40f3b2d
URL:		http://www.provenscaling.com/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-utils
Requires:	perl-DBD-mysql >= 1.0
Requires:	perl-DBI >= 1.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for taking LVM snapshots of MySQL data and mounting them.

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -i -d
mv usr/bin/mysql-snapshot .
mv usr/share/man/man3/* .
mv usr/lib/perl5/vendor_perl/5.8.8/mysql-snapshot.pm .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib},%{_mandir}/man3}
install mysql-snapshot $RPM_BUILD_ROOT%{_bindir}/mysql-snapshot
cp -a mysql-snapshot.pm $RPM_BUILD_ROOT%{perl_vendorlib}
cp -a mysql-snapshot.3pm $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mysql-snapshot
%{perl_vendorlib}/mysql-snapshot.pm
%{_mandir}/man3/mysql-snapshot.*

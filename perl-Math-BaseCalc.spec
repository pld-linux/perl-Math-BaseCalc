#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BaseCalc
Summary:	Math::BaseCalc Perl module - convert numbers between various bases
Summary(pl.UTF-8):	Moduł Perla Math::BaseCalc - konwersja liczb pomiędzy systemami o różnych podstawach
Name:		perl-Math-BaseCalc
Version:	1.016
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f126e63a020828b40b536a72cf679dfb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module facilitates the conversion of numbers between various
number bases. You may define your own digit sets, or use any of
several predefined digit sets.

%description -l pl.UTF-8
Ten moduł ułatwia przeliczanie liczb pomiędzy różnymi systemami. Można
zdefiniować własne zestawy cyfr lub użyć dowolnego z kilku
predefiniowanych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Math/BaseCalc.pm
%{_mandir}/man3/*

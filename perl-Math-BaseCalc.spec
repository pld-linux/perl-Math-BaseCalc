#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BaseCalc
Summary:	Math::BaseCalc Perl module - convert numbers between various bases
Summary(pl):	Modu³ Perla Math::BaseCalc - konwersja liczb pomiêdzy systemami o ró¿nych podstawach
Name:		perl-Math-BaseCalc
Version:	1.011
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e539a438ff8717f22ab83f9dd113686
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module facilitates the conversion of numbers between various
number bases. You may define your own digit sets, or use any of
several predefined digit sets.

%description -l pl
Ten modu³ u³atwia przeliczanie liczb pomiêdzy ró¿nymi systemami. Mo¿na
zdefiniowaæ w³asne zestawy cyfr lub u¿yæ dowolnego z kilku
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

#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Statistics
%define	pnam	Distributions
Summary:	Critical values and upper probabilities of common statistical distributions
Summary(pl.UTF-8):	Wartości krytyczne i górne prawdopodobieństwa popularnych rozkładów statystycznych
Name:		perl-Statistics-Distributions
Version:	1.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	526cb415b30ffeec52563dbcb436ca60
URL:		http://search.cpan.org/dist/Statistics-Distributions/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics::Distributions calculates percentage points (5 significant
digits) of the u (standard normal) distribution, the Student's t
distribution, the chi-square distribution and the F distribution. It
can also calculate the upper probability (5 significant digits) of the
u (standard normal), the chi-square, the t and the F distribution.

These critical values are needed to perform statistical tests, like
the u test, the t test, the F test and the chi-squared test, and to
calculate confidence intervals.

%description -l pl.UTF-8
Statistics::Distributions oblicza percentyle (z dokładnością do 5 cyfr
znaczących) rozkładów u (normalnego), t-Studenta, chi-kwadrat oraz F.
Może także obliczać górne prawdopodobieństwa (z dokładnością do 5 cyfr
znaczących) tych rozkładów.

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
%{perl_vendorlib}/Statistics/*.pm
%{_mandir}/man3/*

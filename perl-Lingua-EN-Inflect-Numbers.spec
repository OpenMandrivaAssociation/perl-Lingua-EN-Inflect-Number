%define module	Lingua-EN-Inflect-Number
%define name	perl-%{module}
%define version 1.1
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Force number of words to singular or plural
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(Lingua::EN::Inflect)
Buildarch:      noarch

%description
This module extends the functionality of Lingua::EN::Inflect with three new
functions available for export:

number:
This takes a word, and determines its number. It returns s for singular, p for
plural, and ambig for words that can be either singular or plural.

to_S / to_PL:
These take a word and convert it forcefully either to singular or to plural.
Lingua::EN::Inflect does funny things if you try to pluralise an already-plural
word, but this module does the right thing.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/*/*


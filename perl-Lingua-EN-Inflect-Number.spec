%define upstream_name	 Lingua-EN-Inflect-Number
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Force number of words to singular or plural
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Lingua::EN::Inflect)

BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files 
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/*/*

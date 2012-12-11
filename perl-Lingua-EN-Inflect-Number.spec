%define upstream_name	 Lingua-EN-Inflect-Number
%define upstream_version 1.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Force number of words to singular or plural
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.bz2

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


%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 504931
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2010.0
+ Revision: 430477
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2009.0
+ Revision: 241602
- rebuild
- fix no-buildroot-tag
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2008.0
+ Revision: 49061
- import perl-Lingua-EN-Inflect-Number


* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2008.0
- first mdv release

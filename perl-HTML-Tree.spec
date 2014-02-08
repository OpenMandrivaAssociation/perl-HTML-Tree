%define upstream_name	 HTML-Tree
%define upstream_version 4.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Epoch:		1

Summary:	Build and scan parse-trees of HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/S/SB/SBURKE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/HTML
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:4.200.0-3mdv2012.0
+ Revision: 765308
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:4.200.0-2
+ Revision: 763861
- rebuilt for perl-5.14.x

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:4.200.0-1
+ Revision: 654088
- update to new version 4.2

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:4.100.0-1mdv2011.0
+ Revision: 596614
- update to 4.1

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1:3.230.0-1mdv2010.1
+ Revision: 420975
- bumping epoch
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.2300-4mdv2009.1
+ Revision: 351962
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.2300-3mdv2009.0
+ Revision: 223792
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2300-2mdv2008.1
+ Revision: 180409
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 3.2300-1mdv2008.0
+ Revision: 20160
- fix version
- 3.23


* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.1901-1mdk
- New version
- fix directory ownership
- rpmbuildupdate aware

* Mon Oct 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.18-2mdk
- Rebuild, misc spec fixes

* Wed Sep 17 2003 Stefan van der Eijk <stefan@eijk.nu> 3.18-1mdk
- 3.18
- revamp .spec file


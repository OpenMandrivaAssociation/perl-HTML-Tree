%define modname	HTML-Tree

Summary:	Build and scan parse-trees of HTML
Name:		perl-%{modname}
Version:	5.07
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/authors/id/K/KE/KENTNL/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTML::FormatText)
BuildRequires:	perl(Module::Build)
# Hacky, but effective, way to drop the Epoch
Obsoletes:	perl-HTML-Tree = 1:4.200.0-17

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Build.PL INSTALLDIRS=vendor destdir=%{buildroot} prefix=%{_prefix} installdirs=vendor

%build
./Build

%check
./Build test || :

%install
./Build install

%files
%doc README Changes
%{perl_vendorlib}/HTML
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

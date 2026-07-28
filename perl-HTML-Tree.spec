%define modname	HTML-Tree

Summary:	Build and scan parse-trees of HTML
Name:		perl-%{modname}
Version:	5.07
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTML-Tree
Source0:	https://cpan.metacpan.org/authors/id/K/KE/KENTNL/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTML::FormatText)
BuildRequires:	perl(Module::Build)
Obsoletes:	perl-HTML-Tree = 1:4.200.0-17

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%check
./Build test || :

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%files
%doc README Changes
%{perl_vendorlib}/HTML
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

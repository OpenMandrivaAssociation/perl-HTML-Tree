%define module	HTML-Tree
%define name	perl-%{module}
%define real_version	3.23
%define version	3.2300
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Build and scan parse-trees of HTML
Group:		Development/Perl
License:	GPL or Artistic
Source:		http://www.cpan.org/authors/id/S/SB/SBURKE/%{module}-%{real_version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep
%setup -q -n %{module}-%{real_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/HTML
%{_mandir}/*/*


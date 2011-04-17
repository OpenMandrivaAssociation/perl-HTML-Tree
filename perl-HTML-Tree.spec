%define upstream_name	 HTML-Tree
%define upstream_version 4.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:	Build and scan parse-trees of HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/S/SB/SBURKE/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/HTML
%{_bindir}/*
%{_mandir}/*/*

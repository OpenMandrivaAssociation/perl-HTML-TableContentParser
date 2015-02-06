%define upstream_name    HTML-TableContentParser
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Do interesting things with the contents of tables
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		perl-HTML-TableContentParser-0.13-fix-tests.patch

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)

BuildArch:	noarch

%description
This package pulls out the contents of a table from a string containing
HTML. Each time a table is encountered, data will be stored in an array
consisting of a hash of whatever was discovered about the table -- id,
name, border, cellspacing etc, and of course data contained within the
table.

The format of each hash will look something like

  attributes            keys from the attributes of the <table> tag
  @{$table_headers}     array of table headers, in order found
  @{$table_rows}        rows discovered, in order

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .tests

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 654973
- rebuild for updated spec-helper

* Tue Dec 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 481286
- adding missing buildrequires:
- import perl-HTML-TableContentParser


* Mon Dec 21 2009 cpan2dist 0.13-1mdv
- initial mdv release, generated with cpan2dist

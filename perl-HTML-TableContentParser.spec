%define upstream_name    HTML-TableContentParser
%define upstream_version 0.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Do interesting things with the contents of tables
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:     perl-HTML-TableContentParser-0.13-fix-tests.patch

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{_mandir}/man3/*
%perl_vendorlib/*



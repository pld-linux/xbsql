Summary:	XBSQL - an SQL wrapper for the XBase library
Summary(pl.UTF-8):	XBSQL - wrapper SQL dla biblioteki XBase
Name:		xbsql
Version:	0.11
Release:	3
License:	LGPL
Group:		Libraries
# from URL - dead ftp://195.92.31.34/pub/xbsql-0.6/xbsql-0.6.tgz
Source0:	http://www.rekallrevealed.org/packages/%{name}-%{version}.tgz
# Source0-md5:	7f8c8584cf0f592660fb2653a4bfc415
Patch0:		%{name}-acfix.patch
URL:		http://www.quaking.demon.co.uk/xbsql/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libtool >= 2:1.5
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	xbase-devel >= 1.8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XBSQL is a wrapper library which provides an SQL-subset interface to
XBase DBMS.

%description -l pl.UTF-8
XBSQL to biblioteka obudowująca dostarczająca interfejs będący
podzbiorem SQL do systemu baz danych XBase.

%package devel
Summary:	Header files for XBSQL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XBSQL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xbase-devel

%description devel
Header files for XBSQL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XBSQL.

%package static
Summary:	Static XBSQL library
Summary(pl.UTF-8):	Statyczna biblioteka XBSQL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XBSQL library.

%description static -l pl.UTF-8
Statyczna biblioteka XBSQL.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Announce ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xql
%attr(755,root,root) %{_libdir}/libxbsql.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libxbsql.so
%{_libdir}/libxbsql.la
%{_includedir}/xbsql.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libxbsql.a

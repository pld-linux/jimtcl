Summary:	Small footprint implementation of Tcl programming language
Name:		jimtcl
Version:	0.73
Release:	2
License:	BSD
Group:		Development/Languages/Tcl
Source0:	https://github.com/msteveb/jimtcl/tarball/0.72#/%{name}-%{version}.tar.gz
# Source0-md5:	c86055ac018d171d76f823213819788f
URL:		http://jim.tcl.tk/
BuildRequires:	asciidoc
BuildRequires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jim is an opensource small-footprint implementation of the Tcl
programming language. It implements a large subset of Tcl and adds new
features like references with garbage collection, closures, built-in
Object Oriented Programming system, Functional Programming commands,
first-class arrays and UTF-8 support. All this with a binary size of
about 100-200kB (depending upon selected options).

%package devel
Summary:	jimtcl header files and development documentation
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
jimtcl header files and development documentation.

%prep
%setup -q -n msteveb-%{name}-5b8ea68

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
./configure \
	--full \
	--shared

%{__make} all Tcl.html

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}

%{makeinstall}

%if "%{_lib}" != "lib"
mv $RPM_BUILD_ROOT{/usr/lib/*,%{_libdir}}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS DEVELOPING README* TODO
%attr(755,root,root) %{_bindir}/jimsh
%dir %{_libdir}/jim
%attr(755,root,root) %{_libdir}/libjim.so

%files devel
%defattr(644,root,root,755)
%doc Tcl.html
%attr(755,root,root) %{_bindir}/build-jim-ext
%{_includedir}/jim*.h

Summary:	KDE Integrated LaTeX Environment
Name:		kile
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://xm1.net.free.fr/kile/%{name}-%{version}.tar.gz
Patch1:		%{name}-fix-compile.patch
URL:		http://xm1.net.free.fr/kile/index.html
BuildRequires:	kdegraphics-devel >= 3.0
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Integrated LaTeX Environment.

%prep
%setup -q
#%patch1 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags} -fno-check-new"
%configure \
	--disable-rpath \
	--%{!?debug:dis}%{?debug:en}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%defattr(-,root,root,0755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kile
%{_applnkdir}/Applications/*.desktop

%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png

Summary:	KDE Integrated LaTeX Environment
Name:		kile
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://xm1.net.free.fr/kile/%{name}-%{version}.tar.gz
Patch1:		%{name}-fix-compile.patch
URL:		http://xm1.net.free.fr/kile/index.html
BuildRequires:	kdelibs-devel >= 3.0
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir        /usr/share/doc/kde/HTML

%description
KDE Integrated LaTeX Environment.

%prep
%setup -q
#%patch1 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags} -fno-check-new -fno-rtti"
%configure \
	--disable-rpath \
	--%{!?debug:dis}%{?debug:en}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}{/hicolor/48x48/apps/kile.png,}
mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications/*.desktop,Office/Wordprocessors}

%find_lang %{name} --with-kde

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%defattr(-,root,root,0755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kile
%{_applnkdir}/Office/Wordprocessors/*.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*/*/apps/*.png

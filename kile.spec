%define relnumber 3
%define build_mdk %(if [[ `grep Mandrake /etc/mandrake-release` ]];then echo 1; else echo 0; fi)
%define build_mdk8 %(if [ `awk '{print $4}' /etc/mandrake-release|cut -f1 -d'.'` = 8 ];then echo 1; else echo 0; fi)

%if %build_mdk8 
%global _iconsdir	%{_datadir}/icons/
%global _miconsdir	%{_datadir}/icons/mini
%global _liconsdir	%{_datadir}/icons/large
%global _menudir	%{_libdir}/menu
%define _prefix        /opt/kde3
%endif


Name: 			kile
Summary: 		Integrated LaTeX Environment for KDE3
Version: 		1.3
Source:	 		http://xm1.net.free.fr/kile/kile-1.3.tar.bz2
Group: 			kde/applications
BuildRoot: 		%{_tmppath}/%{name}-root
License: 		GPL
#Packager: pascal.brachet@free.fr
Distribution: 	Mandrake Linux
Release: 		2mdk
Group: 			Publishing
Provides: 		Kile
Url: 			http://xm1.net.free.fr/kile/index.html
#Vendor: pascal.brachet@free.fr
Requires: 		tetex-latex

# Laurent 1.3-2mdk fix compile
Patch1:			kile-1.3-fix-compile.patch.bz2

%if %build_mdk8
BuildRequires: kdegraphics3 >= 3
%else
BuildRequires: kdegraphics >= 3
%endif

%description
Integrated LaTeX Environment for KDE3
%prep
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%setup -q -nkile-1.3
%patch1 -p1

%build
		CFLAGS="%optflags" CXXFLAGS="%optflags" \
        		./configure --prefix=%_prefix \
                			--disable-rpath \
				            --disable-debug 

%make

%install

make install DESTDIR=%buildroot

# menu
mkdir -p $RPM_BUILD_ROOT/%{_menudir}

cat > $RPM_BUILD_ROOT/%{_menudir}/kile <<EOF
?package(kile):\
needs="x11"\
section="Applications/Publishing"\
title="Kile"\
longtitle="Integrated LaTeX Environment for KDE3"\
command="%{_bindir}/kile"\
icon="kile.png"
EOF

install -D -m644 kile/kile32x32.png $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install -D -m644 kile/kile16x16.png $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install -D -m644 kile/kile48x48.png $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

cd $RPM_BUILD_ROOT


%clean
rm -fr %buildroot

%post
%{update_menus}

%postun
%{clean_menus}

%files 
%defattr (-,root,root)
%defattr(-,root,root,0755)
%doc AUTHORS COPYING INSTALL README TODO

%_menudir/*
%_bindir/*

%_datadir/applnk/Applications/*.desktop

%dir %_datadir/apps/kile/doc/
%doc %_datadir/apps/kile/doc/*.html
%doc %_datadir/apps/kile/doc/*.png

%dir %_datadir/apps/kile/
%_datadir/apps/kile/*.rc

%dir %_datadir/apps/kile/mathsymbols/
%_datadir/apps/kile/mathsymbols/*.png

%dir %_datadir/apps/kile/pics/
%_datadir/apps/kile/pics/*.png


%doc %_datadir/doc/HTML/en/kile/*.html


%_datadir/icons/*.png

%_datadir/icons/hicolor/16x16/apps/*.png
%_datadir/icons/hicolor/32x32/apps/*.png
%_datadir/icons/hicolor/48x48/apps/*.png
%_datadir/icons/large/*.png
%_datadir/icons/mini/*.png

%_datadir/locale/*



%changelog
* Sat Nov 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-2mdk
- Rebuild
- Add patch1 : fix gcc-3.2 compile

* Sat Oct 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-1mdk
- 1.3 

* Mon Oct 07 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-0.beta1.1mdk
- 1.3beta1

* Thu Sep 12 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2-4mdk
- Clean spec file ! => Spec file was illegible !
=> Use this spec file for generate suse or redhat package, I don't
think that it's necessary !


* Tue Sep 10 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2-3mdk
- 1.2

* Sun Aug 18 2002 Buchan Milne <bgmilne@linux-mandrake.com> 1.1-3mdk
- gcc 3.2 rebuild

* Sun Jul 28 2002 Buchan Milne <bgmilne@linux-mandrake.com> 1.1-2mdk
- Club->cooker
- Buildrequires kdegraphics
* Sun Jul 28 2002 Buchan Milne <bgmilne@linux-mandrake.com> 1.1-1mdk
- Merge Mandrake/Redhat/SuSE Spec files with auto-detection
  of Redhat and Mandrake 8.x, setting prefix accordingly.
- Add icons
- Require tetex-latex
- Prevent kile from owning every dir it has a file in.

Summary:	KDE Integrated LaTeX Environment
Name:		kile
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://xm1.net.free.fr/kile/%{name}-%{version}.tar.gz
Patch1:		%{name}-fix-compile.patch
URL:		http://xm1.net.free.fr/kile/
BuildRequires:	kdelibs-devel >= 3.0
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir        /usr/share/doc/kde/HTML

%description
KDE Integrated LaTeX Environment. Features:

 - an editor to write your LaTeX source files (syntax highlighting,
   undo-redo, search-replace, spellcheck ...)
 - the principal LaTex tags can be inserted directly with the "LaTeX",
   "Math" and "Greek" menus
 - 370 mathematical symbols can be inserted in just one click
 - wizards to generate code ('Quick document', 'Quick letter', tabular,
   tabbing and array environments)
 - LaTeX-related programs can be launched via the "Tools" menu
 - contextual help in the "Messages / Log File" frame
 - the standard Bibtex entry types can be inserted in the ".bib" file
   with the "Bibliography" menu
 - a "structure view" of the document for easier navigation of a document
   (by clicking on an item in the "Structure" frame, you can jump directly to
   the corresponding part of your document
 - extensive LaTeX documentation
 - in the "Messages / Log File" frame, you can see information about
   processes and the logfile after a LaTeX compilation
 - the "Next Latex Error" and "Previous Latex Error" commands let you
   reach the LaTeX errors detected by Kile in the log file
 - by clicking on the number of a line in the log file, the cursor jumps
   to the corresponding line in the editor
 - a Gnuplot front end (adaptation of the Xgfe program)
 - support for "Inverse and Forward Search" with KDVI

The program's aim is to simplify the edition of LaTeX source code and the
use of the LaTeX-related programs for users who want to retain control over
their LaTeX documents. 

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

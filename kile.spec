%define		_version	3.0b4
Summary:	KDE Integrated LaTeX Environment
Summary(pl.UTF-8):	Zintegrowane środowisko LaTeXowe dla KDE
Name:		kile
Version:	2.9.94
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://downloads.sourceforge.net/kile/unstable/%{name}-%{_version}/%{name}-%{version}-1.tar.bz2
# Source0-md5:	2e3dc0703044eaa98c3ee19c3b9eb47f
URL:		http://kile.sourceforge.net/
Patch0:		%{name}-cmake.patch
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Qt5Compat-devel
BuildRequires:	QtScript-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	ka6-okular-devel
BuildRequires:	kf6-ktexteditor-devel
BuildRequires:	cmake
BuildRequires:	qt6-build
BuildRequires:	qt6-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	tetex-format-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%global debug_package %{nil}

%description
KDE Integrated LaTeX Environment. Features:

 - an editor to write your LaTeX source files (syntax highlighting,
   undo-redo, search-replace, spellcheck ...)
 - the principal LaTeX tags can be inserted directly with the "LaTeX",
   "Math" and "Greek" menus
 - 370 mathematical symbols can be inserted in just one click
 - wizards to generate code ('Quick document', 'Quick letter', tabular,
   tabbing and array environments)
 - LaTeX-related programs can be launched via the "Tools" menu
 - contextual help in the "Messages / Log File" frame
 - the standard Bibtex entry types can be inserted in the ".bib" file
   with the "Bibliography" menu
 - a "structure view" of the document for easier navigation of a
   document (by clicking on an item in the "Structure" frame, you can
   jump directly to the corresponding part of your document
 - extensive LaTeX documentation
 - in the "Messages / Log File" frame, you can see information about
   processes and the logfile after a LaTeX compilation
 - the "Next Latex Error" and "Previous Latex Error" commands let you
   reach the LaTeX errors detected by Kile in the log file
 - by clicking on the number of a line in the log file, the cursor
   jumps to the corresponding line in the editor
 - a Gnuplot front end (adaptation of the Xgfe program)
 - support for "Inverse and Forward Search" with KDVI

The program's aim is to simplify the edition of LaTeX source code and
the use of the LaTeX-related programs for users who want to retain
control over their LaTeX documents.

%description -l pl.UTF-8
Zintegrowane środowisko LaTeXowe dla KDE. Możliwości:
 - edytor do pisania plików źródłowych w LaTeXu (z podświetlaniem
   składni, cofaniem i powtarzaniem, szukaniem i zastępowaniem, kontrolą
   pisowni...)
 - podstawowe znaczniki LaTeXa mogą być wstawiane bezpośrednio z menu
   "LaTeX", "Math" lub "Greek"
 - 370 symboli matematycznych może być wstawianych pojedynczym
   kliknięciem
 - automaty do generowania kodu ("Szybki dokument", "Szybki list",
   środowiska tabular, tabbing i array)
 - programy związane z LaTeXem mogą być uruchamiane z menu "Tools"
 - kontekstowa pomoc w ramce "Messages / Log File"
 - standardowe typy wpisów Bibtexa mogą być wstawiane do pliku .bib z
   menu "Bibliography"
 - "strukturalny widok" dokumentu dla łatwiejszej nawigacji po
   dokumencie (poprzez kliknięcie elementu w ramce "Structure", można
   skoczyć bezpośrednio do odpowiedniej części dokumentu)
 - obszerna dokumentacja do LaTeXa
 - w ramce "Messages / Log File" można zobaczyć informacje o
   przetwarzaniu i plik loga po kompilacji LaTeXa
 - polecenia "Next Latex Error" i "Previous Latex Error" pozwalają na
   przechodzenie do miejsc wystąpienia błędów znalezionych przez Kile w
   pliku loga
 - po kliknięciu na numerze linii w pliku loga, kursor skacze do
   odpowiedniej linii w edytorze
 - interfejs do Gnuplota (adaptacja programu Xgfe)
 - obsługa "Inverse and Forward Search" w KDVI.

Celem programu jest uproszczenie edycji kodu źródłowego w LaTeXu i
używania programów związanych z LaTeXem dla użytkowników, którzy chcą
zachować kontrolę nad dokumentami w LaTeXu.

%prep
%setup -q
#%patch0 -p1

%build
install -d build
cd build
%cmake \
-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
-DCMAKE_INSTALL_PREFIX=%{_prefix} \
-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
-DKILE_VERSION=%{version} \
../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
DESTDIR=$RPM_BUILD_ROOT \
kde_htmldir=%{_kdedocdir}

%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/*/44x44
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/*/150x150
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/*/310x310

#%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.cwl kile-remote-control.txt 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/kile
%{_datadir}/kconf_update/*
%{_datadir}/config.kcfg/kile.kcfg
%{_desktopdir}/org.kde.kile.desktop
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/*/*/apps/*.svg
%{_datadir}/dbus-1/interfaces/org.kde.kile.main.xml
%{_datadir}/mime/packages/kile.xml
%{_datadir}/metainfo/org.kde.kile.appdata.xml
%{_datadir}/qlogging-categories6//kile.categories
%{_docdir}/

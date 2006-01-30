Summary:	KDE Integrated LaTeX Environment
Summary(pl):	Zintegrowane ¶rodowisko LaTeXowe dla KDE
Name:		kile
Version:	1.9
%define	_beta	b2
Release:	0.%{_beta}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kile/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	d017eee9f8e692f528404c5fa332edba
Patch0:		%{name}-desktop.patch
URL:		http://kile.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	tetex-format-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Integrated LaTeX Environment. Features:

 - an editor to write your LaTeX source files (syntax highlighting,
   undo-redo, search-replace, spellcheck ...)
 - the principal LaTeX tags can be inserted directly with the "LaTeX",
   "Math" and "Greek" menus
 - 370 mathematical symbols can be inserted in just one click
 - wizards to generate code ('Quick document', 'Quick letter',
   tabular, tabbing and array environments)
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

%description -l pl
Zintegrowane ¶rodowisko LaTeXowe dla KDE. Mo¿liwo¶ci:
 - edytor do pisania plików ¼ród³owych w LaTeXu (z pod¶wietlaniem
   sk³adni, cofaniem i powtarzaniem, szukaniem i zastêpowaniem,
   kontrol± pisowni...)
 - podstawowe znaczniki LaTeXa mog± byæ wstawiane bezpo¶rednio z menu
   "LaTeX", "Math" lub "Greek"
 - 370 symboli matematycznych mo¿e byæ wstawianych pojedynczym
   klikniêciem
 - automaty do generowania kodu ("Szybki dokument", "Szybki list",
   ¶rodowiska tabular, tabbing i array)
 - programy zwi±zane z LaTeXem mog± byæ uruchamiane z menu "Tools"
 - kontekstowa pomoc w ramce "Messages / Log File"
 - standardowe typy wpisów Bibtexa mog± byæ wstawiane do pliku .bib z
   menu "Bibliography"
 - "strukturalny widok" dokumentu dla ³atwiejszej nawigacji po
   dokumencie (poprzez klikniêcie elementu w ramce "Structure", mo¿na
   skoczyæ bezpo¶rednio do odpowiedniej czê¶ci dokumentu)
 - obszerna dokumentacja do LaTeXa
 - w ramce "Messages / Log File" mo¿na zobaczyæ informacje o
   przetwarzaniu i plik loga po kompilacji LaTeXa
 - polecenia "Next Latex Error" i "Previous Latex Error" pozwalaj± na
   przechodzenie do miejsc wyst±pienia b³êdów znalezionych przez Kile
   w pliku loga
 - po klikniêciu na numerze linii w pliku loga, kursor skacze do
   odpowiedniej linii w edytorze
 - interfejs do Gnuplota (adaptacja programu Xgfe)
 - obs³uga "Inverse and Forward Search" w KDVI.

Celem programu jest uproszczenie edycji kodu ¼ród³owego w LaTeXu i
u¿ywania programów zwi±zanych z LaTeXem dla u¿ytkowników, którzy chc±
zachowaæ kontrolê nad dokumentami w LaTeXu.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
	--enable-final \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/katepart

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kile
%{_datadir}/mimelnk/text/x-kilepr.desktop
%{_datadir}/apps/kconf_update/kile.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kile*_upd.pl
%{_datadir}/config.kcfg/kile.kcfg
%{_desktopdir}/kde/kile.desktop
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/*/*/apps/*.svgz

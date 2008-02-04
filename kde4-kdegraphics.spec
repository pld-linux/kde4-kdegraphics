#
# Conditional build:
%bcond_with	protections		# protections against fair use (printing and copying)
%bcond_without	hidden_visibility	# no gcc hidden visibility
#
%define		_state		unstable

Summary:	K Desktop Environment - Graphic Applications
Summary(es.UTF-8):	K Desktop Environment - aplicaciones gráficas
Summary(pl.UTF-8):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR.UTF-8):	K Desktop Environment - Aplicações gráficas
%define	orgname	kdegraphics
Name:		kde4-kdegraphics
Version:	4.0.60
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/latest/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	e84096cdb1792b438443a6b59f26bebf
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.1.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	chmlib-devel
BuildRequires:	djvulibre-devel
BuildRequires:	ed
BuildRequires:	exiv2-devel
BuildRequires:	fribidi-devel >= 0.10.4
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-devel
BuildRequires:	ghostscript-devel
BuildRequires:	giflib-devel
BuildRequires:	imlib-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kpathsea
BuildRequires:	lcms-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libieee1284-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	poppler-Qt-devel
BuildRequires:	poppler-qt-devel
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sane-backends-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphic applications for the K Desktop Environment.

Included with this package are:

- Kamera - digital camera support
- KColorEdit - color palette editor
- KColorChooser - color chooser
- KDVI - displays TeX's device independent (.dvi) files,
- KFax - displays fax files,
- KFract - a fractal generator,
- KGhostview - displays postscript (.ps) files,
- KIconedit - icon editor,
- Kooka - a scanning tool
- KPaint - a simple drawing program,
- KRuler - a screen ruler
- KSnapshot - screen capture,
- KuickShow - an image viewer
- KView - displays numerous graphic file formats.

%description -l es.UTF-8
Aplicaciones gráficas para KDE.

Incluidos en este paquete:
- KDVI - visualiza archivos TeX's independientes de dispositivo,
- KFax - visualiza archivos de fax,
- KFract - creador de fractal
- KGhostview - visualiza archivos postscript (.ps),
- KPaint - un programa sencillo de dibujo,
- KView - visualiza numerosos formatos de archivos gráficos.

%description -l pl.UTF-8
Aplikacje graficzne dla KDE.

Pakiet zawiera programy:

- Kamera - obsługa kamer cyfrowych
- KDVI - przeglądarka plików DVI,
- KColorEdit - edytor palety kolorów
- KColorChooser - wybór koloru
- KFax - program do wyświetlania faksów,
- KFract - generator fraktali,
- KGhostview - program do oglądania postscriptu (.ps),
- KIconedit - program do edycji ikon dla KDE,
- KPaint - prosty program do grafiki rastrowej,
- KRuler - linijka ekranowa
- KSnapshot - program do przechwytywania wyglądu ekranu,
- KuickShow - przeglądarka plików graficznych.
- KView - przeglądarka plików graficznych.

%description -l pt_BR.UTF-8
Aplicações gráficas para o KDE.

Incluídos neste pacote:
- KDVI - visualiza arquivos TeX's independentes de dispositivo,
- KFax - visualiza arquivos de fax,
- KFract - gerador de fractal,
- KGhostview - visualiza arquivos postscript (.ps),
- KPaint - um programa simples de desenho,
- KView - visualiza numerosos formatos de arquivos gráficos.

%package devel
Summary:	kdegraphics development files
Summary(pl.UTF-8):	Pliki dla programistów kdegraphics
Summary(pt_BR.UTF-8):	Arquivos de inclusão para compilação de aplicações com kdegraphics
Group:		X11/Development/Libraries
Requires:	kde4-kdelibs-devel
Requires:	%{name}-okular = %{version}
Requires:	%{name}-kolourpaint = %{version}

%description devel
kdegraphics development files.

%description devel -l pl.UTF-8
Pliki dla programistów kdegraphics.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para compilação de aplicações que usem as
bibliotecas do kdegraphics.

%package kamera
Summary:	Digital camera support
Summary(pl.UTF-8):	Obsługa kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase-core >= %{version}

%description kamera
kamera is an IO slave and a KControl panel module which allows you to
access folders and images within any digital camera supported by the
upcoming gPhoto2 libraries. If you have a supported camera, you can
start using it with most KDE applications in two easy steps: simply
configure your camera model and port type from a list in KControl,
then start accessing the camera contents with a kamera:/ URL.

%description kamera -l pl.UTF-8
kamera to moduł IO slave oraz panelu KControl umożliwiający dostęp do
folderów i zdjęć w dowolnym aparacie cyfrowym obsługiwanym przez
biblioteki gPhoto2. Jeśli mamy obsługiwany aparat, można zacząć używać
go w większości aplikacji KDE w dwóch krokach: wybrać model i port
aparatu z listy w KControl, a następnie odwoływać się do zawartości
aparatu przez URL kamera:/.

%package kcolorchooser
Summary:	Color chooser
Summary(pl.UTF-8):	Program do wybierania kolorów
Group:		X11/Applications/Graphics
Requires:	kde4-kdelibs >= %{version}

%description kcolorchooser
Color chooser.

%description kcolorchooser -l pl.UTF-8
Program do wybierania kolorów.

%package kfile
Summary:	Graphic formats enhanced information
Summary(pl.UTF-8):	Rozszerzone informacje o plikach graficznych
Group:		X11/Applications/Graphics
Requires:	konqueror >= %{version}

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations.

%description kfile -l pl.UTF-8
Ten pakiet dodaje do okna dialogowego "właściwości pliku" konquerora
dodatkową zakładkę z rozszerzonymi informacjami o pliku.

%package kgamma
Summary:	A monitor calibration tool
Summary(pl.UTF-8):	Narzędzie do kalibracji monitora
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase-core >= %{version}

%description kgamma
A monitor calibration tool.

%description kgamma -l pl.UTF-8
Narzędzie do kalibracji monitora.

%package kolourpaint
Summary:	KDE Painter
Summary(pl.UTF-8):	Program graficzny KDE
Summary(pt_BR.UTF-8):	Editor básico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase-core >= %{version}

%description kolourpaint
A (very) simple painting program for KDE.

%description kolourpaint -l pl.UTF-8
(Bardzo) prosty program do rysowania pod KDE.

%description kolourpaint -l pt_BR.UTF-8
Editor básico de imagens bitmap.

%package kscanservice
Summary:	Scanning tool
Summary(pl.UTF-8):	Narzędzie do skanowania
Summary(pt_BR.UTF-8):	Um programa de rasterização de imagens, baseado no SANE e libkscan
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase-core >= %{version}

%description kscanservice
Kooka is a KDE application that enables easy scanning using SANE
libraries.

%description kscanservice -l pl.UTF-8
Kooka to aplikacja KDE umożliwiająca łatwe skanowanie przy użyciu
bibliotek SANE.

%description kscanservice -l pt_BR.UTF-8
Um programa de rasterização de imagens, baseado no SANE e libkscan.

%package kruler
Summary:	KRuler
Summary(pl.UTF-8):	Linijka dla KDE
Summary(pt_BR.UTF-8):	Régua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase-core >= %{version}

%description kruler
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description kruler -l pl.UTF-8
KRuler jest prostą aplikacją, z tylko jednym celem w życiu: mierzenie
odległości na ekranie.

%description kruler -l pt_BR.UTF-8
Régua de pixels para a tela.

%package ksnapshot
Summary:	KDE Snap Shot
Summary(pl.UTF-8):	Program do przechwytywania ekranu dla KDE
Summary(pt_BR.UTF-8):	Programa de captura de tela
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase-core >= %{version}

%description ksnapshot
KSnapshot is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description ksnapshot -l pl.UTF-8
KSnapshot to prosta aplikacja do robienia zrzutów ekranu. Potrafi
przechwytywać obraz całego pulpitu lub tylko pojedynczego okna. Obrazy
mogą być następnie zapisane w wielu formatach.

%description ksnapshot -l pt_BR.UTF-8
Programa de captura de tela.

%package svgpart
Summary:	Scalable Vector Graphics for KDE
Summary(pl.UTF-8):	Skalowalna grafika wektorowa (SVG) dla KDE
Group:		X11/Applications/Graphics
Requires:	kde4-kdelibs >= %{version}

%description svgpart
KSVG is a KDE implementation of the Scalable Vector Graphics
Specifications.

%description svgpart -l pl.UTF-8
KSVG stanowi implementację dla KDE specyfikacji skalowalnej grafiki
wektorowej (SVG - Scalable Vector Graphics).

%package okular
Summary:	KDE okular
Summary(pl.UTF-8):	KDE okular
Group:		X11/Applications/Graphics
Requires:	kde4-kdelibs >= %{version}

%description okular
Okular.

%description okular -l pl.UTF-8
Okular.

%package gwenview
Summary:	Simple image viewer for KDE
Summary(pl.UTF-8):	Prosta przeglądarka obrazków dla KDE
Group:		X11/Applications/Graphics
Requires:	kde4-kdelibs >= %{version}

%description gwenview
Gwenview is an image viewer for KDE.

It features a folder tree window and a file list window to provide
easy navigation in your file hierarchy. Image loading is done by the
Qt library, so it supports all image formats your Qt installation
supports.

%description gwenview -l pl.UTF-8
Gwenview to przeglądarka obrazków dla KDE. Ma okno z drzewem katalogów
oraz okno z listą plików w celu zapewnienia łatwej nawigacji w
hierarchii plików. Wczytywanie obrazków jest wykonywane przez
bibliotekę Qt, więc przeglądarka obsługuje wszystkie formaty
obsługiwane przez zainstalowaną wersję Qt.

%prep
%setup -q -n %{orgname}-%{version}

%build
export QTDIR=%{_prefix}
install -d build
cd build
%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
        ../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	gwenview	-p /sbin/ldconfig
%postun	gwenview	-p /sbin/ldconfig

%post	kolourpaint	-p /sbin/ldconfig
%postun	kolourpaint	-p /sbin/ldconfig

%post	okular		-p /sbin/ldconfig
%postun	okular		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkolourpaint4_lgpl.so
%attr(755,root,root) %{_libdir}/libokularcore.so
%attr(755,root,root) %{_libdir}/libgwenviewlib.so
%attr(755,root,root) %{_libdir}/libspectreOkular.so
%{_includedir}/okular

%files kamera
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kamera.so
%attr(755,root,root) %{_libdir}/kde4/kio_kamera.so
%{_datadir}/kde4/services/kamera.desktop
%{_datadir}/kde4/services/camera.protocol
%{_kdedocdir}/en/kamera

%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_desktopdir}/kde4/kcolorchooser.desktop
%{_iconsdir}/[!l]*/*/*/kcolorchooser.*

%files kfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/gsthumbnail.so
%{_datadir}/kde4/services/gsthumbnail.desktop
### ????
%attr(755,root,root) %{_libdir}/strigi/strigita_dvi.so
#%attr(755,root,root) %{_libdir}/strigi/strigita_ico.so

%files kgamma
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xf86gammacfg
%attr(755,root,root) %{_libdir}/kde4/kcm_kgamma.so
%{_datadir}/apps/kgamma
%{_datadir}/kde4/services/kgamma.desktop
%{_iconsdir}/*/*/apps/kgamma.png

%files kolourpaint
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolourpaint4
%attr(755,root,root) %{_libdir}/libkolourpaint4_lgpl.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libkolourpaint4_lgpl.so.?
%{_datadir}/apps/kolourpaint4
%{_desktopdir}/kde4/kolourpaint4.desktop
%{_iconsdir}/*/*/apps/kolourpaint4.*
%{_kdedocdir}/en/kolourpaint4

%files kscanservice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kscanplugin.so
%{_datadir}/kde4/services/scanservice.desktop
%{_iconsdir}/*/*/actions/palette*

%files kruler
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_desktopdir}/kde4/kruler.desktop
%{_iconsdir}/*/*/apps/kruler.*
%{_kdedocdir}/en/kruler

%files ksnapshot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%attr(755,root,root) %{_bindir}/kbackgroundsnapshot
%{_desktopdir}/kde4/ksnapshot.desktop
%{_iconsdir}/*/*/apps/ksnapshot.*
%{_datadir}/dbus-1/interfaces/org.kde.ksnapshot.xml
%{_kdedocdir}/en/ksnapshot

%files svgpart
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/svgpart.so
%{_datadir}/apps/svgpart
%{_datadir}/kde4/services/svgpart.desktop

%files okular
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okular
%attr(755,root,root) %{_libdir}/libokularcore.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/okular*.so
%ghost %attr(755,root,root) %{_libdir}/libokularcore.so.?
%attr(755,root,root) %{_libdir}/libspectreOkular.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libspectreOkular.so.?
%{_datadir}/apps/okular
%{_datadir}/config.kcfg/okular.kcfg
%{_datadir}/config/okular.knsrc
%{_datadir}/kde4/services/okular*.desktop
%{_datadir}/kde4/services/libokular*.desktop
%{_datadir}/kde4/servicetypes/okular*.desktop
%{_desktopdir}/kde4/okular*.desktop
%{_kdedocdir}/en/okular

%files gwenview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwenview
%attr(755,root,root) %{_libdir}/kde4/gvpart.so
%attr(755,root,root) %{_libdir}/kde4/kio_msits.so
%ghost %attr(755,root,root) %{_libdir}/libgwenviewlib.so.?
%attr(755,root,root) %{_libdir}/libgwenviewlib.so.*.*.*
%dir %{_datadir}/apps/gwenview
%{_datadir}/apps/gwenview/gwenviewui.rc
%dir %{_datadir}/apps/gvpart
%{_datadir}/apps/gvpart/gvpart.rc
%{_datadir}/kde4/services/msits.protocol
%{_datadir}/kde4/services/gvpart.desktop
%{_desktopdir}/kde4/gwenview.desktop
%{_iconsdir}/*/*/apps/gwenview.png
%{_iconsdir}/*/scalable/apps/gwenview.svgz
%{_kdedocdir}/en/gwenview
                                                                     

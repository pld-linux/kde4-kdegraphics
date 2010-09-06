# TODO: real descs for okular and KIPI libs
%define		_state		stable
%define		qtver		4.6.3

%define	orgname	kdegraphics
Summary:	K Desktop Environment - Graphic Applications
Summary(es.UTF-8):	K Desktop Environment - aplicaciones gr�ficas
Summary(pl.UTF-8):	K Desktop Environment - Aplikacje graficzne
Summary(pt_BR.UTF-8):	K Desktop Environment - Aplica��es gr�ficas
Name:		kde4-kdegraphics
Version:	4.5.1
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	11c3da572a6205bf5d898e8958d4aadd
Patch100: %{name}-branch.diff
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	chmlib-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	djvulibre-devel
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel >= 0.18.2
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	lcms-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libspectre-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	poppler-Qt-devel
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qimageblitz-devel >= 0.0.6
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sane-backends-devel
BuildRequires:	shared-desktop-ontologies-devel >= 0.5
BuildRequires:	soprano-devel >= 2.4.64
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphic applications for the K Desktop Environment.

Included with this package are:

- Kamera - digital camera support
- KColorChooser - color chooser
- KFile
- KGamma
- KolourPaint - a simple drawing program
- KSANE - a scanning tool
- KRuler - a screen ruler
- KSnapshot - screen capture
- svgpart
- oKular
- gwenview - an image viewer

%description -l es.UTF-8
Aplicaciones gr�ficas para KDE.

Incluidos en este paquete:
- Kamera
- KColorChooser
- KFile
- KGamma
- KolourPaint - un programa sencillo de dibujo
- KSANE
- KRuler
- KSnapshot
- svgpart
- oKular
- gwenview - visualiza numerosos formatos de archivos gr�ficos

%description -l pl.UTF-8
Aplikacje graficzne dla KDE.

Pakiet zawiera programy:

- Kamera - obs�uga kamer cyfrowych
- KColorChooser - wyb�r koloru
- KFile
- KGamma
- KolourPaint - prosty program do grafiki rastrowej
- KRuler - linijka ekranowa
- KSane - narz�dzie do skanowania
- KSnapshot - program do przechwytywania wygl�du ekranu
- svgpart
- oKular
- gwenview - przegl�darka plik�w graficznych

%description -l pt_BR.UTF-8
Aplica��es gr�ficas para o KDE.

Inclu�dos neste pacote:
- Kamera
- KColorChooser
- KFile
- KGamma
- KolourPaint - um programa simples de desenho
- KRuler
- KSANE
- KSnapshot
- svgpart
- oKular
- gwenview - visualiza numerosos formatos de arquivos gr�ficos

%package devel
Summary:	kdegraphics development files
Summary(pl.UTF-8):	Pliki dla programist��w kdegraphics
Summary(pt_BR.UTF-8):	Arquivos de inclus�o para compila��o de aplica��es com kdegraphics
Group:		X11/Development/Libraries
Requires:	%{name}-gwenview = %{version}-%{release}
Requires:	%{name}-kolourpaint = %{version}-%{release}
Requires:	%{name}-ksane = %{version}-%{release}
Requires:	%{name}-okular = %{version}-%{release}
Requires:	kde4-kdelibs-devel
Requires:	kde4-libkdcraw = %{version}-%{release}
Requires:	kde4-libkexiv2 = %{version}-%{release}
Requires:	kde4-libkipi = %{version}-%{release}

%description devel
kdegraphics development files.

%description devel -l pl.UTF-8
Pliki dla programist��w kdegraphics.

%description devel -l pt_BR.UTF-8
Arquivos de inclus�o para compila��o de aplica��es que usem as
bibliotecas do kdegraphics.

%package kamera
Summary:	Digital camera support
Summary(pl.UTF-8):	Obs�uga kamer cyfrowych
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase >= %{version}

%description kamera
kamera is an IO slave and a KControl panel module which allows you to
access folders and images within any digital camera supported by the
upcoming gPhoto2 libraries. If you have a supported camera, you can
start using it with most KDE applications in two easy steps: simply
configure your camera model and port type from a list in KControl,
then start accessing the camera contents with a kamera:/ URL.

%description kamera -l pl.UTF-8
kamera to modu� IO slave oraz panelu KControl umo�liwiaj�cy dost�p do
folder�w i zdj�� w dowolnym aparacie cyfrowym obs�ugiwanym przez
biblioteki gPhoto2. Je�li mamy obs�ugiwany aparat, mo�na zacz�� u�ywa�
go w wi�kszo�ci aplikacji KDE w dw�ch krokach: wybra� model i port
aparatu z listy w KControl, a nast�pnie odwo�ywa� si� do zawarto�ci
aparatu przez URL kamera:/.

%package kcolorchooser
Summary:	Color chooser
Summary(pl.UTF-8):	Program do wybierania kolor�w
Group:		X11/Applications/Graphics
Requires:	kde4-kdelibs >= %{version}

%description kcolorchooser
Color chooser.

%description kcolorchooser -l pl.UTF-8
Program do wybierania kolor�w.

%package kfile
Summary:	Graphic formats enhanced information
Summary(pl.UTF-8):	Rozszerzone informacje o plikach graficznych
Group:		X11/Applications/Graphics
Requires:	kde4-konqueror >= %{version}

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations.

%description kfile -l pl.UTF-8
Ten pakiet dodaje do okna dialogowego "w�a�ciwo�ci pliku" konquerora
dodatkow� zak�adk� z rozszerzonymi informacjami o pliku.

%package kgamma
Summary:	A monitor calibration tool
Summary(pl.UTF-8):	Narz�dzie do kalibracji monitora
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase >= %{version}

%description kgamma
A monitor calibration tool.

%description kgamma -l pl.UTF-8
Narz�dzie do kalibracji monitora.

%package kolourpaint
Summary:	KDE Painter
Summary(pl.UTF-8):	Program graficzny KDE
Summary(pt_BR.UTF-8):	Editor b�sico de imagens bitmap
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase >= %{version}

%description kolourpaint
A (very) simple painting program for KDE.

%description kolourpaint -l pl.UTF-8
(Bardzo) prosty program do rysowania pod KDE.

%description kolourpaint -l pt_BR.UTF-8
Editor b�sico de imagens bitmap.

%package kruler
Summary:	KRuler
Summary(pl.UTF-8):	Linijka dla KDE
Summary(pt_BR.UTF-8):	R�gua de pixels para a tela
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase >= %{version}

%description kruler
KRuler is a very simple application, with only one aim in life. To
measure distances on your screen.

%description kruler -l pl.UTF-8
KRuler jest prost� aplikacj�, z tylko jednym celem w �yciu: mierzenie
odleg�o�ci na ekranie.

%description kruler -l pt_BR.UTF-8
R�gua de pixels para a tela.

%package ksane
Summary:	Scanning tool
Summary(pl.UTF-8):	Narz�dzie do skanowania
Summary(pt_BR.UTF-8):	Um programa de rasteriza��o de imagens, baseado no SANE e libkscan
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdegraphics-kscanservice
Conflicts:	kde4-kdegraphics-kscanservice

%description ksane
Ksane is a KDE application that enables easy scanning using SANE
libraries.

%description ksane -l pl.UTF-8
Ksane to aplikacja KDE umo�liwiaj�ca �atwe skanowanie przy u�yciu
bibliotek SANE.

%description ksane -l pt_BR.UTF-8
Um programa de rasteriza��o de imagens, baseado no SANE e libkscan.

%package ksnapshot
Summary:	KDE Snap Shot
Summary(pl.UTF-8):	Program do przechwytywania ekranu dla KDE
Summary(pt_BR.UTF-8):	Programa de captura de tela
Group:		X11/Applications/Graphics
Requires:	kde4-kdebase >= %{version}

%description ksnapshot
KSnapshot is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description ksnapshot -l pl.UTF-8
KSnapshot to prosta aplikacja do robienia zrzut�w ekranu. Potrafi
przechwytywa� obraz ca�ego pulpitu lub tylko pojedynczego okna. Obrazy
mog� by� nast�pnie zapisane w wielu formatach.

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
KSVG stanowi implementacj� dla KDE specyfikacji skalowalnej grafiki
wektorowej (SVG - Scalable Vector Graphics).

%package okular
Summary:	KDE universal document viewer
Summary(pl.UTF-8):	Uniwersalna przegl�darka dokument�wdla KDE
Group:		X11/Applications/Graphics
Requires:	kde4-kdelibs >= %{version}
Requires:	kio_msits >= %{version}

%description okular
Okular is a universal document browser for KDE.

%description okular -l pl.UTF-8
Okular to uniwersalna przegl�darka dokument�w dla KDE.

%package gwenview
Summary:	Simple image viewer for KDE
Summary(pl.UTF-8):	Prosta przegl�darka obrazk�w dla KDE
Group:		X11/Applications/Graphics
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	gwenview

%description gwenview
Gwenview is an image viewer for KDE.

It features a folder tree window and a file list window to provide
easy navigation in your file hierarchy. Image loading is done by the
Qt library, so it supports all image formats your Qt installation
supports.

%description gwenview -l pl.UTF-8
Gwenview to przegl�darka obrazk�w dla KDE. Ma okno z drzewem katalog�w
oraz okno z list� plik�w w celu zapewnienia �atwej nawigacji w
hierarchii plik�w. Wczytywanie obrazk�w jest wykonywane przez
bibliotek� Qt, wi�c przegl�darka obs�uguje wszystkie formaty
obs�ugiwane przez zainstalowan� wersj� Qt.

%package -n kde4-libkdcraw
Summary:	KDcraw library
Summary(pl.UTF-8):	Biblioteka KDcraw
Group:		X11/Libraries
Obsoletes:	libkdcraw

%description -n kde4-libkdcraw
The KDcraw library is part of the KIPI Project.

%description -n kde4-libkdcraw -l pl.UTF-8
Biblioteka KDcraw jest cz��ci� projektu KIPI.

%package -n kde4-libkexiv2
Summary:	libkexiv2 library
Summary(pl.UTF-8):	Biblioteka libkexiv2
Group:		X11/Libraries

%description -n kde4-libkexiv2
libkexiv2 library.

%description -n kde4-libkexiv2 -l pl.UTF-8
Biblioteka libkexiv2.

%package -n kde4-libkipi
Summary:	kipi library
Summary(pl.UTF-8):	Biblioteka kipi
Group:		X11/Libraries
Obsoletes:	kde4-kipiplugins

%description -n kde4-libkipi
libkipi library.

%description -n kde4-libkipi -l pl.UTF-8
Biblioteka libkipi.

%package -n kio_msits
Summary:	A kioslave for displaying WinHelp files
Group:		X11/Libraries

%description -n kio_msits
A kioslave for displaying WinHelp files.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DGWENVIEW_SEMANTICINFO_BACKEND=Nepomuk \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	kolourpaint	-p /sbin/ldconfig
%postun	kolourpaint	-p /sbin/ldconfig

%post	ksane		-p /sbin/ldconfig
%postun	ksane		-p /sbin/ldconfig

%post	okular		-p /sbin/ldconfig
%postun	okular		-p /sbin/ldconfig

%post	gwenview	-p /sbin/ldconfig
%postun	gwenview	-p /sbin/ldconfig

%post	-n kde4-libkexiv2	-p /sbin/ldconfig
%postun	-n kde4-libkexiv2	-p /sbin/ldconfig

%post	-n kde4-libkdcraw	-p /sbin/ldconfig
%postun	-n kde4-libkdcraw	-p /sbin/ldconfig

%post	-n kde4-libkipi	-p /sbin/ldconfig
%postun	-n kde4-libkipi	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkolourpaint_lgpl.so
%attr(755,root,root) %{_libdir}/libokularcore.so
%attr(755,root,root) %{_libdir}/libgwenviewlib.so
%attr(755,root,root) %{_libdir}/libksane.so
%attr(755,root,root) %{_libdir}/libkexiv2.so
%attr(755,root,root) %{_libdir}/libkdcraw.so
%attr(755,root,root) %{_libdir}/libkipi.so
%{_includedir}/libksane
%{_includedir}/okular
%{_datadir}/apps/cmake/modules/FindOkular.cmake
%{_datadir}/apps/cmake/modules/FindKSane.cmake
%{_pkgconfigdir}/libkdcraw.pc
%{_pkgconfigdir}/libkexiv2.pc
%{_pkgconfigdir}/libkipi.pc
%{_pkgconfigdir}/libksane.pc
%{_includedir}/libkdcraw
%{_includedir}/libkexiv2
%{_includedir}/libkipi

%files kamera
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kcm_kamera.so
%attr(755,root,root) %{_libdir}/kde4/kio_kamera.so
%{_datadir}/kde4/services/kamera.desktop
%{_datadir}/kde4/services/camera.protocol
%{_kdedocdir}/en/kcontrol/kamera

%files kcolorchooser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcolorchooser
%{_desktopdir}/kde4/kcolorchooser.desktop
%{_iconsdir}/[!l]*/*/*/kcolorchooser.*

%files kfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/gsthumbnail.so
%{_datadir}/kde4/services/gsthumbnail.desktop
%{_datadir}/config.kcfg/gssettings.kcfg
%attr(755,root,root) %{_libdir}/strigi/strigiea_dvi.so
%attr(755,root,root) %{_libdir}/strigi/strigiea_tiff.so

%files kgamma
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xf86gammacfg
%attr(755,root,root) %{_libdir}/kde4/kcm_kgamma.so
%{_datadir}/apps/kgamma
%{_datadir}/kde4/services/kgamma.desktop
#%{_iconsdir}/*/*/apps/kgamma.png
%{_kdedocdir}/en/kcontrol/kgamma/

%files kolourpaint
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolourpaint
%attr(755,root,root) %{_libdir}/libkolourpaint_lgpl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkolourpaint_lgpl.so.?
%{_datadir}/apps/kolourpaint
%{_desktopdir}/kde4/kolourpaint.desktop
%{_iconsdir}/*/*/apps/kolourpaint.*
%{_kdedocdir}/en/kolourpaint

%files kruler
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kruler
%{_datadir}/apps/kruler
%{_desktopdir}/kde4/kruler.desktop
%{_iconsdir}/*/*/apps/kruler.*
%{_kdedocdir}/en/kruler

%files ksane
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libksane.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libksane.so.?
%attr(755,root,root) %{_libdir}/kde4/ksaneplugin.so
%{_datadir}/kde4/services/ksane_scan_service.desktop

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
%attr(755,root,root) %ghost %{_libdir}/libokularcore.so.?
%attr(755,root,root) %{_libdir}/kde4/okular*.so
%attr(755,root,root) %{_libdir}/kde4/mobithumbnail.so
%attr(755,root,root) %{_libdir}/kde4/rawthumbnail.so
%attr(755,root,root) %{_libdir}/strigi/strigila_mobi.so
%{_datadir}/apps/okular
%{_datadir}/config.kcfg/okular.kcfg
#%{_datadir}/config/okular.knsrc
%{_datadir}/kde4/services/okular*.desktop
%{_datadir}/kde4/services/libokular*.desktop
%{_datadir}/kde4/services/mobithumbnail.desktop
%{_datadir}/kde4/services/rawthumbnail.desktop
%{_datadir}/kde4/servicetypes/okular*.desktop
%{_desktopdir}/kde4/okular*.desktop
# ??
%{_datadir}/kde4/services/ServiceMenus/slideshow.desktop
#
%{_iconsdir}/hicolor/*/apps/okular.png
#%{_iconsdir}/hicolor/scalable/apps/okular.svgz
%{_kdedocdir}/en/okular

%files gwenview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwenview
%attr(755,root,root) %{_bindir}/gwenview_importer
%attr(755,root,root) %{_libdir}/libgwenviewlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwenviewlib.so.?
%attr(755,root,root) %{_libdir}/kde4/gvpart.so
%dir %{_datadir}/apps/gwenview
%dir %{_datadir}/apps/gwenview/cursors
%{_datadir}/apps/gwenview/cursors/zoom.png
%{_datadir}/apps/gwenview/fullscreenthemes
%{_datadir}/apps/gwenview/gwenviewui.rc
%dir %{_datadir}/apps/gvpart
%{_datadir}/apps/gvpart/gvpart.rc
%{_datadir}/kde4/services/gvpart.desktop
%{_desktopdir}/kde4/gwenview.desktop
%{_datadir}/apps/solid/actions/gwenview_importer.desktop
%{_iconsdir}/*/*/apps/gwenview.png
#%{_iconsdir}/*/scalable/apps/gwenview.svgz
%{_kdedocdir}/en/gwenview

%files -n kde4-libkdcraw
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkdcraw.so.?
%attr(755,root,root) %{_libdir}/libkdcraw.so.*.*.*
#%dir %{_libdir}/libkdcraw6
#%attr(755,root,root) %{_libdir}/libkdcraw6/kdcraw
#%{_libdir}/libkdcraw6/CAMERALIST
%{_datadir}/apps/solid/actions/solid_camera.desktop
%{_datadir}/apps/libkdcraw
%{_iconsdir}/hicolor/*x*/apps/kdcraw.png

%files -n kde4-libkexiv2
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkexiv2.so.?
%attr(755,root,root) %{_libdir}/libkexiv2.so.*.*.*
%dir %{_datadir}/apps/libkexiv2
%dir %{_datadir}/apps/libkexiv2/data
%{_datadir}/apps/libkexiv2/data/topicset.iptc-subjectcode.xml

%files -n kde4-libkipi
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkipi.so.?
%attr(755,root,root) %{_libdir}/libkipi.so.*.*.*
%{_datadir}/apps/kipi
%{_iconsdir}/hicolor/*x*/apps/kipi.png
%{_iconsdir}/hicolor/16x16/actions/black-white.png
%{_iconsdir}/hicolor/16x16/actions/color.png
%{_iconsdir}/hicolor/16x16/actions/gray-scale.png
%{_datadir}/kde4/servicetypes/kipiplugin.desktop

%files -n kio_msits
%defattr(644,root,root,755)
%{_libdir}/kde4/kio_msits.so
%{_datadir}/kde4/services/msits.protocol

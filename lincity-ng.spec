Summary:	Lincity - a Next Generation city/country simulation
Summary(pl):	Lincity - symulator miasta/kraju Nastêpnej Generacji
Name:		lincity-ng
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		Applications/Games
Source0:	http://download.berlios.de/lincity-ng/%{name}-%{version}.tar.bz2
# Source0-md5:	2624857ed9437ac30445884d8593850e
URL:		http://lincity-ng.berlios.de/wiki/index.php/Main_Page
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel >= 1.2.3
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	physfs-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	gettext-devel
BuildRequires:	jam >= 2.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	zlib-devel >= 1.0
Requires:	SDL >= 1.2.5
Requires:	SDL_image >= 1.2.3
Requires:	SDL_mixer >= 1.2.4
Requires:	SDL_ttf >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You are required to build and maintain a city. You must feed, house,
provide jobs and goods for your residents. You can build a sustainable
economy with the help of renewable energy and recycling, or you can go
for broke and build rockets to escape from a pollution ridden and
resource starved planet, it's up to you. Due to the finite resources
available in any one place, this is not a game that you can leave for
long periods of time.

%description -l pl
Trzeba wybudowaæ miasto i nim zarz±dzaæ. Trzeba karmiæ mieszkañców,
zapewniæ im mieszkanie, pracê i inne dobra. Mo¿na stworzyæ solidn±
gospodarkê korzystaj±c z odnawialnych ¼róde³ energii i przetwórstwa
odpadów. Mo¿na te¿ wielkim wysi³kiem zbudowaæ rakiety, aby uciec z
zanieczyszczonej, pozbawionej zasobów planety. Ca³e ¿ycie miasta
znajduje siê w rêkach gracza.

%prep
%setup -q

%build
%configure
/usr/bin/jam

%install
rm -rf $RPM_BUILD_ROOT

/usr/bin/jam -s DESTDIR=$RPM_BUILD_ROOT install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO COPYING-* RELNOTES
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.pal
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_datadir}/%{name}/gui
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/music
%{_datadir}/%{name}/opening
%dir %{_datadir}/%{name}/help
%lang(de) %{_datadir}/%{name}/help/de
%lang(en) %{_datadir}/%{name}/help/en
%lang(es) %{_datadir}/%{name}/help/es
%lang(fr) %{_datadir}/%{name}/help/fr
%lang(nl) %{_datadir}/%{name}/help/nl
%lang(sv) %{_datadir}/%{name}/help/sv
%lang(ca) %{_datadir}/%{name}/locale/ca.po
%lang(ca) %{_datadir}/%{name}/locale/gui/ca.po
%lang(de) %{_datadir}/%{name}/locale/de.po
%lang(de) %{_datadir}/%{name}/locale/gui/de.po
%lang(es) %{_datadir}/%{name}/locale/es.po
%lang(es) %{_datadir}/%{name}/locale/gui/es.po
%lang(fr) %{_datadir}/%{name}/locale/fr.po
%lang(fr) %{_datadir}/%{name}/locale/gui/fr.po
%lang(nl) %{_datadir}/%{name}/locale/nl.po
%lang(nl) %{_datadir}/%{name}/locale/gui/nl.po
%lang(sv) %{_datadir}/%{name}/locale/sv.po
%lang(sv) %{_datadir}/%{name}/locale/gui/sv.po
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

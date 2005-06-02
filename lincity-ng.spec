Summary:	Lincity - a Next Generation city/country simulation
Summary(pl):	Lincity - symulator miasta/kraju Nastêpnej Generacji
Name:		lincity-ng
Version:	0.9
%define	_rel	rc1
Release:	0.%{_rel}.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://download.berlios.de/lincity-ng/lincity-ng-0.9rc1.tar.bz2
# Source0-md5:	e55e0324f872b7a0265ec0814c5d3404
URL:		http://lincity-ng.berlios.de/
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_image-devel >= 1.2.3
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	physfs-devel >= 1.0.0
BuildRequires:	gettext-devel
BuildRequires:	jam >= 2.5
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	zlib-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 and SVGALib strategy game. You are required to build and maintain
a city. You must feed, house, provide jobs and goods for your
residents. You can build a sustainable economy with the help of
renewable energy and recycling, or you can go for broke and build
rockets to escape from a pollution ridden and resource starved planet,
it's up to you. Due to the finite resources available in any one
place, this is not a game that you can leave for long periods of time.
This package contains shared files for X11 and SVGALib.

%description -l pl
Gra strategiczna dla X11 oraz SVGALib. Trzeba wybudowaæ miasto i nim
zarz±dzaæ. Trzeba karmiæ mieszkañców, zapewniæ im mieszkanie, pracê i
inne dobra. Mo¿na stworzyæ solidn± gospodarkê korzystaj±c z odnawialnych 
¼róde³ energii i przetwórstwa odpadów. Mo¿na te¿ wielkim wysi³kiem 
zbudowaæ rakiety, aby uciec z zanieczyszczonej, pozbawionej zasobów 
planety. Ca³e ¿ycie miasta znajduje siê w rêkach gracza. Ten pakiet 
zawiera pliki wspólne dla wersji X11 oraz SVGALib.

%prep
%setup -q -n %{name}-%{version}%{_rel}

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
%doc README* TODO
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
%{_docdir}/%{name}-%{version}%{_rel}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

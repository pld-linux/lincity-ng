Summary:	Lincity - a Next Generation city/country simulation
Summary(pl.UTF-8):	Lincity - symulator miasta/kraju Następnej Generacji
Name:		lincity-ng
Version:	1.1.1
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://download2.berlios.de/lincity-ng/%{name}-%{version}.tar.bz2
# Source0-md5:	b548b04666aa35e44a83e173a6cbe4b1
Patch0:		%{name}-desktop.patch
URL:		http://lincity-ng.berlios.de/wiki/index.php/Main_Page
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	SDL_gfx-devel >= 2.0.13
BuildRequires:	SDL_image-devel >= 1.2.3
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0.8
BuildRequires:	physfs-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	gettext-devel
BuildRequires:	jam >= 2.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel >= 1.0
Requires:	SDL >= 1.2.5
Requires:	SDL_gfx >= 2.0.13
Requires:	SDL_image >= 1.2.3
Requires:	SDL_mixer >= 1.2.4
Requires:	SDL_ttf >= 2.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout	-DNDEBUG

%description
You are required to build and maintain a city. You must feed, house,
provide jobs and goods for your residents. You can build a sustainable
economy with the help of renewable energy and recycling, or you can go
for broke and build rockets to escape from a pollution ridden and
resource starved planet, it's up to you. Due to the finite resources
available in any one place, this is not a game that you can leave for
long periods of time.

%description -l pl.UTF-8
Trzeba wybudować miasto i nim zarządzać. Trzeba karmić mieszkańców,
zapewnić im mieszkanie, pracę i inne dobra. Można stworzyć solidną
gospodarkę korzystając z odnawialnych źródeł energii i przetwórstwa
odpadów. Można też wielkim wysiłkiem zbudować rakiety, aby uciec z
zanieczyszczonej, pozbawionej zasobów planety. Całe życie miasta
znajduje się w rękach gracza.

%prep
%setup -q
%patch0 -p1
%{__sed} 's/ -O3 -g / /' -i Jamrules

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
%lang(cs) %{_datadir}/%{name}/help/cs
%lang(en) %{_datadir}/%{name}/help/en
%lang(es) %{_datadir}/%{name}/help/es
%lang(fr) %{_datadir}/%{name}/help/fr
%lang(nl) %{_datadir}/%{name}/help/nl
%lang(pt_BR) %{_datadir}/%{name}/help/pt_BR
%lang(ru) %{_datadir}/%{name}/help/ru
%lang(sv) %{_datadir}/%{name}/help/sv
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/locale/gui
%lang(ca) %{_datadir}/%{name}/locale/ca.po
%lang(ca) %{_datadir}/%{name}/locale/gui/ca.po
%lang(cs) %{_datadir}/%{name}/locale/cs.po
%lang(cs) %{_datadir}/%{name}/locale/gui/cs.po
%lang(de) %{_datadir}/%{name}/locale/de.po
%lang(de) %{_datadir}/%{name}/locale/gui/de.po
%lang(es) %{_datadir}/%{name}/locale/es.po
%lang(es) %{_datadir}/%{name}/locale/gui/es.po
%lang(fr) %{_datadir}/%{name}/locale/fr.po
%lang(fr) %{_datadir}/%{name}/locale/gui/fr.po
%lang(nl) %{_datadir}/%{name}/locale/nl.po
%lang(nl) %{_datadir}/%{name}/locale/gui/nl.po
%lang(pl) %{_datadir}/%{name}/locale/pl.po
%lang(pl) %{_datadir}/%{name}/locale/gui/pl.po
%lang(pt_BR) %{_datadir}/%{name}/locale/pt_BR.po
%lang(pt_BR) %{_datadir}/%{name}/locale/gui/pt_BR.po
%lang(ru) %{_datadir}/%{name}/locale/ru.po
%lang(ru) %{_datadir}/%{name}/locale/gui/ru.po
%lang(sv) %{_datadir}/%{name}/locale/sv.po
%lang(sv) %{_datadir}/%{name}/locale/gui/sv.po
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

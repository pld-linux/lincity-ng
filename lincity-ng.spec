Summary:	Lincity - a Next Generation city/country simulation
Summary(pl.UTF-8):	Lincity - symulator miasta/kraju Następnej Generacji
%define		git_commit	b9062bec252632ca5d26b98d71453b8762c63173
%define		git_commit_date		20211121
Name:		lincity-ng
Version:	2.9.beta.%{git_commit_date}
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://github.com/lincity-ng/lincity-ng/archive/%{git_commit}/%{name}-%{version}.tar.gz
# Source0-md5:	9264a82a5ef770c249298b09445baf76
Patch0:		%{name}-desktop.patch
Patch1:		format-security.patch
URL:		http://lincity-ng.berlios.de/wiki/index.php/Main_Page
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel >= 2.0.0
BuildRequires:	SDL2_gfx-devel >= 1.0.0
BuildRequires:	SDL2_image-devel >= 2.0.0
BuildRequires:	SDL2_mixer-devel >= 2.0.0
BuildRequires:	SDL2_ttf-devel >= 2.0.12
BuildRequires:	gettext-tools
BuildRequires:	jam >= 2.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	physfs-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel >= 1.0
# needs jam from jam.spec
BuildConflicts:	boost-jam
Requires:	SDL2 >= 2.0.0
Requires:	SDL2_gfx >= 1.0.0
Requires:	SDL2_image >= 2.0.0
Requires:	SDL2_mixer >= 2.0.0
Requires:	SDL2_ttf >= 2.0.12
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
%setup -q -n %{name}-%{git_commit}
%patch0 -p1
%patch1 -p1
%{__sed} 's/ -O3 -g / /' -i Jamrules
%{__sed} -i 's/CREDITS\ //g' Jamfile

%build
sh autogen.sh
%configure
jam

%install
rm -rf $RPM_BUILD_ROOT

jam -s DESTDIR=$RPM_BUILD_ROOT install

#%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
# temporaty solution until the full version is released
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-2.9.beta

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING-* README TODO RELNOTES
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
%lang(ca) %{_datadir}/%{name}/help/ca
%lang(cs) %{_datadir}/%{name}/help/cs
%lang(de) %{_datadir}/%{name}/help/de
%lang(el) %{_datadir}/%{name}/help/el
%lang(en) %{_datadir}/%{name}/help/en
%lang(es) %{_datadir}/%{name}/help/es
%lang(fr) %{_datadir}/%{name}/help/fr
%lang(gd) %{_datadir}/%{name}/help/gd
%lang(gl) %{_datadir}/%{name}/help/gl
%lang(nl) %{_datadir}/%{name}/help/nl
%lang(pt_BR) %{_datadir}/%{name}/help/pt_BR
%lang(ru) %{_datadir}/%{name}/help/ru
%lang(sv) %{_datadir}/%{name}/help/sv
%lang(tr) %{_datadir}/%{name}/help/tr
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/locale/gui
%lang(ca) %{_datadir}/%{name}/locale/ca.po
%lang(ca) %{_datadir}/%{name}/locale/gui/ca.po
%lang(cs) %{_datadir}/%{name}/locale/cs.po
%lang(cs) %{_datadir}/%{name}/locale/gui/cs.po
%lang(da) %{_datadir}/%{name}/locale/da.po
%lang(de) %{_datadir}/%{name}/locale/de.po
%lang(de) %{_datadir}/%{name}/locale/gui/de.po
%lang(el) %{_datadir}/%{name}/locale/el.po
%lang(el) %{_datadir}/%{name}/locale/gui/el.po
%lang(gd) %{_datadir}/%{name}/locale/gd.po
%lang(gd) %{_datadir}/%{name}/locale/gui/gd.po
%lang(es) %{_datadir}/%{name}/locale/es.po
%lang(es) %{_datadir}/%{name}/locale/gui/es.po
%lang(fr) %{_datadir}/%{name}/locale/fr.po
%lang(fr) %{_datadir}/%{name}/locale/gui/fr.po
%lang(gl) %{_datadir}/%{name}/locale/gl.po
%lang(gl) %{_datadir}/%{name}/locale/gui/gl.po
%lang(ja) %{_datadir}/%{name}/locale/ja.po
%lang(ja) %{_datadir}/%{name}/locale/gui/ja.po
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
%lang(tr) %{_datadir}/%{name}/locale/tr.po
%lang(tr) %{_datadir}/%{name}/locale/gui/tr.po
%lang(zh_CN) %{_datadir}/%{name}/locale/zh_CN.po
%lang(zh_CN) %{_datadir}/%{name}/locale/gui/zh_CN.po
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

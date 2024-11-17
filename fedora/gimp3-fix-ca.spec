#
# spec file for package gimp3-fix-ca plugin
#
%define		moname gimp30-fix-ca
%define		plugindir %{_libdir}/gimp/3.0/plug-ins/fix-ca

Name:		gimp3-fix-ca
Version:	0.1
Release:	0
Summary:	A Gimp3 plugin for correcting Chromatic Aberration (CA)
License:	GPLv3+
Group:		Productivity/Graphics/Bitmap Editors
URL:		https://github.com/JoesCat/gimp3-fix-ca
Source0:	https://github.com/JoesCat/gimp3-fix-ca/archive/%{version}/%{name}-%{version}.tar.gz


# Required for building gimp3 plug-in
BuildRequires:	autoconf automake gcc make libtool
# Require gettext, setlocale
Requires:	gettext >= 0.21.1
BuildRequires:	gettext-devel >= 0.21.0
# Require gtk+3.0
Requires:	gtk3 >= 3.24.38
BuildRequires:	gtk3-devel >= 3.24.38
# Require babl newer than 2023 feb 25
Requires:	babl >= 0.1.110
BuildRequires:	babl-devel >= 0.1.110
# Require gegl >= 0.4.50
Requires:	gegl04 >= 0.4.50
BuildRequires:	gegl04-devel >= 0.4.50
# Require gimp-3.0-RC1, >= 2024 nov 04
Requires:	gimp3 >= 2.99.19
Requires:	gimp3-libs >= 2.99.19
BuildRequires:	gimp3-devel >= 2.99.19


%description
A GIMP3 plug-in to correct Chromatic Aberration (CA).
GIMP3-Fix-CA can fix Lateral CA caused due to light traveling through lenses,
and fix Directional CA due to light traveling through dense material
such as glass or water.


%prep
%setup -q


%build
autoreconf --force --install --verbose
%configure
%make_build


#%check
#make check


%install
%make_install INSTALLDIR="%{buildroot}/%{plugindir}" \
      LOCALEDIR="%{buildroot}/%{_datadir}/locale"
%find_lang %{moname}


%files -f %{moname}.lang
%license COPYING
%{plugindir}/fix-ca
%{_datadir}/metainfo/org.gimp.extension.fix3-ca.metainfo.xml


%changelog
* Fri Nov 15 2024 Jose Da Silva <digital@joescat.com> 
- Initial version 0.1 Gimp3-Fix-Ca for GIMP-3.0-RC1 


%global __cmake_in_source_build 1

Name:           freelib
Version:        6.1.0
Release:        1%{?dist}
Summary:        Manage catalogs for LibRusEc and Flibusta libraries
License:        GPLv3+
URL:            https://github.com/petrovvlad/freeLib
%dnl Source0:        https://github.com/petrovvlad/freeLib/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qthttpserver
BuildRequires:  qt6-qtwebsockets
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  quazip-qt6-devel
BuildRequires:  tbb-devel
BuildRequires:  qtkeychain-qt6-devel

%description
freeLib is a catalogs' manager for LibRusEc and Flibusta libraries.
It is a fork of the publicly available freeLib 5.0 , the development of which
has been discontinued.


  * Creation of own libraries based on FB2(.ZIP), EPUB, FBD files.
  * Conversion to AZW3 (KF8), MOBI, MOBI7 (KF7), EPUB formats.
  * Working with several libraries.
  * Import libraries from inpx-files.
  *  Book search and filtering.
  * OPDS and Web servers (QHttpServer required).
  * Saving books to a selected folder.
  * Different export settings for multiple devices.
  * Sending selected book files to email.
  * Setting tags for book, author, series and filtering by tags.
  * Customize book formatting (fonts, lettering, headings, hyphenation, footnotes)
  * Reading books with external applications. You can assign a separate program
    for each format.
    
%define gitdir   %{name}-%{version}

%prep
rm -rf %{gitdir}
git clone --recurse-submodules %{url}.git %{gitdir}
cd %{gitdir}
git checkout v%{version}

%build
cd %{gitdir}
mkdir build
pushd build
%{cmake} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%{cmake} --build . %{?_smp_mflags}
popd


%install
pushd build
%make_install
popd

%files
%doc %{gitdir}/README.md
%license %{gitdir}/LICENSE
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
%autochangelog

Name:		disksearch
Summary:	Catalog and search tool for removable media
Version:	1.2.1
Release:	%mkrel 5
Source:		http://prdownloads.sourceforge.net/disksearch/%{name}-%{version}.tar.bz2
URL:		http://disksearch.sourceforge.net/
License:	GPL
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	imagemagick
Requires:	pygtk2.0-libglade
BuildArch:	noarch

%description
DiskSearch is a tool for searching for files on all your removable media disks
(e.g. CD's, ZIP disks or backup tapes). For instance you can search for songs
on your MP3-CD's or for a document on your backup DVD's. For advanced queries
there is a regular expression search mode.  The search is based on a simple
database file which needs to be filled once by adding all your disks to it.

%prep
%setup -q
perl -p -i -e 's|/usr/local|/usr||g' %name

%build
# for remove rpmlint's warning...

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %name

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=DiskSearch
Comment=Search removable media
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=System;Filesystem;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 resource/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 resource/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 resource/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

mkdir -p %{buildroot}%{_iconsdir}/hicolor/16x16/apps/
convert -geometry 16x16 resource/%name.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/32x32/apps/
convert -geometry 32x32 resource/%name.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}/hicolor/48x48/apps/
convert -geometry 48x48 resource/%name.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc docs/*
%{_bindir}/%name
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/applications/mandriva-%name.desktop


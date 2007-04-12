%define name	disksearch
%define version	1.1.1

Name: 	 	%{name}
Summary: 	Catalog and search tool for removable media
Version: 	%{version}
Release: 	%mkrel 1

Source:		http://prdownloads.sourceforge.net/disksearch/%{name}-%{version}.tar.bz2
URL:		http://disksearch.sourceforge.net/
License:	GPL
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
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

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="DiskSearch" longtitle="Search removable media" section="System/File Tools" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DiskSearch
Comment=Search removable media
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=System;Filesystem;X-MandrivaLinux-System-FileTools;
EOF


#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 resource/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 resource/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 resource/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc docs/*
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/mandriva-%name.desktop


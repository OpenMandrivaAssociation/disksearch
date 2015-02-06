Name:		disksearch
Summary:	Catalog and search tool for removable media
Version:	1.2.1
Release:	7
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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-6mdv2011.0
+ Revision: 610245
- rebuild

* Wed Apr 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.2.1-5mdv2010.1
+ Revision: 534694
- don't define name, version on top of spec.
- fix mixed-use-of-spaces-and-tabs
- remove %%post && %%postun
- add a %%build section (that is empty) to fix rpmlint warning

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-4mdv2010.0
+ Revision: 428279
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-3mdv2009.0
+ Revision: 244340
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 27 2007 Austin Acton <austin@mandriva.org> 1.2.1-1mdv2008.1
+ Revision: 138669
- sync
- new version
- drop buildroot def'n

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat Jul 21 2007 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2008.0
+ Revision: 54188
- New version

* Wed Jun 13 2007 Austin Acton <austin@mandriva.org> 1.1.3-1mdv2008.0
+ Revision: 38557
- new version


* Mon Sep 04 2006 Jerome Soyer <saispo@mandriva.org> 1.1.1-1mdv2007.0
- New release 1.1.1
- XDG Menu

* Wed Aug 24 2005 Austin Acton <austin@mandriva.org> 1.1.0-1mdk
- 1.1.0
- source URL
- translation files

* Sat Nov 06 2004 Austin Acton <austin@mandrake.org> 0.9.1-1mdk
- initial package


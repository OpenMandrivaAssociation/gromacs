Summary: Molecular dynamics package (non-mpi version)
Name:    gromacs
Version: 4.6.3
Release: 1
License: GPL
Group: Sciences/Chemistry
Requires: fftw >= 3.0.1
Source0: ftp://ftp.gromacs.org/pub/gromacs/%{name}-%{version}.tar.gz
Source1: gromacs.rpmlintrc
Buildrequires: cmake
Buildrequires: fftw-devel
BuildRequires: libxml2-devel
URL: http://www.gromacs.org

%description
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics. This
version has the dynamic libs and executables; to hack new
utility programs you also need the headers and static
libs in gromacs-dev. Linux kernel 2.4 or later is STRONGLY
recommended on Pentium III and later processors since
GROMACS then can use assembly loops with SSE instructions.
You can also perform parallel simulations if you install
gromacs-lammpi.

%package devel
Summary: Header files and static libraries for GROMACS
Group: Development/C++
Requires: %{name} = %{version}
Conflicts: %{name} < %{version}

%description devel
This package contains header files, static libraries,
and a program example for the GROMACS molecular
dynamics software. You need it if you want to write your
own analysis programs.

%prep
%setup -q
perl -pi -e "s|CMAKE_INSTALL_PREFIX}/lib|CMAKE_INSTALL_PREFIX}/%{_lib}|" CMakeLists.txt
perl -pi -e "s|set\(GMXLIB lib|set\(GMXLIB %{_lib}|" CMakeLists.txt
find . -type f -exec chmod a+r {} \;

%build
%cmake
# OK, this is ugly, but working ...
perl -pi -e "s/-lm/-lm -pthread/" src/gmxlib/CMakeFiles/gmx.dir/link.txt
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Sep 27 2011 Stéphane Téletchéa <steletch@mandriva.org> 4.5.5-1mdv2012.0
+ Revision: 701578
- Modify only the lib parameter for libdir in CMakeLists.txt
- Fix library dir
- Added a workaround for the missing pthread flag
- Update to 4.5.5

* Tue Mar 22 2011 Stéphane Téletchéa <steletch@mandriva.org> 4.5.4-1
+ Revision: 647499
- Update to 4.5.4

* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 4.5.3-2
+ Revision: 635894
- tighten BR
- install into correct libdir

* Tue Nov 16 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.5.3-1mdv2011.0
+ Revision: 598092
- New version 4.5.3

* Thu Nov 11 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.5.2-1mdv2011.0
+ Revision: 596299
- Workaround cmake build
- Fix installation path
- Fix man and library names
- Add missing buildroot
- Launch the installation from the cmake build subdir
- Missing BR
- Update to cmake system
- Update to 4.5.2
- Update to gromacs 4.5.1

* Mon Mar 15 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.0.7-2mdv2011.0
+ Revision: 519886
- Fix libdir inclusion to avoid owning the directory which prevents removing the debug files

* Mon Dec 14 2009 Stéphane Téletchéa <steletch@mandriva.org> 4.0.7-1mdv2010.1
+ Revision: 478487
- Update to 4.0.7

* Mon Sep 28 2009 Stéphane Téletchéa <steletch@mandriva.org> 4.0.5-1mdv2010.0
+ Revision: 450710
- gromacs uses a libmd now
- Disco is no more present
- Update to 4.0.5
- Disable for now the underlinking check
- Add missing BR (and increase fftw requirement)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.3.2-3mdv2009.0
+ Revision: 246640
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 23 2007 Jérôme Soyer <saispo@mandriva.org> 3.3.2-1mdv2008.1
+ Revision: 101472
- New release
- import gromacs


* Tue Apr 11 2006 Lenny Cartier <lenny@mandriva.com> 3.3.1-1mdk
- 3.3.1

* Mon Nov 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.3-2mdk
- Fix BuildRequires

* Thu Oct 20 2005 Lenny Cartier <lenny@mandriva.com> 3.3-1mdk
- 3.3

* Fri Jun 04 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Apr 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.1.4-3mdk
- buildrequires

* Sun Feb 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.1.4-2mdk
- rebuild

* Tue Dec 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 3.1.4-1mdk 
- from Austin Acton <aacton@yorkul.ca> :
	- initial package for Mandrake 9.0+



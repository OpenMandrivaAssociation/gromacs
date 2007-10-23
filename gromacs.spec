%define name gromacs
%define version 3.3.1
%define release %mkrel 1

Summary: Molecular dynamics package (non-mpi version)
Name: %name
Version: %version
Release: %release
License: GPL
Group: Sciences/Chemistry
Buildroot: %_tmppath/%name-root
Requires: fftw >= 2.1.3 
Source: ftp://ftp.gromacs.org/pub/gromacs/%name-%version.tar.bz2
Buildrequires: libfftw-devel
Buildrequires: X11-devel
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

%description devel
This package contains header files, static libraries,
and a program example for the GROMACS molecular
dynamics software. You need it if you want to write your
own analysis programs. 

%prep
%setup -q

%build
%configure --disable-rpath
%make 

%install
%makeinstall

mv $RPM_BUILD_ROOT/%_mandir/man1/disco.1 $RPM_BUILD_ROOT/%_mandir/man1/g_disco.1

#mkdir -p $RPM_BUILD_ROOT/%_datadir/%name-%version
#mv $RPM_BUILD_ROOT/%_datadir/html $RPM_BUILD_ROOT/%_datadir/%name-%version/
#mv $RPM_BUILD_ROOT/%_datadir/top $RPM_BUILD_ROOT/%_datadir/%name-%version/
#mv $RPM_BUILD_ROOT/%_datadir/template $RPM_BUILD_ROOT/%_datadir/%name-%version/
#mv $RPM_BUILD_ROOT/%_datadir/tutor $RPM_BUILD_ROOT/%_datadir/%name-%version/

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%_bindir/*
%_mandir/man1/*
%_datadir/%name

%files devel
%defattr(-,root,root)
%_includedir/*
%_libdir/*.a
%_libdir/*.la


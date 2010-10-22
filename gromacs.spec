%define name gromacs
%define version 4.5.1
%define release %mkrel 1

Summary: Molecular dynamics package (non-mpi version)
Name: %name
Version: %version
Release: %release
License: GPL
Group: Sciences/Chemistry
Buildroot: %_tmppath/%name-root
Requires: fftw >= 3.0.1
Source: ftp://ftp.gromacs.org/pub/gromacs/%name-%version.tar.gz
Buildrequires: fftw-devel
Buildrequires: gsl-devel
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
%configure2_5x --with-gnu-ld --with-x --with-gsl --enable-shared --without-motif-libraries
%make

%install
%makeinstall

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%_bindir/
%_mandir/man1/*
%_datadir/%name
%_libdir/

%files devel
%defattr(-,root,root)
%_includedir/*
%_libdir/*.a
%_libdir/*.la


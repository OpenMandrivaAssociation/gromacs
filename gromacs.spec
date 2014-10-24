Summary: Molecular dynamics package (non-mpi version)
Name:    gromacs
Version: 4.6.6
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

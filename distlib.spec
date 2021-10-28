#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9147B477339A9B86 (vinay_sajip@yahoo.co.uk)
#
Name     : distlib
Version  : 0.3.3
Release  : 25
URL      : https://files.pythonhosted.org/packages/56/ed/9c876a62efda9901863e2cc8825a13a7fcbda75b4b498103a4286ab1653b/distlib-0.3.3.zip
Source0  : https://files.pythonhosted.org/packages/56/ed/9c876a62efda9901863e2cc8825a13a7fcbda75b4b498103a4286ab1653b/distlib-0.3.3.zip
Source1  : https://files.pythonhosted.org/packages/56/ed/9c876a62efda9901863e2cc8825a13a7fcbda75b4b498103a4286ab1653b/distlib-0.3.3.zip.asc
Summary  : Distribution utilities
Group    : Development/Tools
License  : HPND Python-2.0
Requires: distlib-license = %{version}-%{release}
Requires: distlib-python = %{version}-%{release}
Requires: distlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/appveyor/build/vsajip/distlib
:alt: AppVeyor
.. image:: https://coveralls.io/repos/github/vsajip/distlib/badge.svg?branch=master
:target: https://coveralls.io/github/vsajip/distlib?branch=master

%package license
Summary: license components for the distlib package.
Group: Default

%description license
license components for the distlib package.


%package python
Summary: python components for the distlib package.
Group: Default
Requires: distlib-python3 = %{version}-%{release}

%description python
python components for the distlib package.


%package python3
Summary: python3 components for the distlib package.
Group: Default
Requires: python3-core
Provides: pypi(distlib)

%description python3
python3 components for the distlib package.


%prep
%setup -q -n distlib-0.3.3
cd %{_builddir}/distlib-0.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632321076
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/distlib
cp %{_builddir}/distlib-0.3.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/distlib/79c85e153df486fd6c05a2f7359e1ff6dc288867
cp %{_builddir}/distlib-0.3.3/tests/test_testdist-0.1/LICENSE %{buildroot}/usr/share/package-licenses/distlib/71ff42eed070086a7e794fdab6a1c16495923820
cp %{_builddir}/distlib-0.3.3/tests/testdist-0.1/LICENSE %{buildroot}/usr/share/package-licenses/distlib/71ff42eed070086a7e794fdab6a1c16495923820
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/distlib/71ff42eed070086a7e794fdab6a1c16495923820
/usr/share/package-licenses/distlib/79c85e153df486fd6c05a2f7359e1ff6dc288867

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

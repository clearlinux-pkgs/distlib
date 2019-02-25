#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : distlib
Version  : 0.2.8
Release  : 1
URL      : https://bitbucket.org/pypa/distlib/downloads/distlib-0.2.8.zip
Source0  : https://bitbucket.org/pypa/distlib/downloads/distlib-0.2.8.zip
Summary  : Distribution utilities
Group    : Development/Tools
License  : Python-2.0 ZPL-2.0
Requires: distlib-license = %{version}-%{release}
Requires: distlib-python = %{version}-%{release}
Requires: distlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
This is a simple launcher for Python files, which is functionally equivalent to
the launchers in setuptools but not based on setuptools code. There are two
versions of the launcher - console and GUI - built from the same source code.

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

%description python3
python3 components for the distlib package.


%prep
%setup -q -n distlib-0.2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551107148
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/distlib
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/distlib/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/distlib/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

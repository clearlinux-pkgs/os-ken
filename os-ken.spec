#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-ken
Version  : 0.4.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/13/32/4587df3a8765ef3e479d67d2a0da98d7a15384e24c008bd830369d444a0e/os-ken-0.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/32/4587df3a8765ef3e479d67d2a0da98d7a15384e24c008bd830369d444a0e/os-ken-0.4.1.tar.gz
Summary  : A component-based software defined networking framework for OpenStack.
Group    : Development/Tools
License  : Apache-2.0
Requires: os-ken-bin = %{version}-%{release}
Requires: os-ken-license = %{version}-%{release}
Requires: os-ken-python = %{version}-%{release}
Requires: os-ken-python3 = %{version}-%{release}
Requires: Routes
Requires: eventlet
Requires: msgpack
Requires: netaddr
Requires: oslo.config
Requires: ovs
Requires: pbr
Requires: six
Requires: tinyrpc
BuildRequires : Routes
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : msgpack
BuildRequires : netaddr
BuildRequires : oslo.config
BuildRequires : ovs
BuildRequires : pbr
BuildRequires : six
BuildRequires : tinyrpc

%description
======
os-ken
======
A component-based software defined networking framework in OpenStack.

%package bin
Summary: bin components for the os-ken package.
Group: Binaries
Requires: os-ken-license = %{version}-%{release}

%description bin
bin components for the os-ken package.


%package license
Summary: license components for the os-ken package.
Group: Default

%description license
license components for the os-ken package.


%package python
Summary: python components for the os-ken package.
Group: Default
Requires: os-ken-python3 = %{version}-%{release}

%description python
python components for the os-ken package.


%package python3
Summary: python3 components for the os-ken package.
Group: Default
Requires: python3-core

%description python3
python3 components for the os-ken package.


%prep
%setup -q -n os-ken-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567743971
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-ken
cp LICENSE %{buildroot}/usr/share/package-licenses/os-ken/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/osken
/usr/bin/osken-manager

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-ken/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

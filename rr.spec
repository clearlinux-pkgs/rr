#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rr
Version  : 5.1.0
Release  : 4
URL      : https://github.com/mozilla/rr/archive/5.1.0.tar.gz
Source0  : https://github.com/mozilla/rr/archive/5.1.0.tar.gz
Summary  : Lightweight tool for recording and replaying execution of applications (trees of processes and threads)
Group    : Development/Tools
License  : BSD-2-Clause
Requires: rr-bin
Requires: rr-lib
Requires: rr-data
BuildRequires : capnproto-dev
BuildRequires : cmake
BuildRequires : gdb-bin
BuildRequires : pexpect-legacypython
BuildRequires : python

%description
rr is a lightweight tool for recording and replaying execution of applications (trees of processes and threads).  For more information, please visit

http://rr-project.org

%package bin
Summary: bin components for the rr package.
Group: Binaries
Requires: rr-data

%description bin
bin components for the rr package.


%package data
Summary: data components for the rr package.
Group: Data

%description data
data components for the rr package.


%package lib
Summary: lib components for the rr package.
Group: Libraries
Requires: rr-data

%description lib
lib components for the rr package.


%prep
%setup -q -n rr-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523298817
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -Ddisable32bit=ON -DWILL_RUN_TESTS=OFF -DRR_BUILD_SHARED=ON -DBUILD_TESTS=OFF
make
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build ; make test ; popd

%install
export SOURCE_DATE_EPOCH=1523298817
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rr
/usr/bin/rr_exec_stub
/usr/bin/rr_page_32
/usr/bin/rr_page_32_replay
/usr/bin/rr_page_64
/usr/bin/rr_page_64_replay
/usr/bin/signal-rr-recording.sh

%files data
%defattr(-,root,root,-)
/usr/share/rr/32bit-avx.xml
/usr/share/rr/32bit-core.xml
/usr/share/rr/32bit-linux.xml
/usr/share/rr/32bit-sse.xml
/usr/share/rr/64bit-avx.xml
/usr/share/rr/64bit-core.xml
/usr/share/rr/64bit-linux.xml
/usr/share/rr/64bit-seg.xml
/usr/share/rr/64bit-sse.xml
/usr/share/rr/amd64-avx-linux.xml
/usr/share/rr/amd64-linux.xml
/usr/share/rr/i386-avx-linux.xml
/usr/share/rr/i386-linux.xml

%files lib
%defattr(-,root,root,-)
/usr/lib/librr.so
/usr/lib/rr/librrpreload.so

Summary: Multitech IntelligentSerialInternal (ISI) Support Tools
Name: isicom
Version: 1.0
Release: 1
Copyright: GPL (not Firmware)
Group: Applications/System
URL: http://www.multitech.com/
Source: isicom.tar.gz
Patch0: isicom-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binary images and loader for Multitech IntelligentSerialInternal (ISI) data
files.

%prep
%setup -n isicom
%patch0 -p1

%build
make clean
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{share/isicom,sbin}
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 firmld $RPM_BUILD_ROOT/usr/sbin
#install -m 755 isild $RPM_BUILD_ROOT/etc/rc.d/init.d/
install -m 644 *.bin $RPM_BUILD_ROOT/usr/share/isicom

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (644, root, root)
%attr (755,root,root) /usr/sbin/firmld
/usr/share/isicom/*.bin

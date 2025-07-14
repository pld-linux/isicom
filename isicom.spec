Summary:	Multitech IntelligentSerialInternal (ISI) Support Tools
Summary(pl.UTF-8):	Narzędzia do obsługi Multitech IntelligentSerialInternal (ISI)
Name:		isicom
Version:	1.0
Release:	2
License:	GPL (not Firmware)
Group:		Applications/System
Source0:	%{name}.tar.gz
# Source0-md5:	44e685867c7115db0a4865c159ea4ab9
Patch0:		%{name}-make.patch
URL:		http://www.multitech.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binary images and loader for Multitech IntelligentSerialInternal (ISI)
data files.

%description -l pl.UTF-8
Binarne obrazy i loader dla plików danych Multitech
IntelligentSerialInternal (ISI).

%prep
%setup -q -n isicom
%patch -P0 -p1

%build
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/isicom,%{_sbindir}} \
	$RPM_BUILD_ROOT/etc/rc.d/init.d

install firmld $RPM_BUILD_ROOT%{_sbindir}
#install isild $RPM_BUILD_ROOT/etc/rc.d/init.d/
install *.bin $RPM_BUILD_ROOT%{_datadir}/isicom

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_sbindir}/firmld
%dir %{_datadir}/isicom
%{_datadir}/isicom/*.bin

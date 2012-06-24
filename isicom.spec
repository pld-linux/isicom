Summary:	Multitech IntelligentSerialInternal (ISI) Support Tools
Summary(pl):	Narz�dzia do obs�ugi Multitech IntelligentSerialInternal (ISI)
Name:		isicom
Version:	1.0
Release:	2
License:	GPL (not Firmware)
Group:		Applications/System
Source0:	%{name}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.multitech.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binary images and loader for Multitech IntelligentSerialInternal (ISI)
data files.

%description -l pl
Binarne obrazy i loader dla plik�w danych Multitech
IntelligentSerialInternal (ISI).

%prep
%setup -q -n isicom
%patch0 -p1

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

%define name rt61-firmware
%define rtname RT61_Firmware
%define version 1.2
%define release %mkrel 1

Summary: Firmware for the RT61 chip
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ralinktech.com/ralink/data/%{rtname}_V%{version}.tar.bz2
License: Proprietary
Group: System/Kernel and hardware
Url: http://rt2x00.serialmonkey.com/
BuildArch: noarch

%description
This package contains the firmware files for the RT61 chip, which is
used in WLAN PCMCIA cards.

%prep
%setup -q -n %{rtname}_V%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 rt*.bin %{buildroot}/lib/firmware

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/lib/firmware/rt*.bin



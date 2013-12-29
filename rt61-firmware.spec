%define	rtname	RT61_Firmware

Summary:	Firmware for the RT61 chip
Name:		rt61-firmware
Version:	1.2
Release:	6
Source0:	http://www.ralinktech.com/ralink/data/%{rtname}_V%{version}.tar.bz2
License:	Proprietary
Group:		System/Kernel and hardware
Url:		http://rt2x00.serialmonkey.com/
BuildArch:	noarch

%description
This package contains the firmware files for the RT61 chip, which is
used in WLAN PCMCIA cards.

%prep
%setup -q -n %{rtname}_V%{version}

%build

%install
install -d %{buildroot}/lib/firmware
install -m644 rt*.bin %{buildroot}/lib/firmware

%files
/lib/firmware/rt*.bin

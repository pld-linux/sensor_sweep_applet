Summary:	A GNOME panel applet that allows to monitor a system through the lm_sensors
Name:		sensor_sweep_applet
Version:	0.20.0
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.coverfire.com/sensor_sweep_applet/%{name}-%{version}.tar.gz
URL:		http://www.coverfire.com/sensor_sweep_applet/
BuildRequires:	lm_sensors-devel
Requires:	gnome-core >= 1.2.3
Requires:	lm_sensors
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
Sensor Sweep Applet is a GNOME panel applet that allows you to monitor
your systems health through the lm_sensors kernel modules. Sensor
Sweep is extremely configurable allowing you to specify exactly which
sensors you wish to monitor.

%prep
%setup  -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog NEWS TODO AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz ChangeLog.gz NEWS.gz AUTHORS.gz TODO.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/CORBA/servers/%{name}.gnorba
%{_datadir}/applets/Monitors/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

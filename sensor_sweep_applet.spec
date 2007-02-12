Summary:	A GNOME panel applet that allows to monitor a system through the lm_sensors
Summary(pl.UTF-8):   Aplet panelu GNOME monitorujący system przez lm_sensors
Name:		sensor_sweep_applet
Version:	0.20.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.coverfire.com/sensor_sweep_applet/%{name}-%{version}.tar.gz
# Source0-md5:	70f1f2396e588118d480dee46b7997dd
Patch0:		%{name}-ac.patch
URL:		http://www.coverfire.com/sensor_sweep_applet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel
Requires:	gnome-core >= 1.2.3
Requires:	lm_sensors
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sensor Sweep Applet is a GNOME panel applet that allows you to monitor
your systems health through the lm_sensors kernel modules. Sensor
Sweep is extremely configurable allowing you to specify exactly which
sensors you wish to monitor.

%description -l pl.UTF-8
Sensor Sweep Applet to aplet panelu GNOME pozwalający monitorować
działanie systemu poprzez moduły jądra lm_sensors. Sensor Sweep jest
bardzo konfigurowalny, pozwalając podać które dokładnie sensory
monitorować.

%prep
%setup  -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/CORBA/servers/%{name}.gnorba
%{_datadir}/applets/Monitors/%{name}.desktop
%{_pixmapsdir}/%{name}.png

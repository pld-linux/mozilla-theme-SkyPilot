Summary:	Unnofficial port of the best NN6.1 theme
Summary(pl):	Nieoficjalny port najlepszego tematu dla NN6.1
Name:		mozilla-theme-SkyPilot
Version:	1.5
%define	fver	%(echo %{version} | tr -d .)
%define		_realname	skypilotmu%{fver}
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/%{_realname}.jar
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/skypilot.html
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
SkyPilot - the winner of the best NN6.1 theme competition. Author's
motto was "because every Navigator needs Pilot".

%description -l pl
Zwyciêzca w konkursie Netscape na najlepszy temat dla NN6.1.
Motto jakie przy¶wieca³o autorowi tego tematu to: "Poniewa¿ ka¿dy
Nawigator potrzebuje pilota".

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post 
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt

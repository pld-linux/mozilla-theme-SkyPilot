Summary:	Unnofficial port of the best NN6.1 theme
Summary(pl):	Nieoficjalny port najlepszego tematu dla NN6.1
Name:		mozilla-theme-SkyPilot
Version:	1.2
%define	fver	%(echo %{version} | tr -d .)
%define		_realname	skypilotmu%{fver}
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/%{_realname}.jar
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www0.mozdev.org/themes/skins/skypilot.html
Requires:	mozilla >= 1.0
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)
Buildrequires:	unzip
Buildrequires:	zip

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

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}/tmp
rm -rf $RPM_BUILD_ROOT%{_chromedir}/tmp/*/contents.rdf
cd $RPM_BUILD_ROOT%{_chromedir}/tmp
zip -9 -r $RPM_BUILD_ROOT%{_chromedir}/skypilotmu12.jar ./*
rm -rf $RPM_BUILD_ROOT%{_chromedir}/tmp
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt | grep -v "%{_realname}.jar" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt

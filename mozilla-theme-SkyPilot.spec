Summary:        Unnofficial port of the best NN6.1 theme
Summary(pl):    Nieoficjalny port najlepszego tematu dla NN6.1
Name:           mozilla-theme-SkyPilot
Version:        1.2
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://downloads.mozdev.org/themes/skypilotmu12.jar
Source1:        skypilotmu12-installed-chrome.txt
URL:            http://www0.mozdev.org/themes/skins/gold.html
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	skypilotmu12

%description
%description -l pl
Zwyciêzca w konkursie Netscape na najlepszy temat dla NN6.1.
Motto jakie przy¶wieca³o autorowi tego tematu to: "Poniewa¿ ka¿dy
Nawigator potrzebuje pilota".

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "%{_realname}.jar" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt

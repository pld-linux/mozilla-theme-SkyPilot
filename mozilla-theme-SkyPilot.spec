Summary:	Unnofficial port of the best NN6.1 theme
Summary(pl):	Nieoficjalny port najlepszego motywu dla NN6.1
Name:		mozilla-theme-SkyPilot
%define		_realname	skypilotm15u
Version:	1.9jrc
%define	fver	%(echo %{version} | tr -d .)
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/%{_realname}%{fver}.jar
# Source0-md5:	7c9e5c33a165072dbe428fad40370881
# Source0-size:	1248586
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/skypilot.html
Requires(post,postun):	textutils
Requires:	mozilla >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
SkyPilot - the winner of the best NN6.1 theme competition. Author's
motto was "because every Navigator needs Pilot".

%description -l pl
Zwyciêzca w konkursie Netscape na najlepszy motyw dla NN6.1.
Motto jakie przy¶wieca³o autorowi tego motywu to: "Poniewa¿ ka¿dy
Nawigator potrzebuje pilota".

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
                                                                                                                 
install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt

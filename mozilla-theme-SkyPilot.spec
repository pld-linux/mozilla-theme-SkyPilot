Summary:	Unnofficial port of the best NN6.1 theme
Summary(pl):	Nieoficjalny port najlepszego motywu dla NN6.1
Name:		mozilla-theme-SkyPilot
Version:	1.9i
%define	fver	%(echo %{version} | tr -d .)
%define		_realname	skypilotm12u
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.uk1.mozdev.org/rsync/themes/themes/%{_realname}%{fver}.xpi
# Source0-md5:	c8a23a6aa0129b6d37d815124f3cb3af
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/skypilot.html
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

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
unzip %{SOURCE0} %{_realname}%{fver}.jar -d $RPM_BUILD_ROOT%{_chromedir}

mv -f $RPM_BUILD_ROOT%{_chromedir}/%{_realname}%{fver}.jar $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

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

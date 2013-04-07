Summary:	Ci programming language
Summary(en.UTF-8):	Ć programming language
Summary(pl.UTF-8):	Język programowania Ć
Name:		cito
Version:	0.3.0
Release:	1
License:	GPL v3+
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/cito/%{name}-%{version}.tar.gz
# Source0-md5:	794676f282dc8a2d0b9af220a92ad349
URL:		http://cito.sourceforge.net/
# .NET 3.5 - what is minimal mono version?
BuildRequires:	mono-csharp >= 3
Requires:	mono >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ci is a programming language which can be automatically translated to
C, Java, C#, JavaScript, ActionScript and D. The translator is called
`cito`.

%description -l en.UTF-8
Ć is a programming language which can be automatically translated to
C, Java, C#, JavaScript, ActionScript and D. The translator is called
`cito`.

%description -l pl.UTF-8
Ć to język programowania, który można automatycznie tłumaczyć do
języków C, Java, C#, JavaScript, ActionScript i D. Translator nazywa
się "cito".

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html ci.html ci-logo.ico ci-logo.svg hello.ci
%attr(755,root,root) %{_bindir}/cipad
%attr(755,root,root) %{_bindir}/cito
%dir %{_prefix}/lib/cito
%{_prefix}/lib/cito/cipad.exe
%{_prefix}/lib/cito/cito.exe

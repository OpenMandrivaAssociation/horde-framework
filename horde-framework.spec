%define prj     Horde_Framework

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-framework
Version:       0.0.2
Release:       %mkrel 5
Summary:       Horde core Framework libraries
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-dom
Requires:      horde-form
Requires:      horde-browser
Requires:      horde-cli
Requires:      php-pear-Services_Weather
Requires:      php-pear-Log
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
These classes provide the core functionality of the Horde Application Framework.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{_docdir}/horde

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%{peardir}/Horde.php
%dir %{peardir}/Horde
%{peardir}/Horde/Config.php
%{peardir}/Horde/Help.php
%{peardir}/Horde/Menu.php
%{peardir}/Horde/Registry.php
%{peardir}/Horde/Text.php
%dir %{_docdir}/horde

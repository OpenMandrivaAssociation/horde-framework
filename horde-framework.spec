%define prj     Horde_Framework

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-framework
Version:       0.0.2
Release:       9
Summary:       Horde core Framework libraries
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
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
These classes provide the core functionality of the Horde Application
Framework.


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


%changelog
* Tue Aug 03 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-7mdv2011.0
+ Revision: 565240
- Increased release for rebuild

* Mon Mar 01 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-6mdv2010.1
+ Revision: 512824
- bumped up release
- added Requires:      php-pear-Services_Weather

* Sun Feb 28 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-5mdv2010.1
+ Revision: 512791
- bumped up release to get it rebuilt

* Thu Feb 25 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-4mdv2010.1
+ Revision: 510875
- added Requires:      horde-dom horde-form horde-browser horde-cli

* Thu Feb 25 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2010.1
+ Revision: 510866
- added Requires:      horde-dom horde-form horde-browser horde-cli
  bumped up release

* Sun Feb 21 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 509321
- increade rel version
- removed requires for a temporary buiild

* Mon Feb 15 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 506027
- replaced PreReq with Requires (pre)
- import horde-framework



%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-zookeeper
Version:                0.6.1
Release:                2%{?dist}
Summary:                Module for managing Apache Zookeeper
License:                Apache-2.0

URL:                    https://github.com/deric/puppet-zookeeper

Source0:                https://github.com/deric/puppet-zookeeper/archive/v%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-archive

Requires:               puppet >= 2.7.0

%description
Module for managing Apache Zookeeper

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/zookeeper/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/zookeeper/



%files
%{_datadir}/openstack-puppet/modules/zookeeper/


%changelog
* Tue Dec 20 2016 Alejandro Andreu <alejandroandreu@openmailbox.org>
- Force puppet-zookeeper v0.6.1 as it's the one we use at puppet-midonet_openstack


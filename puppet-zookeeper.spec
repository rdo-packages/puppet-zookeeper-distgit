%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-zookeeper
%global commit 76fc0b0a53a3a83f3322ee81fc01661e375c4d4e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-zookeeper
Version:        1.2.0
Release:        1%{?alphatag}%{?dist}
Summary:        Module for managing Apache Zookeeper
License:        ASL 2.0

URL:            https://github.com/deric/puppet-zookeeper

Source0:        https://github.com/deric/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-datacat
Requires:       puppet >= 2.7.0

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
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/zookeeper/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/zookeeper/



%files
%{_datadir}/openstack-puppet/modules/zookeeper/


%changelog
* Tue Sep 28 2021 RDO <dev@lists.rdoproject.org> 1.2.0-1.76fc0b0git
- Update to post 1.2.0 (76fc0b0a53a3a83f3322ee81fc01661e375c4d4e)




%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-zookeeper
%global commit 5877cbf66372dba04d3a1b84016b83d4e06320bc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-zookeeper
Version:        0.9.0
Release:        0.1%{?alphatag}%{?dist}
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
* Thu Oct 17 2019 RDO <dev@lists.rdoproject.org> 0.9.0-0.1.5877cbfgit
- Update to pre 0.9.0 (5877cbf66372dba04d3a1b84016b83d4e06320bc)



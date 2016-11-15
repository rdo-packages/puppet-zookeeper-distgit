%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-zookeeper
%global commit 53bba0c685da3e43a4c644fbfb6aa1fffe6e5380
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-zookeeper
Version:        0.7.0
Release:        0.1%{?alphatag}%{?dist}
Summary:        Module for managing Apache Zookeeper
License:        Apache-2.0

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 0.7.0-0.1.53bba0c.git
- Newton update 0.7.0 (53bba0c685da3e43a4c644fbfb6aa1fffe6e5380)

* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 0.6.1-1.3bc30fc.git
- Newton update 0.6.1 (3bc30fc4c53d3f017175780b0605169e2ee2ed99)



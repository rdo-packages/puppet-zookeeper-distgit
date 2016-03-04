Name:           puppet-zookeeper
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        Module for managing Apache Zookeeper
License:        Apache-2.0

URL:            https://github.com/deric/puppet-zookeeper

Source0:        https://github.com/deric/puppet-zookeeper/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-datacat
Requires:       puppet >= 2.7.0

%description
Module for managing Apache Zookeeper

%prep
%setup -q -n %{name}-%{version}

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
cp -r %{buildroot}/%{_datadir}/openstack-puppet/modules/zookeeper/



%files
%{_datadir}/openstack-puppet/modules/zookeeper/


%changelog


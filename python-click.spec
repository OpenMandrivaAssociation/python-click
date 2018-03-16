# Created by pyp2rpm-1.0.1
%global pypi_name click
%global with_python3 1
%define _duplicate_files_terminate_build 0

Name:           python-%{pypi_name}
Version:        6.7
Release:        1
Summary:        A simple wrapper around optparse for powerful command line utilities

License:        BSD
URL:            http://github.com/mitsuhiko/click
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools
#BuildRequires:  python-pytest
 
%if %{?with_python3}
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:  python-pytest
%endif # if with_python3


%description
click is a Python package for creating beautiful command line
interfaces in a composable way with as little amount of code as necessary.
It's the "Command Line Interface Creation Kit".  It's highly configurable but
comes with good defaults out of the box.

%if 0%{?with_python3}
%package -n     python-%{pypi_name}
Summary:        A simple wrapper around optparse for powerful command line utilities


%description -n python-%{pypi_name}
click is a Python 3 package for creating beautiful command line
interfaces in a composable way with as little amount of code as necessary.
It's the "Command Line Interface Creation Kit".  It's highly configurable but
comes with good defaults out of the box.
%endif # with_python3


%prep
%setup -q -n %{pypi_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build

%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}

%check
# The following is a cheat as we don't carry python2-test
export LANG=en_GB.utf8.
export LC_ALL=en_GB.utf8.
PYTHONPATH=$(pwd) py.test-%{python3_version} tests --tb=long --verbose 

%%if 0%{?with_python3}
pushd %{py3dir}
export LANG=en_GB.utf8 
export LC_ALL=en_GB.utf8 
PYTHONPATH=$(pwd) py.test-%{python3_version} tests --tb=long --verbose 
popd
%%endif

%files
%doc README 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%%if 0%{?with_python3}
%files -n python-%{pypi_name}
%doc README
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3



# Credit  Robert Kuska <rkuska@redhat.com> 
# Initial package.

# Created by pyp2rpm-1.0.1
%global pypi_name click
%define tarname Click
%global with_python2 1
%define _duplicate_files_terminate_build 0

Name:           python-%{pypi_name}
Version:        7.1.2
Release:        1
Summary:        A simple wrapper around optparse for powerful command line utilities

License:        BSD
URL:            http://github.com/mitsuhiko/click
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:  python-pytest
 
%if %{with_python2}
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools
%endif # if with_python2


%description
Click is a Python package for creating beautiful command line
interfaces in a composable way with as little amount of code as necessary.
It's the "Command Line Interface Creation Kit".  It's highly configurable but
comes with good defaults out of the box.

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        A simple wrapper around optparse for powerful command line utilities


%description -n python2-%{pypi_name}
Click is a Python 2 package for creating beautiful command line
interfaces in a composable way with as little amount of code as necessary.
It's the "Command Line Interface Creation Kit".  It's highly configurable but
comes with good defaults out of the box.
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
%endif # with_python2

%build

%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}

%check
# The following is a cheat as we don't carry python2-test
export LANG=en_GB.utf8.
export LC_ALL=en_GB.utf8.
PYTHONPATH=$(pwd) py.test tests --tb=long --verbose 

%%if %{with_python2}
pushd %{py2dir}
export LANG=en_GB.utf8 
export LC_ALL=en_GB.utf8 
PYTHONPATH=$(pwd) py.test tests --tb=long --verbose 
popd
%%endif

%files
%doc README.rst CHANGES.rst CONTRIBUTING.rst LICENSE.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{tarname}-%{version}-py?.?.egg-info
%%if %{with_python2}
%files -n python2-%{pypi_name}
%doc README.rst CHANGES.rst CONTRIBUTING.rst LICENSE.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{tarname}-%{version}-py?.?.egg-info
%endif # with_python2



# Credit  Robert Kuska <rkuska@redhat.com> 
# Initial package.

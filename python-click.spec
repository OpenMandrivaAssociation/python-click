%global pypi_name click
%define tarname Click
%define _duplicate_files_terminate_build 0

Name:           python-%{pypi_name}
Version:        8.1.3
Release:        1
Summary:        A simple wrapper around optparse for powerful command line utilities

License:        BSD
URL:            http://github.com/mitsuhiko/click
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:  python-pytest
 
%description
Click is a Python package for creating beautiful command line
interfaces in a composable way with as little amount of code as necessary.
It's the "Command Line Interface Creation Kit".  It's highly configurable but
comes with good defaults out of the box.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}

#check
#export LANG=en_GB.utf8
#export LC_ALL=en_GB.utf8
#PYTHONPATH=$(pwd) py.test tests --tb=long --verbose 

%files
%doc README.rst CHANGES.rst LICENSE.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/click-%{version}-py*.egg-info*

%global pypi_name click
%define tarname Click
%define _duplicate_files_terminate_build 0

Name:           python-%{pypi_name}
Version:        8.3.1
Release:        1
Summary:        A simple wrapper around optparse for powerful command line utilities

License:        BSD
URL:            https://github.com/mitsuhiko/click
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:  python-pytest
BuildSystem:    python
 
%description
Click is a Python package for creating beautiful command line
interfaces in a composable way with as little amount of code as necessary.
It's the "Command Line Interface Creation Kit".  It's highly configurable but
comes with good defaults out of the box.

%files
%doc CHANGES.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}.dist-info

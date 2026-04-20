%define module click
%bcond tests 1

Name:		python-click
Version:	8.3.3
Release:	1
Summary:	A simple wrapper around optparse for powerful command line utilities
Group:		Development/Python
License:	BSD
URL:		https://github.com/pallets/click
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:    python
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(flit-core)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:  python%{pyver}dist(pytest)
%endif

%description
Click is a Python package for creating beautiful command line
interfaces in a composable way with as little amount of code as necessary.
It's the "Command Line Interface Creation Kit".  It's highly configurable but
comes with good defaults out of the box.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -rs --tb=short
%endif

%files
%doc CHANGES.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

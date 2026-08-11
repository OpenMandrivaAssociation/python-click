%define module click
%bcond tests 1

Name:		python-click
Version:	8.4.2
Release:	1
Summary:	A simple wrapper around optparse for powerful command line utilities
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://github.com/pallets/click
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz
# Backport of pallets/click#3656 (8.5.0): pytest >= 9.1 rejects
# non-Collection iterables in parametrize when filterwarnings=error.
Patch0:		click-pytest-9.1-parametrize.patch

BuildSystem:    python
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
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
skiptests+="not test_echo_via_pager"
pytest -rs --tb=short -k "$skiptests"
%endif

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

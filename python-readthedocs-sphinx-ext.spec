# Created by pyp2rpm-3.3.5
%global pypi_name readthedocs-sphinx-ext

Name:           python-%{pypi_name}
Version:        2.1.4
Release:        1
Summary:        Sphinx extension for Read the Docs overrides
Group:          Development/Python
License:        MIT
URL:            https://github.com/readthedocs/readthedocs-sphinx-ext
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(jinja2) >= 2.9
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)

%description
Read the Docs Sphinx Extensions This module adds extensions that make Sphinx
easier to use. Some of them require Read the Docs features, others are just
code that we ship and enable during builds on Read the Docs.We currently ship:*
An extension for building docs like Read the Docs

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/readthedocs_ext
%{python3_sitelib}/readthedocs_sphinx_ext-%{version}-py%{python3_version}.egg-info


#
# Conditional build:
%bcond_with	tests	# unit tests (some failing with py3.10)

Summary:	Python 3 based FIDO 2.0 library
Summary(pl.UTF-8):	Biblioteka FIDO 2.0 dla Pythona 3
Name:		python3-fido2
# 1.1.1+ use poetry as buildsystem
Version:	2.0.0
Release:	1
# Yubico code is BSD licensed; includes also:
# pyudf (Apache 2.0)
# public suffix list (MPL 2.0)
License:	BSD, Apache v2.0, MPL v2.0
Group:		Libraries/Python
#Source0Download: https://github.com/Yubico/python-fido2/releases
Source0:	https://github.com/Yubico/python-fido2/releases/download/%{version}/fido2-%{version}.tar.gz
# Source0-md5:	2f3a157e28808c7a34d6ddd88db0aa5d
URL:		https://developers.yubico.com/python-fido2/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-poetry-core >= 2.0.0
%if %{with tests}
BuildRequires:	python3-cryptography >= 2.6
BuildRequires:	python3-cryptography < 48
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides library functionality for communicating with a
FIDO device over USB as well as verifying attestation and assertion
signatures.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do komunikacji z urządzeniami
FIDO po USB, a także weryfikowania podpisów poświadczeń i zapewnień.

%prep
%setup -q -n fido2-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-fido2-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-fido2-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.adoc
%{py3_sitescriptdir}/fido2
%{py3_sitescriptdir}/fido2-%{version}.dist-info
%{_examplesdir}/python3-fido2-%{version}

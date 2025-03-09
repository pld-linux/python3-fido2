#
# Conditional build:
%bcond_with	tests	# unit tests (some failing with py3.10)

Summary:	Python 3 based FIDO 2.0 library
Summary(pl.UTF-8):	Biblioteka FIDO 2.0 dla Pythona 3
Name:		python3-fido2
# 1.1.1+ use poetry as buildsystem
Version:	1.1.0
Release:	2
# Yubico code is BSD licensed; includes also:
# pyudf (Apache 2.0)
# public suffix list (MPL 2.0)
License:	BSD, Apache v2.0, MPL v2.0
Group:		Libraries/Python
#Source0Download: https://github.com/Yubico/python-fido2/releases
Source0:	https://github.com/Yubico/python-fido2/releases/download/%{version}/fido2-%{version}.tar.gz
# Source0-md5:	ee9c06204d6eac131b4f7ca6360b0090
Patch0:		fido2-ctap2.patch
Patch1:		fido2-cryptography.patch
URL:		https://developers.yubico.com/python-fido2/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography >= 2.6
BuildRequires:	python3-cryptography < 43
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
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
%patch -P 0 -p1
%patch -P 1 -p1

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-fido2-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-fido2-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.adoc
%{py3_sitescriptdir}/fido2
%{py3_sitescriptdir}/fido2-%{version}-py*.egg-info
%{_examplesdir}/python3-fido2-%{version}

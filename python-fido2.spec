#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 based FIDO 2.0 library
Summary(pl.UTF-8):	Biblioteka FIDO 2.0 dla Pythona 2
Name:		python-fido2
Version:	0.9.1
Release:	2
# Yubico code is BSD licensed; includes also:
# pyudf (Apache 2.0)
# public suffix list (MPL 2.0)
License:	BSD, Apache v2.0, MPL v2.0
Group:		Libraries/Python
#Source0Download: https://github.com/Yubico/python-fido2/releases
Source0:	https://github.com/Yubico/python-fido2/releases/download/%{version}/fido2-%{version}.tar.gz
# Source0-md5:	bf661f7949a057440e52aad6595a24fa
Patch0:		%{name}-mock.patch
URL:		https://developers.yubico.com/python-fido2/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography >= 1.0
BuildRequires:	python-mock >= 1.0.1
BuildRequires:	python-pyfakefs >= 2.4
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography >= 1.0
BuildRequires:	python3-pyfakefs >= 2.4
BuildRequires:	python3-six
%endif
%endif
Requires:	python-cryptography >= 1.0
Requires:	python-modules >= 1:2.7
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides library functionality for communicating with a
FIDO device over USB as well as verifying attestation and assertion
signatures.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do komunikacji z urządzeniami
FIDO po USB, a także weryfikowania podpisów poświadczeń i zapewnień.

%package -n python3-fido2
Summary:	Python 3 based FIDO 2.0 library
Summary(pl.UTF-8):	Biblioteka FIDO 2.0 dla Pythona 3
Group:		Libraries/Python
Requires:	python3-cryptography >= 1.0
Requires:	python3-modules >= 1:3.4
Requires:	python3-six

%description -n python3-fido2
This package provides library functionality for communicating with a
FIDO device over USB as well as verifying attestation and assertion
signatures.

%description -n python3-fido2 -l pl.UTF-8
Ten pakiet zawiera bibliotekę funkcji do komunikacji z urządzeniami
FIDO po USB, a także weryfikowania podpisów poświadczeń i zapewnień.

%prep
%setup -q -n fido2-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-fido2-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-fido2-%{version}
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-fido2-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-fido2-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.adoc
%{py_sitescriptdir}/fido2
%{py_sitescriptdir}/fido2-%{version}-py*.egg-info
%{_examplesdir}/python-fido2-%{version}
%endif

%if %{with python3}
%files -n python3-fido2
%defattr(644,root,root,755)
%doc COPYING NEWS README.adoc
%{py3_sitescriptdir}/fido2
%{py3_sitescriptdir}/fido2-%{version}-py*.egg-info
%{_examplesdir}/python3-fido2-%{version}
%endif

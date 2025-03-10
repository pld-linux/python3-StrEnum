Summary:	An Enum that inherits from str
Summary(pl.UTF-8):	Enum dziedziczący ze str
Name:		python3-StrEnum
Version:	0.4.15
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/StrEnum/
Source0:	https://files.pythonhosted.org/packages/source/S/StrEnum/StrEnum-%{version}.tar.gz
# Source0-md5:	aa5e934c299dac8731c6db4008deab4d
URL:		https://pypi.org/project/StrEnum/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StrEnum is a Python enum.Enum that inherits from str to complement
enum.IntEnum in the standard library. Supports Python 3.7+ (included
in Python 3.11 standard library).

%description -l pl.UTF-8
StrEnum to pythonowy enum.Enum dziedziczący ze str, aby uzupełnić
enum.IntEnum z biblioteki standardowej. Obsługuje Pythona 3.7+
(został włączony do biblioteki standardowej Pythona 3.11).

%prep
%setup -q -n StrEnum-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/strenum
%{py3_sitescriptdir}/StrEnum-%{version}-py*.egg-info

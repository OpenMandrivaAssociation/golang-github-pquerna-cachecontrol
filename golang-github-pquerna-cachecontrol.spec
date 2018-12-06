# Run tests in check section
%bcond_without check

%global goipath         github.com/pquerna/cachecontrol
%global commit          0923c70de240c513ff98174aa10a783bdcf0560e

%global common_description %{expand:
cachecontrol implements RFC 7234 Hypertext Transfer Protocol (HTTP/1.1): 
Caching. It does this by parsing the Cache-Control and other headers, 
providing information about requests and responses -- but cachecontrol does 
not implement an actual cache backend, just the control plane to make 
decisions about if a particular response is cachable.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Golang HTTP Cache-Control Parser and Interpretation
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires: golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git0923c70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2.20180517git0923c70
- Bump to upstream 0923c70de240c513ff98174aa10a783bdcf0560e
- Fixes Github issue #12

* Thu May 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180517gitfd225a
- First package for Fedora


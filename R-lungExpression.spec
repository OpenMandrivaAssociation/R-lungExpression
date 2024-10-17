%global packname  lungExpression
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2.0
Release:          1
Summary:          ExpressionSets for Parmigiani et al., 2004 Clinical Cancer Research paper
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              https://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase 


BuildRequires:    R-devel Rmath-devel R-Biobase


%description
Data from three large lung cancer studies provided as ExpressionSets

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%{rlibdir}/%{packname}

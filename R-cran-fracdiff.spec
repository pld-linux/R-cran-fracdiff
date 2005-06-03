%define		fversion	%(echo %{version} |tr r -)
%define		modulename	fracdiff
Summary:	Fractionally differenced ARIMA (p,d,q) models
Summary(pl):	U³amkowo ró¿nicowane modele ARIMA (p,d,q)
Name:		R-cran-%{modulename}
Version:	1.1r1
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	e1f624b063789f21c74d85ebaeda60fa
BuildRequires:	R-base >= 2.0.0
BuildRequires:	blas-devel
BuildRequires:	gcc-g77
Requires(post,postun):	R-base >= 2.0.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maximum likelihood estimation of the parameters of a fractionally
differenced ARIMA(p,d,q) model (Haslett and Raftery, Appl.Statistics,
1989).

%description -l pl
Estymacja maksymalnego prawdopodobieñstwa parametrów u³amkowo
ró¿nicowanego modelu ARIMA(p,d,q) (Haslett i Raftery, "Appl.
Statistics", 1989).

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README,ChangeLog}
%{_libdir}/R/library/%{modulename}

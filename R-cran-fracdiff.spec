%define		fversion	%(echo %{version} |tr r -)
%define		modulename	fracdiff
Summary:	Fractionally differenced ARIMA (p,d,q) models
Summary(pl.UTF-8):	Ułamkowo różnicowane modele ARIMA (p,d,q)
Name:		R-cran-%{modulename}
Version:	1.4r2
Release:	1
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	6a6977d175ad963d9675736a8f8d41f7
BuildRequires:	R >= 2.8.1
BuildRequires:	blas-devel
BuildRequires:	gcc-fortran
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maximum likelihood estimation of the parameters of a fractionally
differenced ARIMA(p,d,q) model (Haslett and Raftery, Appl.Statistics,
1989).

%description -l pl.UTF-8
Estymacja maksymalnego prawdopodobieństwa parametrów ułamkowo
różnicowanego modelu ARIMA(p,d,q) (Haslett i Raftery, "Appl.
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
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README,ChangeLog}
%{_libdir}/R/library/%{modulename}

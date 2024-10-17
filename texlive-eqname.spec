Name:		texlive-eqname
Version:	20678
Release:	2
Summary:	Name tags for equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gene/eqname/eqname.sty
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqname.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The \eqname command provides a name tag for the current
equation, in place of an equation number. The name tag will be
picked up by a subsequent \label command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eqname/eqname.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

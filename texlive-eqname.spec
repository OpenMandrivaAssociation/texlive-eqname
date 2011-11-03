# revision 20678
# category Package
# catalog-ctan /macros/latex/contrib/gene/eqname/eqname.sty
# catalog-date 2010-12-04 00:54:21 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-eqname
Version:	20101204
Release:	1
Summary:	Name tags for equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/eqname/eqname.sty
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqname.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The \eqname command provides a name tag for the current
equation, in place of an equation number. The name tag will be
picked up by a subsequent \label command.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eqname/eqname.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

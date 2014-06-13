# revision 20678
# category Package
# catalog-ctan /macros/latex/contrib/gene/eqname/eqname.sty
# catalog-date 2010-12-04 00:54:21 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-eqname
Version:	20101204
Release:	7
Summary:	Name tags for equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/eqname/eqname.sty
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqname.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101204-2
+ Revision: 751538
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101204-1
+ Revision: 718357
- texlive-eqname
- texlive-eqname
- texlive-eqname
- texlive-eqname


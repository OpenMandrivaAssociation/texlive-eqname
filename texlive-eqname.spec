%global tl_name eqname
%global tl_revision 79130

Name:		texlive-%{tl_name}
Epoch:		1
Version:	492
Release:	%{tl_revision}.1
Summary:	Name tags for equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gene/eqname
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqname.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqname.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The \eqname command provides a name tag for the current equation, in
place of an equation number. The name tag will be picked up by a
subsequent \label command.


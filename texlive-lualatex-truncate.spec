Name:		texlive-lualatex-truncate
Version:	67201
Release:	1
Summary:	A wrapper for using the truncate package with LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lualatex-truncate
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-truncate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-truncate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-truncate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a wrapper for the truncate package, thus
fixing issues related to LuaTeX's hyphenation algorithm.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/lualatex-truncate
%{_texmfdistdir}/tex/lualatex/lualatex-truncate
%doc %{_texmfdistdir}/doc/lualatex/lualatex-truncate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

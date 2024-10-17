Name:		texlive-dosepsbin
Version:	29752
Release:	2
Summary:	Deal with DOS binary EPS files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/dosepsbin
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-dosepsbin.bin = %{EVRD}

%description
A Encapsulated PostScript (EPS) file may given in a special
binary format to support the inclusion of a thumbnail. This
file format, commonly known as DOS EPS format starts with a
binary header that contains the positions of the possible
sections: - Postscript (PS); - Windows Metafile Format (WMF);
and - Tag Image File Format (TIFF). The PS section must be
present and either the WMF file or the TIFF file should be
given. The package provides a Perl program that will extract
any of the sections of such a file, in particular providing a
'text'-form EPS file for use with (La)TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/dosepsbin
%{_texmfdistdir}/scripts/dosepsbin/dosepsbin.pl
%doc %{_mandir}/man1/dosepsbin.1*
%doc %{_texmfdistdir}/doc/man/man1/dosepsbin.man1.pdf
%doc %{_texmfdistdir}/doc/support/dosepsbin/Makefile.in
%doc %{_texmfdistdir}/doc/support/dosepsbin/README
%doc %{_texmfdistdir}/doc/support/dosepsbin/clean-case.pl
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.html
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.ltx
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.pdf
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.txt
%doc %{_texmfdistdir}/doc/support/dosepsbin/version.pl
#- source
%doc %{_texmfdistdir}/source/support/dosepsbin/configure
%doc %{_texmfdistdir}/source/support/dosepsbin/configure.ac
%doc %{_texmfdistdir}/source/support/dosepsbin/install-sh

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/dosepsbin/dosepsbin.pl dosepsbin
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

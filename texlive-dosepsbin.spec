# revision 24774
# category Package
# catalog-ctan /support/dosepsbin
# catalog-date 2012-03-22 21:51:23 +0100
# catalog-license artistic
# catalog-version 1.2
Name:		texlive-dosepsbin
Version:	1.2
Release:	1
Summary:	Deal with DOS binary EPS files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/dosepsbin
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.source.tar.xz
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
%doc %{_texmfdistdir}/doc/support/dosepsbin/Makefile.in
%doc %{_texmfdistdir}/doc/support/dosepsbin/README
%doc %{_texmfdistdir}/doc/support/dosepsbin/clean-case.pl
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.html
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.ltx
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.pdf
%doc %{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.txt
%doc %{_texmfdistdir}/doc/support/dosepsbin/version.pl
%doc %{_mandir}/man1/dosepsbin.1*
%doc %{_texmfdir}/doc/man/man1/dosepsbin.man1.pdf
#- source
%doc %{_texmfdistdir}/source/support/dosepsbin/configure
%doc %{_texmfdistdir}/source/support/dosepsbin/configure.ac
%doc %{_texmfdistdir}/source/support/dosepsbin/install-sh

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/dosepsbin/dosepsbin.pl dosepsbin
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

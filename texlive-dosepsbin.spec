%global tl_name dosepsbin
%global tl_revision 29752

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Deal with DOS binary EPS files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/dosepsbin
License:	artistic
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dosepsbin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dosepsbin.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Encapsulated PostScript (EPS) file may given in a special binary
format to support the inclusion of a thumbnail. This file format,
commonly known as DOS EPS format starts with a binary header that
contains the positions of the possible sections: PostScript (PS);
Windows Metafile Format (WMF); and Tag Image File Format (TIFF). The PS
section must be present and either the WMF file or the TIFF file should
be given. The package provides a Perl program that will extract any of
the sections of such a file, in particular providing a 'text'-form EPS
file for use with (La)TeX.


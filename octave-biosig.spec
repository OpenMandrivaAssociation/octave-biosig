%global octpkg biosig

Summary:	Biomedical signal processing tools
Name:		octave-biosig
Version:	2.6.0
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/biosig/
Source0:	https://downloads.sourceforge.net/biosig/biosig4octave-%{version}.src.tar.gz
BuildRequires:  octave-devel >= 3.2.0
BuildRequires:  pkgconfig(libbiosig)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Biomedical signal processing tools.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}4octave-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild


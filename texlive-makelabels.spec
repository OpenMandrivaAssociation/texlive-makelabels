Name:		texlive-makelabels
Version:	60255
Release:	2
Summary:	Add a '\makelabels' feature to KOMA-Script letter classes and package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makelabels
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makelabels.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makelabels.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makelabels.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The standard letter class letter has a label feature. You can
activate it using \makelabels. While in Germany window
envelopes are common, printing labels is not common, and
scrlttr2 has never supported label printing. Using
makelabels.lco does implement a \makelabels feature similar to
the standard letter classes. Currently there are (almost) no
configuration features for makelabels.lco. But you may use the
envlab package after loading makelabels.lco to get various
configuration features.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/makelabels
%{_texmfdistdir}/tex/latex/makelabels
%doc %{_texmfdistdir}/doc/latex/makelabels

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

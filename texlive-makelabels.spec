%global tl_name makelabels
%global tl_revision 60255

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Add a \makelabels feature to KOMA-Script letter classes and package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makelabels
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makelabels.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makelabels.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makelabels.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The standard letter class letter has a label feature. You can activate
it using \makelabels. While in Germany window envelopes are common,
printing labels is not common, and scrlttr2 has never supported label
printing. Using makelabels.lco does implement a \makelabels feature
similar to the standard letter classes. Currently there are (almost) no
configuration features for makelabels.lco. But you may use the envlab
package after loading makelabels.lco to get various configuration
features.


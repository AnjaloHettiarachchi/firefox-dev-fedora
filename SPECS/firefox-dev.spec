Name:       firefox-dev        
Version:    87.0b4    
Release:    7%{?dist}
Summary:    Firefox Developer Edition (formerly "Aurora") pre-beta Web browser

License:    MPLv1.1 or GPLv2+ or LGPLv2+
URL:        https://www.mozilla.org/en-US/firefox/developer/
Source0:    https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version}/linux-x86_64/en-US/firefox-%{version}.tar.bz2
Source1:    firefox_developer_edition.desktop

ExclusiveArch: x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  xdg-utils
BuildRequires:  gtk-update-icon-cache

%description
This is a pre-beta release of Mozilla Firefox intended for Web developers and
enthusiasts who want early access to new features. It receives new updates
(almost) daily, adding and refining support for the very latest Web standards
that won't make it into the stable release of Firefox for some months. It also
comes with some addons for Web development enabled by default.

You may actually find that Developer Edition works just fine for normal everyday
use: Some users set it as their default Web browser. You can sign in to your
normal Firefox account and sync your preferences, extensions, and bookmarks,
etc. Or you can keep the Firefox versions separate, and use different profiles,
even different browser UI themes. Firefox Developer Edition can install
alongside the stable release of Firefox, making it easy to switch back and forth
between the two versions.

That being said, a lot of the technology here is still experimental, and there
will very likely be some bugs, so just remember that by using Developer Edition,
you're helping Mozilla make Firefox the best Web browser they can. And have fun!

Bugs related to Firefox Developer Edition should be reported directly to
Mozilla: <https://bugzilla.mozilla.org/>

Bugs related to this package should be reported at my GitHub project:
<https://github.com/AnjaloHettiarachchi/firefox-dev-rpm/>

%prep
%setup -q -n firefox
export XDG_UTILS_DEBUG_LEVEL=5

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/firefox-dev,%{_bindir},%{_datadir}/applications}

%__cp -r * %{buildroot}/opt/firefox-dev

%__ln_s /opt/firefox-dev/firefox %{buildroot}%{_bindir}/firefox-dev

%post
if [ $1 -gt 1 ] ; then
    xdg-icon-resource install --novendor --size 128 /opt/firefox-dev/browser/chrome/icons/default/default128.png firefox-developer-edition
    gtk-update-icon-cache -f -t /usr/share/icons/hicolor
    desktop-file-install --dir=/usr/share/applications %{SOURCE1}
fi

%files
%{_datadir}/applications/firefox_developer_edition.desktop
%{_bindir}/firefox-dev
/opt/firefox-dev

%changelog
* Fri Feb 19 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com>
- Initial build
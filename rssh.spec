###########################################################################
# rssh.spec - spec file for building RPMs of rssh, specifically for Red Hat
# systems, though probably suitable for others.
#

Summary: a restricted shell for scp or sftp
Name: rssh
Version: 2.3.4
Release: 1
License: BSD
Group: System Environment/Shells
Source: http://www.pizzashack.org/rssh/src/%{name}-%{version}.tar.gz
URL: http://www.pizzashack.org/rssh/
Packager: Derek Martin <rssh-discuss at lists dot sourceforge dot net>
Requires: openssh
Provides: rssh

Buildroot: /tmp/%{name}-%{version}-buildroot

%description
rssh is a restricted shell for use with ssh, which allows the system
administrator to restrict a user's access to a system via scp or sftp, or
both.

%prep
%setup

%build
%configure
%{__make} 

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(644, root, root, 0755)
%doc AUTHORS ChangeLog CHROOT COPYING README SECURITY TODO conf_convert.sh mkchroot.sh
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/rssh.conf
%attr(755, root, root) %{_bindir}/rssh
%attr(4755, root, root) %{_libexecdir}/rssh_chroot_helper

%clean
%{__rm} -rf %{buildroot}


%define pgadmin_version %(date +%Y%m%d)
%define pgadmin_release rh%(rpm -q --qf='%{VERSION}' redhat-release | sed 's/\\..*$//')

Summary: Graphical client for PostgreSQL.
Name: pgadmin3
Version: %{pgadmin_version}
Release: %{pgadmin_release}
License: Artistic
Group: Applications/Databases
Source: pgadmin3-%{pgadmin_version}.tar.gz
URL: http://www.pgadmin.org/
BuildRoot: %{_tmppath}/%{name}-root
# all packages providing an implementation of wxWindows library (regardless of
# the toolkit used) should provide the (virtual) wxwin package, this makes it
# possible to require wxwin instead of requiring "wxgtk or wxmotif or wxqt..."
Requires: gtk2 >= 2.2
BuildRequires: autoconf >= 2.57, automake >= 1.7.5, gtk2-devel >= 2.2, postgresql >= 7.3.2

%description
pgAdmin3 the graphical administration interface of PostgreSQL.

%prep
%setup -q

%build
sh bootstrap
sh configure --enable-debug --enable-unicode --enable-gtk2
make all

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/pgadmin3

%changelog
* Mon Jun 10 2003 Jean-Michel POURE <jm.poure@freesurf.fr>
- Initial build


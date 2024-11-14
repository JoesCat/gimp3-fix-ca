# -*- Autoconf -*-
dnl Process this file with "autoreconf -i;automake" to produce a configure script.

# Copyright (C) 2024 by Joe Da Silva

AC_PREREQ([2.69])
#--------------------------------------------------------------------------
# Setup variables before running AC_INIT
#
# Making point releases:
#   fix_ca_major_version += 0;
#   fix_ca_minor_version += 1; (patches or added function(s))
#
# If any new functions have been added:
#   fix_ca_major_version += 0;
#   fix_ca_minor_version += 1; (added function(s))
#
# If backwards compatibility has been broken:
#   fix_ca_major_version += 1;
#   fix_ca_minor_version = 0;
#
m4_define([fix_ca_name], [gimp3-fix-ca])
m4_define([fix_ca_major_version], [0])
m4_define([fix_ca_minor_version], [1])
m4_define([fix_ca_version],[fix_ca_major_version.fix_ca_minor_version])
m4_define([fix_ca_package_name], [gimp3-fix-ca])
m4_define([fix_ca_package_home], [https://github.com/JoesCat/gimp3-fix-ca])
m4_define([fix_ca_package_email], [https://github.com/JoesCat/gimp3-fix-ca/issues])
#--------------------------------------------------------------------------
AC_INIT([fix_ca_name],[fix_ca_version],[fix_ca_package_email],
	[fix_ca_package_name],[fix_ca_package_home])
#--------------------------------------------------------------------------
AC_CONFIG_SRCDIR([fix-ca.c])
AC_CONFIG_MACRO_DIR([m4])
AC_CANONICAL_TARGET
AC_CANONICAL_HOST
AC_CANONICAL_BUILD
AC_USE_SYSTEM_EXTENSIONS
AM_INIT_AUTOMAKE([foreign -Wall])

#--------------------------------------------------------------------------
# automake 1.12 needs AM_PROG_AR but automake < 1.11.2 doesn't recognize it
m4_ifdef([AM_PROG_AR], [AM_PROG_AR])

LT_INIT
AC_SUBST([LIBTOOL_DEPS])

#--------------------------------------------------------------------------
# Checks for programs.
AC_PROG_CC
AC_PROG_SED
AC_PROG_LN_S
AC_PROG_MKDIR_P
AC_PATH_PROG([CHMOD],[chmod],[:])
AC_CHECK_PROGS([GIMP],[gimp-3.0],[:])
AC_CHECK_PROGS([GIMPTOOL],[gimptool-3.0],[:])
AC_PATH_PROG([MD5SUM],[md5sum],[:])
AC_PATH_PROG([MSGFMT],[msgfmt],[:])
AC_PATH_PROG([MSGINIT],[msginit],[:])
AC_PATH_PROG([MSGMERGE],[msgmerge],[:])
AC_PATH_PROG([STRIP],[strip],[:])
AC_PATH_PROG([XGETTEXT],[xgettext],[:])
AM_CONFIG_HEADER(fix-ca-config.h)
AC_PROG_INSTALL
AC_PROG_MAKE_SET

#--------------------------------------------------------------------------
# Enable silent build rules by default, this requires atleast Automake-1.11
# Disable by passing --disable-silent-rules to configure or using make V=1
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])],[AC_SUBST([AM_DEFAULT_VERBOSITY],[1])])

#--------------------------------------------------------------------------
# The following is for benefit of links using paths relative to top_srcdir.
AC_SUBST([CPPFLAGS],["${CPPFLAGS}"])

#--------------------------------------------------------------------------
# Compiler and Linker flags to override auto detection and insertion.
# Use CFLAGS if you want to add more in addition to autodetect.
AC_ARG_VAR([FCA_CFLAGS],[C compiler flags overriding automatic detection])
AC_ARG_VAR([FCA_LIB],[Linker flags overriding automatic detection])

# Auto detect and add usable compiler warnings (skip if FCA_CFLAGS="").
WCFLAGS=""
AC_LANG_PUSH([C])
AX_CHECK_COMPILE_FLAG([-Wall],[WCFLAGS="$WCFLAGS -Wall"])
AX_CHECK_COMPILE_FLAG([-Wextra],[WCFLAGS="$WCFLAGS -Wextra"])
AX_CHECK_COMPILE_FLAG([-Wcast-align],[WCFLAGS="$WCFLAGS -Wcast-align"])
AX_CHECK_COMPILE_FLAG([-Wbad-function-cast],[WCFLAGS="$WCFLAGS -Wbad-function-cast"])
AX_CHECK_COMPILE_FLAG([-Wc++-compat],[WCFLAGS="$WCFLAGS -Wc++-compat"])
AX_CHECK_COMPILE_FLAG([-Wmissing-prototypes],[WCFLAGS="$WCFLAGS -Wmissing-prototypes"])
AX_CHECK_COMPILE_FLAG([-Wunused],[WCFLAGS="$WCFLAGS -Wunused"])
AX_CHECK_COMPILE_FLAG([-Wdeprecated-declarations],[WCFLAGS="$WCFLAGS -Wdeprecated-declarations"])
AX_CHECK_COMPILE_FLAG([-Wconversion],[WCFLAGS="$WCFLAGS -Wconversion"])
AX_CHECK_COMPILE_FLAG([-Wsign-conversion],[WCFLAGS="$WCFLAGS -Wsign-conversion"])
AX_CHECK_COMPILE_FLAG([-Wformat=2],[WCFLAGS="$WCFLAGS -Wformat=2"])
AX_CHECK_COMPILE_FLAG([-Wformat-security],[WCFLAGS="$WCFLAGS -Wformat-security"])
AX_CHECK_COMPILE_FLAG([-fno-common],[WCFLAGS="$WCFLAGS -fno-common"])
AX_CHECK_COMPILE_FLAG([-Wmissing-declarations],[WCFLAGS="$WCFLAGS -Wmissing-declarations"])
AX_CHECK_COMPILE_FLAG([-Wstrict-prototypes],[WCFLAGS="$WCFLAGS -Wstrict-prototypes"])
AX_CHECK_COMPILE_FLAG([-fPIC],[WCFLAGS="$WCFLAGS -fPIC"])
AX_CHECK_COMPILE_FLAG([-Wstrict-overflow],[WCFLAGS="$WCFLAGS -Wstrict-overflow"])
AX_CHECK_COMPILE_FLAG([-Wpointer-arith],[WCFLAGS="$WCFLAGS -Wpointer-arith"])
AX_CHECK_COMPILE_FLAG([-Wcast-qual],[WCFLAGS="$WCFLAGS -Wcast-qual"])
AX_CHECK_COMPILE_FLAG([-Wcast-align],[WCFLAGS="$WCFLAGS -Wcast-align"])
AX_CHECK_COMPILE_FLAG([-Wpadded],[WCFLAGS="$WCFLAGS -Wpadded"])
AX_CHECK_COMPILE_FLAG([-Woverlength-strings],[WCFLAGS="$WCFLAGS -Woverlength-strings"])
# ARM likely has this, x86 not likely for "half or "_Float16"
AX_CHECK_COMPILE_FLAG([-mfp16-format],[WCFLAGS="$WCFLAGS -mfp16-format"])
# Use the following two combined for clang (if working with "half" or "_Float16"
AX_CHECK_COMPILE_FLAG([-fnative-half-type],[WCFLAGS="$WCFLAGS -fnative-half-type"])
AX_CHECK_COMPILE_FLAG([-fallow-half-arguments-and-returns],[WCFLAGS="$WCFLAGS -fallow-half-arguments-and-returns"])
AC_LANG_POP
# Skip if replacing with FCA_LIB instead.
WLSLIB=""
if test -z $FCA_LIB ; then
   WLSLIB="${WCFLAGS}"
fi
if test "${FCA_CFLAGS}"x != x; then
   WCFLAGS=""
fi

#--------------------------------------------------------------------------
# Check for required libraries.
# NOTE: Some distros don't have /usr/local included in the /etc/ld.so PATH,
# so, PKG_CHECK_MODULES may not find libraries you compile into /usr/local,
# therefore use AC_SEARCH_LIBS, AC_CHECK_FUNC for backup.

# Check for math.h include and math library (some OSes have -lm built-in).
have_libm=maybe
AC_CHECK_HEADER([math.h],
  AC_SEARCH_LIBS([cos],[m],[have_libm=yes],
    AC_CHECK_FUNC([cos],[have_libm=yes])))
if test x"${have_libm}" != xyes; then
  AC_MSG_FAILURE([ERROR: Please install the Math library and math.h],[1])
fi

# Avoid being locked to a particular gettext verion, use what's available.
have_gettext=no
AC_CHECK_HEADERS([intl.h],[have_gettext=yes])
AC_CHECK_FUNC([gettext],[have_gettext=yes],[have_gettext=no])
AC_CHECK_FUNC([bind_textdomain_codeset],,[have_gettext=no])
AC_CHECK_FUNC([textdomain],,[have_gettext=no])
if test x"${have_gettext}" = xno; then
  AC_SEARCH_LIBS([intl],[have_gettext=yes],[
    AC_MSG_ERROR([ERROR: gettext() required! Please install libintl or GETTEXT Packages.])])
fi
AC_CHECK_HEADER([locale.h],
  AC_CHECK_FUNC([setlocale],,[
    AC_MSG_ERROR([ERROR: setlocale() required! Please install setlocale packages.])]))
GETTEXT_PACKAGE=gimp30-fix-ca
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [The gettext translation domain.])
if test x"${have_gettext}" = xyes; then
  AC_DEFINE([HAVE_GETTEXT],1,[Enable use of local languages])
fi

dnl need to hardcode locale
LOCALEDIR='/usr/share/locale'
AC_SUBST(LOCALEDIR)
DATADIR='${datadir}/${fix_ca_name}'
AC_SUBST(DATADIR)

ACLOCAL="$ACLOCAL $ACLOCAL_FLAGS"
AC_SUBST([ACLOCAL],["${ACLOCAL}"])

# Check for libgimp/gimp.h include file and libgimp library.
GIMP_CFLAGS=
GIMP_LIBS=
have_libgimp=no
PKG_CHECK_MODULES([GIMP],[gimp-3.0 gimpui-3.0],[have_libgimp=yes])
if test x"${have_libgimp}" != xyes; then
    AC_MSG_FAILURE([ERROR: Please install the developer version of libgimp3.],[1])
fi
AC_SUBST(GIMP_CFLAGS)
AC_SUBST(GIMP_LIBS)
GIMP_LIBDIR=`${PKG_CONFIG} --variable=gimplibdir gimp-3.0`
AC_SUBST(GIMP_LIBDIR)
GIMP_DATADIR=`${PKG_CONFIG} --variable=gimpdatadir gimp-3.0`
AC_SUBST(GIMP_DATADIR)

AM_CONDITIONAL([HAVEGIMPTOOL],[test "${GIMPTOOL}"x != x])

GTK_CFLAGS=
GTK_LIBS=
have_libgtk=no
PKG_CHECK_MODULES([GTK],[gtk+-3.0],[have_libgtk=yes])
if test x"${have_libgtk}" != xyes; then
    AC_MSG_FAILURE([ERROR: Please install the developer version of libgtk+3.],[1])
fi
AC_SUBST(GTK_CFLAGS)
AC_SUBST(GTK_LIBS)

CPPFLAGS="${CPPFLAGS} AS_ESCAPE([-I${top_builddir}]) AS_ESCAPE([-I${top_srcdir}])"
AC_SUBST([CPPFLAGS],["${CPPFLAGS}"])

#--------------------------------------------------------------------------
# Enable debug_time mode, shows runtime and various printf on command-line.
AC_ARG_ENABLE([debugtime],
  [AS_HELP_STRING([--enable-debugtime],
    [Enable debugging time printf mode on commandline @<:@default=no@:>@])],
  [],[enable_debugtime=no])
if test "x$enable_debugtime" = xyes || test "x$enable_debugtime" = xtrue ; then
  AC_DEFINE([DEBUG_TIME],1,[Define if debugging time using printf.])
fi

#--------------------------------------------------------------------------
# Pass variables to MAKEFILE.AM
AC_SUBST([CPPFLAGS],["${CPPFLAGS}"])
AC_SUBST([LS_CFLAGS])
AC_SUBST([LS_LIB])
AC_SUBST([WCFLAGS])
AC_SUBST([WLSLIB])
AC_SUBST([FIX_CA_MAJOR_VERSION],[fix_ca_major_version])
AC_SUBST([FIX_CA_MINOR_VERSION],[fix_ca_minor_version])
AC_SUBST([FIX_CA_VERSION],[fix_ca_version])
AC_SUBST([FIX_CA_PACKAGE_NAME],[fix_ca_package_name])
AC_SUBST([FIX_CA_EMAIL],[fix_ca_package_email])
AC_SUBST([HOST],["$host"])

dnl Do this here since automake can't process 'if/else/endif in Makefile.am
dnl also note plugin directory recently changed from gimp/2.99 to gimp/3.0
SNIPPET1='
ifeq ($(shell id -u),0)
  bindir = $(GIMP_LIBDIR)/plug-ins/fix-ca
else
  bindir = $(libdir)/gimp/3.0/plug-ins/fix-ca
endif
'
AC_SUBST([SNIPPET1])
AM_SUBST_NOTMAKE([SNIPPET1])
SNIPPET2='
gimplocaledir = $(localedir)
ifeq ($(shell id -u),0)
  gimplocaledir = $(LOCALEDIR)
endif
'
AC_SUBST([SNIPPET2])
AM_SUBST_NOTMAKE([SNIPPET2])

#--------------------------------------------------------------------------
# Pass variables to fix-ca-config.h
AC_DEFINE([FIX_CA_MAJOR_VERSION],["fix_ca_major_version"],[gimp-fix-ca major version])
AC_DEFINE([FIX_CA_MINOR_VERSION],["fix_ca_minor_version"],[gimp-fix-ca minor version])

# Put ifndef wrapper on fix-ca-config.h so we don't call it repeatedly.
AH_TOP([#ifndef FIX_CA_CONFIG_H
#define FIX_CA_CONFIG_H 1])
AH_BOTTOM([

#endif])

#--------------------------------------------------------------------------
AC_CONFIG_FILES([
Makefile
po/Makefile
tests/Makefile
rpm/gimp3-fix-ca.spec
])
AC_OUTPUT
AC_MSG_NOTICE([

Configuration:

  Source code location	${srcdir}
  Build code location	${builddir}
  docs root dir		${datarootdir}
  bin plug-in dir	${GIMP_LIBDIR}/plug-ins/fix-ca
  GIMP3 locale dir	${LOCALEDIR}
  Use locale languages	${have_gettext}
  Compiler		${CC}
  CPPFLAGS		${CPPFLAGS}
  Config auto WCFLAGS	${WCFLAGS}
  Config FCA_CFLAGS	${FCA_CFLAGS}
  Config FCA_LIB	${FCA_LIB}
  GIMP_CFLAGS		${GIMP_CFLAGS}
  GIMP_LIBS		${GIMP_LIBS}
  GTK_CFLAGS		${GTK_CFLAGS}
  GTK_LIBS		${GTK_LIBS}
  CFLAGS		${CFLAGS}
  LIBS			${LIBS}
])

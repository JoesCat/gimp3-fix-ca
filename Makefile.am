# Makefile.am - Top level automakefile for fix-ca

SUBDIRS = . po tests

# The braces around ACLOCAL_FLAGS below instead of parentheses are intentional!
# Otherwise autoreconf misparses the line.
ACLOCAL_AMFLAGS=-I m4 ${ACLOCAL_FLAGS}
AM_CFLAGS = ${CFLAGS} ${CPPFLAGS} ${GIMP_CFLAGS} ${GTK_CFLAGS} ${WCFLAGS} ${FCA_CFLAGS}

AM_CPPFLAGS = -I${builddir} -I${srcdir} ${GIMP_CFLAGS} ${GTK_CFLAGS} -I${includedir}

bin_PROGRAMS = fix-ca
# 'make distcheck' can't write to ${GIMP_LIBDIR}/plug-ins/fix-ca because of
# directory permissions, therefore don't install fix-ca unless it is root
@SNIPPET1@

fix_ca_name    = fix-ca
fix_ca_SOURCES = fix-ca.c
fix_ca.$(OBJEXT): fix-ca-config.h
fix_ca_LDADD   = ${LIBS} ${GIMP_LIBS} ${GTK_LIBS} ${WSLIB} ${FCA_LIB}

metainfodir = ${datarootdir}/metainfo
metainfo_DATA = ${srcdir}/org.gimp.extension.fix3-ca.metainfo.xml

EXTRA_DIST = README.md fix-ca-config.h.in rpm/gimp3-fix-ca.spec.in		\
	img-fix-ca/ex-fixed.jpg img-fix-ca/ex-orig.jpg img-fix-ca/ex-zoom.jpg	\
	img-fix-ca/fix-ca-dialog.png img-fix-ca/full-Wat_Pathum_Wanaram.jpg	\
	img-fix-ca/plug-in-browser.png img-fix-ca/Sea_turtle-dialog_before.png	\
	img-fix-ca/Sea_turtle-dialog.png img-fix-ca/Sea_turtle-fixed.jpg	\
	img-fix-ca/Sea_turtle-orig.jpg img-fix-ca/Sea_turtle-zoom.jpg		\
	img-fix-ca/ex-bran.jpg img-fix-ca/ex-bran-fix.jpg			\
	img-fix-ca/fix-ca-center.jpg img-fix-ca/full-branches.jpg		\
	img-fix-ca/poorman-zoom.jpg org.gimp.extension.fix3-ca.metainfo.xml
nodist_EXTRA_DATA = .git .github
DISTCHECK_CONFIGURE_FLAGS = --disable-silent-rules --enable-debugtime

strip:
	${STRIP} ${builddir}/${fix_ca_name}

# These use gimptool to install/uninstall fix-ca in user directory
# NOTE: gimptool installs fix-ca directly into the plugin directory
install-user:
	${GIMPTOOL} --install-bin ${builddir}/${fix_ca_name}

uninstall-user:
	${GIMPTOOL} --uninstall-bin ${fix_ca_name}

AM_CFLAGS = ${CFLAGS} ${CPPFLAGS} ${GIMP_CFLAGS} ${GTK_CFLAGS} ${WCFLAGS} ${FCA_CFLAGS} -I${top_srcdir} -I${top_builddir}

AM_CPPFLAGS = -I${top_srcdir} -I${top_builddir} ${GIMP_CFLAGS} -I${includedir}

EXTRA_DIST = test-fix-ca.c test1.md5
nodist_EXTRA_DATA = .deps .libs

noinst_PROGRAMS     = test-fix-ca
test_fix_ca_name    = test-fix-ca
test_fix_ca_SOURCES = test-fix-ca.c
test_fix_ca.$(OBJEXT): fix-ca-config.h
test_fix_ca_LDADD   = ${LIBS} ${GIMP_LIBS} ${GTK_LIBS} ${WSLIB} ${FCA_LIB}

update-scm1:
	echo "(define (test-fix-ca-scm)" > ${builddir}/test-fix-ca.scm; \
	echo "  (let* (" >> ${builddir}/test-fix-ca.scm; \
	echo "        (theImage (car (gimp-file-load RUN-NONINTERACTIVE \"${top_srcdir}/img-fix-ca/full-branches.jpg\")))" >> ${builddir}/test-fix-ca.scm; \
	echo "        (drawables (car (gimp-image-get-selected-drawables theImage)))" >> ${builddir}/test-fix-ca.scm; \
	echo "        )" >> ${builddir}/test-fix-ca.scm; \
	echo "    (plug-in-test-fix-ca RUN-NONINTERACTIVE theImage drawables 6.0 -2.4 658 1280 1 0 0 0 0)" >> ${builddir}/test-fix-ca.scm; \
	echo "    (file-bmp-export RUN-NONINTERACTIVE theImage \"${builddir}/test1.bmp\" \"\" FALSE FALSE \"rgb-888\")" >> ${builddir}/test-fix-ca.scm; \
	echo "    (gimp-image-delete theImage)" >> ${builddir}/test-fix-ca.scm; \
	echo "  )" >> ${builddir}/test-fix-ca.scm; \
	echo ")" >> ${builddir}/test-fix-ca.scm; \
	echo "" >> ${builddir}/test-fix-ca.scm; \
	echo "(script-fu-register \"test-fix-ca-scm\"" >> ${builddir}/test-fix-ca.scm; \
	echo "  _\"_test-fix-ca-scm...\"" >> ${builddir}/test-fix-ca.scm; \
	echo "  _\"Simple script to load an image, modify it, and save the resulting image. This uses the test version of gimp-Fix-CA (called test-plug-in-fix-ca).\"" >> ${builddir}/test-fix-ca.scm; \
	echo "  \"Jose Da Silva\"" >> ${builddir}/test-fix-ca.scm; \
	echo "  \"Jose Da Silva\"" >> ${builddir}/test-fix-ca.scm; \
	echo "  \"2024"\" >> ${builddir}/test-fix-ca.scm; \
	echo "  \"RGB*"\" >> ${builddir}/test-fix-ca.scm; \
	echo ")" >> ${builddir}/test-fix-ca.scm; \
	echo "" >> ${builddir}/test-fix-ca.scm; \
	echo "(script-fu-menu-register \"test-fix-ca-scm\"" >> ${builddir}/test-fix-ca.scm; \
	echo "                         \"<Image>/Filters/Colors\")" >> ${builddir}/test-fix-ca.scm; \
	echo "" >> ${builddir}/test-fix-ca.scm

update-test1:
	echo "#!/bin/sh" > ${builddir}/test1.sh; \
	echo "rm -f ${builddir}/test1.bmp" >> ${builddir}/test1.sh; \
	echo "${GIMPTOOL} --install-script ${builddir}/test-fix-ca.scm" >> ${builddir}/test1.sh; \
	echo "${GIMPTOOL} --install-bin ${builddir}/test-fix-ca" >> ${builddir}/test1.sh; \
	echo "${GIMP} --verbose --console-messages -i --batch-interpreter plug-in-script-fu-eval -b '(test-fix-ca-scm RUN-NONINTERACTIVE)' -b '(gimp-quit 0)'" >> ${builddir}/test1.sh; \
	echo "${GIMPTOOL} --uninstall-bin test-fix-ca" >> ${builddir}/test1.sh; \
	echo "${GIMPTOOL} --uninstall-script test-fix-ca.scm" >> ${builddir}/test1.sh; \
	echo "${MD5SUM} -c ${top_srcdir}/tests/test1.md5" >> ${builddir}/test1.sh; \
	${CHMOD} +x ${builddir}/test1.sh

TESTS = ${builddir}/test1.sh

test1.sh:
	make update-scm1; \
	make update-test1

clean-local:
	rm -f ${builddir}/test?.sh ${builddir}/test?.bmp ${builddir}/test*.scm

.PHONY: update-scm1 update-test1

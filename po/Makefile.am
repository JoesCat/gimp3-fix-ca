LANGUAGES = es fr pt
PO_FILES = es.po fr.po pt.po

# Information to help translators:
#
# To create a new pot file, you need to cd into this po directory first:
#   cd po; del gimp30-fix-ca.pot; make update-pot
#
# To update existing po files you need to cd into po directory and then do:
#   cd po; make update-po

@SNIPPET2@

.PHONY: all install install-user uninstall uninstall-user clean $(LANGUAGES)
.PHONY: update-po update-pot

all: update-pot $(LANGUAGES)

$(LANGUAGES):
	if [[ -e $(srcdir)/$@.po ]]; \
	then $(MSGFMT) -c -v -o $(builddir)/$@.mo $(srcdir)/$@.po; \
	else $(MSGFMT) -c -v -o $(builddir)/$@.mo $(builddir)/$@.po; \
	fi

update-po: $(PO_FILES)

$(PO_FILES): $(GETTEXT_PACKAGE).pot
	if [[ -e $(srcdir)/$@ ]]; \
	then $(MSGMERGE) -U $(srcdir)/$@ $^; \
	else $(MSGFMT) -l $(subst .po,,$@) -o $(builddir)/$@ -i $^; \
	fi

install-data-local: $(LANGUAGES)
	for L in $(LANGUAGES); \
	do $(MKDIR_P) -p "$(DESTDIR)$(gimplocaledir)/$$L/LC_MESSAGES"; \
	install -v -m 0644 $(builddir)/$$L.mo "$(DESTDIR)$(gimplocaledir)/$$L/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"; \
	done

uninstall-local: $(LANGUAGES)
	for L in $(LANGUAGES); \
	do rm -vf "$(DESTDIR)$(gimplocaledir)/$$L/LC_MESSAGES/$(GETTEXT_PACKAGE).mo"; \
	done

clean-local:
	rm -f *.po~ *.mo *.mo~

install-user:
	$(warning Will not install gettext files for user installation!)

uninstall-user:
	$(warning Will not uninstall gettext files for user installation!)


update-pot: $(GETTEXT_PACKAGE).pot

$(GETTEXT_PACKAGE).pot:
	$(XGETTEXT) -k_ -k_\" -d $(GETTEXT_PACKAGE) -o $@ \
	--package-version=$(FIX_CA_VERSION) --msgid-bugs-address=$(FIX_CA_EMAIL) \
	../*.c

EXTRA_DIST = $(PO_FILES) $(GETTEXT_PACKAGE).pot

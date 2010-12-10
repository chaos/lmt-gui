SUBDIRS = scripts java

all: lmt.jar

lmt.jar:
	build/mkjar $@ java

CLEANFILES = lmt.jar

runlwatch:
	export LMT_CLASSPATH=lmt.jar; scripts/lwatch 
runlstat:
	export LMT_CLASSPATH=lmt.jar; scripts/lstat

rpmdirs:
	mkdir -p $(top_builddir)/rpm/SPECS
	mkdir -p $(top_builddir)/rpm/SOURCES
	mkdir -p $(top_builddir)/rpm/BUILD
	mkdir -p $(top_builddir)/rpm/RPMS
	mkdir -p $(top_builddir)/rpm/SRPMS

rpm: dist rpmdirs
	rpmbuild -ta --define "_topdir $(realpath $(top_builddir)/rpm)" $(DIST_ARCHIVES)


EXTRA_DIST = META lmt-gui.spec build/mkjar DISCLAIMER sample.lmtrc

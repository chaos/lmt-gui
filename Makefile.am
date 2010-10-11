SUBDIRS = scripts java

all: lmt.jar

lmt.jar:
	build/mkjar $@ java

CLEANFILES = lmt.jar

runlwatch:
	export LMT_CLASSPATH=lmt.jar; scripts/lwatch 
runlstat:
	export LMT_CLASSPATH=lmt.jar; scripts/lstat

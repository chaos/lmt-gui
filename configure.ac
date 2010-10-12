#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.57)
AC_INIT([lmt-gui])
AC_CONFIG_AUX_DIR([config])
AC_CONFIG_SRCDIR([NEWS])
AC_CANONICAL_SYSTEM
X_AC_META
X_AC_EXPAND_INSTALL_DIRS

AM_INIT_AUTOMAKE($META_NAME, $META_VERSION)
AM_CONFIG_HEADER([config/config.h])
AM_MAINTAINER_MODE

dnl JL Custom stuff
AC_ARG_WITH(java,  [  --with-java  override java  executable location: --with-java=/path/to/java])
AC_ARG_WITH(javac, [  --with-javac override javac executable location: --with-javac=/path/to/javac])

JAVA_DIR=`(cd java && pwd)`
CLASSPATH=$JAVA_DIR
for i in `(cd $JAVA_DIR/jars && ls *.jar)`; do
   CLASSPATH=$CLASSPATH:$JAVA_DIR/jars/$i
done
AC_SUBST(CLASSPATH)

# Checks for programs.
AC_PROG_CC
AC_PROG_MAKE_SET

if test "$with_java" != ""
then
    AC_MSG_NOTICE([Using java: $with_java])
    AC_CHECK_FILE($with_java, JAVA=$with_java,
          [AC_MSG_ERROR([Invalid java path specified: $with_java])])
else
    AC_PATH_PROG(JAVA, java, java-not-found, $PATH:/usr/lib/jvm/java)
    if test "$JAVA" = "java-not-found"
    then
       AC_ERROR([Could not find java])
    fi
fi
AC_SUBST(JAVA)

if test "$with_javac" != ""
then
    AC_MSG_NOTICE([Using javac: $with_javac])
    AC_CHECK_FILE($with_javac, JAVAC=$with_javac,
          [AC_MSG_ERROR([Invalid javac path specified: $with_javac])])
else
    AC_PATH_PROG(JAVAC, javac, javac-not-found, $PATH:/usr/lib/jvm/java)
    if test "$JAVAC" = "javac-not-found"
    then
       AC_ERROR([Could not find javac])
    fi
fi


# Checks for libraries.

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([locale.h stdlib.h string.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST

# Checks for library functions.
AC_FUNC_MALLOC
AC_CHECK_FUNCS([atexit strerror])

AC_CONFIG_FILES( \
  Makefile \
  scripts/Makefile \
  java/Makefile \
  java/gov/llnl/lustre/database/Makefile \
  java/gov/llnl/lustre/lwatch/Makefile \
  java/gov/llnl/lustre/lwatch/util/Makefile \
  java/gov/llnl/lustre/lstat/Makefile \
  java/gov/llnl/lustre/utility/Makefile \
)
AC_CONFIG_FILES([scripts/lwatch], [chmod +x scripts/lwatch])
AC_CONFIG_FILES([scripts/lstat],  [chmod +x scripts/lstat])

AC_OUTPUT

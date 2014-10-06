PROGNAME=${0##*/}
if [ "$1" = "-h" ] || [ $(($#)) -lt 2 ]; then
    echo "$PROGNAME: make dynamic link library"
    echo "Usagd: $PROGNAME [-h] -o dllname[.dll] [-l importlibrary[.dll.a]] \
		[-d deffile ] [-v] [-g|w|i] [-u] [-x] [-s] objects [ldargs] [libs]"
    exit 1
fi

function dumpargs
{
    for dd in "$@"; do
        eval echo "$dd =	\\\"\$$dd\\\""
    done
}

PREFIX=x86_64-w64-mingw32-
ROOT_DIR=/usr/x86_64-w64-mingw32

AS="$(ROOT_DIR)/$(PREFIX)as"
GCC="$(ROOT_DIR)/$(PREFIX)gcc"
GPP="$(ROOT_DIR)/$(PREFIX)g++"
LD="$(ROOT_DIR)/$(PREFIX)ld"
DLLTOOL=dlltool.exe
DLLWRAP=dllwrap.exe
EXPORTALL=""
GCCDLLTOOL=GCC-DLLTOOL
WINDRES=windres.exe
#DEFDRIVER=$LD
DEFDRIVER=$DLLTOOL
OPTVERBOSE="--verbose"
SHOW=
LDFLAGS=" -LD:/Progra~1/GnuWin32/lib "
#LIBS=" -lgw32c -liberty -lintl -liconv -lwsock32 -lole32 -luuid -lmsvcp60 "
LIBS=" -liberty "
while getopts ":d:gil:L:o:psuvwx" opt; do
    case $opt in
        d) DEFNAME="$OPTARG" ;;
        g) DRIVER="$GCCDLLTOOL" ;;
        i) DRIVER="$LD" ;;
		l) LIBNAME="$OPTARG" ;;
		L) LDFLAGS="$LDFLAGS -L$OPTARG" ;;
        o) DLLNAME="$OPTARG"  ;;
        u) GCC="$GPP"  ;;
        s) SHOW="echo"  ;;
        w) DRIVER="$DLLWRAP"  ;;
        v) VERBOSE="$OPTVERBOSE" ;;
        x) EXPORTALL="--export-all-symbols" ;;
        *) OTHEROPTS="$OTHEROPTS $aa";echo $aa;
    esac
done
shift $(($OPTIND -1))
DRIVER=$GCC
#dumpargs GCC DRIVER
#SHOW="echo"
#VERBOSE="$OPTVERBOSE"

#if [ "$GCC" = "$GPP" ] && [ "$EXPORTALL" != " " ] ; then
#	EXPORTALL=" "
#fi
#dumpargs EXPORTALL
if [ "$DEFNAME" = "" ]; then
	DEFNAME="${DLLNAME%.dll}.def"
else
	DEFNAME="${DEFNAME%.def}.def"
	if [ ! -f "$DEFNAME" ]; then
		echo "Definitions file "$DEFNAME" does not exist"
		exit
	fi
	EXPORTALL=""
fi

if [ "$DRIVER" = "" ]; then
	DRIVER=$GCC
fi
#dumpargs DRIVER
if [ "${DEFDRIVER:0:1}" = "g" ]; then
	DDOPT="-Wl,"
else
	DDOPT=""
fi
if [ "${DRIVER:0:1}" = "g" ]; then
	LDOPT="-Wl,"
else
	LDOPT=""
fi

LIBNAME=${LIBNAME:-${DLLNAME%.dll}}
LIBNAME=${LIBNAME%.a}
LIBNAME=${LIBNAME%.dll}
LIBNAME=lib${LIBNAME#lib}
#LIBDLLNAME=$(echo $LIBNAME | sed -e "s/[0-9]*$//")
LIBDLLNAME=$LIBNAME
DLLNAME=${DLLNAME:-$LIBNAME}
DLLNAME=${DLLNAME%.dll}
DLL0NAME=$DLLNAME
if [ "$LIBDLLNAME" = "$LIBNAME" ]; then
	if [ -s "$LIBNAME.la" ]; then
		libla="$LIBNAME.la"
	elif [ -s "../$LIBNAME.la" ]; then
		libla="../$LIBNAME.la"
	else
		libla=
	fi
	if [ -s "Makefile" ]; then
		makefile="Makefile"
	elif [ -s "../Makefile" ]; then
		makefile="../Makefile"
	elif [ -s "GNUmakefile" ]; then
		makefile="GNUmakefile"
	elif [ -s "../GNUmakefile" ]; then
		makefile="../GNUmakefile"
	elif [ -s "makefile.mingw" ]; then
		makefile="makefile.mingw"
	elif [ -s "../makefile.mingw" ]; then
		makefile="../makefile.mingw"
	else
		makefile=
	fi
#	dumpargs makefile
	LTVNUL="-1:-1:-1"
	LTVNNUL="-1.-1.-1"
	ltversinfo="$LTVNUL"
	ltversnum="$LTVNNUL"
#	dumpargs ltversinfo ltversnum
	if [ -s "$libla" ]; then
		current=$(grep "current=" $libla | sed -e "s/current=//")
		age=$(grep "age=" $libla | sed -e "s/age=//")
		revision=$(grep "revision=" $libla | sed -e "s/revision=//")
		ltversinfo="$current:$revision:$age"
	fi
#	dumpargs ltversinfo ltversnum
	if [ -s "$makefile" ] && [ "$ltversinfo" = "$LTVNUL" ] ; then
		current=$(grep "LTV*_CURRENT *= *" $makefile | sed -e "s/LTV*_CURRENT *= *//")
		age=$(grep "LTV*_AGE *= *" $makefile | sed -e "s/LTV*_AGE *= *//")
		revision=$(grep "LTV*_REVISION *= *" $makefile | sed -e "s/LTV*_REVISION *= *//")
		ltversinfo="$current:$revision:$age"
		if [ "$ltversinfo" = "::" ]; then
			ltversinfo=$(grep "version-info" $makefile | sed -e "s/^.*version-info *\([^ ]*\).*$/\1/")
		fi
		if [ "$ltversinfo" = "" ]; then
			ltversinfo="$LTVNUL"
		fi
	fi
#	dumpargs ltversinfo ltversnum
	if [ -s "$makefile" ] && [ "$ltversinfo" = "$LTVNUL" ] ; then
			ltversnum=$(grep "version-number" $makefile | sed -e "s/^.*version-number *\([^ ]*\).*$/\1/")
		if [ "$ltversnum" = "" ]; then
			ltversnum=$(grep "^VERSION" $makefile | sed -e "s/^.*VERSION[ \t]*=* *\([^ ]*\).*$/\1/")
		fi
	fi
#	dumpargs ltversinfo ltversnum
fi

RESDIR=". ./resource ../resource ../../resource ../../../resource .. ../.. ../../.."
for rd in $RESDIR; do
	INCLFLAGS="$INCLFLAGS --include-dir $rd"
done
#INCLFLAGS="--include-dir . --include-dir .. --include-dir ../.. --include-dir ./res --include-dir ../res --include-dir ../../res"
#echo "all: $@"
NEXTARG_LTVERSINFO=FALSE
NEXTARG_LTVERSNUM=FALSE
NEXTARG_OMIT=FALSE
for aa in $@; do
	if [ "$NEXTARG_LTVERSINFO" = "TRUE" ]; then
		ltversinfo="$aa"
		NEXTARG_LTVERSINFO=FALSE
	elif [ "$NEXTARG_LTVERSNUM" = "TRUE" ]; then
		ltversnum="$aa"
		NEXTARG_LTVERSNUM=FALSE
	elif [ "$NEXTARG_OMIT" = "TRUE" ]; then
		NEXTARG_OMIT=FALSE
	else
	    case $aa in
			-version-info) NEXTARG_LTVERSINFO=TRUE ;;
			-version-number) NEXTARG_LTVERSNUM=TRUE ;;
			-no-undefined) ;;
			-release) NEXTARG_OMIT=TRUE;;
			-rpath) NEXTARG_OMIT=TRUE;;
			-export-dynamic) EXPORTALL="$aa";;
			--l) LIBS= ;;
    	    *-rc.o) RESOBJECTS="$RESOBJECTS $aa";;
    	    *-res.o) RESOBJECTS="$RESOBJECTS $aa";;
        	*.lo) LIBOBJECTS="$LIBOBJECTS $aa";;
	        *.o) LIBOBJECTS="$LIBOBJECTS $aa";;
#    	    *.a) LIBS="$LIBS $aa ";;
        	-L*) LDFLAGS="$aa $LDFLAGS";;
	        -l*) LIBS="$LIBS $aa ";;
    	    *.dll) LIBS="$LIBS $aa";;
	        *.a) LIBOBJECTS="$LIBOBJECTS $aa";;
	        *.al) LIBOBJECTS="$LIBOBJECTS $aa";;
        	-I*) INCLFLAGS="--include-dir ${aa#-I} $INCLFLAGS ";;
		    -R*) RESD="${aa#-R}"; RESDIR="$RESD $RESDIR"; INCLFLAGS="--include-dir $RESD $INCLFLAGS ";;
			*)  OTHEROPTS="$OTHEROPTS $aa";;
	    esac
	fi
done

#if [ "$DRIVER" = "$GPP" ]; then
#	LIBS="-lstdc++ -lgcc $LIBS"
#fi
#dumpargs LIBS

LIBOBJECTS0="$LIBOBJECTS"
LIBOBJECTS=
for L in $LIBOBJECTS0; do
	if [ -s "$L" ]; then
		LIBOBJECTS="$LIBOBJECTS $L"
	elif [ -s "../$L" ]; then
		LIBOBJECTS="$LIBOBJECTS ../$L"
	else
		LL="${L%/*}/.libs/${L##*/}"
#		dumpargs LL
		if [ -s "$LL" ]; then
			LIBOBJECTS="$LIBOBJECTS $LL"
		elif [ -s "../$LL" ]; then
			LIBOBJECTS="$LIBOBJECTS ../$LL"
		fi
	fi
done
dumpargs LIBOBJECTS LIBS
#dumpargs INCLFLAGS RESDIR

dumpargs ltversinfo	ltversnum
if [ "$ltversinfo" != "$LTVNUL" ]; then
	ltversion=$ltversinfo
dumpargs ltversion
else if [ "$ltversnum" != "" ]; then
	major=${ltversnum%%.*}
	ltversbuildminor=${ltversnum#*.}
	if [ "$ltversbuildminor" != "$ltversnum" ]; then
		minor=${ltversbuildminor%%.*}
	else
		minor=0
	fi
	ltversbuild=${ltversbuildminor#*.}
	if [ "$ltversbuildminor" != "$ltversbuild" ]; then
		build=${ltversbuild%%.*}
	else
		build=0
	fi
	dumpargs ltversnum major minor build
	current=$((major+build))
	revision=$minor
	age=$build
	ltversion=$current:$revision:$age
fi	fi
current=${ltversion%%:*}
age=${ltversion##*:}
ca=$((current-age))
if [ "$ca" != "0" ]; then
	DLLNAME=${DLLNAME}$ca
fi
echo "$ltversion" > $DLL0NAME-ltversion

if [ -n "$SHOW" ] || [ "$VERBOSE" = "$OPTVERBOSE" ]; then
	dumpargs GCC DEFDRIVER DRIVER LIBNAME LDFLAGS LIBS EXCLLIBS INCLDIRS OTHEROPTS \
		ltversnum major minor build ltversion current revision age
fi

function mkrco
{
    LIBRCO=$DLL0NAME-dll-res.o
	for RD in $RESDIR; do
		LIBRC=$RD/$1-dll-res.rc
	dumpargs RD	LIBRC LIBRCO
    	if [ ! -s "$LIBRC" ]; then
			LIBRC=$RD/$1-dll.rc
		fi
    	if [ ! -s "$LIBRC" ]; then
			LIBRC=$RD/$1.rc
		fi
		if [ -s "$LIBRC" ]; then
			break
		fi
	done
	if [ -s "$LIBRC" ]; then
		version=$(grep "#define VER_FILEVERSION " "$LIBRC" | sed -e "s/#define VER_FILEVERSION \(.*$\)/\1/" )
		major=${version%%,*}
		version=${version#*,}
		minor=${version%%,*}
        echo "Creating resource code $LIBRCO" from "$LIBRC"
        $SHOW $WINDRES $INCLFLAGS -i $LIBRC -o $LIBRCO
#		dumpargs RD LIBRC
    fi
    if [ -s "$LIBRCO" ]; then
        RESOBJECTS="$RESOBJECTS $LIBRCO"
    fi
}

major=1
minor=0
if [ "$RESOBJECTS" != "" ]; then
	for RO in $RESOBJECTS; do
		if [ -s $RO ]; then
			RESOBJECTS=$RO
			break
		fi
	done
fi
if [ "$RESOBJECTS" = "" ]; then
	DLLANAME=$(echo $DLLNAME | sed -e "s/[0-9]*$//")
	rm -f $DLLNAME-res.o $DLLNAME-dll-res.o
	mkrco $DLL0NAME
	if ! [ -s $LIBRCO ]; then
    	mkrco $DLLNAME
	fi
	if ! [ -s $LIBRCO ]; then
    	mkrco $LIBNAME
	fi
	if ! [ -s $LIBRCO ]; then
    	mkrco ${DLLNAME#lib}
	fi
	if ! [ -s $LIBRCO ]; then
    	mkrco ${LIBNAME#lib}
	fi
	if ! [ -s $LIBRCO ]; then
    	mkrco $DLLANAME
	fi
fi
if [ -n "$SHOW" ] || [ "$VERBOSE" = "$OPTVERBOSE" ]; then
		dumpargs RD LIBRC
fi

echo "Using resource object file: $RESOBJECTS"
LIBOBJECTS="$LIBOBJECTS $RESOBJECTS"

DEFNAME="${DEFNAME%.def}"
#if [ "$DRIVER" = "$DLLWRAP" ] || [ "$DRIVER" = "$GCCDLLTOOL" ]; then
	if [ ! -s "$DEFNAME.def" ]; then
		DEFNAME=$DLL0NAME
		echo "Generating definitions file $DEFNAME.def"
		$SHOW $DEFDRIVER $VERBOSE $DDOPT$EXPORTALL \
			$DDOPT--output-def=$DEFNAME.def $LIBOBJECTS
	else
		echo "Using definitions file: $DEFNAME.def"
	fi
#fi

LIBOBJECTS="-Wl,--whole-archive $LIBOBJECTS -Wl,--no-whole-archive"
EXCLSYMBOL="DllMainCRTStartup@12"
DLLTOOOLOPTS="$VERBOSE \
	--exclude-symbol=$EXCLSYMBOL\
	--as=$AS \
	--dllname=$DLLNAME.dll \
	--def=$DEFNAME.def \
	--add-stdcall-alias \
	--compat-implib "
#	--kill-at 
#EXCLLIBS=$(echo "$LIBS " | sed -e "s/-l\([^ ]*\)/lib\1.a/g;s/.a lib/.a,lib/g;s/ //g")
if [ "$major" != "" ] && [ "$minor" != "" ]; then
	IMVERSOPT="$LDOPT--major-image-version=$major \
		$LDOPT--minor-image-version=$minor"
fi
GCCOPTS="$VERBOSE \
	$LDOPT-e,_$EXCLSYMBOL \
	-shared \
	$LDOPT-s \
	$LDOPT--enable-auto-import \
	$LDOPT--enable-runtime-pseudo-reloc
	$LDOPT--enable-stdcall-fixup \
	$LDOPT--add-stdcall-alias \
	$LDOPT--enable-auto-image-base \
	$IMVERSOPT \
	-o $DLLNAME.dll \
	$LDOPT--whole-archive \
	$LIBOBJECTS \
	$OTHEROPTS \
	$LDFLAGS \
	$LDOPT--no-whole-archive \
	$LIBS "
#	$LDOPT--kill-at 
# 	$LDOPT--enable-extra-pe-debug 

for RD in $RESDIR; do
	DEFSED="$RD/${DEFNAME}.sed"
	if [ -s "$DEFSED" ]; then
		break
	fi
	DEFSED="$RD/${DLL0NAME}.sed"
	if [ -s "$DEFSED" ]; then
		break
	fi
done
if [ -s "$DEFSED" ]; then
	sed -i~ -f $DEFSED $DEFNAME.def
fi
if [ "$DRIVER" = "$DLLWRAP" ]; then
	$SHOW $DLLWRAP \
		$VERBOSE \
		--driver-name=$GCC \
		$EXPORTALL \
    	--def=$DLLNAME.def \
		--dllname=$DLLNAME.dll \
		--add-stdcall-alias \
		--implib $LIBNAME.dll.a \
		--enable-auto-image-base \
		--enable-stdcall-fixup \
		--soname=$DLLNAME.dll \
		$OTHEROPTS \
		$LIBOBJECTS \
		$LDFLAGS \
		$LIBS 
# --enable-auto-import 

elif [ "$DRIVER" = "$GCC" ] || [ "$DRIVER" = "$LD" ]; then
dumpargs GCC DRIVER
	echo "Creating dynamic library $DLLNAME.dll and import library $LIBDLLNAME.dll.a"
	if [ -n "$EXPORTALL" ]; then
		EXPORTOPT="$LDOPT$EXPORTALL"
	else
		EXPORTOPT=""
	fi
	$SHOW $DRIVER \
	    $LDOPT--out-implib=$LIBDLLNAME.dll.a \
		$EXPORTOPT \
		$LDOPT-s $GCCOPTS \
		$LDOPT--exclude-libs=ALL \
		$DEFNAME.def 
#		$LDOPT--output-def=$DEFNAME.def 
#	    $LDOPT--output-def=$DEFNAME.def 
#	-Wl,--export-all-symbols -Wl,--enable-auto-image-base 


elif [ "$DRIVER" = "$GCCDLLTOOL" ]; then
#$GCC -mdll -mno-cygwin -Wl,--base-file,$library.base -o $dllfile $GCCargs &&
#$DLLTOOL --as=$AS --dllname $dllfile $defswitch --base-file $library.base --output-exp
#$library.exp $objs &&
#$GCC -mdll -mno-cygwin -Wl,--base-file,$library.base,$library.exp -o $dllfile $GCCargs
#&&
#$DLLTOOL --as=$AS --dllname $dllfile $defswitch --base-file $library.base --output-exp
#$library.exp $objs &&
#$GCC -mdll -mno-cygwin -Wl,$library.exp -o $dllfile $GCCargs &&
#$DLLTOOL --as=$AS --dllname $dllfile $defswitch --output-lib $libname.dll.a $objs
	echo "Creating base file $LIBNAME.base"
	$SHOW $GCC -Wl,--base-file,$LIBNAME.base $GCCOPTS

	echo "Creating export file $LIBNAME.exp"
	$SHOW $DLLTOOL $DLLTOOOLOPTS --base-file $LIBNAME.base \
		--output-exp=$LIBNAME.exp
	
	echo "Creating dynamic library $DLLNAME.dll"
	$SHOW $GCC -Wl,--base-file,$LIBNAME.base,$LIBNAME.exp $GCCOPTS

	echo "Creating export file $LIBNAME.exp"
	$SHOW $DLLTOOL $DLLTOOOLOPTS --base-file=$LIBNAME.base \
		--output-exp=$LIBNAME.exp
	
	echo "Creating dynamic library $DLLNAME.dll"
	$SHOW $GCC $LIBNAME.exp	$GCCOPTS

	echo "Creating dynamic import library $LIBDLLNAME.dll.a"
	$SHOW $DLLTOOL $DLLTOOOLOPTS \
		--output-lib=$LIBDLLNAME.dll.a $LIBOBJECTS

	$SHOW rm -f $LIBNAME.exp $LIBNAME.base

fi

# Build Microsoft and Borland import libraries
$SHOW dll2lib.sh $DLLNAME.dll -l $DLL0NAME -d $DEFNAME.def

#$SHOW strip -p $DLLNAME.dll

#mv -f $LIBNAME-gcc.exp $LIBNAME.exp


# picoGym Level 268: File types
Source: https://play.picoctf.org/practice/challenge/268

## Goal
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.<br>
You can download the file from here.<br>
https://artifacts.picoctf.net/c/80/Flag.pdf

## What I learned
```
cpio: http://ftp.us.debian.org/debian/pool/main/c/cpio/

```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/80/Flag.pdf
--2025-09-16 06:25:23--  https://artifacts.picoctf.net/c/80/Flag.pdf
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.77, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5161 (5.0K) [application/octet-stream]
Saving to: 'Flag.pdf'

Flag.pdf                                                   100%[======================================================================================================================================>]   5.04K  --.-KB/s    in 0s      

2025-09-16 06:25:23 (25.3 MB/s) - 'Flag.pdf' saved [5161/5161]
AsianHacker-picoctf@webshell:~$ file Flag.pdf 
Flag.pdf: shell archive text
AsianHacker-picoctf@webshell:~$ binwalk Flag.pdf 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Executable script, shebang: "/bin/sh"
168           0xA8            Executable script, shebang: "/bin/sh' line above, then type 'sh FILE'."
3029          0xBD5           uuencoded data, file name: "flag", file permissions: "600"

AsianHacker-picoctf@webshell:~$ cat Flag.pdf 
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00046
# Made on 2023-03-16 01:40 UTC by <root@4b9f36a8cccb>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
#
# This shar contains:
# length mode       name
# ------ ---------- ------------------------------------------
#   1092 -rw-r--r-- flag
#
MD5SUM=${MD5SUM-md5sum}
f=`${MD5SUM} --version | egrep '^md5sum .*(core|text)utils'`
test -n "${f}" && md5check=true || md5check=false
${md5check} || \
  echo 'Note: not verifying md5sums.  Consider installing GNU coreutils.'
if test "X$1" = "X-c"
then keep_file=''
else keep_file=true
fi
echo=echo
save_IFS="${IFS}"
IFS="${IFS}:"
gettext_dir=
locale_dir=
set_echo=false

for dir in $PATH
do
  if test -f $dir/gettext \
     && ($dir/gettext --version >/dev/null 2>&1)
  then
    case `$dir/gettext --version 2>&1 | sed 1q` in
      *GNU*) gettext_dir=$dir
      set_echo=true
      break ;;
    esac
  fi
done

if ${set_echo}
then
  set_echo=false
  for dir in $PATH
  do
    if test -f $dir/shar \
       && ($dir/shar --print-text-domain-dir >/dev/null 2>&1)
    then
      locale_dir=`$dir/shar --print-text-domain-dir`
      set_echo=true
      break
    fi
  done

  if ${set_echo}
  then
    TEXTDOMAINDIR=$locale_dir
    export TEXTDOMAINDIR
    TEXTDOMAIN=sharutils
    export TEXTDOMAIN
    echo="$gettext_dir/gettext -s"
  fi
fi
IFS="$save_IFS"
if (echo "testing\c"; echo 1,2,3) | grep c >/dev/null
then if (echo -n test; echo 1,2,3) | grep n >/dev/null
     then shar_n= shar_c='
'
     else shar_n=-n shar_c= ; fi
else shar_n= shar_c='\c' ; fi
f=shar-touch.$$
st1=200112312359.59
st2=123123592001.59
st2tr=123123592001.5 # old SysV 14-char limit
st3=1231235901

if   touch -am -t ${st1} ${f} >/dev/null 2>&1 && \
     test ! -f ${st1} && test -f ${f}; then
  shar_touch='touch -am -t $1$2$3$4$5$6.$7 "$8"'

elif touch -am ${st2} ${f} >/dev/null 2>&1 && \
     test ! -f ${st2} && test ! -f ${st2tr} && test -f ${f}; then
  shar_touch='touch -am $3$4$5$6$1$2.$7 "$8"'

elif touch -am ${st3} ${f} >/dev/null 2>&1 && \
     test ! -f ${st3} && test -f ${f}; then
  shar_touch='touch -am $3$4$5$6$2 "$8"'

else
  shar_touch=:
  echo
  ${echo} 'WARNING: not restoring timestamps.  Consider getting and
installing GNU '\''touch'\'', distributed in GNU coreutils...'
  echo
fi
rm -f ${st1} ${st2} ${st2tr} ${st3} ${f}
#
if test ! -d ${lock_dir} ; then :
else ${echo} "lock directory ${lock_dir} exists"
     exit 1
fi
if mkdir ${lock_dir}
then ${echo} "x - created lock directory ${lock_dir}."
else ${echo} "x - failed to create lock directory ${lock_dir}."
     exit 1
fi
# ============= flag ==============
if test -n "${keep_file}" && test -f 'flag'
then
${echo} "x - SKIPPING flag (file already exists)"

else
${echo} "x - extracting flag (text)"
  sed 's/^X//' << 'SHAR_EOF' | uudecode &&
begin 600 flag
M(3QA<F-H/@IF;&%G+R`@("`@("`@("`@,"`@("`@("`@("`@,"`@("`@,"`@
M("`@-C0T("`@("`Q,#(T("`@("`@8`K'<>H`*9*D@0`````!````$F1_<P4`
M```"`F9L86<``$)::#DQ05DF4UD*74ID```A_____9NJ__XYJ/_]W'___^FW
MWNMM?NG9WO;U_&_Q>]MPZ[`!&M`@:`::``&@--&@`-&C3(T-`:&1B`-#30!H
M-`Q!H,@R::`T,AIZC3`F`&A"!IB&F09,3(#)IH!HR-#0!IID:9#0``TR9,F`
M"8$``#3$8C3(`````93]4VH`-`-`R-`T&0:`&(,C1D,0!D#0:-`:&0:-&@::
M::#0`TTPFC$R9`!H`"`$$`W!"`K($;21@*@-Y!<`I07P=^(Q&$.S;(D(:+IC
MJR+H:!#KK=48KLU*+-7ZOF-'1I0BXSNP!^$:(PXCB"BH1QG7XV66>01(%!'F
MA+TN03:BB\1SO=?KKYD8^A.#MHUSSEV>KSZ$E<,$[]?R$`Y>9=N[@(/ED@;]
M+I<E*@$(62A-G5E4J/X+!1G)YN&+#J%&I3XEP@LCO*'5"621EN&5"8S7XC&'
M2@]'$A#+I1J+J["D+OK9/FF#YP/)A'H0@<YGB7G6JA_JE,.D30#BA<D\Q^;J
M'95'>A@]!V5#&@5_Q[K2:LFH5K'!T(&(@C&@E`Q@F$)9MFCN5.$"-R2:FSK8
M:2L8QG/V#-SK_9H2]/8^,9)#6=3?-02VR+/N,6G%BM)RK<<`5J*;MWPTJ7`V
M8M3?@`/`0<PH^=+GCXI^?W]_B[DBG"A(!2ZE,@#'<0`````````````!````
M``````L``````%1204E,15(A(2$`````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
,````````````````
`
end
SHAR_EOF
  (set 20 23 03 16 01 40 15 'flag'
   eval "${shar_touch}") && \
  chmod 0644 'flag'
if test $? -ne 0
then ${echo} "restore of flag failed"
fi
  if ${md5check}
  then (
       ${MD5SUM} -c >/dev/null 2>&1 || ${echo} 'flag': 'MD5 check failed'
       ) << \SHAR_EOF
5f8b21192765e709f6f67e7dab93d1e5  flag
SHAR_EOF

else
test `LC_ALL=C wc -c < 'flag'` -ne 1092 && \
  ${echo} "restoration warning:  size of 'flag' is not 1092"
  fi
fi
if rm -fr ${lock_dir}
then ${echo} "x - removed lock directory ${lock_dir}."
else ${echo} "x - failed to remove lock directory ${lock_dir}."
     exit 1
fi
exit 0

AsianHacker-picoctf@webshell:~$ chmod +x Flag.pdf
AsianHacker-picoctf@webshell:~$ ./Flag.pdf 
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
AsianHacker-picoctf@webshell:~$ ls
Flag.pdf  README.txt  flag  flag.png
AsianHacker-picoctf@webshell:~$ file flag
flag: current ar archive
AsianHacker-picoctf@webshell:~$ whatis ar
ar (1posix)          - create and maintain library archives
ar (1)               - create, modify, and extract from archives
AsianHacker-picoctf@webshell:~$ ar --help
Usage: ar [emulation options] [-]{dmpqrstx}[abcDfilMNoOPsSTuvV] [--plugin <name>] [member-name] [count] archive-file file...
       ar -M [<mri-script]
 commands:
  d            - delete file(s) from the archive
  m[ab]        - move file(s) in the archive
  p            - print file(s) found in the archive
  q[f]         - quick append file(s) to the archive
  r[ab][f][u]  - replace existing or insert new file(s) into the archive
  s            - act as ranlib
  t[O][v]      - display contents of the archive
  x[o]         - extract file(s) from the archive
 command specific modifiers:
  [a]          - put file(s) after [member-name]
  [b]          - put file(s) before [member-name] (same as [i])
  [D]          - use zero for timestamps and uids/gids (default)
  [U]          - use actual timestamps and uids/gids
  [N]          - use instance [count] of name
  [f]          - truncate inserted file names
  [P]          - use full path names when matching
  [o]          - preserve original dates
  [O]          - display offsets of files in the archive
  [u]          - only replace files that are newer than current archive contents
 generic modifiers:
  [c]          - do not warn if the library had to be created
  [s]          - create an archive index (cf. ranlib)
  [l <text> ]  - specify the dependencies of this library
  [S]          - do not build a symbol table
  [T]          - deprecated, use --thin instead
  [v]          - be verbose
  [V]          - display the version number
  @<file>      - read options from <file>
  --target=BFDNAME - specify the target object format as BFDNAME
  --output=DIRNAME - specify the output directory for extraction operations
  --record-libdeps=<text> - specify the dependencies of this library
  --thin       - make a thin archive
 optional:
  --plugin <p> - load the specified plugin
 emulation options: 
  No emulation specific options
ar: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-l1om elf64-k1om elf64-little elf64-big elf32-little elf32-big pe-bigobj-x86-64 pe-i386 srec symbolsrec verilog tekhex binary ihex plugin
Report bugs to <https://sourceware.org/bugzilla/>

AsianHacker-picoctf@webshell:~$ ar x flag
AsianHacker-picoctf@webshell:~$ file flag
flag: cpio archive
AsianHacker-picoctf@webshell:~$ mv flag Flag
AsianHacker-picoctf@webshell:~$ cpio -i < Flag
-bash: cpio: command not found

# If can’t install software (no sudo) then extract using a downloaded .deb
AsianHacker-picoctf@webshell:~$ wget http://ftp.us.debian.org/debian/pool/main/c/cpio/cpio_2.15+dfsg-2_amd64.deb
--2025-09-16 06:49:09--  http://ftp.us.debian.org/debian/pool/main/c/cpio/cpio_2.15+dfsg-2_amd64.deb
Resolving ftp.us.debian.org (ftp.us.debian.org)... 208.80.154.139, 64.50.236.52, 64.50.233.100, ...
Connecting to ftp.us.debian.org (ftp.us.debian.org)|208.80.154.139|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 252116 (246K) [application/vnd.debian.binary-package]
Saving to: 'cpio_2.15+dfsg-2_amd64.deb'

cpio_2.15+dfsg-2_amd64.deb                                 100%[======================================================================================================================================>] 246.21K  --.-KB/s    in 0.1s    

2025-09-16 06:49:09 (1.62 MB/s) - 'cpio_2.15+dfsg-2_amd64.deb' saved [252116/252116]

AsianHacker-picoctf@webshell:~$ ar x cpio_2.15+dfsg-2_amd64.deb 
AsianHacker-picoctf@webshell:~$ tar -xf data.tar.xz 
AsianHacker-picoctf@webshell:~$ ./usr/bin/cpio --version
./usr/bin/cpio: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found (required by ./usr/bin/cpio)

# Installing cpio didn't work so using python script
GitHub Solution: https://github.com/arvindshima/PicoCTF-2022/blob/main/Forensics/file-types.md ⚠️
```

## Flag

## Continue
[Continue](./picoGym0268.md)
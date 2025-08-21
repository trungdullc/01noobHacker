# picoGym Level 0163: Static ain't always noise
Source: https://play.picoctf.org/practice/challenge/163

## Goal
Can you look at the data in this binary: static? This BASH script might help!

## What I learned
```
bash script of objdump
strings
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static ⌨️
--2025-08-19 13:43:43--  https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8376 (8.2K) [application/octet-stream]
Saving to: 'static'

static                                                     100%[======================================================================================================================================>]   8.18K  --.-KB/s    in 0s      

2025-08-19 13:43:43 (135 MB/s) - 'static' saved [8376/8376]

AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh ⌨️
--2025-08-19 13:44:15--  https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 785 [application/octet-stream]
Saving to: 'ltdis.sh'

ltdis.sh                                                   100%[======================================================================================================================================>]     785  --.-KB/s    in 0s      

2025-08-19 13:44:15 (347 MB/s) - 'ltdis.sh' saved [785/785]
AsianHacker-picoctf@webshell:/tmp$ file static ⌨️
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=bedc412be2156b04706c1f2568fcff42306dea27, not stripped
AsianHacker-picoctf@webshell:/tmp$ chmod +x ltdis.sh ⌨️ 
AsianHacker-picoctf@webshell:/tmp$ cat ltdis.sh ⌨️
#!/bin/bash

echo "Attempting disassembly of $1 ..."

#This usage of "objdump" disassembles all (-D) of the first file given by 
#invoker, but only prints out the ".text" section (-j .text) (only section
#that matters in almost any compiled program...

objdump -Dj .text $1 > $1.ltdis.x86_64.txt

#Check that $1.ltdis.x86_64.txt is non-empty
#Continue if it is, otherwise print error and eject

if [ -s "$1.ltdis.x86_64.txt" ]
then
        echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"

        echo "Ripping strings from binary with file offsets..."
        strings -a -t x $1 > $1.ltdis.strings.txt
        echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"

else
        echo "Disassembly failed!"
        echo "Usage: ltdis.sh <program-file>"
        echo "Bye!"
fi

AsianHacker-picoctf@webshell:/tmp$ ./ltdis.sh ⌨️
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file> 👀
Bye!
AsianHacker-picoctf@webshell:/tmp$ ./ltdis.sh static ⌨️ 
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets..
AsianHacker-picoctf@webshell:/tmp$ cat static.ltdis.strings.txt | grep -e "picoCTF" ⌨️
   1020 picoCTF{d15a5m_t34s3r_f6c48608}
AsianHacker-picoctf@webshell:/tmp$ whatis objdump ⌨️
objdump (1)          - display information from object files

Method 2 (Shortcut, not even use sript):
AsianHacker-picoctf@webshell:/tmp$ strings static | grep -e "picoCTF" ⌨️
picoCTF{d15a5m_t34s3r_f6c48608} 🔐
```

## Flag
picoCTF{d15a5m_t34s3r_f6c48608}

## Continue
[Continue](./picoGym0022.md)
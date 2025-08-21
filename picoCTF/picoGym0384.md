# picoGym Level 0384: useless
Source: https://play.picoctf.org/practice/challenge/384

## Goal
There's an interesting script in the user's home directory<br>
The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.<br>
Hostname: saturn.picoctf.net<br>
Port:     65288<br>
Username: picoplayer<br>
Password: password

## What I learned
```
zcat read gz w/o unzip

man looks in manual directories for a file written in roff/groff markup (plain text with formatting macros)
picoplayer@challenge:/usr/share/man$ type man ⌨️
man is hashed (/usr/bin/man)
picoplayer@challenge:/usr/share/man$ which man ⌨️
/usr/bin/man
picoplayer@challenge:/usr/share/man$ man -w useless ⌨️
/usr/local/man/man1/useless.1.gz
picoplayer@challenge:~$ cd /usr/local/man/man1/ ⌨️
picoplayer@challenge:/usr/local/man/man1$ ls -la | grep "useless" ⌨️
-rw-r--r-- 1 root root 506 Aug  4  2023 useless.1.gz
picoplayer@challenge:/usr/local/man/man1$ file useless.1.gz ⌨️
useless.1.gz: gzip compressed data, was "useless.1", last modified: Fri Aug  4 21:57:24 2023, from Unix, original size modulo 2^32 1002
picoplayer@challenge:/usr/local/man/man1$ zcat useless.1.gz ⌨️

.Dd 24/7/22               \" DATE
.Dt useless 1      \" Program name and manual section number
.Sh useless                 \" Section Header - required - don't modify
.Nm useless,
.Nd This is a simple calculator script
.Sh SYNOPSIS             \" Section Header - required - don't modify
.Nm
.Op add sub mul div              \" [-abcd]
.Ar number1  
.Ar number2  
              
.Sh DESCRIPTION          \" Section Header - required - don't modify
Use the 
.Nm 
macro to make simple calulations like addition,subtraction, multiplication and division.

.Sh Examples               
.Bl -tag -width 
.It Pa ./useless add 1 2
This will add 1 and 2 and return 3

.It Pa ./useless mul 2 3
This will return 6 as a product of 2 and 3

.It Pa ./useless div 6 3
This will return 2 as a quotient of 6 and 3

.It Pa ./useless sub 6 5
This will return 1 as a remainder of substraction of 5 from 6  

.Sh Authors
This script was designed and developed by Cylab Africa
.Pp 
picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823} 🔐

# -------------------- Side Quest: If created a C Program and wanted man --------------------
g++ calculator2.cpp -o calculator2 ⌨️
sudo cp calculator2 /usr/local/bin/ ⌨️                   # install in PATH
# calculator2.1 (.1 means “section 1: user commands”)
.TH CALCULATOR2 1 "August 2025" "v1.0" "User Commands"
.SH NAME
calculator2 \- simple calculator for integers
.SH SYNOPSIS
.B calculator2
[\fBadd\fR|\fBsub\fR|\fBmul\fR|\fBdiv\fR] \fInum1 num2\fR
.SH DESCRIPTION
.B calculator2
is a basic command-line calculator that performs addition, subtraction,
multiplication, and division on two integers.
.SH EXAMPLES
Run:
.IP
calculator2 add 2 3
.PP
Outputs:
.IP
Sum: 5
.SH AUTHOR
Written by You.

# Copy it to the right location & compress it
sudo cp calculator2.1 /usr/local/man/man1/ ⌨️
sudo gzip /usr/local/man/man1/calculator2.1 ⌨️

# Update man cache
sudo mandb ⌨️

# Test it
man calculator2 ⌨️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh picoplayer@saturn.picoctf.net -p 65288 ⌨️
The authenticity of host '[saturn.picoctf.net]:65288 ([13.59.203.175]:65288)' can't be established.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[saturn.picoctf.net]:65288' (ED25519) to the list of known hosts.
picoplayer@saturn.picoctf.net's password: ⌨️
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

picoplayer@challenge:~$ ls -la ⌨️
total 16
drwxr-xr-x 1 picoplayer picoplayer   20 Aug 20 00:05 .
drwxr-xr-x 1 root       root         24 Aug  4  2023 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Aug 20 00:05 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
-rwxr-xr-x 1 root       root        517 Mar 16  2023 useless
picoplayer@challenge:~$ file useless ⌨️
useless: Bourne-Again shell script, ASCII text executable
picoplayer@challenge:~$ ./useless ⌨️
Read the code first
picoplayer@challenge:~$ cat useless ⌨️ 
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
        if [[ "$1" == "add" ]]
        then 
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"  

        elif [[ "$1" == "sub" ]]
        then 
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub" 

        elif [[ "$1" == "div" ]]
        then 
          div=$(( $2 / $3 ))
          echo "The quotient is: $div" 

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul" 

        else
          echo "Read the manual" 👀
         
        fi
fi
picoplayer@challenge:~$ ./useless add 2 4 ⌨️
The Sum is: 6
picoplayer@challenge:~$ man useless ⌨️

useless
     useless, -- This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtraction, multiplication and division.

Examples
     ./useless add 1 2
       This will add 1 and 2 and return 3

     ./useless mul 2 3
       This will return 6 as a product of 2 and 3

     ./useless div 6 3
       This will return 2 as a quotient of 6 and 3

     ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823} 🔐
```

## Flag
picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_3823} 

## Continue
[Continue](./picoGym0363.md)
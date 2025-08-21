# picoGym Level 0037: strings it
Source: https://play.picoctf.org/practice/challenge/37

## Goal
Can you find the flag in file without running it?

## What I learned
```
strings
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings ⌨️
--2025-08-19 12:42:54--  https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 776032 (758K) [application/octet-stream]
Saving to: 'strings'

strings                                                    100%[======================================================================================================================================>] 757.84K  1.87MB/s    in 0.4s    

2025-08-19 12:42:54 (1.87 MB/s) - 'strings' saved [776032/776032]

AsianHacker-picoctf@webshell:/tmp$ file strings ⌨️
strings: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=0cdedfba33422d235dba8c90e00fb77b235f1ff8, not stripped
AsianHacker-picoctf@webshell:/tmp$ ls -la strings ⌨️
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 776032 Oct 26  2020 strings
AsianHacker-picoctf@webshell:/tmp$ whatis strings ⌨️
strings (1posix)     - find printable strings in files
strings (1)          - print the sequences of printable characters in files
AsianHacker-picoctf@webshell:/tmp$ strings strings | grep -e "picoCTF" ⌨️
picoCTF{5tRIng5_1T_7f766a23} 🔐

# Curious
AsianHacker-picoctf@webshell:/tmp$ chmod +x strings ⌨️
AsianHacker-picoctf@webshell:/tmp$ ./strings ⌨️
Maybe try the 'strings' function? Take a look at the man page
AsianHacker-picoctf@webshell:/tmp$ rm strings ⌨️
```

## Flag
picoCTF{5tRIng5_1T_7f766a23}

## Continue
[Continue](./picoGym0034.md)
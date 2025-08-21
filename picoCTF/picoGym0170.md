# picoGym Level 0170: Wave a flag
Source: https://play.picoctf.org/practice/challenge/170

## Goal
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

## What I learned
```
chmod
strings
gdb
ltrace not on picoCTF
gef not on picoCTF
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm ⌨️
--2025-08-19 00:03:43--  https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10936 (11K) [application/octet-stream]
Saving to: 'warm'

warm                                                       100%[======================================================================================================================================>]  10.68K  --.-KB/s    in 0s      

2025-08-19 00:03:43 (94.9 MB/s) - 'warm' saved [10936/10936]

AsianHacker-picoctf@webshell:/tmp$ file warm ⌨️
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3aa19b2a9cc4e093d64025eab8f510679b523455, with debug_info, not stripped
AsianHacker-picoctf@webshell:/tmp$ ./warm ⌨️
-bash: ./warm: Permission denied 👀
AsianHacker-picoctf@webshell:/tmp$ ls -la warm ⌨️
-rw-rw-r--👀 1 AsianHacker-picoctf AsianHacker-picoctf 10936 Mar 16  2021 warm
AsianHacker-picoctf@webshell:/tmp$ strings ./warm | grep "CTF" ⌨️
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_30e77291} 🔐

# Method 2: Didn't see it, was wondering why Permission denied (execute is off)
AsianHacker-picoctf@webshell:/tmp$ chmod +x warm ⌨️
AsianHacker-picoctf@webshell:/tmp$ ./warm ⌨️
Hello user! Pass me a -h to learn what I can do!
AsianHacker-picoctf@webshell:/tmp$ ./warm -h ⌨️
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_30e77291} 🔐
```

## Flag
picoCTF{b1scu1ts_4nd_gr4vy_30e77291}

## Continue
[Continue](./picoGym0414.md)
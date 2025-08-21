# picoGym Level 0189: Magikarp Ground Mission
Source: https://play.picoctf.org/practice/challenge/189

## Goal
Password: <b>abcba9f7</b><br>
<b>ssh ctf-player@venus.picoctf.net -p 54124</b>

## What I learned
```
man ssh
man cat
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh ctf-player@venus.picoctf.net -p 54124 ⌨️
The authenticity of host '[venus.picoctf.net]:54124 ([3.131.124.143]:54124)' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[venus.picoctf.net]:54124' (ED25519) to the list of known hosts.
ctf-player@venus.picoctf.net's password: ⌨️
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1103-aws x86_64)
ctf-player@pico-chall$ whoami ⌨️
ctf-player
ctf-player@pico-chall$ id ⌨️
uid=1000(ctf-player) gid=1000(ctf-player) groups=1000(ctf-player)
ctf-player@pico-chall$ cat /etc/shells ⌨️
# /etc/shells: valid login shells
/bin/sh
/bin/bash
/bin/rbash
/bin/dash
ctf-player@pico-chall$ ls -la ⌨️
total 16
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 .
drwxr-xr-x 1 ctf-player ctf-player 4096 Aug 17 02:40 ..
-rw-r--r-- 1 ctf-player ctf-player   14 Mar 16  2021 1of3.flag.txt 👀
-rw-r--r-- 1 ctf-player ctf-player   56 Mar 16  2021 instructions-to-2of3.txt 👀
ctf-player@pico-chall$ cat 1of3.flag.txt ⌨️
picoCTF{xxsh_ 🔐
ctf-player@pico-chall$ file instructions-to-2of3.txt ⌨️ 
instructions-to-2of3.txt: ASCII text
ctf-player@pico-chall$ cat instructions-to-2of3.txt ⌨️
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cd / ⌨️
ctf-player@pico-chall$ pwd ⌨️
/
ctf-player@pico-chall$ ls -la ⌨️
total 92
drwxr-xr-x   1 root root 4096 Aug 17 02:35 .
drwxr-xr-x   1 root root 4096 Aug 17 02:35 ..
-rwxr-xr-x   1 root root    0 Aug 17 02:35 .dockerenv
-rw-r--r--   1 root root   17 Mar 16  2021 2of3.flag.txt 👀
drwxr-xr-x   1 root root 4096 Mar 16  2021 bin
drwxr-xr-x   2 root root 4096 Apr 24  2018 boot
drwxr-xr-x   5 root root  340 Aug 17 02:35 dev
drwxr-xr-x   1 root root 4096 Aug 17 02:35 etc
drwxr-xr-x   1 root root 4096 Mar 16  2021 home
-rw-r--r--   1 root root   51 Mar 16  2021 instructions-to-3of3.txt 👀
drwxr-xr-x   1 root root 4096 Mar 16  2021 lib
drwxr-xr-x   2 root root 4096 Feb 22  2021 lib64
drwxr-xr-x   2 root root 4096 Feb 22  2021 media
drwxr-xr-x   2 root root 4096 Feb 22  2021 mnt
drwxr-xr-x   1 root root 4096 Mar 16  2021 opt
dr-xr-xr-x 188 root root    0 Aug 17 02:35 proc
drwx------   2 root root 4096 Feb 22  2021 root
drwxr-xr-x   1 root root 4096 Aug 17 02:40 run
drwxr-xr-x   1 root root 4096 Mar 16  2021 sbin
drwxr-xr-x   2 root root 4096 Feb 22  2021 srv
dr-xr-xr-x  13 root root    0 Aug 17 02:35 sys
drwxrwxrwt   1 root root 4096 Mar 16  2021 tmp
drwxr-xr-x   1 root root 4096 Feb 22  2021 usr
drwxr-xr-x   1 root root 4096 Feb 22  2021 var
ctf-player@pico-chall$ cat 2of3.flag.txt ⌨️
0ut_0f_\/\/4t3r_ 🔐
ctf-player@pico-chall$ cat instructions-to-3of3.txt ⌨️ 
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ cd ~ ⌨️
ctf-player@pico-chall$ pwd ⌨️
/home/ctf-player
ctf-player@pico-chall$ ls -la ⌨️
total 32
drwxr-xr-x 1 ctf-player ctf-player 4096 Aug 17 02:40 .
drwxr-xr-x 1 root       root       4096 Mar 16  2021 ..
drwx------ 2 ctf-player ctf-player 4096 Aug 17 02:40 .cache
-rw-r--r-- 1 ctf-player ctf-player   80 Mar 16  2021 .profile
drw------- 1 ctf-player ctf-player 4096 Mar 16  2021 .ssh
-rw-r--r-- 1 ctf-player ctf-player   10 Mar 16  2021 3of3.flag.txt 👀
drwxr-xr-x 1 ctf-player ctf-player 4096 Mar 16  2021 drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt ⌨️
21cac893} 
```

## Flag
picoCTF{xxsh_0ut_0f_\/\/4t3r_21cac893} 🔐

## Continue
[Continue](./picoGym0085.md)
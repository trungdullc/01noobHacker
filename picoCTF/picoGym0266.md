# picoGym Level 266: file-run1
Source: https://play.picoctf.org/practice/challenge/266

## Goal
A program has been provided to you, what happens if you try to run it on the command line?<br>
Download the program here.<br>
https://artifacts.picoctf.net/c/220/run

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/220/run ⌨️
--2025-09-29 22:45:52--  https://artifacts.picoctf.net/c/220/run
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.18, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16736 (16K) [application/octet-stream]
Saving to: 'run'

run                                                        100%[======================================================================================================================================>]  16.34K  --.-KB/s    in 0s      

2025-09-29 22:45:52 (109 MB/s) - 'run' saved [16736/16736]

AsianHacker-picoctf@webshell:~$ file run ⌨️
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4d8e230e54db29e0879e7ed9f2b2231eb8c60032, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ ls -la run ⌨️
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 16736 Mar 16  2023 run
AsianHacker-picoctf@webshell:~$ chmod u+x run ⌨️ 
AsianHacker-picoctf@webshell:~$ ./run ⌨️
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b} 🔐
```

## Flag
picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b}

## Continue
[Continue](./picoGym0267.md)
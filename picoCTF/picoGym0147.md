# picoGym Level 0147: Obedient Cat
Source: https://play.picoctf.org/practice/challenge/147

## Goal
This file has a flag in plain sight (aka "in-the-clear")

## What I learned
```
cat
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag ⌨️
--2025-08-19 13:38:13--  https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: 'flag'

flag                                                       100%[======================================================================================================================================>]      34  --.-KB/s    in 0s      

2025-08-19 13:38:14 (11.0 MB/s) - 'flag' saved [34/34]

AsianHacker-picoctf@webshell:/tmp$ file flag ⌨️
flag: ASCII text
AsianHacker-picoctf@webshell:/tmp$ ls -la flag ⌨️
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 34 Mar 16  2021 flag
AsianHacker-picoctf@webshell:/tmp$ whatis cat ⌨️
cat (1)              - concatenate files and print on the standard output
cat (1posix)         - concatenate and print files
AsianHacker-picoctf@webshell:/tmp$ cat flag ⌨️
picoCTF{s4n1ty_v3r1f13d_2fd6ed29} 🔐
```

## Flag
picoCTF{s4n1ty_v3r1f13d_2fd6ed29}

## Continue
[Continue](./picoGym0163.md)
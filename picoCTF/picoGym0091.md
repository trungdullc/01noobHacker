# picoGym Level 0091: Nothing Up My Sleeve
Source: https://play.picoctf.org/practice/challenge/91

## Goal
Let's check that your internet connection is working. This flag is 'in-the-clear', I promise!<br>
Download flag.txt

## What I learned
```
wget 
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:wget https://challenge-files.picoctf.net/c_shape_facility/c5ab744ff8f3427937ae8fc486a7466d4cedb74e4aa7c30919130e94c44b183a/flag.txt ⌨️
--2025-08-20 13:40:59--  https://challenge-files.picoctf.net/c_shape_facility/c5ab744ff8f3427937ae8fc486a7466d4cedb74e4aa7c30919130e94c44b183a/flag.txt
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.40, 3.160.5.18, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.40|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 32 [application/octet-stream]
Saving to: 'flag.txt'

flag.txt                                                   100%[======================================================================================================================================>]      32  --.-KB/s    in 0s      

2025-08-20 13:40:59 (10.9 MB/s) - 'flag.txt' saved [32/32]

AsianHacker-picoctf@webshell:~$ cat flag.txt ⌨️
picoCTF{c0ngr4ts_0n_y0ur_s4n1ty} 🔐
```

## Flag
picoCTF{c0ngr4ts_0n_y0ur_s4n1ty}

## Continue
[Continue](./picoGym0049.md)
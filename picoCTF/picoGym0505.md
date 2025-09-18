# picoGym Level 505: DISKO 1
Source: https://play.picoctf.org/practice/challenge/505

## Goal
Can you find the flag in this disk image?<br>
Download the disk image here<br>
https://artifacts.picoctf.net/c/536/disko-1.dd.gz

## What I learned
```
strings

sleuthkit
    srch_strings
    mmls
    fls
    dd
    icat

Autopsy
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/536/disko-1.dd.gz ⌨️
--2025-09-15 21:27:49--  https://artifacts.picoctf.net/c/536/disko-1.dd.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.77, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 20484476 (20M) [application/octet-stream]
Saving to: 'disko-1.dd.gz'

disko-1.dd.gz                                              100%[======================================================================================================================================>]  19.54M  1.82MB/s    in 11s     

2025-09-15 21:28:00 (1.82 MB/s) - 'disko-1.dd.gz' saved [20484476/20484476]

AsianHacker-picoctf@webshell:~$ gunzip disko-1.dd.gz ⌨️
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  disko-1.dd

AsianHacker-picoctf@webshell:~$ file disko-1.dd ⌨️
disko-1.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat", Media descriptor 0xf8, sectors/track 32, heads 8, sectors 102400 (volumes > 32 MB), FAT (32 bit), sectors/FAT 788, serial number 0x241a4420, unlabeled

# Method 1: strings
AsianHacker-picoctf@webshell:~$ strings disko-1.dd | grep "picoCTF" ⌨️
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef} 🔐

# Method 2: srch_strings utility from sleuthkit
AsianHacker-picoctf@webshell:~$ srch_strings disko-1.dd | grep picoCTF ⌨️
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef} 🔐
```

## Flag
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}

## Continue
[Continue](./picoGym0506.md)
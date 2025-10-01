# picoGym Level 421: packer
Source: https://play.picoctf.org/practice/challenge/421

## Goal
Reverse this linux executable?<br>
binary<br>
https://artifacts.picoctf.net/c_titan/21/out

## What I learned
```
Reverse Engineering
UPX
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/21/out ⌨️
--2025-09-30 03:24:33--  https://artifacts.picoctf.net/c_titan/21/out
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.33, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 336520 (329K) [application/octet-stream]
Saving to: 'out'

out                                                        100%[======================================================================================================================================>] 328.63K  1.86MB/s    in 0.2s    

2025-09-30 03:24:33 (1.86 MB/s) - 'out' saved [336520/336520]

AsianHacker-picoctf@webshell:~$ file out ⌨️
out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
AsianHacker-picoctf@webshell:~$ chmod u+x out ⌨️ 
AsianHacker-picoctf@webshell:~$ strings out | grep picoCTF{ ⌨️
AsianHacker-picoctf@webshell:~$ strings -n 8 out ⌨️
AWAVAUATUS
7069636fH
4354467b
65539585
Enter the password
o unlock,is file: 
lagX7069636f4354467b5539585f
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $ 👀
/proc/self/exe

AsianHacker-picoctf@webshell:~$ upx -d out -o out_unpacked ⌨️⭐⭐⭐⭐⭐
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    872088 <-    336520   38.59%   linux/amd64   out_unpacked

Unpacked 1 file.

AsianHacker-picoctf@webshell:~$ strings -n 12 out_unpacked | tr -d '\n' | grep -o -P 'password.{0,250}' ⌨️
password to unlock this file: You entered: %sPassword correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d 👀Access denied../csu/libc-start.cFATAL: kernel too old__ehdr_start.e_phentsize == sizeof *GL(dl_phd
AsianHacker-picoctf@webshell:~$ strings out_unpacked | grep flag ⌨️
Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d 👀
(mode_flags & PRINTF_FORTIFY) != 0
WARNING: Unsupported flag value(s) of 0x%x in DT_FLAGS_1.
version == NULL || !(flags & DL_LOOKUP_RETURN_NEWEST)
flag.c
_dl_x86_hwcap_flags
_dl_stack_flags

AsianHacker-picoctf@webshell:~$ python -c "print(bytes.fromhex('7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d'))" ⌨️
b'picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_371aa9ff}' 🔐
AsianHacker-picoctf@webshell:~$ echo '7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d' | xxd -r -p ⌨️
picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_371aa9ff} 🔐
https://cyberchef.io/#recipe=From_Hex('Auto')&input=NzA2OTYzNmY0MzU0NDY3YjU1Mzk1ODVmNTU2ZTUwMzQ2MzZiMzE0ZTM2NWY0MjMxNmUzNDUyNjkzMzUzNWYzMzM3MzE2MTYxMzk2NjY2N2Q
```

## Flag
picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_371aa9ff}

## Continue
[Continue](./picoGym0451.md)
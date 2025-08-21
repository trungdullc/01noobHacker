# picoGym Level 0176: Tab, Tab, Attack
Source: https://play.picoctf.org/practice/challenge/176

## Goal
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames

## What I learned
```
tab in terminal
tab + tab
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip ⌨️
--2025-08-18 23:57:12--  https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4520 (4.4K) [application/octet-stream]
Saving to: 'Addadshashanammu.zip'

Addadshashanammu.zip                                       100%[======================================================================================================================================>]   4.41K  --.-KB/s    in 0s      

2025-08-18 23:57:12 (1.83 GB/s) - 'Addadshashanammu.zip' saved [4520/4520]

AsianHacker-picoctf@webshell:/tmp$ unzip Addadshashanammu.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/ ⌨️
AsianHacker-picoctf@webshell:/tmp/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ ls ⌨️
fang-of-haynekhtnamet
AsianHacker-picoctf@webshell:/tmp/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ file ⌨️fang-of-haynekhtnamet 
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=e34ce4e4ee2f7ce7fb251c8f5ab036da9882bc55, not stripped
AsianHacker-picoctf@webshell:/tmp/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ ./fang-of-haynekhtnamet ⌨️
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4} 🔐
```

## Flag
picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}

## Continue
[Continue](./picoGym0170.md)
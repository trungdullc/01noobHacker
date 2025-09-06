# picoGym Level 418: interencdec
Source: https://play.picoctf.org/practice/challenge/418

## Goal
Can you get the real meaning from this file<br>
Download the file here: https://artifacts.picoctf.net/c_titan/109/enc_flag

## What I learned
```
base64
ROT7
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c_titan/109/enc_flag ⌨️
--2025-09-04 06:42:36--  https://artifacts.picoctf.net/c_titan/109/enc_flag
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 73 [application/octet-stream]
Saving to: 'enc_flag'

enc_flag                                                   100%[======================================================================================================================================>]      73  --.-KB/s    in 0s      

2025-09-04 06:42:36 (2.35 MB/s) - 'enc_flag' saved [73/73]

AsianHacker-picoctf@webshell:/tmp$ file enc_flag ⌨️
enc_flag: ASCII text
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag ⌨️
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyMHdNakV5TnpVNGZRPT0nCg== 👀

# Identify: https://www.dcode.fr/cipher-identifier ⭐⭐⭐
  Base64 Coding 👀

# CyberChef
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',false)&input=WWlka00wSnhaR3R3UWxSWWRIRmhSM2cyWVVoc1ptRjZUbkZsVkd3eldWUk9jbGd5TUhkTmFrVjVUbnBWTkdaUlBUMG5DZz09 ⌨️
  b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ=='
# Replace input with output and remove b ' ' and base64
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=ZDNCcWRrcEJUWHRxYUd4NmFIbGZhek5xZVRsM1lUTnJYMjB3TWpFeU56VTRmUT09 ⌨️
  wpjvJAM{jhlzhy_k3jy9wa3k_m0212758} 👀

# Identify: https://www.dcode.fr/cipher-identifier ⭐⭐⭐
  ROT Cipher	
  Caesar Cipher

# Browser: https://www.dcode.fr/rot-cipher ⌨️
Alphabet to use
ABCDEFGHIJKLMNOPQRSTUVWXYZ (Rot13 / Caesar)
[A-Z]+7	picoCTF{caesar_d3cr9pt3d_f0212758} 🔐

# Browser: https://www.dcode.fr/caesar-cipher ⌨️
Shift/Key (number): 7
Use the English alphabet (26 letters from A to Z)

RESULTS
Caesar Cipher - Shift by 7
H,I,J,K,L,M,…F,G
A,B,C,D,E,F,…Y,Z
🠞7 (🠜19)	picoCTF{caesar_d3cr9pt3d_f0212758} 🔐

# Looks like ROT7
```

## Flag
picoCTF{caesar_d3cr9pt3d_f0212758}

## Continue
[Continue](./picoGym0475.md)
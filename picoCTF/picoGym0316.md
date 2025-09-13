# picoGym Level 316: Vigenere
Source: https://play.picoctf.org/practice/challenge/316

## Goal
Can you decrypt this message?<br>
Decrypt this message using this key "CYLAB"<br>
https://artifacts.picoctf.net/c/159/cipher.txt

## What I learned
```
https://www.boxentriq.com/code-breaking/vigenere-cipher

Vigenère cipher, the shift depends on the letters of a repeated keyword

Decrypt
Find Key Row on Left, Find Cipher text letter, See what column letter associated w/ it (Plaintext)
Encrpyt
Find Column (Plaintext), Find Key Row, Intersection is cyphertext

Youtube Solution: https://www.youtube.com/watch?v=8AhAL1JRctY (Watch if have time)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/159/cipher.txt ⌨️
--2025-09-08 21:55:23--  https://artifacts.picoctf.net/c/159/cipher.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 43 [application/octet-stream]
Saving to: 'cipher.txt'

cipher.txt                                                 100%[======================================================================================================================================>]      43  --.-KB/s    in 0s      

2025-09-08 21:55:23 (44.2 MB/s) - 'cipher.txt' saved [43/43]

AsianHacker-picoctf@webshell:/tmp$ ⌨️ cat cipher.txt 
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}

# Method 1: https://www.dcode.fr/vigenere-cipher

Vigenere Decoder
Vigenere ciphertext
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7} ⌨️
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ ⌨️

Knowing the Key/Password:
CYLAB ⌨️

RESULTS: picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7} 🔐

https://www.boxentriq.com/code-breaking/vigenere-cipher
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7} 🔐
```

## Flag
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}

## Continue
[Continue](./picoGym0373.md)
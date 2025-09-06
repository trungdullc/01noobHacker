# picoGym Level 254: basic-mod2
Source: https://play.picoctf.org/practice/challenge/254

## Goal
A new modular challenge! Download the message here:<br>
https://artifacts.picoctf.net/c/180/message.txt<br>
Take each number mod 41 and find the modular inverse for the result<br>
Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore<br>
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## What I learned
```
Note: Read instructions carefully not start w/ 0 ⚠️

a mod m is an integer x such that:
    integers : a and m
    multiply a by x and divide by m, the remainder is 1 👀
    a ⋅ x ≡ 1 (mod m)
    x = a^(−1) * mod m

Example: modular inverse of 3 modulo 11
    3 ⋅ x ≡ 1 (mod 11)
    Try x = 4
    (3 ⋅ 4) (mod 11) == 1? if equal 1 then correct modular inverse

ChatGpt: Modular multiplicative inverse how to solve with python
a = 3
m = 11

x = pow(a, -1, m) 👀
print(x)                # Output: 4

Online Solver: https://www.dcode.fr/modular-inverse ⭐⭐⭐⭐⭐
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/180/message.txt ⌨️
--2025-09-05 23:27:11--  https://artifacts.picoctf.net/c/180/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 89 [application/octet-stream]
Saving to: 'message.txt'

message.txt                                                100%[======================================================================================================================================>]      89  --.-KB/s    in 0s      

2025-09-05 23:27:11 (24.0 MB/s) - 'message.txt' saved [89/89]

AsianHacker-picoctf@webshell:~$ cat message.txt ⌨️
268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131 👀

# Method 1: Brute Force w/ python
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
numbers = [268, 413, 438, 313, 426, 337, 272, 188, 392, 338, 77, 332, 139, 113, 92, 239, 247, 120, 419, 72, 295, 190, 131]
encoding = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_')

# Source: https://www.geeksforgeeks.org/dsa/multiplicative-inverse-under-modulo-m/
def modInverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

if __name__ == "__main__":
    M = 41
    enc_flag: list = []

    # Modify number list w/ inverse mod
    for A in numbers: 
        # print(modInverse(A, M), end=" ")
        enc_flag.append(modInverse(A, M))
    
    # print(enc_flag)
    # [28, 14, 22, 30, 18, 32, 30, 12, 25, 37, 8, 31, 18, 4, 37, 35, 1, 27, 32, 4, 36, 30, 36]

    # this part not map correctly
    for x in enc_flag:
        print(encoding[x % len(encoding)], end="")
    print()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
1NV3R53LY_H4RD_8A05D939 🔐

Method 2: Solve w/ power parameters
from string import ascii_uppercase ❤️
numbers = [268, 413, 438, 313, 426, 337, 272, 188, 392, 338, 77, 332, 139, 113, 92, 239, 247, 120, 419, 72, 295, 190, 131]

encoding = "0" + ascii_uppercase + "0123456789_" ❤️❤️❤️❤️❤️

for i in numbers:
    print(encoding[pow(i, -1, 41)], end="") 👀

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
1NV3R53LY_H4RD_8A05D939 🔐
```

## Flag
picoCTF{1NV3R53LY_H4RD_8A05D939}

## Continue
[Continue](./picoGym0280.md)
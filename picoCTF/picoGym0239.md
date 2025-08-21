# picoGym Level 0239: convertme.py
Source: https://play.picoctf.org/practice/challenge/239

## Goal
Run the Python script and convert the given number from decimal to binary to get the flag

## What I learned
```
CyberChef
python3 bin() ❤️                         print(int("1001011", 2)) ❤️
python3 hex() ❤️                         print(int("0x4b", 16)) ❤️
                                          print(int("4b", 16))
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/23/convertme.py ⌨️
--2025-08-18 23:40:16--  https://artifacts.picoctf.net/c/23/convertme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.92, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1189 (1.2K) [application/octet-stream]
Saving to: 'convertme.py'

convertme.py                                               100%[======================================================================================================================================>]   1.16K  --.-KB/s    in 0s      

2025-08-18 23:40:16 (594 MB/s) - 'convertme.py' saved [1189/1189]

AsianHacker-picoctf@webshell:/tmp$ cat convertme.py ⌨️
import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x4c) + chr(0x06) + chr(0x5d) + chr(0x09) + chr(0x5e) + chr(0x00) + chr(0x41) + chr(0x01) + chr(0x13)

num = random.choice(range(10,101))

print('If ' + str(num) + ' is in decimal base, what is it in binary base?')

ans = input('Answer: ')

try:
  ans_num = int(ans, base=2)
  
  if ans_num == num:
    flag = str_xor(flag_enc, 'enkidu')
    print('That is correct! Here\'s your flag: ' + flag)
  else:
    print(str(ans_num) + ' and ' + str(num) + ' are not equal.')
  
except ValueError:
  print('That isn\'t a binary number. Binary numbers contain only 1\'s and 0\'s')

AsianHacker-picoctf@webshell:/tmp$ python3 convertme.py ⌨️ 
If 75 is in decimal base, what is it in binary base? 
Answer: 1001011 ⌨️
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_9c3b7d4d} 🔐

AsianHacker-picoctf@webshell:/tmp$ python3 -c "print(bin(75))" ⌨️
0b1001011 👀
```

## Flag
picoCTF{4ll_y0ur_b4535_9c3b7d4d}

## Continue
[Continue](./picoGym0176.md)
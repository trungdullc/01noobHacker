# picoGym Level 0240: fixme1.py
Source: https://play.picoctf.org/practice/challenge/240

## Goal
Fix the syntax error in this Python script to print the flag

## What I learned
```
python3 space is important
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/26/fixme1.py ⌨️
--2025-08-18 23:19:59--  https://artifacts.picoctf.net/c/26/fixme1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.92, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 837 [application/octet-stream]
Saving to: 'fixme1.py'

fixme1.py                                                  100%[======================================================================================================================================>]     837  --.-KB/s    in 0s      

2025-08-18 23:19:59 (806 MB/s) - 'fixme1.py' saved [837/837]

AsianHacker-picoctf@webshell:/tmp$ cat fixme1.py ⌨️
import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) + chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) + chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x5e) + chr(0x52) + chr(0x0c) + chr(0x01) + chr(0x42) + chr(0x57) + chr(0x59) + chr(0x0a) + chr(0x14)
  
flag = str_xor(flag_enc, 'enkidu')
  print('That is correct! Here\'s your flag: ' + flag)

# Run it to find where error is vs looking thru all lines
AsianHacker-picoctf@webshell:/tmp$ python3 fixme1.py ⌨️
  File "/tmp/fixme1.py", line 20 👀
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent 👀

# Fix: rm indent from line :20 w/ vi
AsianHacker-picoctf@webshell:/tmp$ vi fixme1.py ⌨️ 
AsianHacker-picoctf@webshell:/tmp$ python3 fixme1.py ⌨️ 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a} 🔐
```

## Flag
picoCTF{1nd3nt1ty_cr1515_09ee727a}

## Continue
[Continue](./picoGym0241.md)
# picoGym Level 287: patchme.py
Source: https://play.picoctf.org/practice/challenge/287

## Goal
Can you get the flag?<br>
Run this Python program in the same directory as this encrypted flag.<br>
https://artifacts.picoctf.net/c/202/patchme.flag.py<br>
https://artifacts.picoctf.net/c/202/flag.txt.enc

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/202/patchme.flag.py https://artifacts.picoctf.net/c/202/flag.txt.enc ⌨️
--2025-09-26 23:03:59--  https://artifacts.picoctf.net/c/202/patchme.flag.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 980 [application/octet-stream]
Saving to: 'patchme.flag.py'

patchme.flag.py                                            100%[======================================================================================================================================>]     980  --.-KB/s    in 0s      

2025-09-26 23:03:59 (441 MB/s) - 'patchme.flag.py' saved [980/980]

--2025-09-26 23:03:59--  https://artifacts.picoctf.net/c/202/flag.txt.enc
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 36 [application/octet-stream]
Saving to: 'flag.txt.enc'

flag.txt.enc                                               100%[======================================================================================================================================>]      36  --.-KB/s    in 0s      

2025-09-26 23:03:59 (11.8 MB/s) - 'flag.txt.enc' saved [36/36]

FINISHED --2025-09-26 23:03:59--
Total wall clock time: 0.2s
Downloaded: 2 files, 1016 in 0s (193 MB/s)
AsianHacker-picoctf@webshell:~$ file flag.txt.enc ⌨️
flag.txt.enc: data
AsianHacker-picoctf@webshell:~$ cat flag.txt.enc ⌨️

CR1@    UYX+
6FP_S
     FG
AsianHacker-picoctf@webshell:~$ cat patchme.flag.py ⌨️ 
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    # extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('flag.txt.enc', 'rb').read()

def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \ 👀
                   "-=90" + \ 👀
                   "adfjhgj321" + \ 👀
                   "sleuth9000"): 👀
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")

level_1_pw_check()

AsianHacker-picoctf@webshell:~$ python3 patchme.flag.py ⌨️
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000 ⌨️
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33} 🔐
```

## Flag
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}

## Continue
[Continue](./picoGym0175.md)
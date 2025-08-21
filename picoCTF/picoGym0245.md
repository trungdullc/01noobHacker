# picoGym Level 0245: PW Crack 1
Source: https://play.picoctf.org/practice/challenge/245

## Goal
Can you crack the password to get the flag?<br>
Download the password checker here and you'll need the encrypted flag in the same directory too

## What I learned
```
Don't store passwords as plaintext in code
python3
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/10/level1.py ⌨️
--2025-08-19 17:11:57--  https://artifacts.picoctf.net/c/10/level1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.71, 3.160.5.93, 3.160.5.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.71|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 876 [application/octet-stream]
Saving to: 'level1.py'

level1.py                                                  100%[======================================================================================================================================>]     876  --.-KB/s    in 0s      

2025-08-19 17:11:57 (671 MB/s) - 'level1.py' saved [876/876]

AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/10/level1.flag.txt.enc ⌨️
--2025-08-19 17:12:16--  https://artifacts.picoctf.net/c/10/level1.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.42, 3.160.5.18, 3.160.5.71, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 30 [application/octet-stream]
Saving to: 'level1.flag.txt.enc'

level1.flag.txt.enc                                        100%[======================================================================================================================================>]      30  --.-KB/s    in 0s      

2025-08-19 17:12:16 (7.39 MB/s) - 'level1.flag.txt.enc' saved [30/30]

AsianHacker-picoctf@webshell:/tmp$ file level1.flag.txt.enc ⌨️
level1.flag.txt.enc: data
AsianHacker-picoctf@webshell:/tmp$ cat level1.flag.txt.enc ⌨️
FPR
   umw
iK
_i
  UD
AsianHacker-picoctf@webshell:/tmp$ cat level1.py ⌨️
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level1.flag.txt.enc', 'rb').read()

def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"): 👀
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_1_pw_check()

AsianHacker-picoctf@webshell:/tmp$ python3 level1.py ⌨️
Please enter correct password for flag: 691d ⌨️
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419} 🔐
```

## Flag
picoCTF{545h_r1ng1ng_56891419}

## Continue
[Continue](./picoGym0246.md)
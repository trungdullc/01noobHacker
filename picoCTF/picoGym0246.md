# picoGym Level 0246: PW Crack 2
Source: https://play.picoctf.org/practice/challenge/246

## Goal
Can you crack the password to get the flag?<br>
Download the password checker here and you'll need the encrypted flag in the same directory too

## What I learned
```
python3
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/14/level2.py ⌨️
--2025-08-19 17:25:36--  https://artifacts.picoctf.net/c/14/level2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.71, 3.160.5.42, 3.160.5.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.71|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 914 [application/octet-stream]
Saving to: 'level2.py'

level2.py                                                  100%[======================================================================================================================================>]     914  --.-KB/s    in 0s      

2025-08-19 17:25:36 (701 MB/s) - 'level2.py' saved [914/914]

AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/14/level2.flag.txt.enc ⌨️
--2025-08-19 17:25:49--  https://artifacts.picoctf.net/c/14/level2.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.93, 3.160.5.71, 3.160.5.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.93|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 31 [application/octet-stream]
Saving to: 'level2.flag.txt.enc'

level2.flag.txt.enc                                        100%[======================================================================================================================================>]      31  --.-KB/s    in 0s      

2025-08-19 17:25:49 (26.0 MB/s) - 'level2.flag.txt.enc' saved [31/31]

AsianHacker-picoctf@webshell:/tmp$ file level2.flag.txt.enc ⌨️
level2.flag.txt.enc: data
AsianHacker-picoctf@webshell:/tmp$ cat level2.flag.txt.enc ⌨️
D
 Vw1%B@W
        \:ZRWS:ZT
                 T
AsianHacker-picoctf@webshell:/tmp$ strings level2.flag.txt.enc ⌨️ 
Vw1%B@
RWS:Z
AsianHacker-picoctf@webshell:/tmp$ cat level2.py ⌨️
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

flag_enc = open('level2.flag.txt.enc', 'rb').read()

def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ): 👀
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_2_pw_check()

AsianHacker-picoctf@webshell:/tmp$ python3 -c "print(chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))" ⌨️
4ec9
AsianHacker-picoctf@webshell:/tmp$ python3 level2.py ⌨️
Please enter correct password for flag: 4ec9 ⌨️
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681} 🔐
```

## Flag
picoCTF{tr45h_51ng1ng_9701e681}

## Continue
[Continue](./picoGym0247.md)
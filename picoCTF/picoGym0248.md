# picoGym Level 0248: PW Crack 4
Source: https://play.picoctf.org/practice/challenge/248

## Goal
Can you crack the password to get the flag?<br>
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.<br>
There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script

## What I learned
```
Same as PW Crack 3
CrackStation: https://crackstation.net/
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/21/level4.py https://artifacts.picoctf.net/c/21/level4.flag.txt.enc https://artifacts.picoctf.net/c/21/level4.hash.bin ⌨️
--2025-08-19 21:51:25--  https://artifacts.picoctf.net/c/21/level4.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2085 (2.0K) [application/octet-stream]
Saving to: 'level4.py'

level4.py                                                  100%[======================================================================================================================================>]   2.04K  --.-KB/s    in 0s      

2025-08-19 21:51:25 (1.15 GB/s) - 'level4.py' saved [2085/2085]

--2025-08-19 21:51:25--  https://artifacts.picoctf.net/c/21/level4.flag.txt.enc
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 33 [application/octet-stream]
Saving to: 'level4.flag.txt.enc'

level4.flag.txt.enc                                        100%[======================================================================================================================================>]      33  --.-KB/s    in 0s      

2025-08-19 21:51:25 (28.9 MB/s) - 'level4.flag.txt.enc' saved [33/33]

--2025-08-19 21:51:25--  https://artifacts.picoctf.net/c/21/level4.hash.bin
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 16 [application/octet-stream]
Saving to: 'level4.hash.bin'

level4.hash.bin                                            100%[======================================================================================================================================>]      16  --.-KB/s    in 0s      

2025-08-19 21:51:25 (14.3 MB/s) - 'level4.hash.bin' saved [16/16]

FINISHED --2025-08-19 21:51:25--
Total wall clock time: 0.3s
Downloaded: 3 files, 2.1K in 0s (529 MB/s)

# Method 1: Attack the .bin
AsianHacker-picoctf@webshell:/tmp$ bvi level4.hash.bin ⌨️

bvi version 1.4.0 Copyright (C) 1996-2014 by Gerhard Buergmann
00000000  64 C1 EF 00 36 A9 A8 D1 76 FB C3 81 C4 AB DA 52                      d...6...v......R
AsianHacker-picoctf@webshell:/tmp$ xxd -p level4.hash.bin ⌨️
64c1ef0036a9a8d176fbc381c4abda52
AsianHacker-picoctf@webshell:/tmp$ hexdump -C level4.hash.bin ⌨️
00000000  64 c1 ef 00 36 a9 a8 d1  76 fb c3 81 c4 ab da 52  |d...6...v......R|
00000010
AsianHacker-picoctf@webshell:/tmp$ hexdump level4.hash.bin ⌨️
0000000 c164 00ef a936 d1a8 fb76 81c3 abc4 52da                             ⚠️ Numbers are backwards (Little endian)
0000010
AsianHacker-picoctf@webshell:/tmp$ lscpu | grep "Byte Order" ⌨️
Byte Order:                           Little Endian
AsianHacker-picoctf@webshell:/tmp$ echo "64 c1 ef 00 36 a9 a8 d1  76 fb c3 81 c4 ab da 52" | tr -d " "
64c1ef0036a9a8d176fbc381c4abda52

# CrackStation: https://crackstation.net/
Hash Input: 64c1ef0036a9a8d176fbc381c4abda52
Result: 9f63

# Run Python w/ 9f63
AsianHacker-picoctf@webshell:/tmp$ python3 level4.py ⌨️
Please enter correct password for flag: 9f63 ⌨️
Welcome back... your flag, user:
picoCTF{fl45h_5pr1ng1ng_d770d48c} 🔐

# Method 2: Brute Force Python Program
AsianHacker-picoctf@webshell:/tmp$ cat level4.py ⌨️
import hashlib

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

flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_4_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

level_4_pw_check()

# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"]

# Modify Python Program
AsianHacker-picoctf@webshell:/tmp$ vi level4.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat level4.py ⌨️
import hashlib

pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"] 👀

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

flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_4_pw_check():
    # user_pw = input("Please enter correct password for flag: ")
    for user_pw in pos_pw_list: 👀
        user_pw_hash = hash_pw(user_pw)
    
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        print("That password is incorrect")

level_4_pw_check()

# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
# pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"]

# Run Modified Python Program
AsianHacker-picoctf@webshell:/tmp$ python3 level4.py ⌨️ 
That password is incorrect
That password is incorrect
...
That password is incorrect
That password is incorrect
That password is incorrect
Welcome back... your flag, user:
picoCTF{fl45h_5pr1ng1ng_d770d48c} 🔐
```

## Flag
picoCTF{fl45h_5pr1ng1ng_d770d48c}

## Continue
[Continue](./picoGym0249.md)
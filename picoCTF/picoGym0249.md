# picoGym Level 0249: PW Crack 5
Source: https://play.picoctf.org/practice/challenge/249

## Goal
Can you crack the password to get the flag?<br>
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a <b>dictionary with all possible passwords</b> based on the password conventions we've seen so far.

## What I learned
```
Note: Didn't use md5sum this time to hash used custom

Input primitives in Python:
    input() → reads a full line from stdin (as a str)
    sys.stdin.readline() → like input() but includes trailing \n
    file.readline() → read a line from a file
    file.readlines() → read all lines into a list of strings
    file.read() → read the whole file into one string
    for line in file → iterate line by line

Once got a string able to convert:
    int(s) → parse string s as integer
    float(s) → parse string s as floating-point
    str(s) → ensure it’s a string
    s.split() → split line into words (default: split on whitespace)
    map(int, s.split()) → parse multiple ints from a line
    map(float, s.split()) → parse multiple floats

with open("data.txt") as f:
    for line in f:
        words = line.split()                        # rm \n
        print(words)

JavaScript/Java .trim()
Python .strip()         rm leading and ending whitespaces                   # Note: Easier to see in VSC

# See available methods
dir(str) ❤️❤️❤️❤️❤️

# help from shell
python3 -m pydoc str.strip
python3 -m pydoc -k strip
    -k: keyword

# help
help(str.strip) ❤️❤️❤️❤️❤️
print(str.strip.__doc__) ❤️❤️❤️❤️❤️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/32/level5.py https://artifacts.picoctf.net/c/32/level5.flag.txt.enc https://artifacts.picoctf.net/c/32/level5.hash.bin https://artifacts.picoctf.net/c/32/dictionary.txt ⌨️
--2025-08-19 22:22:27--  https://artifacts.picoctf.net/c/32/level5.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.18, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1168 (1.1K) [application/octet-stream]
Saving to: 'level5.py'

level5.py                                                  100%[======================================================================================================================================>]   1.14K  --.-KB/s    in 0s      

2025-08-19 22:22:28 (946 MB/s) - 'level5.py' saved [1168/1168]

--2025-08-19 22:22:28--  https://artifacts.picoctf.net/c/32/level5.flag.txt.enc
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 31 [application/octet-stream]
Saving to: 'level5.flag.txt.enc'

level5.flag.txt.enc                                        100%[======================================================================================================================================>]      31  --.-KB/s    in 0s      

2025-08-19 22:22:28 (13.1 MB/s) - 'level5.flag.txt.enc' saved [31/31]

--2025-08-19 22:22:28--  https://artifacts.picoctf.net/c/32/level5.hash.bin
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 16 [application/octet-stream]
Saving to: 'level5.hash.bin'

level5.hash.bin                                            100%[======================================================================================================================================>]      16  --.-KB/s    in 0s      

2025-08-19 22:22:28 (10.5 MB/s) - 'level5.hash.bin' saved [16/16]

--2025-08-19 22:22:28--  https://artifacts.picoctf.net/c/32/dictionary.txt
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 327680 (320K) [application/octet-stream]
Saving to: 'dictionary.txt'

dictionary.txt                                             100%[======================================================================================================================================>] 320.00K  1.91MB/s    in 0.2s    

2025-08-19 22:22:28 (1.91 MB/s) - 'dictionary.txt' saved [327680/327680]

FINISHED --2025-08-19 22:22:28--
Total wall clock time: 0.5s
Downloaded: 4 files, 321K in 0.2s (1.91 MB/s)
AsianHacker-picoctf@webshell:/tmp$ ls -la ⌨️
total 332
drwxrwxrwt 1 root                root                   115 Aug 19 22:22 .
drwxr-xr-x 1 root                root                    70 Aug 19 21:39 ..
drwx------ 3 root                root                    41 Mar  5 02:13 .wine-0
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 327680 Mar 16  2023 dictionary.txt
drwxr-xr-x 2 root                root                     6 Mar  5 02:09 hsperfdata_root
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf     31 Mar 16  2023 level5.flag.txt.enc
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf     16 Mar 16  2023 level5.hash.bin
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf   1168 Mar 16  2023 level5.py
drwxr-xr-x 3 root                root                    45 Mar  5 02:13 node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ head dictionary.txt ⌨️ 
0000
0001
0002
0003
0004
0005
0006
0007
0008
0009
AsianHacker-picoctf@webshell:/tmp$ tail dictionary.txt ⌨️
fff6
fff7
fff8
fff9
fffa
fffb
fffc
fffd
fffe
ffff

# Method 2: Brute Force by Modifying Python Program
AsianHacker-picoctf@webshell:/tmp$ cat level5.py ⌨️
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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()
with open("dictionary.txt", "r") as f: 👀
    words = [line.strip() for line in f] 👀 strip to rm \n, could use ghex to see

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_5_pw_check():
    # user_pw = input("Please enter correct password for flag: ")
    for user_pw in words: 👀 Brute Force
        user_pw_hash = hash_pw(user_pw)
    
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        # print("That password is incorrect")                   # Got annoying seeing all incorrect output

level_5_pw_check()

# Run Python Program
AsianHacker-picoctf@webshell:/tmp$ python3 level5.py ⌨️
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_40f26f81} 🔐
```

## Flag
picoCTF{h45h_sl1ng1ng_40f26f81}

## Continue
[Continue](./picoGym0384.md)
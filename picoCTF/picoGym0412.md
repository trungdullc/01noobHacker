# picoGym Level 412: Custom encryption
Source: https://play.picoctf.org/practice/challenge/412

## Goal
Can you get sense of this code file and write the function that will decode the given encrypted file content.<br>
Find the encrypted file here flag_info and code file might be good to analyze and get the flag.<br>
flag_info: https://artifacts.picoctf.net/c_titan/92/enc_flag <br>
code file: https://artifacts.picoctf.net/c_titan/92/custom_encryption.py

## What I learned
```
Reverse Engineering

Youtube Solutiion: https://www.youtube.com/watch?v=6tEOaDMMPVs (Watch Later)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c_titan/92/enc_flag https://artifacts.picoctf.net/c_titan/92/custom_encryption.py ⌨️
--2025-09-10 23:11:10--  https://artifacts.picoctf.net/c_titan/92/enc_flag
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.18, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'enc_flag'

enc_flag                                                   100%[======================================================================================================================================>]     270  --.-KB/s    in 0s      

2025-09-10 23:11:11 (107 MB/s) - 'enc_flag' saved [270/270]

--2025-09-10 23:11:11--  https://artifacts.picoctf.net/c_titan/92/custom_encryption.py 
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 1411 (1.4K) [application/octet-stream]
Saving to: 'custom_encryption.py'

custom_encryption.py                                       100%[======================================================================================================================================>]   1.38K  --.-KB/s    in 0s      

2025-09-10 23:11:11 (949 MB/s) - 'custom_encryption.py' saved [1411/1411]

FINISHED --2025-09-10 23:11:11--
Total wall clock time: 0.2s
Downloaded: 2 files, 1.6K in 0s (418 MB/s)
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag ⌨️
a = 89
b = 27
cipher is: [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]

AsianHacker-picoctf@webshell:/tmp$ cat custom_encryption.py ⌨️
from random import randint
import sys

def generator(g, x, p):
    return pow(g, x) % p

def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher

def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True

def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p) 👀
    b = randint(g-10, g) 👀
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')

if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")

# ChatGPT: Solved for us or we would have to understand each function to reverse engineer
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
def generator(g, x, p):
    return pow(g, x, p)

def dynamic_xor_decrypt(cipher_text, text_key):
    key_length = len(text_key)
    decrypted_chars = []
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_chars.append(chr(ord(char) ^ ord(key_char)))
    # reverse back
    return "".join(decrypted_chars[::-1])

def decrypt(cipher, shared_key, text_key):
    semi_chars = []
    for num in cipher:
        if num == 0:
            semi_chars.append(chr(0))
        else:
            semi_chars.append(chr(num // (shared_key * 311)))
    semi_cipher = "".join(semi_chars)
    return dynamic_xor_decrypt(semi_cipher, text_key)

# Parameters
p = 97
g = 31
a = 89              # (random number from p-10 to p, both included)
b = 27              # (random number from g-10 to g, both included)
u = generator(g, a, p)
v = generator(g, b, p)
shared_key = generator(v, a, p)

cipher = [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104,
          156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732,
          231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332,
          119424, 182868, 97032, 26124, 44784, 63444]

plaintext = decrypt(cipher, shared_key, "trudeau")
print("Recovered plaintext:", plaintext)

AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
Recovered plaintext: picoCTF{custom_d2cr0pt6d_dc499538} 🔐
```

## Flag
picoCTF{custom_d2cr0pt6d_dc499538}

## Continue
[Continue](./picoGym0210.md)
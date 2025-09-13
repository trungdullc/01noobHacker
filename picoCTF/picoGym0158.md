# picoGym Level 158: New Caesar
Source: https://play.picoctf.org/practice/challenge/158

## Goal
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{})<br>
mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj<br>
new_caesar.py: https://mercury.picoctf.net/static/b82dc751249b75b2509315c59f8200c7/new_caesar.py

## What I learned
```
Reverse Engineering Function
print() is your friend

Youtube Solution: https://www.youtube.com/watch?v=yaZP4bMn4pU
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/b82dc751249b75b2509315c59f8200c7/new_caesar.py ⌨️
--2025-09-10 00:08:40--  https://mercury.picoctf.net/static/b82dc751249b75b2509315c59f8200c7/new_caesar.py
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 589 [application/octet-stream]
Saving to: 'new_caesar.py'

new_caesar.py                                              100%[======================================================================================================================================>]     589  --.-KB/s    in 0s      

2025-09-10 00:08:40 (191 MB/s) - 'new_caesar.py' saved [589/589]

AsianHacker-picoctf@webshell:/tmp$ cat new_caesar.py ⌨️
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
        enc = ""
        for c in plain:
                binary = "{0:08b}".format(ord(c))
                enc += ALPHABET[int(binary[:4], 2)]
                enc += ALPHABET[int(binary[4:], 2)]
        return enc

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
print(enc)

# Modify above code to decode
# Method 1:
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py 
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
        enc = ""
        for c in plain:
                binary = "{0:08b}".format(ord(c))
                enc += ALPHABET[int(binary[:4], 2)]
                enc += ALPHABET[int(binary[4:], 2)]
        return enc

# Added a decode fx
def b16_decode(cipher):
    enc = ""
    for i in range(0, len(cipher), 2):
        binary ="{0:04b}".format(ALPHABET.index(cipher[i]))+"{0:04b}".format(ALPHABET.index(cipher[i+1]))
        enc += chr(int(binary,2))
    return enc

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
print(enc)

# Added stuff below
encflag = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
print(len(encflag))

for key in ALPHABET:
    dec = ""
    for c in encflag:
        dec += shift(c, key)
    b16 = b16_decode(dec)
    print(key, b16)
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py 
igjfihkehhkeiikh
78
a ËÚµÚÛµÇÇËÌÊËÈÉ
b ÜëÆëì¦ÆØ©ÛØ¨Ü¨¯ØÝ« Ý­« ¯§­ ¯¯®¯­ÛÜÙ©Ø­Ú
c íü×üý·×éºìé¹í¹°éî¼±î¾¼±°¸¾±°°¿°¾ìíêºé¾ë
ÈèúËýúÊþÊÁúÿÍÂÿÏÍÂÁÉÏÂÁÁÀÁÏýþûËúÏü
e ùÙù
     Ü
      ÛÛÒ
         ÞÓÐÞÓÒÚÐÓÒÒÑÒÐ
                       Ü
                        Ð
f /
/ ê
íììãïäáïäãëáäããâãáíá
g !01û -ý!ýô-"ðõ"òðõôüòõôôóôò !.þ-ò/
h 2A,AB
12?>0  ,>1>2>33
i CR=RS=OBOCODDBC@OA
j TcNcd.NP!SP T 'PU#(U%#('/%(''&'%STQ!P%R
k et_tu?_a2da1e18af49f649806988786deb2a6c 🔐
l v
`
@`rCurBvBIrwEJwGEJIAGJIIHIGuvsCrGt
m qQqTSSZV[XV[ZRX[ZZYZX
                       TX

n §¨bedgliglkcilkkjkiei
o ©¸¸¹s¥v¨¥u©u|¥ªx}ªzx}|tz}||{|z¨©¦v¥z§
p ºÉ¤ÉÊ
       ¤¶¹¶º¶»»
¹º·¶¸

# Method 2:
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️ 
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

cipher_text = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"

def b16_decode(solve):
    dec = ""
    for idx in range(0, len(solve), 2):
        # Get the current and next letters so we can create the one letter that
        # was split in half by `b16_encode`.
        c1 = solve[idx]
        c2 = solve[idx + 1]
        # Determine the location of these letters in the alphabet. The coresponds to
        # the code inside the square brackets `ALPHABET[int(binary[:4], 2)]` from
        # `b16_encode`.
        c1 = ALPHABET.index(c1)
        c2 = ALPHABET.index(c2)
        # Convert the numbers to binary
        binary1 = "{0:04b}".format(c1)
        binary2 = "{0:04b}".format(c2)
        # Add the two binary strings together to recover the encoded character
        binary = int(binary1 + binary2, 2)

        dec += chr(binary)
    return dec

def unshift(c, k):
    # Offset the letters in the opposite direction.
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    # Instead of moving forward through the alphabet, move backwards.
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def is_ascii(s):
    return len(s) == len(s.encode())

# Try every possible offset to see what key produces the flag.
for letter in ALPHABET:
    # `letter` is the key
    dec = ""
    # Apply the opposite of the `shift` function on each letter.
    for i, c in enumerate(cipher_text):
        dec += unshift(c, letter)
    # Reverse the `b16_encode` function.
    dec = b16_decode(dec)
    # Only show potential flags that are ascii.
    if is_ascii(dec) and " " not in dec:
        print("Flag: picoCTF{%s}" % dec)
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py 
Flag: picoCTF{et_tu?_a2da1e18af49f649806988786deb2a6c} 🔐
Flag: picoCTF{CR=RS=OBOCODDBC@OA}
Flag: picoCTF{2A,AB
12?>0}             ,>1>2>33

# Method 3:
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
import string

ALPHABET = string.ascii_lowercase[:16]  # first 16 letters a-p

def decryptFlag(enc1):
    # try all possible shifts 0–15
    for a in range(16):
        enc = ""
        combined = ""

        # shifting step
        for ch in enc1:
            t1 = ord(ch)
            t2 = a
            enc += ALPHABET[(t1 - t2) % len(ALPHABET)]

        # decryption step (take pairs of shifted chars -> 8-bit char)
        x = 0
        while x < len(enc) - 1:
            firstChar = ord(enc[x]) - 97
            fBit1 = "{0:04b}".format(firstChar)

            secondChar = ord(enc[x + 1]) - 97
            fBit2 = "{0:04b}".format(secondChar)

            tempCombine = fBit1 + fBit2
            combined += chr(int(tempCombine, 2))
            x += 2

        print(f"Shift {a}: {combined}")
        print("-" * 40)

flag = 'mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj'

decryptFlag(flag)
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py 
Shift 0: ÜëÆëì¦ÆØ©ÛØ¨Ü¨¯ØÝ« Ý­« ¯§­ ¯¯®¯­ÛÜÙ©Ø­Ú
----------------------------------------
Shift 1: ËÚµÚÛµÇÇËÌÊËÈÉ
----------------------------------------
Shift 2: ºÉ¤ÉÊ
              ¤¶¹¶º¶»»
¹º·¶¸
----------------------------------------
Shift 3: ©¸¸¹s¥v¨¥u©u|¥ªx}ªzx}|tz}||{|z¨©¦v¥z§
----------------------------------------
Shift 4: §¨bedgliglkcilkkjkiei
----------------------------------------
Shift 5: qQqTSSZV[XV[ZRX[ZZYZX
                              TX

----------------------------------------
Shift 6: v
`
@`rCurBvBIrwEJwGEJIAGJIIHIGuvsCrGt
----------------------------------------
Shift 7: et_tu?_a2da1e18af49f649806988786deb2a6c 🔐
----------------------------------------
Shift 8: TcNcd.NP!SP T 'PU#(U%#('/%(''&'%STQ!P%R
----------------------------------------
Shift 9: CR=RS=OBOCODDBC@OA
----------------------------------------
Shift 10: 2A,AB
12?>0          ,>1>2>33
----------------------------------------
Shift 11: !01û -ý!ýô-"ðõ"òðõôüòõôôóôò !.þ-ò/
----------------------------------------
Shift 12: /
/ ê
íììãïäáïäãëáäããâãáíá
----------------------------------------
Shift 13: ùÙù
             Ü
              ÛÛÒ
                 ÞÓÐÞÓÒÚÐÓÒÒÑÒÐ
                               Ü
                                Ð
----------------------------------------
ÈèúËýúÊþÊÁúÿÍÂÿÏÍÂÁÉÏÂÁÁÀÁÏýþûËúÏü
----------------------------------------
Shift 15: íü×üý·×éºìé¹í¹°éî¼±î¾¼±°¸¾±°°¿°¾ìíêºé¾ë
----------------------------------------
```

## Flag
picoCTF{et_tu?_a2da1e18af49f649806988786deb2a6c}

## Continue
[Continue](./picoGym0003.md)
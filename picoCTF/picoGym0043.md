# picoGym Level 43: Easy1
Source: https://play.picoctf.org/practice/challenge/43

## Goal
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? <br>
We've given you the encrypted flag, key, and a table to help <b>UFJKXQZQUNB</b> with the key of <b>SOLVECRYPTO</b>.<br>
Can you use this table to solve it?<br>
https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt

## What I learned
```
Google: Encryption Method w/ key and table
    Vigenère cipher

ENCRYPT
    TOP COLUMN w/ Plaintext
    LEFT ROW w/ Key
    Result: Ciphertext
DECRYPT
    LEFTROW w/ Key
    Search Ciphertext and go up to COLUMN
    Result: Plaintext
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt ⌨️
--2025-09-04 19:39:50--  https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1571 (1.5K) [application/octet-stream]
Saving to: 'table.txt'

table.txt                                                  100%[======================================================================================================================================>]   1.53K  --.-KB/s    in 0s      

2025-09-04 19:39:50 (795 MB/s) - 'table.txt' saved [1571/1571]

AsianHacker-picoctf@webshell:/tmp$ cat table.txt ⌨️
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z     PLAINTEXT 
   +----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
KEY

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "SOLVECRYPTO"
encrypted_flag = "UFJKXQZQUNB"

def modular_subtraction(encrypted_flag) -> str:
  res = ""
  for i in range(len(encrypted_flag)):
    if (ord(encrypted_flag[i]) - ord(key[i])) >= 0:
        res += chr(ord(encrypted_flag[i]) - ord(key[i]) + 65)
    else:
        res += chr(ord(encrypted_flag[i]) - ord(key[i]) + 91)
  return res

def main() -> None:
    print("And the flag is: picoCTF{" + modular_subtraction(encrypted_flag) + "}")

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
And the flag is: picoCTF{CRYPTOISFUN} 🔐

Method 2: CyberChef
https://cyberchef.io/#recipe=Vigen%C3%A8re_Decode('SOLVECRYPTO')&input=VUZKS1hRWlFVTkI
    CRYPTOISFUN 👀
```

## Flag
picoCTF{CRYPTOISFUN}

## Continue
[Continue](./picoGym0125.md)
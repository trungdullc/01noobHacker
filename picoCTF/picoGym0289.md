# picoGym Level 289: rail-fence
Source: https://play.picoctf.org/practice/challenge/289

## Goal
A type of transposition cipher is the rail fence cipher, which is described here<br>
https://en.wikipedia.org/wiki/Rail_fence_cipher<br>
Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?<br>
Download the message here<br>
https://artifacts.picoctf.net/c/190/message.txt<br>
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.<br>

## What I learned
```
WE ARE DISCOVERED. RUN AT ONCE.         # Note: Spaces and punctuation are omitted

Encrypted:
W . . . E . . . C . . . R . . . U . . . O . . . 
. E . R . D . S . O . E . E . R . N . T . N . E 
. . A . . . I . . . V . . . D . . . A . . . C . 

Rail fence cipher, plaintext is written downwards diagonally on successive "rails" of an imaginary fence, then moving up when the bottom rail is reached, down again when the top rail is reached, and so on until the whole plaintext is written out. 
Ciphertext is then read off in rows.

Asian Method
    Find Online Decoder ❤️❤️❤️❤️❤️
    If not created find code online or use ChatGPT and modify/test (no need reinvent wheel for CTF challenge)
    Create custom code researching the algorithm and math equations
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/190/message.txt ⌨️
--2025-09-09 21:20:11--  https://artifacts.picoctf.net/c/190/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 56 [application/octet-stream]
Saving to: 'message.txt'

message.txt                                        100%[=============================================================================================================>]      56  --.-KB/s    in 0s      

2025-09-09 21:20:11 (2.45 MB/s) - 'message.txt' saved [56/56]

AsianHacker-picoctf@webshell:/tmp$ cat message.txt ⌨️
Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA 👀

# Method 1: Online Decoders:
https://www.dcode.fr/rail-fence-cipher
Rail Fence Decoder
ZigZag ciphertext
Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA ⌨️

Keep punctuation and spaces:                                    # Important: Make sure checked

Parameters and Options
Key/Number number of rows/levels (height) 4 ⌨️

Start from Top (left) ↘↗
No initial offset (recommended)
DECRYPT RAIL FENCE

T						a												_		...
h				l		g				:		W				3		D		...
e		f						s				H		R				0	    ...
i						3						                                ...

The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3 🔐

https://www.boxentriq.com/code-breaking/rail-fence-cipher
The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3 🔐

https://cryptii.com/pipes/rail-fence-cipher
The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3 🔐

https://cyberchef.io/#recipe=Rail_Fence_Cipher_Decode(4,0)&input=VGEgXzdONkRERGhsZzpXM0RfSDNDMzFOX18wRDNlZiBzSFIwNTNGMzhONDNEMEYgaTMzX19fTkE
The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3 🔐

Method 2:
Google: python code for rail fence
https://www.geeksforgeeks.org/dsa/rail-fence-cipher-encryption-decryption/

AsianHacker-picoctf@webshell:~$ cd /tmp/
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

def encryptRailFence(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
    
def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
            
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
        
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
            
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

if __name__ == "__main__":
    print(decryptRailFence("Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA", 4))
    message = decryptRailFence("Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA", 4)
    flag_part = message.split(" ")[-1]
    print("picoCTF{%s}" %flag_part) 🕵️‍♀️                            # Old % formatting
    # str.format() style
    # print("picoCTF{{{}}}".format(flag_part)) 🕵️‍♀️
    # f-string style (Python 3.6+) uses {{}}
    # print(f"picoCTF{{{flag_part}}}") 🕵️‍♀️
    
# Give Credit: Pratik Somwanshi
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py 
The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3 🔐
```

## Flag
picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3} 🔐

## Continue
[Continue](./picoGym0040.md)
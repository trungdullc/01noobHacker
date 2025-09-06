# picoGym Level 253: basic-mod1 🧠🧠🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/253

## Goal
We found this weird message being passed around on the servers, we think we have a working decryption scheme<br>
Download the message here: https://artifacts.picoctf.net/c/127/message.txt<br>
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore<br>
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## What I learned
```
n % 37 produces results in 0..36
36 was missing make it underscore (didn't read carefully)

0:A                               26:0
1:B                               27:1
2:C                               28:2
3:D                               29:3
4:E                               30:4
5:F                               31:5
6:G                               32:6
7:H                               33:7
8:I                               34:8
9:J                               35:9
10:K                              36:_
11:L
12:M
13:N
14:O
15:P
16:Q
17:R
18:S
19:T
20:U
21:V
22:W
23:X
24:Y
25:Z
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/127/message.txt ⌨️
--2025-09-05 21:45:50--  https://artifacts.picoctf.net/c/127/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 85 [application/octet-stream]
Saving to: 'message.txt'

message.txt                                                100%[======================================================================================================================================>]      85  --.-KB/s    in 0s      

2025-09-05 21:45:50 (5.75 MB/s) - 'message.txt' saved [85/85]

AsianHacker-picoctf@webshell:/tmp$ cat message.txt ⌨️
128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140 👀

# Write Custom Script
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3 ❤️
mapping: dict[int, str] = {}
answer: list[str] = []

# map 36 directly
mapping[36] = '_'

# 0–25 -> A–Z
# mapping.update({i: chr(ord('A') + i) for i in range(26)}) ❤️
for i in range(26):
    mapping[i] = chr(ord('A') + i)

# 26–35 -> 0–9
# mapping.update({26 + i: str(i) for i in range(10)}) ❤️
for i in range(10):
    mapping[26 + i] = str(i)

def mod37_mapper() -> None:
    global answer                       # Note: can update global list ❤️

    # Convert string to python list
    numberString = "128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"
    numbers = list(map(int, numberString.split())) ❤️❤️❤️❤️❤️

    # Mod each by 37
    # for i in range(len(numbers)):
    #    numbers[i] = numbers[i] % 37
    # Using list comprehension
    numbers = [int(num) % 37 for num in numberString.split()] ❤️❤️❤️

    # Map numbers to characters using the dictionary
    answer = [mapping[num] for num in numbers] ❤️❤️❤️

    # Join into a string
    print("picoCTF{" +"".join(answer) + "}") ❤️❤️❤️

def main() -> None:
    mod37_mapper()

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
picoCTF{R0UND_N_R0UND_79C18FB3} 🔐

Method 2: Turn mod 37 into tuple by hand
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3

def basicMod1():
    enc_flag = (128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140) 👀
    encoding = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9','_') 👀 manual labor or ChatGPT

    for i in range(len(enc_flag)):
        print(encoding[enc_flag[i]%37], end="")
    print()

basicMod1()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
R0UND_N_R0UND_79C18FB3 🔐
```

## Flag
picoCTF{R0UND_N_R0UND_79C18FB3}

## Continue
[Continue](./picoGym0254.md)
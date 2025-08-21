# picoGym Level 0035: Based 🧠🧠🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/35

## Goal
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc jupiter.challenges.picoctf.org 15130.

## What I learned
```
tmux new-session \; split-window -h \; attach ❤️❤️❤️❤️❤️
    Ctrl + b + o

printf/echo doesn't do binary → ASCII (must convert to decimal/hex)

# binary_to_text.py
user_input = input("Enter Binary Stream: ")

user_input = user_input.split(" ")

converted_string = ""

for b in user_input:
    converted_string += chr(int(b, 2))

print(converted_string)

# octal_to_text.py
user_input = input("Enter Octal Stream: ")

user_input = user_input.split(" ")

converted_string = ""

for b in user_input:
    converted_string += chr(int(b, 8))

print(converted_string)

# hex_to_text.py, Input number
bytes.fromhex('6d6170').decode('utf-8')

# Decimal to ASCII, Note: Use Base 10
https://cyberchef.io/#recipe=From_Charcode('Space',10)&input=OTkgOTcgMTE2
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 15130 ⌨️
Please give the 01110011 01101111 01100011 01101011 01100101 01110100 as a word.
...
you have 45 seconds.....

Input:
socket ⌨️
Please give me the  164 141 142 154 145 as a word.
Input:
table ⌨️
Please give me the 6d6170 as a word.
Input:
map ⌨️
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8} 🔐

# First Question: Binary to Char
https://cyberchef.io/#recipe=From_Binary('Space',8)&input=MDExMTAwMTEgMDExMDExMTEgMDExMDAwMTEgMDExMDEwMTEgMDExMDAxMDEgMDExMTAxMDA
AsianHacker-picoctf@webshell:~$ python3 -c "print(''.join([chr(int(b, 2)) for b in '01110011 01101111 01100011 01101011 01100101 01110100'.split()]))"
socket ⌨️

# Second Question: Octal to Word
https://cyberchef.io/#recipe=From_Octal('Space')&input=MTY0IDE0MSAxNDIgMTU0IDE0NQ
AsianHacker-picoctf@webshell:~$ python3 -c "print(''.join(chr(int(x,8)) for x in '164 141 142 154 145'.split()))" ⌨️
table
AsianHacker-picoctf@webshell:~$ python3 -c "print('\164\141\142\154\145')" ⌨️
table

# Third Question: From Hex to Word
https://cyberchef.io/#recipe=From_Hex('Auto')&input=NmQ2MTcw 
AsianHacker-picoctf@webshell:~$ python3 -c "print(bytes.fromhex('6d6170').decode('utf-8'))" ⌨️
map
AsianHacker-picoctf@webshell:~$ python3 -c "print('\x6d\x61\x70')" ⌨️
map
```

## Flag
picoCTF{learning_about_converting_values_02167de8}

## Continue
[Continue](./picoGym0048.md)
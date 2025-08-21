# picoGym Level 0242: Glitch Cat
Source: https://play.picoctf.org/practice/challenge/242

## Goal
Our flag printing service has started glitching!<br>
nc saturn.picoctf.net 64513

## What I learned
```
python3 chr(): https://docs.python.org/3/library/functions.html#chr
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc saturn.picoctf.net 64513 ⌨️
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
^C ⌨️
AsianHacker-picoctf@webshell:~$ python3 -c "print('\x61\x34\x33\x39\x32\x64\x32\x65')" ⌨️
a4392d2e

# ChatGPT says chr() python3 convert hex to ASCII
AsianHacker-picoctf@webshell:~$ python3 -c "print('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}')" ⌨️
picoCTF{gl17ch_m3_n07_a4392d2e} 🔐 
```

## Flag
picoCTF{gl17ch_m3_n07_a4392d2e} 

## Continue
[Continue](./picoGym0425.md)
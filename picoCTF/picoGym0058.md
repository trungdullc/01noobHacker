# picoGym Level 0058: Warmed Up
Source: https://play.picoctf.org/practice/challenge/58

## Goal
What is 0x3D (base 16) in decimal (base 10)?

## What I learned
```
hex
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:/tmp$ python3 -c "print('\x3D')" ⌨️
=
AsianHacker-picoctf@webshell:/tmp$ printf '\x3D\n' ⌨️
=
AsianHacker-picoctf@webshell:/tmp$ echo -e '\x3D' ⌨️
=

# Look up on ASCII decimal value or use python
AsianHacker-picoctf@webshell:/tmp$ python3 -c "print(ord('='))" ⌨️
61

# Modify Answer
picoCTF{61} 🔐
```

## Flag
picoCTF{=}

## Continue
[Continue](./picoGym0086.md)
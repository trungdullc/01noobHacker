# picoGym Level 0022: Lets Warm Up
Source: https://play.picoctf.org/practice/challenge/22

## Goal
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## What I learned
```
hex
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:/tmp$ python3 -c "print('\x70')" ⌨️
p
AsianHacker-picoctf@webshell:/tmp$ printf '\x70\n' ⌨️
p
AsianHacker-picoctf@webshell:/tmp$ echo -e '\x70' ⌨️
p

# Modify Answer
picoCTF{p} 🔐
```

## Flag
picoCTF{p}

## Continue
[Continue](./picoGym0058.md)
# picoGym Level 0067: Bases
Source: https://play.picoctf.org/practice/challenge/67

## Goal
What does this <b>bDNhcm5fdGgzX3IwcDM1</b> mean? I think it has something to do with bases.

## What I learned
```
base64
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ whatis base64 ⌨️
base64 (1)           - base64 encode/decode data and print to standard output
AsianHacker-picoctf@webshell:~$ echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d ⌨️
l3arn_th3_r0p35 👀

# Modify format
picoCTF{l3arn_th3_r0p35} 🔐
```

## Flag
picoCTF{l3arn_th3_r0p35}

## Continue
[Continue](./picoGym0442.md)
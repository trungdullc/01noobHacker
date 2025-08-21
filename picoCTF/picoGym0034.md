# picoGym Level 0034: what's a net cat?
Source: https://play.picoctf.org/practice/challenge/34

## Goal
Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 25103 to get the flag?
nc jupiter.challenges.picoctf.org 25103

## What I learned
```
nc
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ whatis nc ⌨️
nc (1)               - arbitrary TCP and UDP connections and listens
AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 25103 ⌨️
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587} 🔐
```

## Flag
picoCTF{nEtCat_Mast3ry_d0c64587}

## Continue
[Continue](./picoGym0156.md)
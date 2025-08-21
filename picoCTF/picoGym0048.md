# picoGym Level 0048: plumbing
Source: https://play.picoctf.org/practice/challenge/48

## Goal
Sometimes you need to handle process data outside of a file. Can you find a way to <b>keep the output from this program and search for the flag</b>? Connect to <b>jupiter.challenges.picoctf.org 7480</b>.

## What I learned
```
pipeline a netcat server echo
```

## Side Quest
```
# nc Server
nc -l -p 7480 < file.txt ⌨️

# Keep server open for multiple clients
while true; do nc -l -p 7480 < file.txt; done ⌨️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 7480 ⌨️
This is defintely not a flag
Not a flag either
Not a flag either
Not a flag either
Not a flag either
I don't think this is a flag either
This is defintely not a flag
I don't think this is a flag either
Not a flag either
Not a flag either
This is defintely not a flag
Again, I really don't think this is a flag
I don't think this is a flag either
AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 7480 | wc ⌨️

  10001   61592  286135
AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 7480 | grep "picoCTF" ⌨️
picoCTF{digital_plumb3r_06e9d954} 🔐
```

## Flag
picoCTF{digital_plumb3r_06e9d954}

## Continue
[Continue](./picoGym0015.md)
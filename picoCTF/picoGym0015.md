# picoGym Level 0015: mus1c
Source: https://play.picoctf.org/practice/challenge/15

## Goal
I wrote you a song. Put it in the picoCTF{} flag format.

## What I learned
```
Google: rockstar program language
Google: online rockstar compiler
  https://codewithrockstar.com/online.html

```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/c594d8d915de0129d92b4c41e25a2313/lyrics.txt ⌨️
--2025-08-20 17:17:41--  https://jupiter.challenges.picoctf.org/static/c594d8d915de0129d92b4c41e25a2313/lyrics.txt
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 772 [application/octet-stream]
Saving to: 'lyrics.txt'

lyrics.txt                                                 100%[======================================================================================================================================>]     772  --.-KB/s    in 0s      

2025-08-20 17:17:41 (267 MB/s) - 'lyrics.txt' saved [772/772]
AsianHacker-picoctf@webshell:/tmp$ cat lyrics.txt ⌨️
Pico's a CTFFFFFFF
my mind is waitin
It's waitin

Put my mind of Pico into This
my flag is not found
put This into my flag
put my flag into Pico


shout Pico
shout Pico
shout Pico

My song's something
put Pico into This

Knock This down, down, down
put This into CTF

shout CTF
my lyric is nothing
Put This without my song into my lyric
Knock my lyric down, down, down

shout my lyric

Put my lyric into This
Put my song with This into my lyric
Knock my lyric down

shout my lyric

Build my lyric up, up ,up

shout my lyric
shout Pico
shout It

Pico CTF is fun
security is important
Fun is fun
Put security with fun into Pico CTF
Build Fun up
shout fun times Pico CTF
put fun times Pico CTF into my song

build it up

shout it
shout it

build it up, up
shout it
shout Pico

# Rockstar Compiler Online: https://codewithrockstar.com/online.html
Output:
114
114
114
111
99
107
110
114
110
48
49
49
51
114

# CyberChef Decimal: Base10 to ASCII
https://cyberchef.io/#recipe=From_Charcode('Space',10)&input=MTE0IDExNCAxMTQgMTExIDk5IDEwNyAxMTAgMTE0IDExMCA0OCA0OSA0OSA1MSAxMTQ
rrrocknrn0113r

# Modify flag
picoCTF{rrrocknrn0113r} 🔐
```

## Flag
picoCTF{rrrocknrn0113r}

## Continue
[Continue](./picoGym0082.md)
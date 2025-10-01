# picoGym Level 368: Ready Gladiator 0
Source: https://play.picoctf.org/practice/challenge/368

## Goal
Can you make a CoreWars warrior that always loses, no ties?<br>
Your opponent is the Imp. The source is available here.<br>
https://artifacts.picoctf.net/c/310/imp.red<br>
If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:<br>
nc saturn.picoctf.net 64038 < imp.red

## What I learned
```
Reverse Engineering

Google: Corewars
https://en.wikipedia.org/wiki/Core_War
Opcode	Mnemonic	Argument(s)	Action
0	    DAT	B	    A non-executable instruction used to store the data value B.
1	    MOV	A, B	Move the contents of A to location B.
2	    ADD	A, B	Add the contents of A to the contents of location B and store the result in location B.
3	    SUB	A, B	Subtract the contents of A from the contents of location B and store the result in location B.
4	    JMP	A	    Jump to location A.
5	    JMZ	A, B	If the contents of B is zero, jump to location A; otherwise, continue with the next instruction.
6	    JMG	A, B	If the contents of B is greater than zero, jump to location A; otherwise, continue with the next instruction.
7	    DJZ	A, B	Decrement contents of location B by 1. If location B is now zero, jump to location A; otherwise, continue with next instruction.
8	    CMP	A, B	Compare contents of A with contents of B. If they're not equal, skip next instruction; otherwise, execute the next instruction.

https://corewars.org/index.html
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/310/imp.red ⌨️
--2025-10-01 03:36:21--  https://artifacts.picoctf.net/c/310/imp.red
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45 [application/octet-stream]
Saving to: 'imp.red'

imp.red                                                    100%[======================================================================================================================================>]      45  --.-KB/s    in 0s      

2025-10-01 03:36:22 (43.2 MB/s) - 'imp.red' saved [45/45]

AsianHacker-picoctf@webshell:~$ file imp.red ⌨️
imp.red: ASCII text
AsianHacker-picoctf@webshell:~$ cat imp.red ⌨️
;redcode
;name Imp Ex
;assert 1
mov 0, 1 👀
end

AsianHacker-picoctf@webshell:~$ vi imp.red ⌨️
AsianHacker-picoctf@webshell:~$ cat imp.red ⌨️
;redcode
;name Imp Ex
;assert 1
dat 0, 1
end

AsianHacker-picoctf@webshell:~$ nc saturn.picoctf.net 64038 < imp.red ⌨️
;redcode
;name Imp Ex
;assert 1
dat 0, 1
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
dat 0, 1
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_a7bf8a57} 🔐
```

## Flag
picoCTF{h3r0_t0_z3r0_4m1r1gh7_a7bf8a57}

## Continue
[Continue](./picoGym0369.md)
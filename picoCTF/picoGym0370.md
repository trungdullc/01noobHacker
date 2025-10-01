# picoGym Level 370: Ready Gladiator 2
Source: https://play.picoctf.org/practice/challenge/370

## Goal
Can you make a CoreWars warrior that wins every single round?<br>
Your opponent is the Imp. The source is available here.<br>
https://artifacts.picoctf.net/c/282/imp.red<br>
If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:<br>
nc saturn.picoctf.net 49929 < imp.red<br>
To get the flag, you must beat the Imp all 100 rounds.

## What I learned
```
Reverse Engineering

Google: Corewars for Dummies
https://corewars.org/docs/dummies.html

17 instructions:
    DAT  data
    MOV  move
    ADD  add
    SUB  subtract
    MUL  multiply
    DIV  divide
    MOD  modula (remainder of division)
    JMP  jump
    JMZ  jump if zero
    JMN  jump if not zero
    DJN  decrement, jump if not zero
    SPL  split execution
    SLT  skip if less than
    CMP  compare (see SEQ)
    SEQ  skip if equal
    SNE  skip if not equal
    NOP  no operation

Google: defeat corewar imp 100%
https://www.reddit.com/r/programminggames/comments/11vaxk8/beat_classic_imp_100_of_the_time_in_corewars/
Note: Same as picoGym0379
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/282/imp.red ⌨️
--2025-10-01 15:38:51--  https://artifacts.picoctf.net/c/282/imp.red
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45 [application/octet-stream]
Saving to: 'imp.red'

imp.red                                                    100%[======================================================================================================================================>]      45  --.-KB/s    in 0s      

2025-10-01 15:38:51 (12.2 MB/s) - 'imp.red' saved [45/45]

AsianHacker-picoctf@webshell:~$ cat imp.red ⌨️
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end

AsianHacker-picoctf@webshell:~$ vi imp_gate ⌨️
AsianHacker-picoctf@webshell:~$ nc saturn.picoctf.net 49929 < imp_gate ⌨️ 
;assert 1
gate equ wait-10
wait JMP wait,<gate
end wait
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;assert 1
gate equ wait-10
wait JMP wait,<gate
end wait
end

Rounds: 100
Warrior 1 wins: 100
Warrior 2 wins: 0
Ties: 0
You did it!
picoCTF{d3m0n_3xpung3r_ed173f56} 🔐
```

## Flag
picoCTF{d3m0n_3xpung3r_ed173f56}

## Continue
[Continue](./picoGym0428.md)
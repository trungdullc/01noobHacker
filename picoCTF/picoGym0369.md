# picoGym Level 369: Ready Gladiator 1
Source: https://play.picoctf.org/practice/challenge/369

## Goal
Can you make a CoreWars warrior that wins?<br>
Your opponent is the Imp. The source is available here.<br>
https://artifacts.picoctf.net/c/410/imp.red<br>
If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:<br>
nc saturn.picoctf.net 50643 < imp.red<br>
To get the flag, you must beat the Imp at least once out of the many rounds.

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

https://corewars.org/docs/book1.html
Name:           Imp Gate
Speed:          None
Size:           1
Durability:     Strong
Effectiveness:  Excellent against imps, Extremely Poor against others
Score:

gate equ wait-10 👀
wait JMP wait,<gate 👀
end wait 👀

Imp Gate waits and destroys imps that happen to pass 10 instructions before it. It is seldom overrun by imps and its small size makes it difficult to locate. The imp gate is defensive by nature, and will not win against a stationary enemy unless this enemy self-destructs.
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/410/imp.red
--2025-10-01 03:45:37--  https://artifacts.picoctf.net/c/410/imp.red
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 45 [application/octet-stream]
Saving to: 'imp.red'

imp.red                                                    100%[======================================================================================================================================>]      45  --.-KB/s    in 0s      

2025-10-01 03:45:37 (19.6 MB/s) - 'imp.red' saved [45/45]

AsianHacker-picoctf@webshell:~$ cat imp.red ⌨️
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
AsianHacker-picoctf@webshell:~$ vi imp_gate.red ⌨️
AsianHacker-picoctf@webshell:~$ cat imp_gate.red ⌨️
gate equ wait-10
wait JMP wait,<gate
end wait
end
AsianHacker-picoctf@webshell:~$ nc saturn.picoctf.net 50643 < imp_gate.red ⌨️
gate equ wait-10
wait JMP wait,<gate
end wait
end
Submit your warrior: (enter 'end' when done)

Warrior1:
gate equ wait-10
wait JMP wait,<gate
end wait
end

Warning:
        Missing ';assert'. Warrior may not work with the current setting
Number of warnings: 1

Rounds: 100
Warrior 1 wins: 100
Warrior 2 wins: 0
Ties: 0
You did it!
picoCTF{1mp_1n_7h3_cr055h41r5_0b0942be} 🔐
```

## Flag
picoCTF{1mp_1n_7h3_cr055h41r5_0b0942be}

## Continue
[Continue](./picoGym0370.md)
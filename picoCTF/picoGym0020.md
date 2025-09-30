# picoGym Level 20: asm1
Source: https://play.picoctf.org/practice/challenge/20

## Goal
What does asm1(0x2e0) return? Submit the flag as a hexadecimal value (starting with '0x').<br>
NOTE: Your submission for this question will NOT be in the normal flag format. Source<br>
https://jupiter.challenges.picoctf.org/static/f1c2358ff7d1e9386e41552c549cf2f6/test.S

## What I learned
```
Reverse Engineering

x = 0x2e0 = 736

int asm1(int x) {
    if (x > 0x3fb) {
        if (x == 0x559)
            return x - 0xa;
        else
            return x + 0xa;
    } else {
        if (x == 0x280)
            return x + 0xa;
        else
            return x - 0xa;
    }
}

0x2d6 (decimal 726)
```

## Side Quest
```
asm1:
<+0>:   push   ebp                              ; save old base pointer
<+1>:   mov    ebp,esp                          ; set up new stack frame
<+3>:   cmp    DWORD PTR [ebp+0x8],0x3fb        ; compare arg with 0x3FB (1019)
<+10>:  jg     0x512 <asm1+37>                  ; if > 0x3FB, jump
<+12>:  cmp    DWORD PTR [ebp+0x8],0x280        ; compare arg with 0x280 (640)
<+19>:  jne    0x50a <asm1+29>                  ; if not equal, jump
<+21>:  mov    eax,DWORD PTR [ebp+0x8]          ; load arg into eax
<+24>:  add    eax,0xa                          ; eax = arg + 10
<+27>:  jmp    0x529 <asm1+60>                  ; jump to return
<+29>:  mov    eax,DWORD PTR [ebp+0x8]          ; load arg
<+32>:  sub    eax,0xa                          ; eax = arg - 10
<+35>:  jmp    0x529 <asm1+60>                  ; jump to return
<+37>:  cmp    DWORD PTR [ebp+0x8],0x559        ; compare arg with 0x559 (1369)
<+44>:  jne    0x523 <asm1+54>                  ; if not equal, jump
<+46>:  mov    eax,DWORD PTR [ebp+0x8]          ; load arg
<+49>:  sub    eax,0xa                          ; eax = arg - 10
<+52>:  jmp    0x529 <asm1+60>                  ; jump to return
<+54>:  mov    eax,DWORD PTR [ebp+0x8]          ; load arg
<+57>:  add    eax,0xa                          ; eax = arg + 10
<+60>:  pop    ebp                              ; restore base pointer
<+61>:  ret                                     ; return, result in eax
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/f1c2358ff7d1e9386e41552c549cf2f6/test.S ⌨️
--2025-09-29 21:35:28--  https://jupiter.challenges.picoctf.org/static/f1c2358ff7d1e9386e41552c549cf2f6/test.S
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 638 [application/octet-stream]
Saving to: 'test.S'

test.S                                                     100%[======================================================================================================================================>]     638  --.-KB/s    in 0s      

2025-09-29 21:35:28 (283 MB/s) - 'test.S' saved [638/638]

AsianHacker-picoctf@webshell:~$ cat test.S ⌨️
asm1:
        <+0>:   push   ebp                              # ebp = 0x2e0 = 736
        <+1>:   mov    ebp,esp
        <+3>:   cmp    DWORD PTR [ebp+0x8],0x3fb        # ebp+0x8 = 0x3fb
        <+10>:  jg     0x512 <asm1+37>                  # 0x2e0 > 0x3fb == True
        <+12>:  cmp    DWORD PTR [ebp+0x8],0x280        # ebp+0x8 = 0x280
        <+19>:  jne    0x50a <asm1+29>
        <+21>:  mov    eax,DWORD PTR [ebp+0x8]
        <+24>:  add    eax,0xa
        <+27>:  jmp    0x529 <asm1+60>
        <+29>:  mov    eax,DWORD PTR [ebp+0x8]
        <+32>:  sub    eax,0xa
        <+35>:  jmp    0x529 <asm1+60>
        <+37>:  cmp    DWORD PTR [ebp+0x8],0x559        # 0x2e0 = 0x559
        <+44>:  jne    0x523 <asm1+54>
        <+46>:  mov    eax,DWORD PTR [ebp+0x8]
        <+49>:  sub    eax,0xa                          # eax = 0x2e0 - 0xa = 736 - 10 = 726 (0x2d6)
        <+52>:  jmp    0x529 <asm1+60>
        <+54>:  mov    eax,DWORD PTR [ebp+0x8]
        <+57>:  add    eax,0xa
        <+60>:  pop    ebp                              🔐
        <+61>:  ret 
```

## Flag
0x2d6

## Continue
[Continue](./picoGym0134.md)
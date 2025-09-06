# picoGym Level 21: Tapping
Source: https://play.picoctf.org/practice/challenge/21

## Goal
Theres tapping coming in from the wires<br>
What's it saying nc jupiter.challenges.picoctf.org 48247

## What I learned
```
Morse Codes does not handle { }
A ·-            N -·                0 ----- 
B -···          O ---               1 ·---- 
C -·-·          P ·--·              2 ··---
D -··           Q --·-              3 ···-- 
E ·             R ·-·               4 ····- 
F ··-·          S ···               5 ····· 
G --·           T -                 6 -····
H ····          U ··-               7 --···
I ··            V ···-              8 ---·· 
J ·---          W ·--               9 ----·
K -·-           X -··-
L ·-··          Y -·--
M --            Z --·· 
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 48247 ⌨️
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ..--- -.... .---- ....- ...-- ---.. .---- ---.. .---- }

# Cipher Identifier: https://www.dcode.fr/cipher-identifier ⭐⭐⭐⭐⭐
    Morse Code 👀
    Tap Code Cipher

# Method 1: CyberChef
https://cyberchef.io/#recipe=From_Morse_Code('Space','Line%20feed')&input=Li0tLiAuLiAtLi0uIC0tLSAtLi0uIC0gLi4tLiB7IC0tIC0tLS0tIC4tLiAuLi4gLi4uLS0gLS4tLiAtLS0tLSAtLi4gLi4uLS0gLi0tLS0gLi4uIC4uLS4gLi4tIC0uIC4tLS0tIC4uLS0tIC0uLi4uIC4tLS0tIC4uLi4tIC4uLi0tIC0tLS4uIC4tLS0tIC0tLS4uIC4tLS0tIH0 ⌨️
    PICOCTFM0RS3C0D31SFUN1261438181 🔐
```

## Flag
PICOCTF{M0RS3C0D31SFUN1261438181}

## Continue
[Continue](./picoGym0162.md)
# picoGym Level 68: The Numbers
Source: https://play.picoctf.org/practice/challenge/68

## Goal
The numbers... what do they mean?<br>
https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png<br>
16 9 3 15 3 20 6 { 20 8 5 <br>
14 21 13 2 5 18 19 13 1 <br>
19 15 14 }

## What I learned
```
https://www.dcode.fr/cipher-identifier

Substitution Cipher based on Letter Number (A1Z26)
  A = 1
  Z = 26
```

## Solution
```
https://webshell.picoctf.org/

# Identify: https://www.dcode.fr/cipher-identifier ⭐⭐⭐
  Letter Number Code (A1Z26) A=1, B=2, C=3 👀
# Browser: https://www.dcode.fr/letter-number-cipher ⌨️
  [A1Z26]	PICOCTFTHENUMBERSMASON 🕵️‍♀️

# CyberChef
https://cyberchef.io/#recipe=A1Z26_Cipher_Decode('Space')&input=MTYgOSAzIDE1IDMgMjAgNiB7IDIwIDggNSAxNCAyMSAxMyAyIDUgMTggMTkgMTMgMSAxOSAxNSAxNCB9 ⌨️
  picoctf.thenumbersmason. 🕵️‍♀️
```

## Flag
PICOCTF{THENUMBERSMASON}

## Continue
[Continue](./picoGym0418.md)
# picoGym Level 0086: 2Warm
Source: https://play.picoctf.org/practice/challenge/86

## Goal
Can you convert the number 42 (base 10) to binary (base 2)?

## What I learned
```
RapidTables: https://www.rapidtables.com/convert/number/decimal-to-binary.html?x=42
Binary number (6 digits)
101010
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ python3 -c "print(bin(42))" ⌨️
0b101010

# Modify Answer
picoCTF{101010} 🔐
```

## Flag
picoCTF{101010}

## Continue
[Continue](./picoGym0243.md)
# picoGym Level 0414: endianness
Source: https://play.picoctf.org/practice/challenge/414

## Goal
Know of little and big endian?<br>
nc titan.picoctf.net 52975

## What I learned
```
num = 305419896                             # 0x12345678

# Big-endian                                # Little-endian (most x86 systems)
print(num.to_bytes(4, "big"))               print(num.to_bytes(4, "little"))

b'\x12\x34\x56\x78'                         b'\x78\x56\x34\x12'

data = b'\x12\x34\x56\x78'                  # Need data to be reversed
print(int.from_bytes(data, "big"))          print(int.from_bytes(data, "little"))
# 305419896                                 # Note: 2018915346 ⚠️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc titan.picoctf.net 52975 ⌨️
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: elbvx                                                                         # Note: This word changes, got to be fast
Enter the Little Endian representation: 7876626c65 ⌨️            
Correct Little Endian representation!
Enter the Big Endian representation: 656c627678 ⌨️
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_91bc76a4} 🔐

# Big Endian
https://cyberchef.io/#recipe=To_Hex('None',0)&input=ZWxidng
# Little Endian
# https://cyberchef.io/#recipe=Reverse('Character')To_Hex('None',0)&input=ZWxidng
```

## Flag
picoCTF{3ndi4n_sw4p_su33ess_91bc76a4}

## Continue
[Continue](./picoGym0238.md)
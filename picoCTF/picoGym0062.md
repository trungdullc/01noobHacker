# picoGym Level 62: 13
Source: https://play.picoctf.org/practice/challenge/62

## Goal
Cryptography can be easy, do you know what ROT13 is?<br>
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

## What I learned
```
ROT 13
```

## Solution
```
https://webshell.picoctf.org/

Method 1: CyberChef
https://cyberchef.io/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3thYmdfZ2JiX29ucV9ic19uX2NlYm95cnp9 ⌨️
  picoCTF{not_too_bad_of_a_problem} 🔐

Method 2: tr
AsianHacker-picoctf@webshell:~$ echo "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}" | tr 'A-Za-z' 'N-ZA-Mn-za-m' ⌨️
picoCTF{not_too_bad_of_a_problem} 🔐

Method 3: https://www.dcode.fr/cipher-identifier
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz} 👀
  ROT13
https://www.dcode.fr/rot-13-cipher
  picoCTF{not_too_bad_of_a_problem} 🔐

Method 4: Custom python script
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3

def decode_rot13() -> None:
    alpha_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha_lower.upper()
    cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
    message = ""

    for letter in cipher:
        if letter in alpha_lower:
            message += alpha_lower[alpha_lower.index(letter)+13]
        elif letter in alpha_upper:
            message += alpha_upper[alpha_upper.index(letter)+13]
        else:
            message += letter
    print(message)

if __name__ == "__main__":
    decode_rot13()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️ 
picoCTF{not_too_bad_of_a_problem} 🔐
```

## Flag
picoCTF{not_too_bad_of_a_problem}

## Continue
[Continue](./picoGym0068.md)
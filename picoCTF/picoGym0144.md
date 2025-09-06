# picoGym Level 144: Mod 26
Source: https://play.picoctf.org/practice/challenge/144

## Goal
Cryptography can be easy, do you know what ROT13 is?<br>
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}

## What I learned
```
Cryptography

ROT13
```

## Solution
```
https://webshell.picoctf.org/

Method 1: CyberChef
https://cyberchef.io/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3thcmtnX2d2enJfVid5eV9nZWxfMl9lYmhhcWZfYnNfZWJnMTNfaHlMaWNJbnR9 ⌨️
  picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag} 🔐

Method 2: tr
AsianHacker-picoctf@webshell:~$ echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}" | tr 'A-Za-z' 'N-ZA-Mn-za-m' ⌨️
picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag} 🔐

Method 3: https://www.dcode.fr/cipher-identifier
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt} 👀
  ROT13
https://www.dcode.fr/rot-13-cipher
  picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag} 🔐

Method 4: Custom python script
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3

def decode_rot13() -> None:
    alpha_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha_lower.upper()
    cipher = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
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
picoCTF{next_time_I'll_try_2_rounds_of_rot13_aFxtzQWR} 🔐
```

## Flag
picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}

## Continue
[Continue](./picoGym0062.md)
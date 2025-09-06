# picoGym Level 307: substitution0
Source: https://play.picoctf.org/practice/challenge/307

## Goal
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?<br>
Download the message here<br>
https://artifacts.picoctf.net/c/154/message.txt

## What I learned
```
Substitution Cipher

Caesar cipher (a special case)
    A shift of the alphabet by k

Homophonic substitution
    One plaintext letter can map to multiple possible symbols (to hide frequency patterns)

Polyalphabetic substitution
    Uses multiple different substitution alphabets (Vigenère cipher)

Simple substitution is easy to break using frequency analysis, since some letters (like E, T, A) occur far more often in English

ZGSOCXPQUYHMILERVTBWNAFJDKzgsocxpquyhmilervtbwnafjdk: encrypted
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz: key

Google: cryptogram solver (will find key if do ABCDEFGHIJKLMNOPQRSTUVWXYZ)
https://www.quipqiup.com/ ⭐⭐⭐⭐⭐
Cipher Identifier (Not used): https://www.dcode.fr/cipher-identifier ⭐⭐⭐
Frequency Analysis (Not used): https://www.dcode.fr/frequency-analysis ⭐⭐⭐
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/154/message.txt ⌨️
--2025-09-06 03:50:14--  https://artifacts.picoctf.net/c/154/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 670 [application/octet-stream]
Saving to: 'message.txt'

message.txt                                                100%[======================================================================================================================================>]     670  --.-KB/s    in 0s      

2025-09-06 03:50:14 (165 MB/s) - 'message.txt' saved [670/670]

AsianHacker-picoctf@webshell:/tmp$ cat message.txt ⌨️
ZGSOCXPQUYHMILERVTBWNAFJDK 👀

Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX} 👀

Method 1: https://www.dcode.fr/monoalphabetic-substitution
Alphabetic substitution ciphertext: 
Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX} ⌨️

Other decryption methods
Knowing the substitution alphabet:
ZGSOCXPQUYHMILERVTBWNAFJDK ⌨️
DECRYPT

The flag is: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF} 🔐

# Method 2: mapping w/ python
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
import string

# Key from ciphertext (first line)
key = "ZGSOCXPQUYHMILERVTBWNAFJDK"
alphabet = string.ascii_uppercase

# Build mapping: cipher -> plain
decode_map = {key[i]: alphabet[i] for i in range(26)}

def substitution_decrypt(text: str) -> str:
    result = []
    for ch in text:
        if ch.upper() in decode_map:
            # preserve case
            plain = decode_map[ch.upper()]
            result.append(plain.lower() if ch.islower() else plain)
        else:
            result.append(ch)
    return "".join(result)

ciphertext = """Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}"""

print(substitution_decrypt(ciphertext))

AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️ 
Hereupon Legrand arose, with a grave and stately air, and brought me the beetle
from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at
that time, unknown to naturalists—of course a great prize in a scientific point
of view. There were two round black spots near one extremity of the back, and a
long one near the other. The scales were exceedingly hard and glossy, with all the
appearance of burnished gold. The weight of the insect was very remarkable, and,
taking all things into consideration, I could hardly blame Jupiter for his opinion
respecting it.

The flag is: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF} 🔐

Method 3: Another mapping w/ python
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python3 
import string

with open("message.txt") as fileptr:
    contents = fileptr.read()

uppercase_key = "ZGSOCXPQUYHMILERVTBWNAFJDK"
lowercase_key = uppercase_key.lower()

def substitution_solver() -> None:
    for character in contents:
        if character.isupper():
            position = uppercase_key.index(character)
            print(string.ascii_uppercase [position], end="")
        elif character.islower():
            position = lowercase_key.index (character)
            print(string.ascii_lowercase [position], end="")
        else:
            print(character, end="")

def main() -> None:
    substitution_solver()

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
ABCDEFGHIJKLMNOPQRSTUVWXYZ 

Hereupon Legrand arose, with a grave and stately air, and brought me the beetle
from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at
that time, unknown to naturalists—of course a great prize in a scientific point
of view. There were two round black spots near one extremity of the back, and a
long one near the other. The scales were exceedingly hard and glossy, with all the
appearance of burnished gold. The weight of the insect was very remarkable, and,
taking all things into consideration, I could hardly blame Jupiter for his opinion
respecting it.

The flag is: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF} 🔐
```

## Flag
picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}

## Continue
[Continue](./picoGym0307.md)
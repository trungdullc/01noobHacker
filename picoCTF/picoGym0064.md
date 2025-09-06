# picoGym Level 64: caesar
Source: https://play.picoctf.org/practice/challenge/64

## Goal
Decrypt this message<br>
https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext

## What I learned
```
Caesar Cipher: shift each letter of the alphabet by a fixed number
There's only 26 possibilities for a Caesar cipher
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext ⌨️
--2025-09-05 00:39:36--  https://jupiter.challenges.picoctf.org/static/7d707a443e95054dc4cf30b1d9522ef0/ciphertext
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 35 [application/octet-stream]
Saving to: 'ciphertext'

ciphertext                                                 100%[======================================================================================================================================>]      35  --.-KB/s    in 0s      

2025-09-05 00:39:36 (15.2 MB/s) - 'ciphertext' saved [35/35]

AsianHacker-picoctf@webshell:/tmp$ file ciphertext ⌨️
ciphertext: ASCII text, with no line terminators
AsianHacker-picoctf@webshell:/tmp$ cat ciphertext ⌨️
picoCTF{gvswwmrkxlivyfmgsrhnrisegl} 👀

ChatGPT: 
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python
cipher = "gvswwmrkxlivyfmgsrhnrisegl"

def rot_finder() -> None:
    for shift in range(26):
        plaintext = ""
        for c in cipher:
            if c.isalpha():
                # shift letters (wrap around a-z)
                plaintext += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            else:
                plaintext += c
        print(f"Shift {shift:2}: {plaintext}")

def main() -> None:
    rot_finder()
    
if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
Shift  0: gvswwmrkxlivyfmgsrhnrisegl
Shift  1: hwtxxnslymjwzgnhtsiosjtfhm
Shift  2: ixuyyotmznkxahoiutjptkugin
Shift  3: jyvzzpunaolybipjvukqulvhjo
Shift  4: kzwaaqvobpmzcjqkwvlrvmwikp
Shift  5: laxbbrwpcqnadkrlxwmswnxjlq
Shift  6: mbyccsxqdrobelsmyxntxoykmr
Shift  7: nczddtyrespcfmtnzyouypzlns
Shift  8: odaeeuzsftqdgnuoazpvzqamot
Shift  9: pebffvatgurehovpbaqwarbnpu
Shift 10: qfcggwbuhvsfipwqcbrxbscoqv
Shift 11: rgdhhxcviwtgjqxrdcsyctdprw
Shift 12: sheiiydwjxuhkrysedtzdueqsx
Shift 13: tifjjzexkyvilsztfeuaevfrty
Shift 14: ujgkkafylzwjmtaugfvbfwgsuz
Shift 15: vkhllbgzmaxknubvhgwcgxhtva
Shift 16: wlimmchanbylovcwihxdhyiuwb
Shift 17: xmjnndiboczmpwdxjiyeizjvxc
Shift 18: ynkooejcpdanqxeykjzfjakwyd
Shift 19: zolppfkdqeboryfzlkagkblxze
Shift 20: apmqqglerfcpszgamlbhlcmyaf
Shift 21: bqnrrhmfsgdqtahbnmcimdnzbg
Shift 22: crossingtherubicondjneoach 🔐
Shift 23: dspttjohuifsvcjdpoekofpbdi
Shift 24: etquukpivjgtwdkeqpflpgqcej
Shift 25: furvvlqjwkhuxelfrqgmqhrdfk

Manual w/ CyberChef:
    https://cyberchef.io/#recipe=ROT13(true,true,false,22)&input=Z3Zzd3dtcmt4bGl2eWZtZ3NyaG5yaXNlZ2w ⌨️

Manual via Terminal:
AsianHacker-picoctf@webshell:/tmp$ echo "gvswwmrkxlivyfmgsrhnrisegl" | tr 'a-z' 'w-za-v' ⌨️
crossingtherubicondjneoach 🔐
```

## Flag
picoCTF{crossingtherubicondjneoach}

## Continue
[Continue](./picoGym0031.md)
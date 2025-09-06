# picoGym Level 162: Mind your Ps and Qs
Source: https://play.picoctf.org/practice/challenge/162

## Goal
In RSA, a small e value can be problematic, but what about N?<br>
Can you decrypt this?<br>
https://mercury.picoctf.net/static/12d820e355a7775a2c9129b2622a7eb6/values

## What I learned
```
The public key gives you n and e
The private key requires knowing d, which is calculated using φ(n) = (p−1)(q−1) 👀
But to get φ(n), you need to know p and q
Breaking RSA = factorizing n

Given a large number n, integer factorization means finding which prime numbers multiply together to make n
    n is the modulus
    n = 77 = p × q
    factors: 7 × 11
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/12d820e355a7775a2c9129b2622a7eb6/values ⌨️
--2025-09-05 07:46:57--  https://mercury.picoctf.net/static/12d820e355a7775a2c9129b2622a7eb6/values
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 206 [application/octet-stream]
Saving to: 'values'

values                                                     100%[======================================================================================================================================>]     206  --.-KB/s    in 0s      

2025-09-05 07:46:57 (178 MB/s) - 'values' saved [206/206]

AsianHacker-picoctf@webshell:/tmp$ file values ⌨️
values: ASCII text
AsianHacker-picoctf@webshell:/tmp$ cat values ⌨️
Decrypt my super sick RSA:
c: 843044897663847841476319711639772861390329326681532977209935413827620909782846667 👀
n: 1422450808944701344261903748621562998784243662042303391362692043823716783771691667 👀
e: 65537 👀

# Method 1: RSA Decoder: https://www.dcode.fr/rsa-cipher ⭐⭐⭐⭐⭐
    picoCTF{sma11_N_n0_g0od_00264570} 🔐

# Method 2: Solving p & q manually
# Integer Factorization Calculator: https://www.alpertron.com.ar/ECM.HTM (9 min wait) ⭐
# Add n to textbox and press Factor

Results:
1422 450808 944701 344261 903748 621562 998784 243662 042303 391362 692043 823716 783771 691667 (82 digits) = 2159 947535 959146 091116 171018 558446 546179 (40 digits)👀 × 658558 036833 541874 645521 278345 168572 231473 (42 digits)👀

AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3

# Source: stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# modified code below, find p & q
def solve_flag() -> None:
    p = 2159947535959146091116171018558446546179
    q = 658558036833541874645521278345168572231473
    n = p * q
    phi = (p-1)*(q-1)           # can solve for phi when p and q known

    e = 65537
    d = modinv(e, phi)
    c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
    plain = pow(c,d, n)
    print(plain)
    print(hex(plain))
    print(bytearray.fromhex(hex(plain)[2:]).decode())

def main() -> None:
    solve_flag()

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
13016382529449106065927291425342535437996222135352905256639555294957886055592061
0x7069636f4354467b736d6131315f4e5f6e305f67306f645f30303236343537307d
picoCTF{sma11_N_n0_g0od_00264570} 🔐

Method 3: https://github.com/tadryanom/Ganapati_RsaCtfTool ⭐⭐⭐
# Note: Offline version of https://www.dcode.fr/rsa-cipher
# Install first
python3 RsaCtfTool.py ⌨️
python3 RsaCtfTool.py -n 1422450808944701344261903748621562998784243662042303391362692043823716783771691667 -e 65537 --uncipher 843044897663847841476319711639772861390329326681532977209935413827620909782846667 ⌨️

utf-8: picoCTF{sma11_N_n0_g0od_00264570} 🔐
```

## Flag
picoCTF{sma11_N_n0_g0od_00264570}

## Continue
[Continue](./picoGym0253.md)
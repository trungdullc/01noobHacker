# picoGym Level 470: EVEN RSA CAN BE BROKEN???
Source: https://play.picoctf.org/practice/challenge/470

## Goal
This service provides you an encrypted flag. Can you decrypt it with just N & e?<br>
Connect to the program with netcat:<br>
$ nc verbal-sleep.picoctf.net 63695<br>
The program's source code can be downloaded here<br>
https://challenge-files.picoctf.net/c_verbal_sleep/2b0f68c54cfcb2dafd4ca90c4abcbe73c208f09edf65af336fc7023e1c1314ca/encrypt.py

## What I learned
```
RSA (Rivest, Shamir, and Adleman who invented it in 1977) is an asymmetric encryption algorithm

That means it uses two different keys:
    Public key → can be shared with anyone (used to encrypt or verify)
    Private key → kept secret (used to decrypt or sign)

Key generation
    Pick two large prime numbers, p and q
    Multiply them: n = p * q
    Choose an exponent e (public)
    Compute the private exponent d
Your keys are:
    Public key = (e, n)
    Private key = (d, n)

To encrypt a message M:
    C = M^e mod n
To decrypt:
    M = C^d mod n

RSA modulus weak because used 2 as one of its primes (bad practice)
Youtube Solution: https://www.youtube.com/watch?v=6wQaf8jgTjk
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://challenge-files.picoctf.net/c_verbal_sleep/2b0f68c54cfcb2dafd4ca90c4abcbe73c208f09edf65af336fc7023e1c1314ca/encrypt.py ⌨️
--2025-09-04 15:54:05--  https://challenge-files.picoctf.net/c_verbal_sleep/2b0f68c54cfcb2dafd4ca90c4abcbe73c208f09edf65af336fc7023e1c1314ca/encrypt.py
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.18, 3.160.5.95, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 703 [application/octet-stream]
Saving to: 'encrypt.py'

encrypt.py                                                 100%[======================================================================================================================================>]     703  --.-KB/s    in 0s      

2025-09-04 15:54:05 (210 MB/s) - 'encrypt.py' saved [703/703]

AsianHacker-picoctf@webshell:/tmp$ cat encrypt.py ⌨️
from sys import exit
from Crypto.Util.number import bytes_to_long, inverse
from setup import get_primes

e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag):
    pubkey, _privkey = gen_key(1024)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    N, cypher  = main(flag)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()

AsianHacker-picoctf@webshell:/tmp$ python3 encrypt.py ⌨️ 
Traceback (most recent call last):
  File "/tmp/encrypt.py", line 3, in <module>
    from setup import get_primes
ModuleNotFoundError: No module named 'setup'

AsianHacker-picoctf@webshell:/tmp$ nc verbal-sleep.picoctf.net 63695 ⌨️
N: 25037474239035258096014739231159950626707312819481617522986435958886040311217803931906134820182817937158673916330863748467339449950686811130345208537763546
e: 65537
cyphertext: 18132301254987859542925321395736446544117085698506348109810744484211384555774624572596515676421384959329448434906971414033878904773150983604703475617789913

AsianHacker-picoctf@webshell:/tmp$ nc verbal-sleep.picoctf.net 63695 ⌨️
N: 25943347427469742633543868581112201692807379808861277038169977554523758428461072340140289553834445538156559599148948636300189015474181329614032042760225034
e: 65537
cyphertext: 4984477605019949896413407854002111847331170724466869784447813321593096972193739231041486486398225713828098091565249824540086884991570110154548744649198003

AsianHacker-picoctf@webshell:/tmp$ nc verbal-sleep.picoctf.net 63695 ⌨️
N: 19861500293951958605163557215257740609665469231151468147565147286216228811757116428864645644898165018622334509769636510632397412728348815732693023991320854
e: 65537
cyphertext: 5300451116843914896482907434894806628130786465477232351436105550290809582255984888950437802449420669781063419702177627088196779111702244898482139428214587

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
# RSA Weak Key Attack
# In this challenge, one of the primes (p) was set to 2
# That makes factoring N trivial: N = p * q = 2 * q
# Once N is factored, we can recover the private key and decrypt the ciphertext

from Crypto.Util.number import long_to_bytes

# RSA public key modulus (N) given in the challenge
N = 22952767426310255116948069979828903923176912862995126428957200057833691132544816333101206252253814833951686520908362571114738760042764047607726784642073434

# RSA public exponent (e) - standard value
e = 65537

# RSA ciphertext given in the challenge
c = 700406502525108084791799270348672159219758358780880299048896254769487055031493945930484575728341052482800279944604336191947025602241107050228507777853749

# ----------------------------------------------------------
# Step 1: Factor N
# Since N is even, we can check if one factor is 2 by dividing.
p = 2
q = N // p  # q must be the other prime factor

print(f"[+] Factors found: p = {p}, q = {q}")

# ----------------------------------------------------------
# Step 2: Compute φ(N)
# φ(N) = (p-1)*(q-1). When p = 2, this simplifies to (q-1).
phi_N = (p - 1) * (q - 1)
print(f"[+] φ(N) = {phi_N}")

# ----------------------------------------------------------
# Step 3: Compute private key exponent d
# d is the modular inverse of e modulo φ(N).
d = pow(e, -1, phi_N)
print(f"[+] Private key exponent d = {d}")

# ----------------------------------------------------------
# Step 4: Decrypt the ciphertext
# m = c^d mod N
m = pow(c, d, N)
print(f"[+] Decrypted integer m = {m}")

# ----------------------------------------------------------
# Step 5: Convert integer back to bytes
# RSA messages are encoded as integers, so we need to convert back.
flag = long_to_bytes(m)
print(f"[+] Flag: {flag}")

AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️ 
[+] Factors found: p = 2, q = 11476383713155127558474034989914451961588456431497563214478600028916845566272408166550603126126907416975843260454181285557369380021382023803863392321036717
[+] φ(N) = 11476383713155127558474034989914451961588456431497563214478600028916845566272408166550603126126907416975843260454181285557369380021382023803863392321036716
[+] Private key exponent d = 9170144893827831070305473096370754014869504218200907775037014933767008739627801065928489767702027262535269908909533719590197328586595548171825293584932629
[+] Decrypted integer m = 3030612722376619015339251852200174143198160267119207878925874759940477
[+] Flag: b'picoCTF{tw0_1$_pr!m31c9046c4}' 🔐

Method 2: RSA Decipher Online: https://www.dcode.fr/rsa-cipher
picoCTF{tw0_1$_pr!m31c9046c4} 🔐
```

## Flag
picoCTF{tw0_1$_pr!m31c9046c4}

## Continue
[Continue](./picoGym0043.md)
# picoGym Level 210: spelling-quiz
Source: https://play.picoctf.org/practice/challenge/210

## Goal
I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.<br>
https://artifacts.picoctf.net/picoMini+by+redpwn/Cryptography/spelling-quiz/public.zip

## What I learned
```
encrypt.py              monoalphabetic substitution cipher (simple substitution)
                        encrypt contents of all .txtfiles in current directory and subdirectories
flag.txt                encrypted flag

If don’t know original plaintexts of study-guide.txt
    then need frequency analysis or crib-dragging

Since key(dictionary) for this substitution cipher is produced randomly, unable to reverse-engineer to find key
Frequency Analysis: https://www.101computing.net/frequency-analysis/
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/picoMini+by+redpwn/Cryptography/spelling-quiz/public.zip ⌨️
--2025-09-11 03:27:03--  https://artifacts.picoctf.net/picoMini+by+redpwn/Cryptography/spelling-quiz/public.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1449681 (1.4M) [binary/octet-stream]
Saving to: 'public.zip'

public.zip                                                 100%[======================================================================================================================================>]   1.38M  1.83MB/s    in 0.8s    

2025-09-11 03:27:04 (1.83 MB/s) - 'public.zip' saved [1449681/1449681]

AsianHacker-picoctf@webshell:/tmp$ unzip public.zip ⌨️
Archive:  public.zip
   creating: public/
  inflating: public/encrypt.py       
  inflating: public/study-guide.txt  
 extracting: public/flag.txt
AsianHacker-picoctf@webshell:/tmp$ rm public.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ cd public/ ⌨️
AsianHacker-picoctf@webshell:/tmp/public$ ls ⌨️
encrypt.py  flag.txt  study-guide.txt
AsianHacker-picoctf@webshell:/tmp/public$ head -n 10 study-guide.txt ⌨️
gocnfwnwtr
sxlyrxaic
dcrrtfrxcv
uxbvwavcq
lwvicwtiwm
pwtmwnxvicq
avingciisa
ylwtmrcawx
mwaxdcrrxuwlwvq
yciflwnf
AsianHacker-picoctf@webshell:/tmp/public$ cat encrypt.py ⌨️
import random
import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]

alphabet = list('abcdefghijklmnopqrstuvwxyz') 👀
random.shuffle(shuffled := alphabet[:]) 👀
dictionary = dict(zip(alphabet, shuffled)) 👀

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)
AsianHacker-picoctf@webshell:/tmp/public$ cat flag.txt 
brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm
AsianHacker-picoctf@webshell:/tmp/public$ wc -l study-guide.txt ⌨️
272543 study-guide.txt

# Method 1:
https://www.dcode.fr/cipher-identifier
    Hill Cipher	
    Substitution Cipher 👀
https://www.dcode.fr/monoalphabetic-substitution

Results:
PERHAPS_THE_DOG_JUMPED_OVER_WAS_JUST_TIRED 🔐 KURCHICINE MALFEASOR GREENHEART BAPTISTRY LITORINOID VINDICATORY STOCKROOMS FLINDERSIA DISAGREEABILITY FROHLICH DISAMENITY OUTSPARSPYING PREINCLINATION MELANIZING PREOBEDIENT CHLORALFORMAMIDE NONELECTROLYTIC ASCERTAINABLE THORACOPLASTIES PINNACLET PAPERWEIGHTS INCARNATION NONPUERILITY UNPREFINED BRASSLIKE

# Method 2:
https://www.boxentriq.com/code-breaking/substitution-cipher
brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm
gocnfwnwtr
sxlyrxaic
dcrrtfrxcv
uxbvwavcq
lwvicwtiwm
pwtmwnxvicq
avingciisa
ylwtmrcawx
mwaxdcrrxuwlwvq
yciflwnf
mwaxsrtwvq
iovabxcabqwtd
bcrwtnlwtxvwit
srlxtwkwtd
bcriurmwrtv
nflicxlyicsxswmr
titrlrnvcilqvwn
xanrcvxwtxulr
vficxniblxavwra
bwttxnlrv
bxbrcerwdfva
wtnxctxvwit
titborcwlwvq
otbcrywtrm
ucxaalwgr

Score	    Text
23725       perhaps the dog jumped over was just tired 👀 kurchicine malfeasor greenheart baptistry litorinoid vindicatory stockrooms flindersia disagreeability frohlich disamenity outsparspying preinclination melanizing preobedient chloralformamide nonelectrolytic ascertainable thoracoplasties pinnaclet paperweights incarnation nonpuerility unprefined brasslike

Method 3:
# Frequency Analysis
AsianHacker-picoctf@webshell:/tmp/public$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
from collections import Counter

def main() -> None:
    with open("study-guide.txt") as f:
        text = f.read()

    # keep only alphabetic characters
    letters = [c for c in text.lower() if c.isalpha()]

    counts = Counter(letters)

    # show results sorted by most common
    for letter, freq in counts.most_common():
        print(f"{letter}: {freq}")

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:/tmp/public$ chmod +x pythonScript.py ⌨️❤️
AsianHacker-picoctf@webshell:/tmp/public$ ./pythonScript.py ⌨️
r: 311363
w: 270080
x: 239284
t: 216936
i: 214772
a: 206355
c: 205401
v: 198197
l: 162351
n: 131465
o: 107082
b: 96529
m: 90628
s: 87009
f: 76513
d: 66435
q: 57699
u: 49432
y: 30493
p: 27458
g: 17173
e: 14940
k: 11862
z: 8354
j: 4794
h: 3251

# Doing online using partial list
https://www.dcode.fr/frequency-analysis
W	36×	11.36%	
R	32×	10.09%	
C	27×	8.52%	
X	26×	8.2%	
T	25×	7.89%	
V	23×	7.26%	
I	21×	6.62%	
A	18×	5.68%	
L	16×	5.05%	
B	14×	4.42%	
N	13×	4.1%	
M	11×	3.47%	
F	9×	2.84%	
S	7×	2.21%	
Q	7×	2.21%	
D	6×	1.89%	
O	6×	1.89%	
Y	5×	1.58%	
U	5×	1.58%	
G	3×	0.95%	
H	2×	0.63%	
P	2×	0.63%	
E	2×	0.63%	
K	1×	0.32%	
 
https://www.quipqiup.com/
# Note: Use clues if not found
# Clue: r = e ❤️
0	-2.372	perhaps_the_dog_jumped_over_was_just_tired 🔐 kurchicine malfeasor greenheart baptistry litorinoid vindicatory stockrooms flindersia disagreeability frohlich disamenity outsparspying preinclination melanizing preobedient chloralformamide nonelectrolytic ascertainable thoracoplasties pinnaclet paperweights incarnation nonpuerility unprefined brasslike
```

## Flag
picoCTF{perhaps_the_dog_jumped_over_was_just_tired}

## Continue
[Continue](./picoGym0006.md)
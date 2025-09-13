# picoGym Level 407: C3
Source: https://play.picoctf.org/practice/challenge/407

## Goal
This is the Custom Cyclical Cipher!<br>
Download the ciphertext here.<br>
https://artifacts.picoctf.net/c_titan/47/ciphertext<br>
Download the encoder here.<br>
https://artifacts.picoctf.net/c_titan/47/convert.py<br>
Enclose the flag in our wrapper for submission. If the flag was "example" you would submit "picoCTF{example}".

## What I learned
```
python2 and python3
python3 with
```

## Solution
```
https://webshell.picoctf.org/

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat ciphertext ⌨️
DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat convert.py ⌨️
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur = lookup1.index(char)
  out += lookup2[(cur - prev) % 40]
  prev = cur

sys.stdout.write(out)

# Reverse Engineer into terminal
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\pythonScript.py ⌨️
ciphertext = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"
lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

prev = 0
recovered = ""
for char in ciphertext:
    idx_o = lookup2.index(char)
    cur = (idx_o + prev) % 40
    recovered += lookup1[cur]
    prev = cur

print(recovered)

# Note: Result (plaintext is Python2 script):
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python.exe .\pythonScript.py
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1

# Decode w/ python script w/ hardcoded string named chars
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\pythonScript.py ⌨️
chars = """#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input   
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):   
    if i == b * b * b:        
        print chars[i] #prints
        b += 1 / 1
"""

b = 1
out = []
for i in range(len(chars)):
    if i == b * b * b:
        out.append(chars[i])
        b += 1

print("".join(out))

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python.exe .\pythonScript.py ⌨️
adlibs 🔐

Method 2: Reverse Engineer into file named plain.py
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python .\pythonScript.py ⌨️
Decryption complete → plain.py
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\pythonScript.py ⌨️
#!/usr/bin/env python3

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"  

# read ciphertext from file
with open("ciphertext", "r", encoding="utf-8") as f:  
    ciphertext = f.read().strip()

prev = 0
recovered = ""
for char in ciphertext:
    idx_o = lookup2.index(char)
    cur = (idx_o + prev) % 40
    recovered += lookup1[cur]
    prev = cur

# write output to plain.py
with open("plain.py", "w", encoding="utf-8") as f:    
    f.write(recovered)

print("Decryption complete â†’ plain.py")

# Decode plain.py
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> cat .\pythonScript.py ⌨️
#!/usr/bin/env python3
#asciiorder
#fortychars
#selfinput
#pythontwo

with open("plain.py", "r") as f:  
        chars = f.read()

# chars = ""
# from fileinput import input
# for line in input():
#    chars += line
flag = ""
for i in range(len(chars)):
        if i == b * b * b:
                print(chars[i]) #prints, Note: needed to fix add ()
                flag += chars[i]
                b += 1 / 1

print(f"picoCTF{{{flag}}}")

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python.exe .\pythonScript.py ⌨️
a
d
l
i
b
s 👀
picoCTF{adlibs} 🔐
```

## Flag
picoCTF{adlibs}

## Continue
[Continue](./picoGym0422.md)
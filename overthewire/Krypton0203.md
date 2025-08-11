# Krypton Level 2 → Level 3 Known Ciphertext Attack

## Previous Flag
<b>CAESARISEASY</b>

## Goal
Use previous password to log in to <b>krypton.labs.overthewire.org</b> with username <b>krypton3</b> using SSH on <b>port 2231</b>. In this example, the <b>cipher mechanism is not available to you</b>. You have <b>intercepted more than one message</b>. Password is found in the <b>file krypton4</b>. You have also found 3 other files (found1, found2, found3).

You know the following important details:
The message plaintexts are in American English (*** very important) - They were produced from the same key (*** even better!)

## What I learned
```
Frequency Analysis      A classic cryptanalysis method for breaking substitution ciphers
In English:
    Most common letter is E (followed by T, A, O, I, N)
Can also analyze bigrams (2-letter combos like TH, HE, IN) or trigrams (THE, AND, ING) to refine guesses

Cryptography: http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
Letter/Word Frequency List: https://letterfrequency.org/
    Letter Frequency in the English Language: etaoinsrhldcumfpgwybvkxjqz

Freq Analysis Tool: https://www.dcode.fr/frequency-analysis (copy file1 file2 file3) ⭐⭐⭐⭐⭐
    Items to Analyze: Trigrams (set of 3 characters, THE) will be useful
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh krypton3@krypton.labs.overthewire.org -p 2231 ⌨️
krypton3@krypton:~$ cd /krypton/krypton3/ ⌨️
krypton3@krypton:/krypton/krypton3$ ls -la ⌨️
total 36
drwxr-xr-x 2 root     root     4096 Jul 28 19:05 .       
drwxr-xr-x 9 root     root     4096 Jul 28 19:05 ..      
-rw-r----- 1 krypton3 krypton3 1542 Jul 28 19:05 found1  
-rw-r----- 1 krypton3 krypton3 2128 Jul 28 19:05 found2  
-rw-r----- 1 krypton3 krypton3  560 Jul 28 19:05 found3  
-rw-r----- 1 krypton3 krypton3   56 Jul 28 19:05 HINT1   
-rw-r----- 1 krypton3 krypton3   37 Jul 28 19:05 HINT2   
-rw-r----- 1 krypton3 krypton3   42 Jul 28 19:05 krypton4
-rw-r----- 1 krypton3 krypton3  785 Jul 28 19:05 README
krypton3@krypton:/krypton/krypton3$ cat krypton4 ⌨️
KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS 🧠
krypton3@krypton:/krypton/krypton3$ for i in {A..Z}; do cat found1 found2 found3 | tr -cd $i | wc -c | tr -d '\n'; printf " $i \n"; done | sort -nr ⌨️
456 S 
340 Q 
301 J 
257 U 
246 B 
240 N 
227 G 
227 C 
210 D 
132 Z 
130 V 
129 W 
86 M  
84 Y  
75 T 
71 X 
67 K 
64 E 
60 L 
55 A 
28 F 
19 I 
12 O
4 R
4 H
2 P

# Assume encrpytion E → S (since E the most common char in English), map the above
S → E  
Q → T  
J → A  
U → O  
B → I  
N → N  
G → S  
C → R  
D → H  
Z → D  
V → L  
W → U  
M → C  
Y → M  
T → F  
X → Y  
K → W  
E → G  
L → P  
A → B  
F → V  
I → K  
O → X  
R → Q  
H → J  
P → Z

# Right Side: English, Left Side Solve
krypton3@krypton:/krypton/krypton3$ cat krypton4 | tr 'SQJUBNGCDZVWMYTXKELAFIORHP' 'ETAOINSRHDLUCMFYWGPBVKXQJZ' ⌨️
WELLU ISEAH ELEKE LYICN MTOOW INURO BNCAE
krypton3@krypton:/krypton/krypton3$ cat krypton4 | tr 'JDSKV' 'THEWL' ⌨️
WELLW BGETH ELEIE LXBMN YQUUW BNWCU ANMTE 
krypton3@krypton:/krypton/krypton3$ cat krypton4 | tr 'SQJUBNGCDZVWMYTXKELAFIORHP' 'EATSORNIHCLDUPYFWGMBKVXQJZ' ⌨️
WELLD ONETH ELEVE LFOUR PASSW ORDIS BRUTE 🔐
```

## Flag
<b>BRUTE</b>

## Continue
[Continue](./Krypton0304.md)
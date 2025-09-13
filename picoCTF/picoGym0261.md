# picoGym Level 261: credstuff
Source: https://play.picoctf.org/practice/challenge/261

## Goal
We found a leak of a blackmarket website's login credentials<br>
Can you find the password of the user cultiris and successfully decrypt it?<br>
Download the leak here<br>
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on<br>
https://artifacts.picoctf.net/c/151/leak.tar

## What I learned
```
grep -nr to find line as well
sed and awk search on specific line
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/151/leak.tar ⌨️
--2025-09-08 23:05:55--  https://artifacts.picoctf.net/c/151/leak.tar
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 30720 (30K) [application/octet-stream]
Saving to: 'leak.tar'

leak.tar                                                   100%[======================================================================================================================================>]  30.00K  --.-KB/s    in 0.009s  

2025-09-08 23:05:55 (3.19 MB/s) - 'leak.tar' saved [30720/30720]

AsianHacker-picoctf@webshell:/tmp$ tar -xf leak.tar ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
encrypted.txt  hsperfdata_root  leak  leak.tar  node-compile-cache  readmycert.csr
AsianHacker-picoctf@webshell:/tmp$ cd leak/ ⌨️
AsianHacker-picoctf@webshell:/tmp/leak$ ls ⌨️
passwords.txt  usernames.txt
AsianHacker-picoctf@webshell:/tmp/leak$ grep -rn "cultiris" usernames.txt ⌨️❤️
378:cultiris 👀
AsianHacker-picoctf@webshell:/tmp/leak$ sed -n "378p" passwords.txt ⌨️❤️
cvpbPGS{P7e1S_54I35_71Z3} 👀
AsianHacker-picoctf@webshell:/tmp/leak$ awk 'NR==378' passwords.txt ⌨️❤️
cvpbPGS{P7e1S_54I35_71Z3} 👀

# Identify Cipher
https://www.dcode.fr/cipher-identifier
    ROT-13 Cipher	
    ROT Cipher
AsianHacker-picoctf@webshell:/tmp/leak$ for i in {1..25}; do
>   echo "ROT $i: "
>   echo "cvpbPGS{P7e1S_54I35_71Z3}" | tr 'A-Za-z' "$(echo {A..Z} | tr -d ' ' | cut -c$((i+1))-26)$(echo {A..Z} | tr -d ' ' | cut -c1-$i)$(echo {a..z} | tr -d ' ' | cut -c$((i+1))-26)$(echo {a..z} | tr -d ' ' | cut -c1-$i)"
> done ⌨️
ROT 1: 
dwqcQHT{Q7f1T_54J35_71A3}
ROT 2: 
exrdRIU{R7g1U_54K35_71B3}
ROT 3: 
fyseSJV{S7h1V_54L35_71C3}
ROT 4: 
gztfTKW{T7i1W_54M35_71D3}
ROT 5: 
haugULX{U7j1X_54N35_71E3}
ROT 6: 
ibvhVMY{V7k1Y_54O35_71F3}
ROT 7: 
jcwiWNZ{W7l1Z_54P35_71G3}
ROT 8: 
kdxjXOA{X7m1A_54Q35_71H3}
ROT 9: 
leykYPB{Y7n1B_54R35_71I3}
ROT 10: 
mfzlZQC{Z7o1C_54S35_71J3}
ROT 11: 
ngamARD{A7p1D_54T35_71K3}
ROT 12: 
ohbnBSE{B7q1E_54U35_71L3}
ROT 13: 
picoCTF{C7r1F_54V35_71M3} 🔐
ROT 14: 
qjdpDUG{D7s1G_54W35_71N3}
ROT 15: 
rkeqEVH{E7t1H_54X35_71O3}
ROT 16: 
slfrFWI{F7u1I_54Y35_71P3}
ROT 17: 
tmgsGXJ{G7v1J_54Z35_71Q3}
ROT 18: 
unhtHYK{H7w1K_54A35_71R3}
ROT 19: 
voiuIZL{I7x1L_54B35_71S3}
ROT 20: 
wpjvJAM{J7y1M_54C35_71T3}
ROT 21: 
xqkwKBN{K7z1N_54D35_71U3}
ROT 22: 
yrlxLCO{L7a1O_54E35_71V3}
ROT 23: 
zsmyMDP{M7b1P_54F35_71W3}
ROT 24: 
atnzNEQ{N7c1Q_54G35_71X3}
ROT 25: 
buoaOFR{O7d1R_54H35_71Y3}
```

## Flag
picoCTF{C7r1F_54V35_71M3}

## Continue
[Continue](./picoGym0312.md)
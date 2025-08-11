# Krypton Level 0 → Level 1 base64 ROT13

## Previous Flag
N/A

## Goal
Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:
S1JZUFRPTklTR1JFQVQ= 👀

Use this password to log in to <b>krypton.labs.overthewire.org</b> with username <b>krypton1</b> using SSH on <b>port 2231</b>.  The password for level 2 is in the <b>file krypton2</b>. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text.

## What I learned
```
Krypton is teaching basic cryptography
Base64 is a way to encode binary data into ASCII text using 64 printable characters, making it safe for transmission over text-based protocols
    ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
base64 -d
CyberChef

Caesar cipher: A substitution cipher that shifts each letter of the alphabet by a fixed number of positions (direct)
ROT13: A Caesar cipher with a fixed shift of 13, making encryption and decryption identical for the 26-letter alphabet
ROT5: A digit-only cipher that shifts each numeral by 5, wrapping around after 9, and works the same way for encryption and decryption

krypton1@krypton:/krypton/krypton1$ echo "aa" | tr "a" "x"
xx
krypton1@krypton:/krypton/krypton1$ echo "abccba" | tr "a-z" "A-Z"
ABCCBA
# Note: tr doesn’t allow descending ranges 🐱‍💻
krypton1@krypton:/krypton/krypton1$ echo "abccba" | tr "a-z" "Z-A"
tr: range-endpoints of 'Z-A' are in reverse collating sequence order
krypton1@krypton:/krypton/krypton1$ echo "abccba" | tr "abcdefghijklmnopqrstuvwxyz" "zyxwvutsrqponmlkjihgfedcba"
zyxxyz
# Note: a-zA-Z solve case insensitive but 26 x 2 = 52 characters
krypton1@krypton:/krypton/krypton1$ echo "AbcCba" | tr 'a-zA-Z' 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
ZyxXyz

alias                               # view all alias
alias lall="ls -la"                 # Note: no spaces
alias | column -t -s'='             # Get-Alias | Format-Table -AutoSize
    -s'='                           tells column to split on = sign
    -t                              makes a table with aligned columns
unalias lall
    ~/.bashrc                       # Permanent
    ~/.zshrc                        # Permanent

# ROT13 for letters
alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"

# ROT5 for digits
alias rot5="tr '0-9' '5-90-4'"

# Combined ROT13+ROT5 (ROT18)
alias rot18="tr 'A-Za-z0-9' 'N-ZA-Mn-za-m5-90-4'"

# ROT47 for printable ASCII
alias rot47="tr '\!-~' 'P-~\!-O'"

# Suspect ROT Cipher (Brute Force) ❤️❤️❤️❤️❤️
for i in {1..25}; do
    upper=$(echo {A..Z} | tr -d ' ' | sed -E "s/(.{$i})(.*)/\2\1/")
    lower=$(echo {a..z} | tr -d ' ' | sed -E "s/(.{$i})(.*)/\2\1/")
    echo "ROT$i: $(echo 'YRIRY GJB CNFFJBEQ EBGGRA' | tr 'A-Za-z' "$upper$lower")"
done
```

## Solution
```
# Note: base64 not for Windows
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> echo S1JZUFRPTklTR1JFQVQ= | base64 -d ⌨️
base64 : The term 'base64' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the 
name, or if a path was included, verify that the path is correct and try again.
At line:1 char:29
+ echo S1JZUFRPTklTR1JFQVQ= | base64 -d
+                             ~~~~~~
    + CategoryInfo          : ObjectNotFound: (base64:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

# PowerShell Built in Decoder
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("S1JZUFRPTklTR1JFQVQ=")) ⌨️
KRYPTONISGREAT 🔐

# CyberChef
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=UzFKWlVGUlBUa2xUUjFKRlFWUT0
KRYPTONISGREAT 🔐

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh krypton1@krypton.labs.overthewire.org -p 2231 ⌨️
The authenticity of host '[krypton.labs.overthewire.org]:2231 ([13.48.176.69]:2231)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This host key is known by the following other names/addresses:
    C:\Users\trung.DESKTOP-G7C81CH/.ssh/known_hosts:6: bandit.labs.overthewire.org
    C:\Users\trung.DESKTOP-G7C81CH/.ssh/known_hosts:7: [leviathan.labs.overthewire.org]:2223
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[krypton.labs.overthewire.org]:2231' (ED25519) to the list of known hosts.
                      _                     _
                     | | ___ __ _   _ _ __ | |_ ___  _ __
                     | |/ / '__| | | | '_ \| __/ _ \| '_ \
                     |   <| |  | |_| | |_) | || (_) | | | |
                     |_|\_\_|   \__, | .__/ \__\___/|_| |_|
                                |___/|_|

                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

krypton1@krypton.labs.overthewire.org's password: ⌨️ 
krypton1@krypton:~$ ls -la ⌨️
total 20
drwxr-xr-x   2 root root 4096 Jul 28 19:04 .
drwxr-xr-x 150 root root 4096 Jul 28 19:06 ..
-rw-r--r--   1 root root  220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root root 3851 Jul 28 18:47 .bashrc     
-rw-r--r--   1 root root  807 Mar 31  2024 .profile
krypton1@krypton:~$ cat /etc/krypton_pass/krypton1 ⌨️
KRYPTONISGREAT      
krypton1@krypton:~$ cat /etc/krypton_pass/krypton2 ⌨️
cat: /etc/krypton_pass/krypton2: Permission denied
krypton1@krypton:/$ cd .. ⌨️
krypton1@krypton:/$ ls ⌨️
behemoth           boot     etc      👀krypton  lib64              lost+found  media   opt   run                 snap  tmp     var   
bin                dev      formulaone  lib      lib.usr-is-merged  manpage     mnt     proc  sbin                srv   usr     vortex
bin.usr-is-merged  drifter  home        lib32    libx32             maze        narnia  root  sbin.usr-is-merged  sys   utumno
krypton1@krypton:/$ cd /krypton/ ⌨️
krypton1@krypton:/krypton$ ls -la ⌨️
total 36
drwxr-xr-x  9 root root 4096 Jul 28 19:05 .       
drwxr-xr-x 31 root root 4096 Jul 30 18:01 ..      
drwxr-xr-x  2 root root 4096 Jul 28 19:05 krypton1 👀
drwxr-xr-x  2 root root 4096 Jul 28 19:05 krypton2
drwxr-xr-x  2 root root 4096 Jul 28 19:05 krypton3
drwxr-xr-x  2 root root 4096 Jul 28 19:05 krypton4
drwxr-xr-x  2 root root 4096 Jul 28 19:05 krypton5
drwxr-xr-x  3 root root 4096 Jul 28 19:05 krypton6
drwxr-xr-x  2 root root 4096 Jul 28 19:05 krypton7
krypton1@krypton:/krypton$ cd krypton1 ⌨️
krypton1@krypton:/krypton/krypton1$ ls -la ⌨️
total 16
drwxr-xr-x 2 root     root     4096 Jul 28 19:05 .       
drwxr-xr-x 9 root     root     4096 Jul 28 19:05 ..      
-rw-r----- 1 krypton1 krypton1   26 Jul 28 19:05 krypton2
-rw-r----- 1 krypton1 krypton1  882 Jul 28 19:05 README  
krypton1@krypton:/krypton/krypton1$ cat README ⌨️ 
Welcome to Krypton!

This game is intended to give hands on experience with cryptography     
and cryptanalysis.  The levels progress from classic ciphers, to modern,
easy to harder.

Although there are excellent public tools, like cryptool,to perform     
the simple analysis, we strongly encourage you to try and do these
without them for now.  We will use them in later excercises.

** Please try these levels without cryptool first **

The first level is easy.  The password for level 2 is in the file
'krypton2'.  It is 'encrypted' using a simple rotation called ROT13. 👀
It is also in non-standard ciphertext format.  When using alpha characters for
cipher text it is normal to group the letters into 5 letter clusters,
regardless of word boundaries.  This helps obfuscate any patterns.

This file has kept the plain text word boundaries and carried them to
the cipher text.

Enjoy!
krypton1@krypton:/krypton/krypton1$ cat krypton2 ⌨️
"YRIRY GJB CNFFJBEQ EBGGRA" 🧠

krypton1@krypton:/krypton/krypton1$ for i in {1..25}; do
>     upper=$(echo {A..Z} | tr -d ' ' | sed -E "s/(.{$i})(.*)/\2\1/")
>     lower=$(echo {a..z} | tr -d ' ' | sed -E "s/(.{$i})(.*)/\2\1/")
>     echo "ROT$i: $(echo 'YRIRY GJB CNFFJBEQ EBGGRA' | tr 'A-Za-z' "$upper$lower")"
> done ⌨️
ROT1: ZSJSZ HKC DOGGKCFR FCHHSB
ROT2: ATKTA ILD EPHHLDGS GDIITC
ROT3: BULUB JME FQIIMEHT HEJJUD
ROT4: CVMVC KNF GRJJNFIU IFKKVE
ROT5: DWNWD LOG HSKKOGJV JGLLWF
ROT6: EXOXE MPH ITLLPHKW KHMMXG
ROT7: FYPYF NQI JUMMQILX LINNYH
ROT8: GZQZG ORJ KVNNRJMY MJOOZI
ROT9: HARAH PSK LWOOSKNZ NKPPAJ
ROT10: IBSBI QTL MXPPTLOA OLQQBK
ROT11: JCTCJ RUM NYQQUMPB PMRRCL
ROT12: KDUDK SVN OZRRVNQC QNSSDM
ROT13: LEVEL TWO PASSWORD ROTTEN 🔐
ROT14: MFWFM UXP QBTTXPSE SPUUFO
ROT15: NGXGN VYQ RCUUYQTF TQVVGP
ROT16: OHYHO WZR SDVVZRUG URWWHQ
ROT17: PIZIP XAS TEWWASVH VSXXIR
ROT18: QJAJQ YBT UFXXBTWI WTYYJS
ROT19: RKBKR ZCU VGYYCUXJ XUZZKT
ROT20: SLCLS ADV WHZZDVYK YVAALU
ROT21: TMDMT BEW XIAAEWZL ZWBBMV
ROT22: UNENU CFX YJBBFXAM AXCCNW
ROT23: VOFOV DGY ZKCCGYBN BYDDOX
ROT24: WPGPW EHZ ALDDHZCO CZEEPY
ROT25: XQHQX FIA BMEEIADP DAFFQZ

https://cyberchef.io/#recipe=ROT13(true,true,false,13)&input=WVJJUlkgR0pCIENORkZKQkVRIEVCR0dSQQ
LEVEL TWO PASSWORD ROTTEN 🔐

krypton1@krypton:/krypton/krypton1$ alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'" ⌨️
krypton1@krypton:/krypton/krypton1$ echo "YRIRY GJB CNFFJBEQ EBGGRA" | rot13 ⌨️
LEVEL TWO PASSWORD ROTTEN 🔐
```

## Flag
<b>ROTTEN</b>

## Continue
[Continue](./Krypton0102.md)
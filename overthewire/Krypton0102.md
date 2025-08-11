# Krypton Level 1 → Level 2 Caesar Cipher w/ tr

## Previous Flag
<b>ROTTEN</b>

## Goal
Use previous password to log in to <b>krypton.labs.overthewire.org</b> with username <b>krypton2</b> using SSH on <b>port 2231</b>. Password in <b>file krypton3</b>. It is in <b>5 letter group ciphertext</b>👀. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a <b>program that will encrypt anything you wish</b> to give it using the key.

Additional Information:
The encrypt binary will look for the keyfile in your <b>current working directory</b>. Therefore, it might be best to create a working direcory in /tmp and in there a link to the keyfile. As the <b>encrypt binary runs setuid krypton3</b>, you also need to give krypton3 access to your working directory.

Here is an example:
krypton2@melinda:~$ mktemp -d ⌨️
/tmp/tmp.Wf2OnCpCDQ
krypton2@melinda:~$ cd /tmp/tmp.Wf2OnCpCDQ ⌨️
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ ln -s /krypton/krypton2/keyfile.dat ⌨️
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ ls ⌨️
keyfile.dat
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ chmod 777 . ⌨️
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ /krypton/krypton2/encrypt /etc/issue 🐱‍💻
krypton2@melinda:/tmp/tmp.Wf2OnCpCDQ$ ls ⌨️
ciphertext  keyfile.dat

## What I learned
```
Monoalphebetic Cipher
    Caesar cipher shifts alphabet by a set number
        plain:  a b c d e f g h i j k ...
        cipher: G H I J K L M N O P Q ...

Simple substitution cipher (aka monoalphabetic substitution cipher) different than Caesar Cipher

keyfile is a file that contains Caesar cipher shift value (key) that encrypt binary will use
    if it contains 13, binary file does ROT13
    if it contains 1, binary files does ROT1
        A B C ... Z     Encryption key = 1, shift forward: A → B
        B C D ... A     Decryption key = 26 − 1 = 25, shift backward: B → A 
                        Check: (2 + 25) % 26 = 1 (letter “A” again)
                        Alphabet has 26 letters, any shift wraps around
                        Shifting forward by 27 is same as shifting by 1
                        Shifting backward by -1 is same as shifting forward by 25

If know the encryption key from keyfile then can instantly calculate decryption key
The plug it into your Caesar/ROT script to decode
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh krypton2@krypton.labs.overthewire.org -p 2231 ⌨️
krypton2@krypton:~$ cd /krypton/ ⌨️
krypton2@krypton:/krypton$ cd krypton2/ ⌨️
krypton2@krypton:/krypton/krypton2$ ls -la ⌨️
total 36
drwxr-xr-x 2 root     root      4096 Jul 28 19:05 .
drwxr-xr-x 9 root     root      4096 Jul 28 19:05 ..
-rwsr-x--- 1 krypton3 krypton2 16336 Jul 28 19:05 encrypt    
-rw-r----- 1 krypton3 krypton3    27 Jul 28 19:05 keyfile.dat
-rw-r----- 1 krypton2 krypton2    13 Jul 28 19:05 krypton3 👀   
-rw-r----- 1 krypton2 krypton2  1815 Jul 28 19:05 README
krypton2@krypton:/krypton/krypton2$ file encrypt ⌨️
encrypt: setuid ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c24be5fc744ab4be8336753b62a5b969d6a5da67, for GNU/Linux 3.2.0, not stripped
krypton2@krypton:/krypton/krypton2$ file keyfile.dat ⌨️
keyfile.dat: regular file, no read permission
krypton2@krypton:/krypton/krypton2$ file krypton3 ⌨️
krypton3: ASCII text
krypton2@krypton:/krypton/krypton2$ cat krypton3 ⌨️
OMQEMDUEQMEK

krypton2@krypton:/krypton/krypton2$ for i in {1..25}; do
>     upper=$(echo {A..Z} | tr -d ' ' | sed -E "s/(.{$i})(.*)/\2\1/")
>     lower=$(echo {a..z} | tr -d ' ' | sed -E "s/(.{$i})(.*)/\2\1/")
>     echo "ROT$i: $(echo 'OMQEMDUEQMEK' | tr 'A-Za-z' "$upper$lower")"
> done ⌨️
ROT1: PNRFNEVFRNFL
ROT2: QOSGOFWGSOGM
ROT3: RPTHPGXHTPHN
ROT4: SQUIQHYIUQIO
ROT5: TRVJRIZJVRJP
ROT6: USWKSJAKWSKQ
ROT7: VTXLTKBLXTLR
ROT8: WUYMULCMYUMS
ROT9: XVZNVMDNZVNT
ROT10: YWAOWNEOAWOU
ROT11: ZXBPXOFPBXPV
ROT12: AYCQYPGQCYQW
ROT13: BZDRZQHRDZRX
ROT14: CAESARISEASY 🔐 Note: Do bottom way since cipher not always human readable
ROT15: DBFTBSJTFBTZ
ROT16: ECGUCTKUGCUA
ROT17: FDHVDULVHDVB
ROT18: GEIWEVMWIEWC
ROT19: HFJXFWNXJFXD
ROT20: IGKYGXOYKGYE
ROT21: JHLZHYPZLHZF
ROT22: KIMAIZQAMIAG
ROT23: LJNBJARBNJBH
ROT24: MKOCKBSCOKCI
ROT25: NLPDLCTDPLDJ

krypton2@krypton:/krypton/krypton2$ mktemp -d ⌨️
/tmp/tmp.h4G0yt9QEm
krypton2@krypton:/krypton/krypton2$ cd /tmp/tmp.h4G0yt9QEm ⌨️
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ ln -s /krypton/krypton2/keyfile.dat ⌨️
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ ls -la ⌨️
total 484
drwx------     2 krypton2 krypton2   4096 Aug 11 02:47 .
drwxrwx-wt 11042 root     root     487424 Aug 11 02:47 ..
lrwxrwxrwx     1 krypton2 krypton2     29 Aug 11 02:47 keyfile.dat -> /krypton/krypton2/keyfile.dat 👀
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ chmod 777 . ⌨️
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ ls -la ⌨️
total 484
drwxrwxrwx     2 krypton2 krypton2   4096 Aug 11 02:47 .
drwxrwx-wt 11042 root     root     487424 Aug 11 02:47 ..
lrwxrwxrwx     1 krypton2 krypton2     29 Aug 11 02:47 keyfile.dat -> /krypton/krypton2/keyfile.dat
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ echo "AAAAA" > encrypt.txt ⌨️
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ cat encrypt.txt ⌨️
AAAAA
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ /krypton/krypton2/encrypt encrypt.txt ⌨️
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ ls -la ⌨️
total 492
drwxrwxrwx     2 krypton2 krypton2   4096 Aug 11 02:50 .
drwxrwx-wt 11045 root     root     487424 Aug 11 02:50 ..
-rw-rw-r--     1 krypton3 krypton2      5 Aug 11 02:50 ciphertext 👀
-rw-rw-r--     1 krypton2 krypton2      6 Aug 11 02:49 encrypt.txt
lrwxrwxrwx     1 krypton2 krypton2     29 Aug 11 02:47 keyfile.dat -> /krypton/krypton2/keyfile.dat
krypton2@krypton:/tmp/tmp.h4G0yt9QEm$ cat ciphertext ⌨️
MMMMM

# A(1) and M(13)
# encryption key = 13 -1 = 12
# decryption key = 26 -12 = 14
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 012345678901234

krypton2@krypton:~$ cd /krypton/krypton2/ ⌨️
krypton2@krypton:/krypton/krypton2$ ls ⌨️
encrypt  keyfile.dat  krypton3  README
krypton2@krypton:/krypton/krypton2$ cat krypton3 ⌨️ 
OMQEMDUEQMEK
krypton2@krypton:/krypton/krypton2$ alias rot14="tr 'A-Za-z' 'O-ZA-No-za-n'" ⌨️
krypton2@krypton:/krypton/krypton2$ echo krypton3 ⌨️         # Noob mistake
krypton3
krypton2@krypton:/krypton/krypton2$ cat krypton3 | rot14 ⌨️
CAESARISEASY 🔐
```

## Flag
<b>CAESARISEASY</b>

## Continue
[Continue](./Krypton0203.md)
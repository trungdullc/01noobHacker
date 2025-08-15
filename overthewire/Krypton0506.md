# Krypton Level 5 → Level 6 Stream Cipher (ASCII → Bytes)

## Previous Flag
<b>RANDOM</b>

## Goal
Use previous password to log in to <b>krypton.labs.overthewire.org</b> with username <b>krypton6</b> using SSH on <b>port 2231</b>. For example, imagine you and your confident have agreed on a key using the book ‘A Tale of Two Cities’ as your key, in 256 byte blocks.

The cipher works as such:

Each plaintext message is broken into <b>256 byte blocks</b>. For each block of plaintext, a corresponding 256 byte block from the book is used as the key, starting from the first chapter, and progressing. <b>No part of the book is ever re-used as key</b>. The use of a key of the same length as the plaintext, and only using it once is called a “One Time Pad”.

Look in the </b>krypton6 directory</b>. You will find a <b>file plain1</b>, a 256 byte block. You will also see a <b>file key1</b>, the first 256 bytes of ‘A Tale of Two Cities’. The <b>file cipher1</b> is the cipher text of plain1. As you can see it is very difficult to break the cipher without the key knowledge.

If the encryption is truly random letters, and only used once, then it is impossible to break. A truly random “One Time Pad” key cannot be broken. Consider intercepting a ciphertext message of 1000 bytes. One could brute force for the key, but due to the random key nature, you would produce every single valid 1000 letter plaintext as well.

Choosing keys that are the same size as the plaintext is impractical. Therefore, <b>other methods</b> must be used to obscure ciphertext against frequency analysis in a simple substitution cipher. The impracticality of an ‘infinite’ key means that the randomness, or <b>entropy</b>, of the encryption is introduced via the method.

We have seen the method of ‘substitution’. Even in modern crypto, substitution is a valid technique. Another technique is <b>‘transposition’, or swapping of bytes</b>.

Modern ciphers break into two types; <b>symmetric and asymmetric</b>.

Symmetric ciphers come in two flavours: <b>block and stream</b>.

Until now, we have been playing with classical ciphers, approximating ‘block’ ciphers. A block cipher is done in fixed size blocks. For example, in the previous paragraphs we discussed breaking text and keys into 256 byte blocks, and working on those blocks. Block ciphers use a fixed key to perform substituion and transposition ciphers on each block discretely.

Its time to employ a <b>stream cipher</b>. A stream cipher attempts to create an on-the-fly ‘random’ keystream to encrypt the incoming plaintext one byte at a time. Typically, the <b>‘random’ key byte is xor’d with the plaintext to produce the ciphertext</b>. If the random keystream can be replicated at the recieving end, then a further xor will produce the plaintext once again.

  <table>
    <caption>XOR and OR Truth Table</caption>
    <thead>
      <tr>
        <th>A</th>
        <th>B</th>
        <th>A ⊕ B (XOR)</th>
        <th>A ∨ B (OR)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>0</td><td>1</td><td>1</td><td>1</td></tr>
      <tr><td>1</td><td>0</td><td>1</td><td>1</td></tr>
      <tr><td>1</td><td>1</td><td class="highlight">0</td><td>1</td></tr>
    </tbody>
  </table>

From this example forward, we will be <b>working with bytes</b>, not ASCII text, so a hex editor/dumper like <b>hexdump</b> is a necessity. Now is the right time to start to learn to use tools like <b>cryptool</b>.

In this example, the <b>keyfile is in your directory</b>, however it is not readable by you. The binary ‘encrypt6’ is also available. It will read the keyfile and encrypt any message you desire, using the key AND a ‘random’ number. You get to perform a ‘known ciphertext’ attack by introducing plaintext of your choice. The challenge here is not simple, but the ‘random’ number generator is weak.

See <b>HINT1</b>. If you have further difficulty use <b>HINT2</b>.
Password is <b>encrypted with encrypt6</b>.

## What I learned
```
hexdump     A command-line tool that displays file contents as hexadecimal bytes, often used to inspect raw binary data
xxd         Similar to hexdump but creates a hex dump & also revert it back to binary, useful for editing and inspecting hex
stream cipher   Encryption method that XORs plaintext bytes w/ a keystream byte-by-byte, producing ciphertext
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh krypton6@krypton.labs.overthewire.org -p 2231 ⌨️
krypton6@krypton:~$ cd /krypton/krypton6/ ⌨️
krypton6@krypton:/krypton/krypton6$ ls -la ⌨️
total 56
drwxr-xr-x 3 root     root      4096 Jul 28 19:05 .
drwxr-xr-x 9 root     root      4096 Jul 28 19:05 ..
-rwsr-x--- 1 krypton7 krypton6 16528 Jul 28 19:05 encrypt6   
-rw-r----- 1 krypton6 krypton6   164 Jul 28 19:05 HINT1      
-rw-r----- 1 krypton6 krypton6    11 Jul 28 19:05 HINT2      
-rw-r----- 1 krypton7 krypton7    11 Jul 28 19:05 keyfile.dat
-rw-r----- 1 krypton6 krypton6    15 Jul 28 19:05 krypton7   
drwxr-xr-x 2 root     root      4096 Jul 28 19:05 onetime    
-rw-r----- 1 krypton6 krypton6  4342 Jul 28 19:05 README
krypton6@krypton:/krypton/krypton6$ cat HINT1 ⌨️
The 'random' generator has a limited number of bits, and is periodic.   
Entropy analysis and a good look at the bytes in a hex editor will help.

There is a pattern!
krypton6@krypton:/krypton/krypton6$ cat HINT2 ⌨️
8 bit LFSR
krypton6@krypton:/krypton/krypton6$ echo $(cat krypton7) ⌨️
PNUKLYLWRQKGKBE 👀
krypton6@krypton:/krypton/krypton6$ file encrypt6 ⌨️
encrypt6: setuid ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=cca8b9e45420935c0b2b66dd60bb01df2542d7f2, for GNU/Linux 3.2.0, not stripped
krypton6@krypton:/krypton/krypton6$ ./encrypt6 ⌨️
usage: encrypt6 foo bar 
Where: foo is the file containing the plaintext and bar is the destination ciphertext file.
krypton6@krypton:/krypton/krypton6$ cd onetime/ ⌨️
krypton6@krypton:/krypton/krypton6/onetime$ ls -la ⌨️
total 20
drwxr-xr-x 2 root     root     4096 Jul 28 19:05 .
drwxr-xr-x 3 root     root     4096 Jul 28 19:05 ..
-rw-r----- 1 krypton6 krypton6  255 Jul 28 19:05 cipher1
-rw-r----- 1 krypton6 krypton6  256 Jul 28 19:05 key1
-rw-r----- 1 krypton6 krypton6  256 Jul 28 19:05 plain1
krypton6@krypton:/krypton/krypton6/onetime$ cat cipher1;echo ⌨️
ABJGGZVHEIKLHMXIZKWZHBAUAPPHSJKHBTYXQPWCLPHSMIVOAKVYYWMQHXMLOIDEZYPURHMJOQSIWHAWESVRWBJTCIWDINKWIJXDMRIPNNRQBUKHDKPACMIQGJEQXXIGWIAARGWPHAXYASYRFAZKFMWWKGKTUHNYLLIESXIOICBAWJMMDEUHBRKTCABLXTCSUYTYELDXKJNWZMLVRFBSFLHQTDXOEVSISWYMYMHYLMSUFJGWJEUDJESTAIPNJPQ
krypton6@krypton:/krypton/krypton6/onetime$ cat key1 ⌨️
ITWASTHEBESTOFTIMESITWASTHEWORSTOFTIMESITWASTHEAGEOFWISDOMITWASTHEAGEOFFOOLISHNESSITWASTHEEPOCHOFBELIEFITWASTHEEPOCHOFINCREDULITYITWASTHESEASONOFLIGHTITWASTHESEASONOFDARKNESSITWASTHESPRINGOFHOPEITWASTHEWINTEROFDESPAIRWEHADEVERYTHINGBEFOREUSWEHADNOTHINGBEF
krypton6@krypton:/krypton/krypton6/onetime$ cat plain1 ⌨️ 
SINGOGODDESSTHEANGEROFACHILLESSONOFPELEUSTHATBROUGHTCOUNTLESSILLSUPONTHEACHAEANSMANYABRAVESOULDIDITSENDHURRYINGDOWNTOHADESANDMANYAHERODIDITYIELDAPREYTODOGSANDVULTURESFORSOWERETHECOUNSELSOFJOVEFULFILLEDFROMTHEDAYONWHICHTHESONOFATREUSKINGOFMENANDGREATACHILL
krypton6@krypton:/krypton/krypton6/onetime$ cd .. ⌨️
krypton6@krypton:/krypton/krypton6$ mktemp -d ⌨️
/tmp/tmp.n9wFsFcsfA
krypton6@krypton:/krypton/krypton6$ cd /tmp/tmp.n9wFsFcsfA ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ ln -s /krypton/krypton6/keyfile.dat ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ ls -la ⌨️
total 516
drwx------     2 krypton6 krypton6   4096 Aug 12 00:14 .
drwxrwx-wt 12058 root     root     520192 Aug 12 00:14 ..
lrwxrwxrwx     1 krypton6 krypton6     29 Aug 12 00:14 keyfile.dat -> /krypton/krypton6/keyfile.dat
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ chmod 777 . ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ ls -la ⌨️
total 516
drwxrwxrwx     2 krypton6 krypton6   4096 Aug 12 00:14 .
drwxrwx-wt 12058 root     root     520192 Aug 12 00:15 ..
lrwxrwxrwx     1 krypton6 krypton6     29 Aug 12 00:14 keyfile.dat -> /krypton/krypton6/keyfile.dat
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ /krypton/krypton6/encrypt6 /krypton/krypton6/onetime/key1 outputtext.txt
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ cat outputtext.txt ⌨️
MBYTVZFMZDCMVSLQDJPGVLFMXVGGFEWBQYWOKMQHDPHFLPVFDCQUBCWRQWZGAIUMKKYOCNPYVBDQJMKCUHNNAOUDYRIXQVKUDJCKSXMVLERXQFGTUIGVQPZAGZGWXRGBWHDPHFLPVXBYUDSIJZKQYGMBYTVZFMQDKLVAGNUFOIPTXMMHYKJGLMUIUOLOMERHWRABNFPRJTBCRHGBFSHMUIDOPECGKWLIWZPYEGPVGYJCTOLFAMJTGTMBFHXZIRX
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ man xxd ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ xxd -b outputtext.txt ⌨️             # default dump by hex need binary
00000000: 01001101 01000010 01011001 01010100 01010110 01011010  MBYTVZ
00000006: 01000110 01001101 01011010 01000100 01000011 01001101  FMZDCM
0000000c: 01010110 01010011 01001100 01010001 01000100 01001010  VSLQDJ
00000012: 01010000 01000111 01010110 01001100 01000110 01001101  PGVLFM
00000018: 01011000 01010110 01000111 01000111 01000110 01000101  XVGGFE
0000001e: 01010111 01000010 01010001 01011001 01010111 01001111  WBQYWO
00000024: 01001011 01001101 01010001 01001000 01000100 01010000  KMQHDP
0000002a: 01001000 01000110 01001100 01010000 01010110 01000110  HFLPVF
00000030: 01000100 01000011 01010001 01010101 01000010 01000011  DCQUBC
00000036: 01010111 01010010 01010001 01010111 01011010 01000111  WRQWZG
0000003c: 01000001 01001001 01010101 01001101 01001011 01001011  AIUMKK
00000042: 01011001 01001111 01000011 01001110 01010000 01011001  YOCNPY
00000048: 01010110 01000010 01000100 01010001 01001010 01001101  VBDQJM
0000004e: 01001011 01000011 01010101 01001000 01001110 01001110  KCUHNN
00000054: 01000001 01001111 01010101 01000100 01011001 01010010  AOUDYR
0000005a: 01001001 01011000 01010001 01010110 01001011 01010101  IXQVKU
00000060: 01000100 01001010 01000011 01001011 01010011 01011000  DJCKSX
00000066: 01001101 01010110 01001100 01000101 01010010 01011000  MVLERX
0000006c: 01010001 01000110 01000111 01010100 01010101 01001001  QFGTUI
00000072: 01000111 01010110 01010001 01010000 01011010 01000001  GVQPZA
00000078: 01000111 01011010 01000111 01010111 01011000 01010010  GZGWXR
0000007e: 01000111 01000010 01010111 01001000 01000100 01010000  GBWHDP
00000084: 01001000 01000110 01001100 01010000 01010110 01011000  HFLPVX
0000008a: 01000010 01011001 01010101 01000100 01010011 01001001  BYUDSI
00000090: 01001010 01011010 01001011 01010001 01011001 01000111  JZKQYG
00000096: 01001101 01000010 01011001 01010100 01010110 01011010  MBYTVZ
0000009c: 01000110 01001101 01010001 01000100 01001011 01001100  FMQDKL
000000a2: 01010110 01000001 01000111 01001110 01010101 01000110  VAGNUF
000000a8: 01001111 01001001 01010000 01010100 01011000 01001101  OIPTXM
000000ae: 01001101 01001000 01011001 01001011 01001010 01000111  MHYKJG
000000b4: 01001100 01001101 01010101 01001001 01010101 01001111  LMUIUO
000000ba: 01001100 01001111 01001101 01000101 01010010 01001000  LOMERH
000000c0: 01010111 01010010 01000001 01000010 01001110 01000110  WRABNF
000000c6: 01010000 01010010 01001010 01010100 01000010 01000011  PRJTBC
000000cc: 01010010 01001000 01000111 01000010 01000110 01010011  RHGBFS
000000d2: 01001000 01001101 01010101 01001001 01000100 01001111  HMUIDO
000000d8: 01010000 01000101 01000011 01000111 01001011 01010111  PECGKW
000000de: 01001100 01001001 01010111 01011010 01010000 01011001  LIWZPY
000000e4: 01000101 01000111 01010000 01010110 01000111 01011001  EGPVGY
000000ea: 01001010 01000011 01010100 01001111 01001100 01000110  JCTOLF
000000f0: 01000001 01001101 01001010 01010100 01000111 01010100  AMJTGT
000000f6: 01001101 01000010 01000110 01001000 01011000 01011010  MBFHXZ
000000fc: 01001001 01010010 01011000                             IRX
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ xxd -b /krypton/krypton6/onetime/key1 ⌨️
00000000: 01001001 01010100 01010111 01000001 01010011 01010100  ITWAST
00000006: 01001000 01000101 01000010 01000101 01010011 01010100  HEBEST
0000000c: 01001111 01000110 01010100 01001001 01001101 01000101  OFTIME
00000012: 01010011 01001001 01010100 01010111 01000001 01010011  SITWAS
00000018: 01010100 01001000 01000101 01010111 01001111 01010010  THEWOR
0000001e: 01010011 01010100 01001111 01000110 01010100 01001001  STOFTI
00000024: 01001101 01000101 01010011 01001001 01010100 01010111  MESITW
0000002a: 01000001 01010011 01010100 01001000 01000101 01000001  ASTHEA
00000030: 01000111 01000101 01001111 01000110 01010111 01001001  GEOFWI
00000036: 01010011 01000100 01001111 01001101 01001001 01010100  SDOMIT
0000003c: 01010111 01000001 01010011 01010100 01001000 01000101  WASTHE
00000042: 01000001 01000111 01000101 01001111 01000110 01000110  AGEOFF
00000048: 01001111 01001111 01001100 01001001 01010011 01001000  OOLISH
0000004e: 01001110 01000101 01010011 01010011 01001001 01010100  NESSIT
00000054: 01010111 01000001 01010011 01010100 01001000 01000101  WASTHE
0000005a: 01000101 01010000 01001111 01000011 01001000 01001111  EPOCHO
00000060: 01000110 01000010 01000101 01001100 01001001 01000101  FBELIE
00000066: 01000110 01001001 01010100 01010111 01000001 01010011  FITWAS
0000006c: 01010100 01001000 01000101 01000101 01010000 01001111  THEEPO
00000072: 01000011 01001000 01001111 01000110 01001001 01001110  CHOFIN
00000078: 01000011 01010010 01000101 01000100 01010101 01001100  CREDUL
0000007e: 01001001 01010100 01011001 01001001 01010100 01010111  ITYITW
00000084: 01000001 01010011 01010100 01001000 01000101 01010011  ASTHES
0000008a: 01000101 01000001 01010011 01001111 01001110 01001111  EASONO
00000090: 01000110 01001100 01001001 01000111 01001000 01010100  FLIGHT
00000096: 01001001 01010100 01010111 01000001 01010011 01010100  ITWAST
0000009c: 01001000 01000101 01010011 01000101 01000001 01010011  HESEAS
000000a2: 01001111 01001110 01001111 01000110 01000100 01000001  ONOFDA
000000a8: 01010010 01001011 01001110 01000101 01010011 01010011  RKNESS
000000ae: 01001001 01010100 01010111 01000001 01010011 01010100  ITWAST
000000b4: 01001000 01000101 01010011 01010000 01010010 01001001  HESPRI
000000ba: 01001110 01000111 01001111 01000110 01001000 01001111  NGOFHO
000000c0: 01010000 01000101 01001001 01010100 01010111 01000001  PEITWA
000000c6: 01010011 01010100 01001000 01000101 01010111 01001001  STHEWI
000000cc: 01001110 01010100 01000101 01010010 01001111 01000110  NTEROF
000000d2: 01000100 01000101 01010011 01010000 01000001 01001001  DESPAI
000000d8: 01010010 01010111 01000101 01001000 01000001 01000100  RWEHAD
000000de: 01000101 01010110 01000101 01010010 01011001 01010100  EVERYT
000000e4: 01001000 01001001 01001110 01000111 01000010 01000101  HINGBE
000000ea: 01000110 01001111 01010010 01000101 01010101 01010011  FOREUS
000000f0: 01010111 01000101 01001000 01000001 01000100 01001110  WEHADN
000000f6: 01001111 01010100 01001000 01001001 01001110 01000111  OTHING
000000fc: 01000010 01000101 01000110 00001010                    BEF.
# Need XOR those to get key, this to long

krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ python -c "(print(A*256))" ⌨️   # Note: No python in ssh shell
Command 'python' not found, did you mean:    
  command 'python3' from deb python3
  command 'python' from deb python-is-python3 ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ printf '%.0sA' {1..256};echo ⌨️
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ printf '%.0sA' {1..256} > A.txt ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ cat A.txt ⌨️
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ /krypton/krypton6/encrypt6 A.txt output.txt ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ cat output.txt ⌨️
EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSI

# Notice Repeat, key looks like 30 characters
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
EICTDGYIYZKTHNSI

https://www.dcode.fr/vigenere-cipher
Vigenere Decoder
Vigenere ciphertext: PNUKLYLWRQKGKBE ⌨️
Decryption method
Knowing the Key/Password: EICTDGYIYZKTHNSIRFXYCPFUEOCKRN ⌨️
DECRYPT
Results: LFSRISNOTRANDOM 🔐

Method 2: Don't do this method was trying see what hexdump do different (waste time)
# Generate a plaintext
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ printf 'A%.0s' {1..256} > known.txt ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ cat known.txt ⌨️
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# Encrypt it
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ /krypton/krypton6/encrypt6  known.txt  cipher_known ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ cat cipher_known ⌨️
EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSI
# Dump to hex
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ hexdump -v -e '/1 "%02X "' cipher_known > cipher_known.hex ⌨️
krypton6@krypton:/tmp/tmp.n9wFsFcsfA$ cat cipher_known.hex ⌨️
45 49 43 54 44 47 59 49 59 5A 4B 54 48 4E 53

# Convert these hex bytes to ASCII characters:
45 = E
49 = I
43 = C
54 = T
44 = D
47 = G
59 = Y
49 = I
59 = Y
5A = Z
4B = K
54 = T
48 = H
4E = N
53 = S

# This method using hexdump kinda useless if have convert back to ASCII and use on website use other version
```

## Flag
<b>LFSRISNOTRANDOM</b>

## Continue
[Continue](./Krypton0607.md)
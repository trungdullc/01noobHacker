# picoGym Level 3: la cifra de
Source: https://play.picoctf.org/practice/challenge/3

## Goal
I found this cipher in an old book. Can you figure out what it says?<br>
Connect with nc jupiter.challenges.picoctf.org 58295.

## What I learned
```
Depends on site used

Hashcat brute-forcing/dictionary-attacking hashes, but not classical ciphers like Vigenère
Hashcat is built to attack modern hash functions (MD5, SHA1, bcrypt)

How people usually solve Vigenère
    Frequency analysis & Kasiski examination
        Estimate key length by looking for repeating patterns
        Do frequency analysis on each shifted alphabet
    Online solvers
    Custom scripts (Python has pycipher)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 58295 ⌨️
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xf966878l}

Tnj qixxe wkqw-duhfmkseej ipsiwtpznzn uk l puqjarusahjeii htpnjc hubpvkw, hay rldk fcoaso 1467 be Qpot Gltzndtg Fwbkwei.

Zmp Volpnèxj Nivmpr ox ehkwpfuwp surptorps ifwlki ehk Fwbkwei Jndc uw Llhjcto Htpnjc.

# Method 1:
https://www.guballa.de/vigenere-solver ⌨️❤️❤️❤️❤️❤️
Key length statistics
Key
length	    Score	Key
3	        62.18	wgf
4	        99.24	flag 👀
5	        59.92	flgha
6	        62.80	fgfwal

It is interesting how in history people often receive credit for things they did not create

During the course of history, the Vigenère Cipher has been reinvented many times

It was falsely attributed to Blaise de Vigenère as it was originally described in 1553 by Giovan Battista Bellaso in his book La cifra del. Sig. Giovan Battista Bellaso 

For the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a} 🔐

The first well-documented description of a polyalphabetic cipher however, was made around 1467 by Leon Battista Alberti.

The Vigenère Cipher is therefore sometimes called the Alberti Disc or Alberti Cipher.

In 1508, Johannes Trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the Vigenère Cipher.

Bellaso’s second booklet appeared in 1555 as a continuation of the first. The lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.

# Method 2:
https://www.boxentriq.com/code-breaking/cipher-identifier ⌨️
Analysis Results
    Bifid Cipher (46 votes)
    Unknown Cipher (41 votes)
    Beaufort Autokey Cipher (5 votes)
    Vigenere Cipher (4 votes) 👀 Note: Not top but is used
    Beaufort Cipher (2 votes)
    Vigenere Autokey Cipher (2 votes)

https://www.boxentriq.com/code-breaking/vigenere-cipher ⌨️
Auto Solve
Note: Not find correct but close
12258	flagfgflag	it is isozwjnonsb how in histowt kjtkgj taten receive hmzino atw ohings they dny ity xmjfoe during the hjpwxz jk mdstory the vilzieqk roonys blm cyph sdocbdtikc suos ecnyd cu vgh lzrhkke uuncccoeye su qrzohk ck pjaphzmj fn it was origisvgqd yzxhmibed in by gitqvs gvoynnta bellaso is cdx gjjp qv cifra del sil bdtavi gfotista bellaxj atw ocj nhplementatiti jk ycdx hdpher a table nn atwhzi gt sliding the qjrjw cvqk jf an ordinard vgumvwjy aor an apparesogd wviith number of plfxzx bdom wzspect to th

11081	flagflagfg	it is interjnonsb ctb dn history petkgj taojs meceive credno atw ocnsbs they did noy xmjfoz izming the courxz jk mdnytmy the vigenzqk roontx ggm cyph sythwdtikc sptx zcnyd cu qlm gzrhkke pzsxccoeye nz vmzohk ck kofkhzmj fn dy bvs originalld yzxhmdgjy in by giovan gvoynnof gzllaso in his gjjp qv xnkma del sig gioavi gfoonxoa bellaso fow ocj nhkqjhentation of ycdx hdkmjm a table is fowhzi gt nqnying the lowew cvqk ja fs jrdinary alpmvwjy ajw fi apparently wviith izrwer of places bdom wznujxt to th
Still not seeing the correct result? Then try experimenting with the Auto Solve settings or use the Cipher Identifier Tool.

Knowing the encryption key: flag ⌨️
Decode

# Method 3
https://www.dcode.fr/cipher-identifier ⌨️
Encrypted Message Identifier
Ciphertext to recognize

Results:
    Jefferson Wheel Cipher	
    Vigenere Cipher	👀
    Autoclave Cipher	
    Beaufort Cipher	
    Rozier Cipher	
    Vernam Cipher (One Time Pad)	
    Variant Beaufort Cipher

ANALYZE

https://www.dcode.fr/vigenere-cipher ⌨️
AUTOMATIC DECRYPTION

Note: Not find exact match like Method 2
Note: Solving w/ this not as clear

# Method 4: Not the best since not have vigenere cracker
https://cyberchef.io/#recipe=Vigen%C3%A8re_Decode('flag')&input=TmUgaXkgbnl0a3dwc3pueWcgbnRoIGl0IG10c3p0Y3kgdmp6cHJqIHpmemp5IHJraHBpYmogbnJraXR0IGx0YyB0bm55Z3kgeXNlZSBpdGQgdHRlIGN4amx0awoKSWZyb3NyIHRuaiBub2F3ZGUgdWsgc2l5eXpyZSwgeXNlIEJucmV06HdwIENvdXNleCBtbHMgaGpwbiB4anRuYmp5dGtpIHhhdGQgZWlzamQKCkl6IGJscyBsZndza3FqIGF6eWNpaHplZWogeXogQnJmdHNrIGlwIFZvbHBu6HhqIGxzIG95IGhheSB0Y2ltbnlhcnFqIGRreG5yb2dwZCBvcyAxNTUzIG15IE1uenZncyBNYXp5dHN6ZiBNZXJxbHN1IG55IGhveCBtb3VwIFdhIGlucXJnIGlwbC4gWW5yLiBHb3RnYXQgR2x0em5kdGcgR3BscmZkbyAKCkx0YyB0bmogdG12cXBta3NlYXpuem4gdWsgZWhveCBuaXZtcHIgZyB5bGJyaiB0cyBsdGNta2kgbXkgeXF0ZG9zciB0bmogd29jamMgaGdxcSBvbCBmeSBveGl0bmd3aiBhcnVzYWhqZSBmdXcgbG4gZ3VhYXhqeXRyZCBjYXRpem0gdHp4Ymt3IHpmIHZxbGNreCBoaXptIGNleXVwY3ogeXogdG5qIGZwdmpjIGhncXFwb2h6Q1pLe20zMTFhNTBfMHhfYTFybjN4M19oMWFoM3hmOTY2ODc4bH0KClRuaiBxaXh4ZSB3a3F3LWR1aGZta3NlZWogaXBzaXd0cHpuem4gdWsgbCBwdXFqYXJ1c2FoamVpaSBodHBuamMgaHVicHZrdywgaGF5IHJsZGsgZmNvYXNvIDE0NjcgYmUgUXBvdCBHbHR6bmR0ZyBGd2Jrd2VpLgoKWm1wIFZvbHBu6HhqIE5pdm1wciBveCBlaGt3cGZ1d3Agc3VycHRvcnBzIGlmd2xraSBlaGsgRndia3dlaSBKbmRjIHV3IExsaGpjdG8gSHRwbmpjLg
```

## Flag
picoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}

## Continue
[Continue](./picoGym0159.md)
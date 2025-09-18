# picoGym Level 103: Trivial Flag Transfer Protocol
Source: https://play.picoctf.org/practice/challenge/103

## Goal
Figure out how they moved the flag.<br>
https://mercury.picoctf.net/static/e4836d9bcc740d457f4331d68129a0bc/tftp.pcapng

## What I learned
```
Wireshark
opcodes
    1 — Read Request (RRQ)
    2 — Write Request (WRQ)
    3 — Data (DATA)
    4 — Acknowledgment (ACK)
    5 — Error (ERROR)
    6 — Option Acknowledgment (OACK) (used in TFTP extensions, RFC 2347)

steghide --extract -sf <file> -p ""
rz -y ❤️❤️❤️❤️❤️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/e4836d9bcc740d457f4331d68129a0bc/tftp.pcapng ⌨️
--2025-09-17 00:03:21--  https://mercury.picoctf.net/static/e4836d9bcc740d457f4331d68129a0bc/tftp.pcapng
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 52116496 (50M) [application/octet-stream]
Saving to: 'tftp.pcapng'

tftp.pcapng                                        100%[=============================================================================================================>]  49.70M  1.82MB/s    in 27s     

2025-09-17 00:03:49 (1.82 MB/s) - 'tftp.pcapng' saved [52116496/52116496]

AsianHacker-picoctf@webshell:/tmp$ file tftp.pcapng ⌨️
tftp.pcapng: pcapng capture file - version 1.0
AsianHacker-picoctf@webshell:/tmp$ exiftool tftp.pcapng ⌨️
ExifTool Version Number         : 12.40
File Name                       : tftp.pcapng
Directory                       : .
File Size                       : 50 MiB
File Modification Date/Time     : 2021:03:15 18:24:47+00:00
File Access Date/Time           : 2025:09:17 00:03:54+00:00
File Inode Change Date/Time     : 2025:09:17 00:03:49+00:00
File Permissions                : -rw-rw-r--
Error                           : Unknown file type
AsianHacker-picoctf@webshell:/tmp$ strings tftp.pcapng | grep "picoCTF" ⌨️
AsianHacker-picoctf@webshell:/tmp$ binwalk tftp.pcapng ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
3202          0xC82           gzip compressed data, fastest compression, from Unix, last modified: 1970-01-01 00:00:00 (null date)
4856          0x12F8          xz compressed data
188254        0x2DF5E         PC bitmap, Windows 3.x format,, 605 x 454 x 24
1289958       0x13AEE6        PC bitmap, Windows 3.x format,, 4032 x 3024 x 24
5051098       0x4D12DA        Broadcom header, number of sections: 38797312,
8690459       0x849B1B        rzip compressed data - version 87.76 (1415270489 bytes)
9466123       0x90710B        LANCOM OEM file
12246567      0xBADE27        LANCOM firmware header, model: "QXKRYLQXKQXKQWKOUJNTIKQFIODIODJPELRGMSHMSHMSHLRGJPEHNCIODNTIRXMRXMZbWgqejuinznkwkiuiqxmlmcOPFCD:@@6?>4@?5A>5B?6A>5?<3>;2>;2>;2>;", firmware version: "JPWJ", RC74, build 87 ("OVIPWJQX")
12262610      0xBB1CD2        LANCOM firmware header, model: "PWJPWJQXKRYLRYLRYLPWJPVJOUJNTIMSHLRGJPEJPEJPELRGLR", firmware version: "JPWJ", RC72, build 87 ("MTGNUHPW")
12311131      0xBBDA5B        LANCOM firmware header, model: "OVJPXMPXMPXMPXMPXMOWLOWLPXMOWLOWLOWLPXMOWLOWLQYNT\Q[eY]j^arefwjbsf`maWaU=D9/3(8:0:;1AB8=>4>>4", firmware version: "KPWJ", RC73, build 88 ("NUHOVIQX")
12343591      0xBC5927        LANCOM firmware header, model: "X`UU]RT\QV^SW_TU]RS[PT\QV^SV^SV^S[eYal`eqeduhdxkfzmi}pj|om{odoc`h]T[PAG<:?4:>39:0;:0=<2=<2=<2<90;8/<90?<3A>5@=4?<3?<3>;2=:1>;2?<", firmware version: "TYaV", RC77, build 95 ("PWJRYMT\")
14834600      0xE25BA8        Microsoft executable, MS-DOS
15038870      0xE57996        Broadcom header, number of sections: 324294729,
18292756      0x1172014       StuffIt Deluxe Segment (data): fVefVefVefVdeUcdT`aQ_`P``Ra`R`_Q`_QbaScbTebVfbWb^Sa]R_[P[VMTOFQLCTND
18988201      0x121BCA9       StuffIt Deluxe Segment (data): fVdeUbcS`aQ_`P_`P``PaaQ``P``P__O__O^^N^^N^^N^^N\\L[[KYYI\ZK]ZK\YJ^[L\YJZWHZWHZWHZVG[VG]XI\WHZUFWRCUPAUPAVQBWRCYTEYTEYTEXSDXSDXSD
19178156      0x124A2AC       rzip compressed data - version 89.67 (1263815251 bytes)
19343936      0x1272A40       StuffIt Deluxe Segment (data): fVcdTbdT`cS^aQ\_OSWGPVEJP?KQ@V\KW]LX^M`fUjn^lo_XZJBC3JK;QQAQO@TQBTPAUPASN?RM>UPATO@TO@UPATO@TO@TO@UPAVQBUPAUPAUPAVQBUPATPARO@SPA
19532037      0x12A0905       HPACK archive data
19780793      0x12DD4B9       StuffIt Deluxe Segment (data): fVgiYfiYcfVbeUadT_bR\_O\_O_bRadT`cS^aQ\_OZ]M]_O`aQ_`P_`P^_O^^N^^N^^N__O``P`^OebSb_Pc`Qb`Q__O^_O`aQbcScdTcdT^_O[\LUVFTUEWWGXYIWZJ
20607295      0x13A713F       StuffIt Deluxe Segment (data): fV`aQYZJTUEWXHYZJUUESSCWWGYWHZWH\YJa^OeaRa\MUO@[TE]TF[RDXOAaXJ[RDRI;SJ<UL>UL>UL>VM?XOAXOAWN@TK>SJ=UL?WNAUL?RI<QH;TK>VM@WNATK>RI<
20704295      0x13BEC27       StuffIt Deluxe Segment (data): fV_`PhiYacS[^NUYIW]Lem\[eTckZw}lyzjjgXRM>LE6NE7UL>UL>VM?YPBWN@VM?VM?WN@WN@VM?RI;PG9QH:SJ<TK=TK=UL>WN@UL>TK=UL>VM?VM?UL>TK=SJ<TK=
21206404      0x1439584       StuffIt Deluxe Segment (data): fVop`vwguvfpqamn^kl\ttdjgX_ZKZTE^WHb[Lb[L`YJ^WH`YJb[Ld]Nc\Mb[Lb[L`YJ_XIaZKc\Mf_PjcTe^Od]Nf_PaZKc]N^YJXSDYTE\WH\WHSO@TQBb_PspaecT
21561607      0x1490107       StuffIt Deluxe Segment (data): fVhiYmm]kkZ^^L[ZHb`NdbP][I][I[YGWUCcaOmkYhfTecQgeSdbP
21932765      0x14EAADD       rzip compressed data - version 90.73 (1432243550 bytes)
22457685      0x156AD55       VMware4 disk image
34625814      0x2105916       StuffIt Deluxe Segment (data): fdbcaZ[YOPNPQO]^\`a_WXV[\Zefddec^_]OPNMNLXYW`a_mnlmnl\][YZXRSQCDB?@>DEC@A?BCADECCDB:;9897BCACDBEFDFGE675'(&./-<=;;:9;98<:9A?>B@?
50157110      0x2FD5636       PC bitmap, Windows 3.x format,, 807 x 605 x 24
51915447      0x3182AB7       StuffIt Deluxe Segment (data): fV_aQ[\McdT]^KON;[WFWR@JC1RJ9TM<VN=\SBbYGSJ9YR@WP>UN<

# Method 1: Wireshark, extract useful files
Filter: tftp.opcode == 1 ⌨️❤️❤️❤️
9	    8.684408491	10.10.10.11	10.10.10.12	TFTP	    60	Read Request, File: plan, Transfer type: octet
11	    37.013336835	10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
19	    54.121134261	10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
22	    59.164775845	10.10.10.11	10.10.10.12	TFTP	62	Read Request, File: program.deb, Transfer type: octet
567	    62.995474862	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture1.bmp, Transfer type: octet
3790	67.595239703	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture2.bmp, Transfer type: octet
146683	111.171248607	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture3.bmp, Transfer type: octet
Filter: tftp.type ⌨️❤️❤️❤️❤️❤️
1	    0.000000000	    10.10.10.11	10.10.10.12	TFTP	67	Write Request, File: instructions.txt, Transfer type: octet 👀
9	    8.684408491	    10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
11	    37.013336835	10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
19	    54.121134261	10.10.10.11	10.10.10.12	TFTP	60	Read Request, File: plan, Transfer type: octet
22	    59.164775845	10.10.10.11	10.10.10.12	TFTP	62	Read Request, File: program.deb, Transfer type: octet 👀
567	    62.995474862	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture1.bmp, Transfer type: octet 👀
3790	67.595239703	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture2.bmp, Transfer type: octet 👀
146683	111.171248607	10.10.10.11	10.10.10.12	TFTP	63	Read Request, File: picture3.bmp, Transfer type: octet 👀

# Highlight the files with ctrl, File → Export Objects → TFTP → Save All ❤️
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads> cat .\instructions.txt ⌨️
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA 👀

https://www.dcode.fr/cipher-identifier
    ROT-13 Cipher 👀
    Substitution Cipher	
https://www.dcode.fr/rot-13-cipher
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN 👀

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads> cat .\plan ⌨️
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF 👀

https://www.dcode.fr/rot-13-cipher
IUSEDTHEPROGRAMANDHIDITWITH-🐱‍💻DUEDILIGENCE🐱‍💻.CHECKOUTTHEPHOTOS

# Upload picture1.bmp, picture2.bmp, picture3.bmp
AsianHacker-picoctf@webshell:~$ rz -y ⌨️
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  picture1.bmp👀  picture2.bmp👀  picture3.bmp👀
AsianHacker-picoctf@webshell:~$ steghide --extract -sf ./picture1.bmp -p "DUEDILIGENCE" ⌨️
steghide: could not extract any data with that passphrase!
AsianHacker-picoctf@webshell:~$ steghide --extract -sf ./picture2.bmp -p "DUEDILIGENCE" ⌨️
steghide: premature end of file "./picture2.bmp" while reading bmp data.
AsianHacker-picoctf@webshell:~$ steghide --extract -sf ./picture3.bmp -p "DUEDILIGENCE" ⌨️
wrote extracted data to "flag.txt".
AsianHacker-picoctf@webshell:~$ cat flag.txt ⌨️
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919} 🔐
```

## Flag
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919} 

## Continue
[Continue](./picoGym0030.md)
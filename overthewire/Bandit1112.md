# Bandit Level 11 → Level 12 Hexdumps and compression and file signatures

## Previous Flag
<b>7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4</b>

## Goal
Use previous password to log in SSH with user <b>bandit12</b> on port <b>2220</b>.  Password stored <b>data.txt</b>, which is a <b>hexdump of a file</b> that has been <b>repeatedly compressed</b>.  Use command <b>“mktemp -d”</b> and <b>cp data.txt to it</b>

## What I learned
```
hex dumps are a hexidecimal view of computer data (HD)
xxd look different than zipped binaries
This exercise many file names mislabeled so need use file command and rename w/ mv
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit12@bandit.labs.overthewire.org -p 2220 ⌨️
bandit12@bandit:~$ ls ⌨️
data.txt
bandit12@bandit:~$ cat data.txt ⌨️ 
00000000: 1f8b 0808 41d4 f767 0203 6461 7461 322e  ....A..g..data2.
00000010: 6269 6e00 0149 02b6 fd42 5a68 3931 4159  bin..I...BZh91AY
00000020: 2653 59a8 ffa7 8f00 001d 7fff dbeb 7ffa  &SY.............
00000030: bb7f a5ef bb7e f5fb fdff b7c7 f3ff ff7f  .....~..........
00000040: ff7f fff7 deba fdfa eff7 dddf b001 3b19  ..............;.
00000050: a200 d01a 0190 0034 0006 800d 0340 0346  .......4.....@.F
00000060: 8000 0340 0320 0069 a034 0640 0346 4680  ...@. .i.4.@.FF.
00000070: 68d1 a68c 8321 9313 4da4 f510 6406 8003  h....!..M...d...
00000080: 4006 9a00 000d 000d 0069 a007 a9a0 001a  @........i......
00000090: 1b50 03d4 01a6 9a1e a001 a343 4683 469a  .P.........CF.F.
000000a0: 3d40 001a 7a8d 01a0 074c 801e a1a6 8064  =@..z....L.....d
000000b0: 01a3 d434 00c4 0d00 000d 0001 a680 1a19  ...4............
000000c0: 0061 0f53 41a0 0000 0d00 341a 0320 0034  .a.SA.....4.. .4
000000d0: d1ea 0168 4882 8244 0130 5550 f16b f52e  ...hH..D.0UP.k..
000000e0: a322 cb9f bb8c aaf6 e244 cc70 b151 47c8  .".......D.p.QG.
000000f0: 6c03 a3ae 4a81 1ee0 03ce 840e a978 2046  l...J........x F
00000100: 630b 4b0d 9883 7078 e7e8 5bfb 68f1 f685  c.K...px..[.h...
00000110: 6f46 771c 3920 449f f0cb 39e2 0841 10b5  oFw.9 D...9..A..
00000120: 8714 e981 115c d1bc 2da4 318b 106c 904e  .....\..-.1..l.N
00000130: 9328 5e97 405a 4054 21db e049 1a32 5f3d  .(^.@Z@T!..I.2_=
00000140: 7069 408f f0a4 8ce5 fbea 282c 51d1 49e4  pi@.......(,Q.I.
00000150: d52f 0762 dd90 27b8 79d3 0499 52e0 060c  ./.b..'.y...R...
00000160: fd91 a474 d408 88f3 1fda d2d1 325a baeb  ...t........2Z..
00000170: bfe7 f0f6 cc3c 776d f369 e73c 47d4 66ea  .....<wm.i.<G.f.
00000180: 4b90 e404 03b3 6a09 4687 945d 09ef 706b  K.....j.F..]..pk
00000190: 8f82 2503 80d0 0a0a 3e60 f879 bf02 2d42  ..%.....>`.y..-B
000001a0: bf37 9c96 4b22 585c 35c8 3cf1 da9f 518b  .7..K"X\5.<...Q.
000001b0: ccd5 a68c 9647 aa38 8a50 89d2 f89c 1ff0  .....G.8.P......
000001c0: 1042 18c3 6549 400d fe17 ec74 3171 6d74  .B..eI@....t1qmt
000001d0: a8bb 0def f11a 5a69 0e70 aa34 0037 b180  ......Zi.p.4.7..
000001e0: 1540 c4d2 0af7 e290 8784 ce9e 147a 6836  .@...........zh6
000001f0: 944b 3f18 2ba2 c620 af92 fb01 184f 3def  .K?.+.. .....O=.
00000200: 1b7d 0162 733d adca 90ac 7142 8319 f703  .}.bs=....qB....
00000210: 5930 69e2 8320 9110 5d63 0db9 9294 d4ef  Y0i.. ..]c......
00000220: 50b9 5907 0924 92c1 014e a284 25ce a6ef  P.Y..$...N..%...
00000230: 67b2 4e06 6d21 4136 2ac0 292d 6638 033c  g.N.m!A6*.)-f8.<
00000240: 21af be4e 13bb b74f 2c10 18c7 eea3 c436  !..N...O,......6
00000250: c988 05e6 5638 1ff1 7724 5385 090a 8ffa  ....V8..w$S.....
00000260: 78f0 d951 192d 4902 0000                 x..Q.-I...
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ whatis xxd gzip bzip2 tar ⌨️
xxd (1)              - make a hex dump or do the reverse.
gzip (1)             - compress or expand files
bzip2 (1)            - a block-sorting file compressor, v1.0.8
tar (1)              - an archiving utility
bandit12@bandit:~$ mktemp -d ⌨️
/tmp/tmp.6z1rr0OeCb
bandit12@bandit:~$ cp data.txt /tmp/tmp.6z1rr0OeCb ⌨️
bandit12@bandit:~$ cd /tmp/tmp.6z1rr0OeCb ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ xxd -r data.txt > hex.txt ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ rm data.txt ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ cat hex.txt ⌨️
4 4��hH��D0UP�k�.�"˟�����D�p�QG�l��J��΄�x Fc������޺�����߰;���4�
��px��[�h���oFw9 D���9A���\Ѽ-�1�l�N�(^�@Z@T!��I2_=pi@�����(,Q�I��/bݐ'�y��R�
                                                                           ���t�����2Z������<wm�i�<G�f�K���j    F��]    �pk��%��

��Zip�47��@��X\5�<�ڟQ��զ��G�8�P�����B�eI@
�����P�YK?+�� ��$��N��%Φ�g�Nm!A6*�)-f8<!��N��O,���6Ɉ�V8�w$S�
��x��Q-Ibandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file hex.txt 
hex.txt: gzip compressed data, was "data2.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 585 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv hex.txt hex.gz ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ ls ⌨️
hex
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file hex ⌨️
hex: bzip2 compressed data, block size = 900k 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv hex hex.bz2 ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ bzip2 -d hex.bz2 ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ ls ⌨️
hex
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file hex ⌨️ 
hex: gzip compressed data, was "data4.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 20480 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv hex hex.gz ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ gzip -d hex.gz ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file hex ⌨️
hex: POSIX tar archive (GNU) 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv hex hex.tar ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ tar -xf hex.tar ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ ls ⌨️
data5.bin  hex.tar
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file data5.bin ⌨️ 
data5.bin: POSIX tar archive (GNU) 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ rm hex.tar ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv data5.bin data5.tar ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ tar -xf data5.tar ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ ls ⌨️
data5.tar  data6.bin
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ rm data5.tar ⌨️ 
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file data6.bin ⌨️ 
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv data6.bin data6.bz2 ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ bzip2 -d data6.bz2 ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ ls ⌨️
data6
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file data6 ⌨️ 
data6: POSIX tar archive (GNU) 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv data6 data6.tar ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ tar -xf data6.tar ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ ls ⌨️
data6.tar  data8.bin
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ rm data6.tar ⌨️ 
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file data8.bin ⌨️
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Apr 10 14:22:57 2025, max compression, from Unix, original size modulo 2^32 49 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ mv data8.bin data8.gz ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ gzip -d data8.gz ⌨️
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ ls ⌨️
data8
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ file data8 ⌨️ 
data8: ASCII text 👀
bandit12@bandit:/tmp/tmp.6z1rr0OeCb$ cat data8 ⌨️
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn 🔐
```

## Flag
<b>FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn</b>

## Continue
[Continue](/overthewire/Bandit1213.md)
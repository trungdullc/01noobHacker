# picoGym Level 450: Verify
Source: https://play.picoctf.org/practice/challenge/450

## Goal
People keep trying to trick my players with imitation flags.<br>
I want to make sure they get the real thing!<br>
I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.<br>
ssh -p 60444 ctf-player@rhea.picoctf.net<br>
Using the password 1db87a14. Accept the fingerprint with yes, and ls once connected to begin.<br>
Remember, in a shell, passwords are hidden!<br>
Checksum: 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a<br>
To decrypt the file once you've verified the hash, run ./decrypt.sh files/<file>.

## What I learned
```
Create a SHA checksum of file/directory
  sha256sum <file>
  sha256sum <directory>/* ❤️

Checksums let you tell if a file is complete and from the original distributor
If the hash doesn't match, it's a different file
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh -p 60444 ctf-player@rhea.picoctf.net ⌨️
The authenticity of host '[rhea.picoctf.net]:60444 ([3.136.191.228]:60444)' can't be established.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[rhea.picoctf.net]:60444' (ED25519) to the list of known hosts.
ctf-player@rhea.picoctf.net's password: ⌨️
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1021-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls ⌨️
checksum.txt  decrypt.sh  files
ctf-player@pico-chall$ ls -la ⌨️
total 20
drwxr-xr-x 3 ctf-player ctf-player   57 Mar 12  2024 .
drwxr-xr-x 1 ctf-player ctf-player   20 Sep 13 02:23 ..
-rw-r--r-- 1 root       root         65 Mar 12  2024 checksum.txt
-rwxr-xr-x 1 root       root        856 Mar 12  2024 decrypt.sh
drwxr-xr-x 2 ctf-player ctf-player 8192 Mar 12  2024 files
ctf-player@pico-chall$ cat checksum.txt ⌨️ 
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a 👀
ctf-player@pico-chall$ cat decrypt.sh ⌨️
        #!/bin/bash

        # Check if the user provided a file name as an argument
        if [ $# -eq 0 ]; then
            echo "Expected usage: decrypt.sh <filename>"
            exit 1
        fi

        # Store the provided filename in a variable
        file_name="$1"

        # Check if the provided argument is a file and not a folder
        if [ ! -f "/home/ctf-player/drop-in/$file_name" ]; then
            echo "Error: '$file_name' is not a valid file. Look inside the 'files' folder with 'ls -R'!"
            exit 1
        fi

        # If there's an error reading the file, print an error message 👀
        if ! openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "/home/ctf-player/drop-in/$file_name" -k picoCTF; then
            echo "Error: Failed to decrypt '$file_name'. This flag is fake! Keep looking!"
        fi
ctf-player@pico-chall$ cd files/ ⌨️
ctf-player@pico-chall$ ls ⌨️
0SgkM1fC  2cdcb2de  5ymaOO07  8WA32dcd  AgQhab96  DINN9cgG  GFWqPjn6  JhHZxLSp  MV2AJR5r  OkXybbh3  RKOBoCMd  UgDsmf5L  WnOWGw9n  ZZzeAnnA  cdZ1Ao5D  gr99Nl0G  lEjMl22a  nVO17uZV  pV3BIyJh  sGOAdKy2  w2pqQhei  z5y1jgty
0aer7B0J  2eijwTPh  6GzNwIbL  8WYKhs9b  AlhLQIGI  DNwq8kf8  GhwoHV4M  JrbVOugk  MXItXLsj  OtnjktH8  RSQ5Ynin  V3xeKcD7  WwobUdQA  aDI9kNj8  chvVzQdY  gru5fnYQ  lMIM4IQe  npy5LylP  pVFybOWo  sKOkwRCd  w80nVzZO  zHpAJtSR
0b3lt0HK  3FOFUCD5  6dZQoo4O  8d6678sz  Au8Ov7jr  Dq8qjJ8S  Gpbebiyr  KAS20Z1p  MYdMdURn  PNNRiq3F  RV6BgBu6  VBHAXd7G  WzxM1rI6  aUzSODcp  cmhkISVH  hRF2XNzg  lbsGcfLr  nxx3UCp8  qAUGa8Jx  svPh5fI5  w8E8Jd9J  zJHj9Wev
0ia8IBYb  3aMAegi2  6mT8PiGl  9LMKbufv  B8RXEf4S  Dr3JaQz7  H6Mlhvd5  KCoDTFB7  MavUz60O  PkxFO6fj  RWol5Yvg  VM5DLaA2  X3z7ayAf  agmwERM5  cvnPhBaQ  iKH9t6m9  lbszmcDf  oLZldZsM  qIqcOTDP  t4IiokLf  wHR2ydKC  zQZjRCvK
0uUAy06x  3laJICck  760ZV0rr  9YFDyvy5  BMlbLM49  Dt7YKSAq  HS8wBLPJ  Ka9uxW6u  Md3PHwRz  PoAr7OrB  RXQH6a3z  VU1Tnx8J  X5Vhdb8H  b5TZpaRr  d0OYmJbG  ih4q9ziU  mDzgzkrP  oNfmBvds  qKIr0SCL  tenQzijC  wvNy3kRU  zmrLJtwD
17iH5ioj  3mHrLQG2  7KoII9M8  9rtRtn1R  BpkwKiOq  E1grB9Sb  IMoTEVt4  Kc5sfOun  MvDDPtoW  PtRzswzh  RrQhgxZJ  VZqopSEM  Y4FnPPHX  b8hbdeFv  d0rJvLyw  jQXi84ic  mMNEp8Zi  oWfAJ9wj  qMqcX95Y  tkv0UoX3  xZDQnhCn  zoSxd2Nl
1CY2Hque  3nroY5Wt  7NBIv8bi  9wXkj9wB  C0PnAa7J  ETctMG1o  IjkDI0gL  KhnreD4t  NAwNCfiS  QBtXtwy6  Rrq6u3VG  Vc1VEpYz  YEOowfPv  bMcbuEVi  d1usLAwO  jnOnhjk8  mg4g9Eoi  ocTCyt2G  qfWh95Q9  tmkJMhbV  y2XXKk9C  zp4ssY0Q
1LPOMJE7  4BRDZhS7  7Snixk9W  9wzwojIO  C3l9qdYz  EYaK1nX6  IwVJbP5E  L9tRKUkW  NB0dzXJg  QCHOeksH  STlIDlxJ  Vc6sosw2  YZc8J6Vf  bVoP3eel  dxJZggkO  kDlGNWXG  mqsieQoa  ocoustRi  rPOS47wB  ud4LEsxA  y8THzTYH
1P5dsfLj  4EqhTV10  7eaPaid5  A2SZHgJV  CChBmQFs  FYfLvi5w  J7BJ7tAo  LZgQIZ9b  NHSLSull  QOHEW95s  Scml7yYd  VhrXhFPH  YjEaz92U  bZEwUIec  eRcEh616  kQMlzWUP  myF2mI2w  orQXAz13  rXWuGW1m  uhLtbHVL  yOmzIQym
1Tst6fbt  4Fegg7AZ  7ylewstJ  A8X4q2Hn  CDg6fdfa  FcWqkSIP  JD0ZwfH8  LnKLtxdL  NYT2nPuv  QTetbcxE  Sn9XVrp6  W7K36eZ0  YkYjwuGz  blsMKCvn  eoW9IJAR  kTDaKoIe  n1PE7llz  oxeNN5uA  rgZiIAPZ  vQmN5k6y  yTiWOwXD
2CyEUmhf  4gMs4KnO  7zsihLxd  ABh1G8a0  CTTDdMGJ  FhDH2g8j  JIPRVMlG  LoSmsO5t  NlN25jkt  QcXjRtBd  TWbymLFA  WYlISi4n  ZEEtJ79A  bnahMLHf  fpXvjTBY  kvSPifOB  n6yqXRv8  oyrMYyZY  rjta4881  vQtPAQBH  yb3Ro4yS
2MgqiK3F  4l9DWh5d  8N3DHyAn  AUijzvDq  CXVq5spu  FkO80Me6  JLE4rtY5  MAd4OQmU  NlymPzCl  Qm0B85oQ  TXecNl9L  WaA6y2oF  ZK4affS3  cO1o2qFY  fw6XlbF3  kvpk6rIp  nSepPhk6  p0qmvEGQ  ryxNv3Er  vmLoCSN5  ypzAaM0c
2R1dcXMM  5HAN1XjT  8NfqFqEn  AWnJiVoE  Cwfv60OS  FlEOSTL0  JLuwL5UE  MBaThKzn  NrbmwP3r  Qxx5KB3R  Tx4sSuiN  WjUfazgU  ZO3IvMwL  cVywfT1b  g1qINnts  l70cIeRx  nTEqj1Ol  p3lVedu9  rzQKjmcB  vt86VpBP  yzW64294
2SLEujSI  5ntikrlo  8OpGe3TY  AfnUEE9s  DGOlVleK  GEtA0Z9a  JVT3ckAg  MLDxW9mt  O3c1wd4r  R84tLxGR  UCbhwrDb  WnH4XGQ0  ZQ7ftng7  cZXSF7wu  gewOpz6a  l8tB6vEL  nU797aVT  pREkecwB  s3TrU3bC  vzBdlMd6  z1DTGQLy
ctf-player@pico-chall$ cat 0SgkM1fC ⌨️
BBvRRqQKUPktNVtHLduMndBGzmE5HjuqrbWePjUvG8r9GmskrgfdGQYbZLrYfXw
ctf-player@pico-chall$ cd .. ⌨️

ctf-player@pico-chall$ cat files/2cdcb2de ⌨️
Salted__EƋ
xhG     u0<     YԘL\Nrove
                         ӕvث
ctf-player@pico-chall$ sha256sum files/2cdcb2de ⌨️ 
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de 👀
ctf-player@pico-chall$ cat files/0SgkM1fC ⌨️
BBvRRqQKUPktNVtHLduMndBGzmE5HjuqrbWePjUvG8r9GmskrgfdGQYbZLrYfXw
ctf-player@pico-chall$ sha256sum files/0SgkM1fC ⌨️
bfdc01f76e8bc1005b776a1ec5549e36be5fb4c1e7f4f74df1b6d6131cee8cea  files/0SgkM1fC
ctf-player@pico-chall$ cat files/2cdcb2de ⌨️
Salted__EƋ
xhG     u0<     YԘL\Nrove
                         ӕvث
ctf-player@pico-chall$ sha256sum files/2cdcb2de ⌨️ 
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de

ctf-player@pico-chall$ ./decrypt.sh ⌨️
Expected usage: decrypt.sh <filename>
ctf-player@pico-chall$ sha256sum files/* | head -n 10 ⌨️
bfdc01f76e8bc1005b776a1ec5549e36be5fb4c1e7f4f74df1b6d6131cee8cea  files/0SgkM1fC
5a17f5fc0a4155df971ab0203d2fb05cc7195987b59140761f32f6d5c31b9de6  files/0aer7B0J
f73351bd65fe61f42271034530a5407d7d55eb3db76fbc9bb571364d3ea68555  files/0b3lt0HK
03745554bdecc96203cc3247cf90c727ee99c93308664a9dc5cd59e2aa15721c  files/0ia8IBYb
afd9ef148f40ceed70513115c42d089a897f50427caf999b2f555c6060bb2f67  files/0uUAy06x
7aff8340cdf99b9fe05035e5baf5a89668702e14ff3fc0f00b77eec42225bf56  files/17iH5ioj
56582ffb01b8f43e23e4d2ede263f5679588391ccd22ae307845fcf23f91b572  files/1CY2Hque
9b54d11b62e34e9e98d3c19acc3ce58f3c981b52a73fcabd8e0e67fd2f34ae08  files/1LPOMJE7
d00acb64414a2159cd79dd4d3f44f7e50d0ce6713e69e28ca3dca17e348a1545  files/1P5dsfLj
d99059d151a6953d015df736a672b2dd0ad3cc859f13114afa127ee36beaef74  files/1Tst6fbt
ctf-player@pico-chall$ sha256sum files/* | grep 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a ⌨️⭐⭐⭐⭐⭐
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de 👀
ctf-player@pico-chall$ ./decrypt.sh files/2cdcb2de ⌨️
picoCTF{trust_but_verify_2cdcb2de} 🔐
ctf-player@pico-chall$ openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "files/2cdcb2de" -k picoCTF ⌨️
picoCTF{trust_but_verify_2cdcb2de} 🔐
```

## Flag
picoCTF{trust_but_verify_2cdcb2de}

## Continue
[Continue](./picoGym0423.md)
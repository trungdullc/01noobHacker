# picoGym Level 308: substitution1
Source: https://play.picoctf.org/practice/challenge/308

## Goal
A second message has come in the mail, and it seems almost identical to the first one.<br>
Maybe the same thing will work again<br>
Download the message here<br>
https://artifacts.picoctf.net/c/182/message.txt

## What I learned
```
Google: Cryptography Solver Online
https://www.quipqiup.com/
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/182/message.txt ⌨️
--2025-09-08 21:27:20--  https://artifacts.picoctf.net/c/182/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 638 [application/octet-stream]
Saving to: 'message.txt'

message.txt                                                100%[======================================================================================================================================>]     638  --.-KB/s    in 0s      

2025-09-08 21:27:20 (402 MB/s) - 'message.txt' saved [638/638]

AsianHacker-picoctf@webshell:/tmp$ cat message.txt ⌨️
SYTe (eakdy tkd sjbyndr yar thjm) jdr j yobr kt skxbnyrd ersndzyo skxbryzyzkc. Skcyreyjcye jdr bdrercyrq gzya j ery kt sajhhrcmre gazsa yrey yarzd sdrjyzwzyo, yrsaczsjh (jcq mkkmhzcm) evzhhe, jcq bdklhrx-ekhwzcm jlzhzyo. Sajhhrcmre nenjhho skwrd j cnxlrd kt sjyrmkdzre, jcq garc ekhwrq, rjsa ozrhqe j eydzcm (sjhhrq j thjm) gazsa ze enlxzyyrq yk jc kchzcr eskdzcm erdwzsr. SYTe jdr j mdrjy gjo yk hrjdc j gzqr jddjo kt skxbnyrd ersndzyo evzhhe zc j ejtr, hrmjh rcwzdkcxrcy, jcq jdr akeyrq jcq bhjorq lo xjco ersndzyo mdknbe jdkncq yar gkdhq tkd tnc jcq bdjsyzsr. Tkd yaze bdklhrx, yar thjm ze: bzskSYT{TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS}

Method 1: https://www.quipqiup.com/
CTFs (short for capture the flag) are a type of computer security competition. Contestants are presented with a set of challenges which test their creativity, technical (and googling) skills, and problem-solving ability. Challenges usually cover a number of categories, and when solved, each yields a string (called a flag) which is submitted to an online scoring service. CTFs are a great way to learn a wide array of computer security skills in a safe, legal environment, and are hosted and played by many security groups around the world for fun and practice. For this problem, the flag is: picoCTF{FR3QU3NCY_4774CK5_4R3_C001_7AA384BC} 🔐

Method 2: Frequency Analysis and Manually Solve
https://www.dcode.fr/frequency-analysis
```

## Flag
picoCTF{FR3QU3NCY_4774CK5_4R3_C001_7AA384BC} 

## Continue
[Continue](./picoGym0309.md)
# picoGym Level 0166: Python Wrangling
Source: https://play.picoctf.org/practice/challenge/166

## Goal
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

## What I learned
```
python3 argument
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:/tmp$ cd ⌨️
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py ⌨️
--2025-08-19 03:27:57--  https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py 
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1328 (1.3K) [application/octet-stream]
Saving to: 'ende.py'

ende.py                                                    100%[======================================================================================================================================>]   1.30K  --.-KB/s    in 0s      

2025-08-19 03:27:57 (1.09 GB/s) - 'ende.py' saved [1328/1328]

AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt ⌨️
--2025-08-19 03:28:20--  https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 33 [application/octet-stream]
Saving to: 'pw.txt'

pw.txt                                                     100%[======================================================================================================================================>]      33  --.-KB/s    in 0s      

2025-08-19 03:28:20 (10.7 MB/s) - 'pw.txt' saved [33/33]

AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en ⌨️
--2025-08-19 03:28:39--  https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 140 [application/octet-stream]
Saving to: 'flag.txt.en'

flag.txt.en                                                100%[======================================================================================================================================>]     140  --.-KB/s    in 0s      

2025-08-19 03:28:39 (60.0 MB/s) - 'flag.txt.en' saved [140/140]

AsianHacker-picoctf@webshell:/tmp$ ls -la ⌨️
total 12
drwxrwxrwt 1 root                root                  54 Aug 19 03:28 .
drwxr-xr-x 1 root                root                  50 Aug 19 03:02 ..
drwx------ 3 root                root                  41 Mar  5 02:13 .wine-0
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 1328 Mar 16  2021 ende.py 👀
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf  140 Mar 16  2021 flag.txt.en 👀
drwxr-xr-x 2 root                root                   6 Mar  5 02:09 hsperfdata_root
drwxr-xr-x 3 root                root                  45 Mar  5 02:13 node-compile-cache
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf   33 Mar 16  2021 pw.txt 👀
AsianHacker-picoctf@webshell:/tmp$ file flag.txt.en ⌨️
flag.txt.en: ASCII text, with no line terminators
AsianHacker-picoctf@webshell:/tmp$ file pw.txt ⌨️
pw.txt: ASCII text
AsianHacker-picoctf@webshell:/tmp$ cat pw.txt ⌨️
aa821c16aa821c16aa821c16aa821c16
AsianHacker-picoctf@webshell:/tmp$ cat flag.txt.en ⌨️
gAAAAABgUAIWjVP_Ne1VPrHlLZKpvfaifN7qlLoN7NEzOpAl55av7sPuV8wQZj9V-6oI_x4L10O8R-b9c19INaTFrlGbT6YxQeLXd2S3FQA8HmFxU9NILpJGEtVPsGpzPAmLSsRwezRX
AsianHacker-picoctf@webshell:/tmp$ python3 ende.py ⌨️
Usage: ende.py (-e/-d) [file] 👀
AsianHacker-picoctf@webshell:/tmp$ python3 ende.py -d flag.txt.en ⌨️
Please enter the password:aa821c16aa821c16aa821c16aa821c16 ⌨️
picoCTF{4p0110_1n_7h3_h0us3_aa821c16} 🔐
```

## Flag
picoCTF{4p0110_1n_7h3_h0us3_aa821c16}

## Continue
[Continue](./picoGym0371.md)
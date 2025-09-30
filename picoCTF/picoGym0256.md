# picoGym Level 256: bloat.py
Source: https://play.picoctf.org/practice/challenge/256

## Goal
Run this Python program in the same directory as this encrypted flag.<br>
https://artifacts.picoctf.net/c/105/bloat.flag.py<br>
https://artifacts.picoctf.net/c/105/flag.txt.enc

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/105/bloat.flag.py https://artifacts.picoctf.net/c/105/flag.txt.enc ⌨️
--2025-09-26 23:50:00--  https://artifacts.picoctf.net/c/105/bloat.flag.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1557 (1.5K) [application/octet-stream]
Saving to: 'bloat.flag.py'

bloat.flag.py                                              100%[======================================================================================================================================>]   1.52K  --.-KB/s    in 0s      

2025-09-26 23:50:00 (377 MB/s) - 'bloat.flag.py' saved [1557/1557]

--2025-09-26 23:50:00--  https://artifacts.picoctf.net/c/105/flag.txt.enc
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 35 [application/octet-stream]
Saving to: 'flag.txt.enc'

flag.txt.enc                                               100%[======================================================================================================================================>]      35  --.-KB/s    in 0s      

2025-09-26 23:50:00 (39.4 MB/s) - 'flag.txt.enc' saved [35/35]

FINISHED --2025-09-26 23:50:00--
Total wall clock time: 0.2s
Downloaded: 2 files, 1.6K in 0s (317 MB/s)

AsianHacker-picoctf@webshell:~$ cat bloat.flag.py ⌨️
import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

def arg133(arg432):
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]: 👀
    return True
  else:
    print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
a[81]+a[68]+a[66]+a[83])
    sys.exit(0)
    return False

def arg111(arg444):
  return arg122(arg444.decode(), a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+\
a[75]+a[72]+a[78]+a[77])

# Please enter correct password for flag: 
def arg232():
  return input(a[47]+a[75]+a[68]+a[64]+a[82]+a[68]+a[94]+a[68]+a[77]+a[83]+\
a[68]+a[81]+a[94]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+\
a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+a[81]+a[67]+a[94]+\
a[69]+a[78]+a[81]+a[94]+a[69]+a[75]+a[64]+a[70]+a[25]+a[94])
def arg132():
  return open('flag.txt.enc', 'rb').read()

def arg112():
  print(a[54]+a[68]+a[75]+a[66]+a[78]+a[76]+a[68]+a[94]+a[65]+a[64]+a[66]+\
a[74]+a[13]+a[13]+a[13]+a[94]+a[88]+a[78]+a[84]+a[81]+a[94]+a[69]+\
a[75]+a[64]+a[70]+a[11]+a[94]+a[84]+a[82]+a[68]+a[81]+a[25])

def arg122(arg432, arg423):
    arg433 = arg423
    i = 0
    while len(arg433) < len(arg432):
        arg433 = arg433 + arg423[i]
        i = (i + 1) % len(arg423)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(arg432,arg433)])
arg444 = arg132()
arg432 = arg232()
arg133(arg432)
arg112()
arg423 = arg111(arg444)
print(arg423)
sys.exit(0)

# Find cmp
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

print(a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68])

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️ 
happychance 👀

AsianHacker-picoctf@webshell:~$ python3 bloat.flag.py ⌨️
Please enter correct password for flag: happychance ⌨️
happychance
Welcome back... your flag, user:
picoCTF{d30bfu5c4710n_f7w_5e14b257} 🔐
```

## Flag
picoCTF{d30bfu5c4710n_f7w_5e14b257}

## Continue
[Continue](./picoGym0121.md)
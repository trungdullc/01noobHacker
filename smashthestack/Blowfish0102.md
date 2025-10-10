# Blowfish Level 01 → 02 SSH Login w/ ssh

## Previous Flag
```
N/A
```

## Goal
Instructions located in the README file in each levels home directory<br>
Passwords are stored in /pass<br>
Use /code as /tmp<br>
Telnet to blowfish.smashthestack.org port 6666 to recieve an encrypted passwd.<br>
Decrypt it and log in to level2<br><br>
ssh -l level2 blowfish.smashthestack.org -p 2222

## What I learned
```
ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -l level2 blowfish.smashthestack.org -p 2222
ROT13
```

## Solution
```
# Enable built-in Telnet client
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> dism /online /Enable-Feature /FeatureName:TelnetClient ⌨️

Deployment Image Servicing and Management tool
Version: 10.0.19041.3636

Image Version: 10.0.19045.6332

Enabling feature(s)
[==========================100.0%==========================] 
The operation completed successfully.

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> telnet blowfish.smashthestack.org 6666 ⌨️

Encrypted Password is: GungJnfRnfl 👀

Connection to host lost.

https://www.dcode.fr/cipher-identifier
    Note: Could not identify but ChatGPT
https://www.dcode.fr/rot-13-cipher
    ThatWasEasy 🔐

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh -l level2 blowfish.smashthestack.org -p 2222 ⌨️
Unable to negotiate with 84.22.114.35 port 2222: no matching host key type found. Their offer: ssh-rsa,ssh-dss
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -l level2 blowfish.smashthestack.org -p 2222 ⌨️❤️
The authenticity of host '[blowfish.smashthestack.org]:2222 ([84.22.114.35]:2222)' can't be established.
RSA key fingerprint is SHA256:c+1K1fiQNZXmSzGDooOfwrE7FJWhHjMVkP8oiXeqiuo.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[blowfish.smashthestack.org]:2222' (RSA) to the list of known hosts.
level2@blowfish.smashthestack.org's password: ⌨️ ThatWasEasy
   _        __                          ___              __ 
 /\ \     /\_ \                       /'___\ __         /\ \
 \ \ \____\//\ \     ___   __  __  __/\ \__//\_\    ____\ \ \___
  \ \ '__`\ \ \ \   / __`\/\ \/\ \/\ \ \  __\/\ \  /' __\\ \  _ `\
   \ \ \_\ \ \_\ \_/\ \_\_\ \ \_/ \_/ \ \ \_/\ \ \/\__  `\\ \ \ \ \
    \ \____/ /\____\ \____/\ \___x___/'\ \_\  \ \_\/\____/ \ \_\ \_\
     \/___/  \/____/\/___/  \/__//__/   \/_/   \/_/\/___/   \/_/\/_/
     wargame ++ smashthestack.org ++ now in version 2.0

     1. Thou shalt NOT root or otherwise harm the box.
     2. Thou shalt NOT do any network access from this box.
     3. Thou shalt NOT use /tmp, /levels/tmp or /var/tmp for personal code.
     4. Thou shalt give the root pass to l3thal if you manage to change it.

     Passwords are in /pass.
     There is a README in each users home directory.
     /tmp && /var/tmp will be flushed daily by cron.
     Use /code plz for umm, code ;D
     IF YOU LEAVE FILES IN /levels/tmp U SUCK ..plz remove them kthnx! ;D
     The password for the last level will get you into
     Tux, the more advanced wargame. Join #blowfish on
     irc.smashthestack.org with any questions.

     Admin - s0ttle@smashthestack.org
level2@blowfish:~$ whoami ⌨️
level2
level2@blowfish:~$ ls ⌨️
README
level2@blowfish:~$ cat README ⌨️ 
There is a backdoor to the next level hidden somewhere on this system, find it, and get the pass for level3 from /pass/level3
```

## Flag
ThatWasEasy

## Continue
[Continue](./Blowfish0204.md)
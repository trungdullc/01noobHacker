# picoGym Level 0424: Super SSH
Source: https://play.picoctf.org/practice/challenge/424

## Goal
Can you ssh as <b>ctf-player to titan.picoctf.net</b> at <b>port 51138</b> to get the flag? You'll also need the password <b>f3b61b38</b>. If asked, accept the fingerprint with yes.

## What I learned
```
Secure Shell (SSH)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:/tmp$ ssh ctf-player@titan.picoctf.net -p 51138 ⌨️
The authenticity of host '[titan.picoctf.net]:51138 ([3.139.174.234]:51138)' can't be established.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[titan.picoctf.net]:51138' (ED25519) to the list of known hosts.
ctf-player@titan.picoctf.net's password: ⌨️
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_3e293eea} 🔐
Connection to titan.picoctf.net closed.
```

## Flag
picoCTF{s3cur3_c0nn3ct10n_3e293eea}

## Continue
[Continue](./picoGym0411.md)
# picoGym Level 0436: SansAlpha
Source: https://play.picoctf.org/practice/challenge/436

## Goal
The Multiverse is within your grasp! Unfortunately, the server that contains the secrets of the multiverse is in a universe where keyboards only have numbers and (most) symbols.<br>
sh -p 57647 ctf-player@mimas.picoctf.net<br>
Use password: 6abf4a82

## What I learned
```
Was trying to get to
  /usr/bin/cat
  /usr/bin/echo
  /usr/bin/base64                           # Was most stable option
# Navigate System by wildcards and numbers
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh -p 57647 ctf-player@mimas.picoctf.net ⌨️
The authenticity of host '[mimas.picoctf.net]:57647 ([52.15.88.75]:57647)' can't be established.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[mimas.picoctf.net]:57647' (ED25519) to the list of known hosts.
ctf-player@mimas.picoctf.net's password: ⌨️
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1016-aws x86_64)

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

# Method 1: Wildcards
SansAlpha$ ls ⌨️                                      # Remember: Only numbers and some special charactesr
SansAlpha: Unknown character detected
SansAlpha$ * ⌨️
bash: blargh: command not found
SansAlpha$ */ ⌨️
bash: blargh/: Is a directory

SansAlpha$ ./* ⌨️                                     # These 2 makes the most since to me in current dir
bash: ./blargh: Is a directory
SansAlpha$ ./*/* ⌨️
bash: ./blargh/flag.txt: Permission denied

SansAlpha$ /* ⌨️                                      # checks root directory
bash: /bin: Is a directory
SansAlpha$ */* ⌨️
bash: blargh/flag.txt: Permission denied
SansAlpha$ /*/??? ⌨️                                  # trying get into /bin/cat but awk is before
E: Invalid operation /bin/awk
SansAlpha$ /*/?????? ⌨️
/bin/base32: extra operand ‘/bin/base64’
Try '/bin/base32 --help' for more information.
SansAlpha$ /*/????64 */* ⌨️
/bin/base64: extra operand ‘/bin/x86_64’
Try '/bin/base64 --help' for more information.
SansAlpha$ /*/???[!_]64 */* ⌨️
/bin/base64: extra operand ‘blargh/flag.txt’
Try '/bin/base64 --help' for more information.
SansAlpha$ /*/???[!_]64 */????.* ⌨️
cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV84YjNkODNhZH0=
SansAlpha$ /*/???[!_]64 */????.??? ⌨️
cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV84YjNkODNhZH0=

https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=Y21WMGRYSnVJREFnY0dsamIwTlVSbnMzYURFMVgyMTFNVGN4ZGpOeU5UTmZNVFZmYlRSa2JqTTFOVjg0WWpOa09ETmhaSDA9

AsianHacker-picoctf@webshell:~$ echo "cmV0dXJuIDAgcGljb0NURns3aDE1X211MTcxdjNyNTNfMTVfbTRkbjM1NV84YjNkODNhZH0=" | base64 -d ⌨️
return 0 picoCTF{7h15_mu171v3r53_15_m4dn355_8b3d83ad} 🔐

Method 2: awk shorthand: awk '$0' flag.txt (NOTE: NOT 100% success rate) ⚠️
SansAlpha$ /???/??? "$0" ./*/????.* ⌨️
E: Invalid operation /bin/awk
SansAlpha$ ___=($(/???/??? 2>&1)) ⌨️                           # Trying capture E: but didn't work
SansAlpha$ ${___[0]} ⌨️
bash: WARNING:: command not found
SansAlpha$ ${___[1]} ⌨️
apt 2.0.6 (amd64)
Usage: apt [options] command
SansAlpha$ ${___[17]} ⌨️                                       # Use above method, just know this method exist as well
Usage: mawk [Options] [Program] [file ...]
```

## Flag
picoCTF{7h15_mu171v3r53_15_m4dn355_8b3d83ad} 

## Continue
[Continue](./picoGym0377.md)
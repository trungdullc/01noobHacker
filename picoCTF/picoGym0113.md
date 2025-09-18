# picoGym Level 113: Disk, disk, sleuth!
Source: https://play.picoctf.org/practice/challenge/113

## Goal
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz<br>
https://mercury.picoctf.net/static/920731987787c93839776ce457d5ecd6/dds1-alpine.flag.img.gz

## What I learned
```
srch_strings
strings

.bash_history
.ash_history (Alpine Linux)
.zsh_history (zsh)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/920731987787c93839776ce457d5ecd6/dds1-alpine.flag.img.gz ⌨️
--2025-09-17 21:08:34--  https://mercury.picoctf.net/static/920731987787c93839776ce457d5ecd6/dds1-alpine.flag.img.gz
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 29768910 (28M) [application/octet-stream]
Saving to: 'dds1-alpine.flag.img.gz'

dds1-alpine.flag.img.gz                            100%[=============================================================================================================>]  28.39M  1.82MB/s    in 16s     

2025-09-17 21:08:50 (1.82 MB/s) - 'dds1-alpine.flag.img.gz' saved [29768910/29768910]

AsianHacker-picoctf@webshell:/tmp$ gunzip dds1-alpine.flag.img.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
dds1-alpine.flag.img 👀  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ file dds1-alpine.flag.img ⌨️
dds1-alpine.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x10,81,1), startsector 2048, 260096 sectors
AsianHacker-picoctf@webshell:/tmp$ fsstat dds1-alpine.flag.img ⌨️
Cannot determine file system type
AsianHacker-picoctf@webshell:/tmp$ exiftool dds1-alpine.flag.img ⌨️ 
ExifTool Version Number         : 12.40
File Name                       : dds1-alpine.flag.img
Directory                       : .
File Size                       : 128 MiB
File Modification Date/Time     : 2021:03:16 00:19:29+00:00
File Access Date/Time           : 2025:09:17 21:09:22+00:00
File Inode Change Date/Time     : 2025:09:17 21:09:14+00:00
File Permissions                : -rw-rw-r--
Error                           : Unknown file type

# Method 1: srch_strings or strings
AsianHacker-picoctf@webshell:/tmp$ strings dds1-alpine.flag.img | grep "picoCTF" ⌨️
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0} 🔐
AsianHacker-picoctf@webshell:/tmp$ srch_strings dds1-alpine.flag.img | grep picoCTF ⌨️
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0} 🔐

AsianHacker-picoctf@webshell:/tmp$ mmls dds1-alpine.flag.img ⌨️
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)

AsianHacker-picoctf@webshell:/tmp$ fls -r dds1-alpine.flag.img -o 2048 | grep "picoCTF" ⌨️
AsianHacker-picoctf@webshell:/tmp$ fls -r dds1-alpine.flag.img -o 2048 | grep "flag" ⌨️
AsianHacker-picoctf@webshell:/tmp$ fls -r dds1-alpine.flag.img -o 2048 | grep "history" ⌨️

AsianHacker-picoctf@webshell:/tmp$ fls dds1-alpine.flag.img -o 2048 ⌨️
d/d 10161:      home
d/d 11: lost+found
r/r 12: .dockerenv
d/d 2033:       bin
d/d 8129:       boot
d/d 6097:       dev
d/d 16257:      etc
d/d 28449:      lib
d/d 22353:      media
d/d 24385:      mnt
d/d 26417:      opt
d/d 24386:      proc
d/d 26418:      root
d/d 24387:      run
d/d 26419:      sbin
d/d 20321:      srv
d/d 20322:      sys
d/d 20323:      tmp
d/d 24388:      usr
d/d 20324:      var
V/V 32513:      $OrphanFiles
AsianHacker-picoctf@webshell:/tmp$ fls dds1-alpine.flag.img -o 26418 ⌨️
Cannot determine file system type
# Note: Searching randomly thru system is a pain use Autopsy

# Method 2: Autopsy (easier to find locatin than above)
```

## Flag
picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}

## Continue
[Continue](./picoGym0081.md)
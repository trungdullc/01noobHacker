# picoGym Level 413: Dear Diary
Source: https://play.picoctf.org/practice/challenge/413

## Goal
If you can find the flag on this disk image, we can close the case for good!<br>
Download the disk image here.<br>
https://artifacts.picoctf.net/c_titan/63/disk.flag.img.gz

## What I learned
```
In digital forensics, analysts often start with a small window of sectors (commonly 8 or 16) to check signatures, headers, and offsets before diving deeper into partitions or carving data.

Google: defineinnocuous
  not harmful or offensive

Others:
  Forensic Toolkit (FTK): https://www.exterro.com/ftk-product-downloads/forensic-toolkit-ftk-8-0-0
  Foremost
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/63/disk.flag.img.gz ⌨️
--2025-09-22 02:55:32--  https://artifacts.picoctf.net/c_titan/63/disk.flag.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 68353329 (65M) [application/octet-stream]
Saving to: 'disk.flag.img.gz'

disk.flag.img.gz                                           100%[======================================================================================================================================>]  65.19M  1.82MB/s    in 36s     

2025-09-22 02:56:08 (1.82 MB/s) - 'disk.flag.img.gz' saved [68353329/68353329]

AsianHacker-picoctf@webshell:~$ gunzip disk.flag.img.gz ⌨️

gzip: disk.flag.img: No space left on device ⚠️
AsianHacker-picoctf@webshell:~$ mv disk.flag.img.gz /tmp ⌨️
AsianHacker-picoctf@webshell:~$ cd /tmp ⌨️
AsianHacker-picoctf@webshell:/tmp$ gunzip disk.flag.img.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
disk.flag.img 👀 hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ file disk.flag.img ⌨️
disk.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x26,94,56), startsector 2048, 614400 sectors; partition 2 : ID=0x82, start-CHS (0x26,94,57), end-CHS (0x47,1,58), startsector 616448, 524288 sectors; partition 3 : ID=0x83, start-CHS (0x47,1,59), end-CHS (0x82,138,8), startsector 1140736, 956416 sectors
AsianHacker-picoctf@webshell:/tmp$ exiftool disk.flag.img ⌨️
ExifTool Version Number         : 12.40
File Name                       : disk.flag.img
Directory                       : .
File Size                       : 1024 MiB
File Modification Date/Time     : 2024:02:17 22:59:43+00:00
File Access Date/Time           : 2025:09:22 02:57:10+00:00
File Inode Change Date/Time     : 2025:09:22 02:56:59+00:00
File Permissions                : -rw-rw-r--
Error                           : Unknown file type
AsianHacker-picoctf@webshell:/tmp$ strings disk.flag.img | grep "picoCTF" ⌨️

# Method 1: Sleuth Kit
AsianHacker-picoctf@webshell:/tmp$ mmls disk.flag.img ⌨️
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000616447   0000614400   Linux (0x83)
003:  000:001   0000616448   0001140735   0000524288   Linux Swap / Solaris x86 (0x82)
004:  000:002   0001140736   0002097151   0000956416   Linux (0x83) 👀

AsianHacker-picoctf@webshell:/tmp$ fls disk.flag.img -o 1140736 ⌨️
d/d 32513:      home
d/d 11: lost+found
d/d 32385:      boot
d/d 64769:      etc
d/d 32386:      proc
d/d 13: dev
d/d 32387:      tmp
d/d 14: lib
d/d 32388:      var
d/d 21: usr
d/d 32393:      bin
d/d 32395:      sbin
d/d 32539:      media
d/d 203:        mnt
d/d 32543:      opt
d/d 204:        root 👀
d/d 32544:      run
d/d 205:        srv
d/d 32545:      sys
d/d 32530:      swap
V/V 119417:     $OrphanFiles

AsianHacker-picoctf@webshell:/tmp$ fls disk.flag.img -o 1140736 204 ⌨️
r/r 1837:       .ash_history
d/d 1842:       secret-secrets 👀

# Note: d/d means directory 👀
AsianHacker-picoctf@webshell:/tmp$ icat disk.flag.img -o 1140736 1842 ⌨️
2
 .
force-wait.sh4(innocuous-file.txt5its-all-in-the-name
                                                     f
AsianHacker-picoctf@webshell:/tmp$ fls disk.flag.img -o 1140736 1842 ⌨️
r/r 1843:       force-wait.sh
r/r 1844:       innocuous-file.txt 👀
r/r 1845:       its-all-in-the-name 👀

# 8: number of sectors to extract starting from the specified offset
AsianHacker-picoctf@webshell:/tmp$ icat -o 0001140736  disk.flag.img 8 | strings | head -n 10 ⌨️
#eQY
z7OU
oyseoyseoyse
oyse`]
oyseoyseoyse
oyseoyseoyse
oyse
lost+found
boot
oyseoyseoyse

AsianHacker-picoctf@webshell:/tmp$ icat -o 0001140736  disk.flag.img 8 | strings | sort | uniq | grep "file" ⌨️
base.files
bootchart.files
btrfs.files
cachefiles
cachefiles.ko.gz
cryptkey.files
cryptsetup.files
dhcp.files
ewaitfile
filelayout
flexfilelayout
https.files
innocuous-file.txt 👀
keymap.files
lvm.files
nbd.files
network.files
nfs_layout_flexfiles.ko.gz
nfs_layout_nfsv41_files.ko.gz
original-filename
profile
profile.d
raid.files
wireguard.files
xfs.files
zfs.files

# View contents in Hex, xxd
AsianHacker-picoctf@webshell:/tmp$ icat -o 0001140736 disk.flag.img 8 | xxd | grep ".txt" ⌨️
001f8840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
001fbc40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
001fdc40: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
001ff440: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00201840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00203c40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00206040: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00207840: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00209c40: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
0020b440: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
0020d840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
0020fc40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00211440: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......

# Expanded grep search to display 3 lines (-A3) of context after each match
AsianHacker-picoctf@webshell:/tmp$ icat -o 0001140736  disk.flag.img 8 | xxd | grep ".txt" -A3 ⌨️
001f8840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
001f8850: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001f8860: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001f8870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
001fbc40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
001fbc50: a803 1101 6f72 6967 696e 616c 2d66 696c  ....original-fil
001fbc60: 656e 616d 6500 0000 0000 0000 0000 0000  ename...........
001fbc70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
001fdc40: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
001fdc50: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001fdc60: 0000 0000 0000 0000 3507 0000 8c03 0301  ........5.......
001fdc70: 7069 6300 0000 0000 0000 0000 0000 0000  pic👀.............
--
001ff440: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
001ff450: a803 0301 6f43 5400 0000 0000 0000 0000  ....oCT👀.........
001ff460: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001ff470: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00201840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00201850: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
00201860: 467b 3100 0000 0000 0000 0000 0000 0000  F{1👀.............
00201870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00203c40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00203c50: a803 0301 5f35 3300 0000 0000 0000 0000  ...._53👀.........
00203c60: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00203c70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00206040: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00206050: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
00206060: 335f 6e00 0000 0000 0000 0000 0000 0000  3_n👀.............
00206070: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00207840: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00207850: a803 0301 346d 3300 0000 0000 0000 0000  ....4m3👀.........
00207860: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00207870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00209c40: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00209c50: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
00209c60: 355f 3800 0000 0000 0000 0000 0000 0000  5_8👀.............
00209c70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
0020b440: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
0020b450: a803 0301 3064 3200 0000 0000 0000 0000  ....0d2👀.........
0020b460: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0020b470: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
0020d840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
0020d850: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
0020d860: 3462 3300 0000 0000 0000 0000 0000 0000  4b3👀.............
0020d870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
0020fc40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
0020fc50: a803 0201 307d 0000 0000 0000 0000 0000  ....0}👀..........
0020fc60: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0020fc70: 0000 0000 0000 0000W 0000 0000 0000 0000  ................
--
00211440: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00211450: 0000 0000 0000 0000 3507 0000 9c03 1301  ........5.......
00211460: 6974 732d 616c 6c2d 696e 2d74 6865 2d6e  its-all-in-the-n
00211470: 616d 6500 0000 0000 0000 0000 0000 0000  ame.............

# Method 2: Autopsy
Data Sources
  disk.flag.image_1 Host
    disk.flag.img
      vol4 (Linux (0x83) 1140736-2097151)
        root
          secret-secrets (5)

# Examine bytes of image of innocuous-file.txt
# Run in HxD
# Search innocuous
  Search direction
    All
# Look thru all ASCII dump
```

## Flag
picoCTF{1_533_n4m35_80d24b30}

## Continue
[Continue](./picoGym0415.md)
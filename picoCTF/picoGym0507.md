# picoGym Level 506: DISKO 3
Source: https://play.picoctf.org/practice/challenge/507

## Goal
Can you find the flag in this disk image? This time, its not as plain as you think it is!<br>
Download the disk image here.<br>
https://artifacts.picoctf.net/c/543/disko-3.dd.gz

## What I learned
```
fls
icat

Kali Linux:
fdisk -l disko-3.dd ⌨️                          # Analyze the Disk Layout
sudo mkdir /mnt/disko-3 ⌨️
sudo mount -o loop disko-3.dd /mnt/disko- ⌨️    # Mount the Disk Image
ls /mnt/disko-3 ⌨️                              # Explore the Mounted Image
ls -l /mnt/disko-3/log ⌨️
cp /mnt/disko-3/log/flag.gz . ⌨️
gunzip flag.gz ⌨️
cat flag ⌨️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/543/disko-3.dd.gz ⌨️
--2025-09-15 22:59:54--  https://artifacts.picoctf.net/c/543/disko-3.dd.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 20766101 (20M) [application/octet-stream]
Saving to: 'disko-3.dd.gz'

disko-3.dd.gz                                              100%[======================================================================================================================================>]  19.80M  1.82MB/s    in 11s     


2025-09-15 23:00:05 (1.82 MB/s) - 'disko-3.dd.gz' saved [20766101/20766101]

AsianHacker-picoctf@webshell:/tmp$ gunzip disko-3.dd.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
disko-3.dd  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ file disko-3.dd ⌨️
disko-3.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat", Media descriptor 0xf8, sectors/track 32, heads 8, sectors 204800 (volumes > 32 MB), FAT (32 bit), sectors/FAT 1576, serial number 0x49838d0b, unlabeled
AsianHacker-picoctf@webshell:/tmp$ mmls disko-3.dd          # Note: boot sector not a partition, so no output ⌨️

# Method 1: fls and icat
AsianHacker-picoctf@webshell:/tmp$ fls disko-3.dd ⌨️
d/d 4:  log 👀
v/v 3225859:    $MBR
v/v 3225860:    $FAT1
v/v 3225861:    $FAT2
V/V 3225862:    $OrphanFiles
AsianHacker-picoctf@webshell:/tmp$ fls disko-3.dd 4 ⌨️
d/d 22: private
d/d 24: sysstat
d/d 26: stunnel4
d/d 28: mysql
d/d 30: inetsim
d/d 32: installer
r/r 519123:     vmware-vmsvc-root.2.log
r/r 519125:     kern.log.4.gz
r/r 519127:     Xorg.0.log
r/r 519130:     vmware-network.4.log
r/r 519132:     boot.log
r/r 519134:     syslog.3.gz
r/r 519137:     vmware-vmtoolsd-root.log
r/r 522627:     daemon.log
r/r 522628:     flag.gz
r/r * 522629:   _ESSAGES
r/r 522632:     alternatives.log.2.gz
r/r 522634:     debug
d/d 522636:     lightdm
r/r 522639:     vmware-network.6.log
r/r 522642:     alternatives.log
r/r 555285:     vmware-vmsvc-root.1.log
r/r 555288:     Xorg.0.log.old
r/r 555291:     vmware-network.8.log
r/r 555294:     vmware-vmsvc-root.log
r/r 555297:     vmware-vmsvc-root.3.log
r/r 556259:     boot.log.6
r/r 556262:     vmware-network.5.log
r/r 556265:     macchanger.log.4.gz
d/d 556267:     apt
r/r 556269:     dpkg.log.1
r/r 556271:     boot.log.5
r/r 556273:     wtmp
r/r 575571:     dpkg.log.5.gz
r/r 575573:     lastlog
r/r 575576:     vmware-network.3.log
r/r 575578:     syslog.4.gz
r/r 575580:     boot.log.1
r/r 575583:     vmware-network.2.log
r/r 575585:     faillog
r/r 603171:     kern.log.3.gz
r/r 603173:     dpkg.log.4.gz
r/r 603176:     vmware-network.1.log
r/r 603179:     vmware-network.7.log
d/d 603181:     journal
r/r 603184:     vmware-network.log
r/r 603186:     dpkg.log.2.gz
AsianHacker-picoctf@webshell:/tmp$ fls disko-3.dd 4 | grep flag ⌨️
r/r 522628:     flag.gz

# extract flag.gz out of memory w/ icat
AsianHacker-picoctf@webshell:/tmp$ icat disko-3.dd 522628 > flag.gz ⌨️❤️❤️❤️❤️❤️
AsianHacker-picoctf@webshell:/tmp$ gunzip flag.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
disko-3.dd  flag  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ file flag ⌨️
flag: ASCII text
AsianHacker-picoctf@webshell:/tmp$ cat flag ⌨️
Here is your flag
picoCTF{n3v3r_z1p_2_h1d3_654235e0} 🔐

# Method 2: Autopsy
Create a new case
Tools → Run Ingest Modules → disko-3.dd
Go to top right and click Keyword search and search for flag
flag.gz will be highlighted and Autopsy will automaticaly decompress the gzip file automatically be visible in Data Content Tab

# Method 3: binwalk (Use w/ caution: memory exhaust, also more math required)
# extract embedded files
AsianHacker-picoctf@webshell:/tmp$ binwalk -e disko-3.dd ⌨️
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
18246144      0x1166A00       gzip compressed data, from Unix, last modified: 2025-02-25 23:11:02
18287104      0x1170A00       gzip compressed data, from Unix, last modified: 2025-03-09 05:50:00
18654208      0x11CA400       gzip compressed data, has original file name: "flag", from Unix, last modified: 2025-07-17 15:06:53
19439104      0x1289E00       gzip compressed data, from Unix, last modified: 2025-01-22 16:03:08

# 18654208 / 512 = 36434
# count 19439104 - 18654208 / 512 = 1533
AsianHacker-picoctf@webshell:/tmp$ dd if=disko-3.dd of=flag.gz bs=512 skip=36434 count=1533 ⌨️
dd: error writing 'flag.gz': No space left on device
1145+0 records in
1144+0 records out
585728 bytes (586 kB, 572 KiB) copied, 0.0101116 s, 57.9 MB/s
AsianHacker-picoctf@webshell:/tmp$ gunzip flag.gz ⌨️

gzip: flag.gz: decompression OK, trailing garbage ignored
AsianHacker-picoctf@webshell:/tmp$ cat flag ⌨️
Here is your flag
picoCTF{n3v3r_z1p_2_h1d3_654235e0} 🔐
```

## Flag
picoCTF{n3v3r_z1p_2_h1d3_654235e0}

## Continue
[Continue](./picoGym0019.md)
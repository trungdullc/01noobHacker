# picoGym Level 87: Pitter, Patter, Platters
Source: https://play.picoctf.org/practice/challenge/87

## Goal
'Suspicious' is written all over this disk image.<br>
Download suspicious.dd.sda1<br>
https://challenge-files.picoctf.net/c_shape_facility/568c311b7dcfcd8a4ff1b30ad1c9dcb41069add275d72304a79d2e5d31c1f5fe/suspicious.dd.sda1

## What I learned
```
mount -o loop needs CAP_SYS_ADMIN, which is blocked in sandbox
Instead of mount, use user-space tools that don’t need root

Slack space is the unused space at the end of a file cluster. When a file doesn’t fully occupy its allocated cluster, the leftover space is called slack space. This hidden area can sometimes contain remnants of previous files or hidden data.
        Slack files are created with a “-slack” extension
        icat -s
        xxd -s <hexaddy>
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_shape_facility/ 568c311b7dcfcd8a4ff1b30ad1c9dcb41069add275d72304a79d2e5d31c1f5fe/suspicious.dd.sda1 ⌨️
--2025-09-18 06:11:11--  https://challenge-files.picoctf.net/c_shape_facility/568c311b7dcfcd8a4ff1b30ad1c9dcb41069add275d72304a79d2e5d31c1f5fe/suspicious.dd.sda1
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.40, 3.160.5.64, 3.160.5.18, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.40|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 32868864 (31M) [application/octet-stream]
Saving to: 'suspicious.dd.sda1'

suspicious.dd.sda1                                         100%[======================================================================================================================================>]  31.35M  1.82MB/s    in 17s     

2025-09-18 06:11:29 (1.82 MB/s) - 'suspicious.dd.sda1' saved [32868864/32868864]

AsianHacker-picoctf@webshell:~$ file suspicious.dd.sda1 ⌨️
suspicious.dd.sda1: Linux rev 1.0 ext3 filesystem data, UUID=fc168af0-183b-4e53-bdf3-9c1055413b40 (needs journal recovery)

AsianHacker-picoctf@webshell:~$ exiftool suspicious.dd.sda1 ⌨️
ExifTool Version Number         : 12.40
File Name                       : suspicious.dd.sda1
Directory                       : .
File Size                       : 31 MiB
File Modification Date/Time     : 2025:08:18 15:06:13+00:00
File Access Date/Time           : 2025:09:18 06:11:35+00:00
File Inode Change Date/Time     : 2025:09:18 06:11:29+00:00
File Permissions                : -rw-rw-r--
Error                           : First 1024 bytes of file is binary zeros

AsianHacker-picoctf@webshell:~$ mount -o loop suspicious.dd.sda1 fs ⌨️
mount: fs: mount failed: Operation not permitted. ⚠️

AsianHacker-picoctf@webshell:~$ binwalk -e suspicious.dd.sda1 ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Linux EXT filesystem, blocks count: 32096, image size: 32866304, rev 1.0, ext3 filesystem data, UUID=fc168af0-183b-4e53-bdf3-9c1055415541

AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  _suspicious.dd.sda1.extracted 👀 suspicious.dd.sda1
AsianHacker-picoctf@webshell:~$ cd _suspicious.dd.sda1.extracted/ ⌨️
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted$ ls ⌨️
0.ext  ext-root 👀
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted$ cd ext-root/ ⌨️
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted/ext-root$ ls ⌨️
boot  suspicious-file.txt 👀 tce
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted/ext-root$ cat suspicious-file.txt ⌨️
Nothing to see here! But you may want to look here --> 👀
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted/ext-root$ cd tce/ ⌨️
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted/ext-root/tce$ ls ⌨️
mydata.tgz  onboot.lst  optional
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted/ext-root/tce$ cd optional/ ⌨️
AsianHacker-picoctf@webshell:~/_suspicious.dd.sda1.extracted/ext-root/tce/optional$ ls ⌨️
bzip2-lib.tcz          gcc_libs.tcz          glib2.tcz.md5.txt   libtirpc.tcz          nano.tcz.md5.txt            ncurses.tcz.dep      nginx.tcz.md5.txt                          openssh.tcz.dep            pcre.tcz
bzip2-lib.tcz.md5.txt  gcc_libs.tcz.md5.txt  libdnet.tcz         libtirpc.tcz.md5.txt  ncurses-common.tcz          ncurses.tcz.md5.txt  open-vm-tools-modules-3.8.13-tinycore.tcz  openssh.tcz.md5.txt        pcre.tcz.dep
fuse.tcz               glib2.tcz             libffi.tcz          nano.tcz              ncurses-common.tcz.md5.txt  nginx.tcz            open-vm-tools.tcz                          openssl-1.0.0.tcz          pcre.tcz.md5.txt
fuse.tcz.md5.txt       glib2.tcz.dep         libffi.tcz.md5.txt  nano.tcz.dep          ncurses.tcz                 nginx.tcz.dep        openssh.tcz                                openssl-1.0.0.tcz.md5.txt

Method 1: strings and xxd -s 
# offset in decimal
AsianHacker-picoctf@webshell:~$ strings -td suspicious.dd.sda1 | grep "Nothing to see here" ⌨️
2098176 👀 Nothing to see here! But you may want to look here -->
# offset in hexadecimal 0x
AsianHacker-picoctf@webshell:~$ strings -a -t x suspicious.dd.sda1 | grep "Nothing to see here" ⌨️
 200400 👀 Nothing to see here! But you may want to look here -->

AsianHacker-picoctf@webshell:~$ xxd -s 0x200400 -l 200 suspicious.dd.sda1 ⌨️                                  
00200400: 4e6f 7468 696e 6720 746f 2073 6565 2068  Nothing to see h
00200410: 6572 6521 2042 7574 2079 6f75 206d 6179  ere! But you may
00200420: 2077 616e 7420 746f 206c 6f6f 6b20 6865   want to look he
00200430: 7265 202d 2d3e 0a7d 0033 0039 0038 0036  re -->.}.3.9.8.6
00200440: 0033 0031 0032 0066 005f 0033 003c 005f  .3.1.2.f._.3.<._
00200450: 007c 004c 006d 005f 0031 0031 0031 0074  .|.L.m._.1.1.1.t
00200460: 0035 005f 0033 0062 007b 0046 0054 0043  .5._.3.b.{.F.T.C
00200470: 006f 0063 0069 0070 0000 0000 0000 0000  .o.c.i.p........ 👀
00200480: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00200490: 0000 0000 0000 0000 0000 0000 0000 0000  ................
002004a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
002004b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
002004c0: 0000 0000 0000 0000                      ........

# Method 2: fls and icat -s
AsianHacker-picoctf@webshell:~$ fls suspicious.dd.sda1 | grep 'suspicious-file.txt' ⌨️
r/r 12: suspicious-file.txt
AsianHacker-picoctf@webshell:~$ icat -r suspicious.dd.sda1 12 ⌨️
Nothing to see here! But you may want to look here -->
AsianHacker-picoctf@webshell:~$ icat -s suspicious.dd.sda1 12 ⌨️
Nothing to see here! But you may want to look here -->
}3986312f_3<_|Lm_111t5_3b{FTCocip 👀

# Method 2: dd w/ skip in decimal format
AsianHacker-picoctf@webshell:~$ dd if=suspicious.dd.sda1 skip=2098176 count=128 iflag=skip_bytes,count_bytes of=slice ⌨️
0+1 records in
0+1 records out
128 bytes copied, 7.9626e-05 s, 1.6 MB/s

AsianHacker-picoctf@webshell:~$ cat slice ⌨️
Nothing to see here! But you may want to look here -->
}3986312f_3<_|Lm_111t5_3b{FTCocip 👀

AsianHacker-picoctf@webshell:~$ xxd slice ⌨️
00000000: 4e6f 7468 696e 6720 746f 2073 6565 2068  Nothing to see h
00000010: 6572 6521 2042 7574 2079 6f75 206d 6179  ere! But you may
00000020: 2077 616e 7420 746f 206c 6f6f 6b20 6865   want to look he
00000030: 7265 202d 2d3e 0a7d 0033 0039 0038 0036  re -->.}.3.9.8.6
00000040: 0033 0031 0032 0066 005f 0033 003c 005f  .3.1.2.f._.3.<._
00000050: 007c 004c 006d 005f 0031 0031 0031 0074  .|.L.m._.1.1.1.t
00000060: 0035 005f 0033 0062 007b 0046 0054 0043  .5._.3.b.{.F.T.C
00000070: 006f 0063 0069 0070 0000 0000 0000 0000  .o.c.i.p........ 👀

# Optional: Tool for reversing
AsianHacker-picoctf@webshell:~$ python -c "print(''.join(reversed('}.8.3.4.6.0.c.a.e._.3.<._.|.L.m._.1.1.1.t.5._.3.b.{.F.T.C.o.c.i.p'.split('.'))))"  ⌨️
picoCTF{b3_5t111_mL|_<3_eac06438} 🔐
AsianHacker-picoctf@webshell:~$ python -c "print(''.join(reversed('}3986312f_3<_|Lm_111t5_3b{FTCocip')))" ⌨️
picoCTF{b3_5t111_mL|_<3_f2136893} 🔐
AsianHacker-picoctf@webshell:~$ python -c "print('}3986312f_3<_|Lm_111t5_3b{FTCocip'[::-1])" ⌨️
picoCTF{b3_5t111_mL|_<3_f2136893} 🔐

# Method 3: Autopsy
Settings: Hide Slack Files in the (disable both)
```

## Flag
picoCTF{b3_5t111_mL|_<3_f2136893}

## Continue
[Continue](./picoGym0237.md)
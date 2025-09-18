# picoGym Level 284: Operation Oni
Source: https://play.picoctf.org/practice/challenge/284

## Goal
Download this disk image, find the key and log into the remote machine.<br>
https://artifacts.picoctf.net/c/69/disk.img.gz<br>
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.<br>
Remote machine: ssh -i key_file -p 55775 ctf-player@saturn.picoctf.net

## What I learned
```
mmls, fls, icat
Autopsy
ssh privatekey
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/69/disk.img.gz ⌨️
--2025-09-17 20:18:33--  https://artifacts.picoctf.net/c/69/disk.img.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 48132743 (46M) [application/octet-stream]
Saving to: 'disk.img.gz'

disk.img.gz                                        100%[=============================================================================================================>]  45.90M  1.82MB/s    in 25s     

2025-09-17 20:18:59 (1.82 MB/s) - 'disk.img.gz' saved [48132743/48132743]

AsianHacker-picoctf@webshell:/tmp$ gunzip disk.img.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
disk.img 👀 hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ file disk.img ⌨️
disk.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0xc,223,19), startsector 2048, 204800 sectors; partition 2 : ID=0x83, start-CHS (0xc,223,20), end-CHS (0x1d,81,52), startsector 206848, 264192 sectors
AsianHacker-picoctf@webshell:/tmp$ exiftool disk.img ⌨️ 
ExifTool Version Number         : 12.40
File Name                       : disk.img
Directory                       : .
File Size                       : 230 MiB
File Modification Date/Time     : 2023:08:04 20:29:23+00:00
File Access Date/Time           : 2025:09:17 20:19:22+00:00
File Inode Change Date/Time     : 2025:09:17 20:19:14+00:00
File Permissions                : -rw-rw-r--
Error                           : Unknown file type

AsianHacker-picoctf@webshell:/tmp$ strings disk.img | grep "picoCTF" ⌨️
AsianHacker-picoctf@webshell:/tmp$ unzip disk.img ⌨️
Archive:  disk.img
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of disk.img or
        disk.img.zip, and cannot find disk.img.ZIP, period.

# Method 1: mmls, fls, icat, dd
AsianHacker-picoctf@webshell:/tmp$ mmls disk.img ⌨️
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start           End          Length       Description
000:  Meta      0000000000      0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000      0000002047   0000002048   Unallocated
002:  000:000   0000002048👀   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848👀   0000471039   0000264192   Linux (0x83)
AsianHacker-picoctf@webshell:/tmp$ fls -r -o 2048 disk.img | grep -i flag ⌨️
AsianHacker-picoctf@webshell:/tmp$ fls -r -o 206848 disk.img | grep -i flag ⌨️

AsianHacker-picoctf@webshell:/tmp$ fls -o 2048 disk.img ⌨️
d/d 11: lost+found
r/r 12: ldlinux.sys
r/r 13: ldlinux.c32
r/r 15: config-virt
r/r 16: vmlinuz-virt
r/r 17: initramfs-virt
l/l 18: boot
r/r 20: libutil.c32
r/r 19: extlinux.conf
r/r 21: libcom32.c32
r/r 22: mboot.c32
r/r 23: menu.c32
r/r 14: System.map-virt
r/r 24: vesamenu.c32
V/V 25585:      $OrphanFiles

AsianHacker-picoctf@webshell:/tmp$ fls -o 206848 disk.img ⌨️
d/d 458:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root 👀
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles

AsianHacker-picoctf@webshell:/tmp$ fls -r -o 206848 -p disk.img | grep ssh ⌨️
r/r 2147:       etc/conf.d/sshd
l/l 54: etc/runlevels/default/sshd
r/r 2148:       etc/init.d/sshd
d/d 14: etc/ssh
r/r 15: etc/ssh/ssh_host_ed25519_key
r/r 16: etc/ssh/ssh_host_ed25519_key.pub
r/r 17: etc/ssh/ssh_host_ecdsa_key
r/r 18: etc/ssh/ssh_host_ecdsa_key.pub
r/r 19: etc/ssh/ssh_host_dsa_key
r/r 20: etc/ssh/ssh_host_dsa_key.pub
r/r 21: etc/ssh/ssh_host_rsa_key
r/r 22: etc/ssh/ssh_host_rsa_key.pub
r/r 2136:       etc/ssh/ssh_config
r/r * 2149(realloc):    etc/ssh/.apk.16471ab68a45fec9b921250f1074bc33a7b969d9c4f5baec
r/r 2149:       etc/ssh/sshd_config
r/r 2135:       etc/ssh/moduli
r/r 2084:       usr/bin/ssh-keygen
r/- * 0:        usr/bin/ssh-copy-id
r/- * 0:        usr/bin/ssh-keyscan
r/- * 0:        usr/bin/ssh-pkcs11-helper
r/r 2140:       usr/bin/ssh-add
r/r 2145:       usr/bin/ssh
r/r 2144:       usr/bin/ssh-pkcs11-helper
r/r 2143:       usr/bin/ssh-keyscan
r/r 2142:       usr/bin/ssh-copy-id
r/r 2141:       usr/bin/ssh-agent
r/r 2150:       usr/sbin/sshd
r/r 676:        usr/share/openrc/support/init.d.examples/sshd
d/d 3907:       usr/lib/ssh
r/r 2152:       usr/lib/ssh/ssh-sk-helper
r/r 2146:       usr/lib/ssh/sftp-server
r/r * 2152(realloc):    usr/lib/ssh/.apk.aaef7b6e9311b326086bba1413f8c2554daed95e4f2ba320
r/r 2151:       usr/lib/ssh/ssh-pkcs11-helper
r/r 712:        sbin/setup-sshd
d/d 3916:       root/.ssh 👀
r/r 2345:       root/.ssh/id_ed25519 👀
r/r 2346:       root/.ssh/id_ed25519.pub 👀

AsianHacker-picoctf@webshell:/tmp$ fls -o 206848 -p disk.img 3916 ⌨️  
r/r 2345:       id_ed25519 👀
r/r 2346:       id_ed25519.pub 👀

AsianHacker-picoctf@webshell:/tmp$ icat -o 206848 disk.img 2345 ⌨️
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----

AsianHacker-picoctf@webshell:/tmp$ icat -o 206848 disk.img 2346 ⌨️
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGCtd7hso2E7OQItY6aTjMMyKZb1FVmeBfnVjyHcGYos root@localhost

AsianHacker-picoctf@webshell:/tmp$ icat -o 206848 disk.img 2345 > key_file.txt ⌨️
AsianHacker-picoctf@webshell:/tmp$ chmod 600 key_file.txt ⌨️❤️

AsianHacker-picoctf@webshell:/tmp$ ssh -i private_key.txt -p 55775 ctf-player@saturn.picoctf.net ⌨️
The authenticity of host '[saturn.picoctf.net]:55775 ([13.59.203.175]:55775)' can't be established.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[saturn.picoctf.net]:55775' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.8.0-1035-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ ls ⌨️
flag.txt
ctf-player@challenge:~$ cat flag.txt ⌨️
picoCTF{k3y_5l3u7h_339601ed} 🔐

# Method 2: Autopsy
# Under root look at .ash_history (View what files where modified)
# Note: Click on private file look at meta data to see permissions
```

## Flag
picoCTF{k3y_5l3u7h_339601ed}

## Continue
[Continue](./picoGym0113.md)
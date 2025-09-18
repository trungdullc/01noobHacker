# picoGym Level 506: DISKO 2
Source: https://play.picoctf.org/practice/challenge/506

## Goal
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!<br>
Download the disk image here.<br>
https://artifacts.picoctf.net/c/539/disko-2.dd.gz

## What I learned
```
dd

Autopsy
FTK Imager

Not on server:
fdisk : https://www.youtube.com/watch?v=xewLljxXk7Y
kpartx
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/539/disko-2.dd.gz ⌨️
--2025-09-15 21:47:20--  https://artifacts.picoctf.net/c/539/disko-2.dd.gz
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.18, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16617522 (16M) [application/octet-stream]
Saving to: 'disko-2.dd.gz'

disko-2.dd.gz                                              100%[======================================================================================================================================>]  15.85M  1.82MB/s    in 8.7s    

2025-09-15 21:47:29 (1.82 MB/s) - 'disko-2.dd.gz' saved [16617522/16617522]

AsianHacker-picoctf@webshell:~$ gunzip disko-2.dd.gz ⌨️
AsianHacker-picoctf@webshell:~$ file disko-2.dd ⌨️
disko-2.dd: DOS/MBR boot sector; partition 1 : ID=0x83, start-CHS (0x0,32,33), end-CHS (0x3,80,13), startsector 2048, 51200 sectors; partition 2 : ID=0xb, start-CHS (0x3,80,14), end-CHS (0x7,100,29), startsector 53248, 65536 sectors
AsianHacker-picoctf@webshell:~$ strings disko-2.dd | grep "picoCTF{" ⌨️
picoCTF{4_P4Rt_1t_i5_d3f931a0}
picoCTF{4_P4Rt_1t_i5_a3930df1}
picoCTF{4_P4Rt_1t_i5_f1d0a339}
picoCTF{4_P4Rt_1t_i5_fad03913}
picoCTF{4_P4Rt_1t_i5_139df3a0}
picoCTF{4_P4Rt_1t_i5_f931d3a0}
picoCTF{4_P4Rt_1t_i5_30da391f}
picoCTF{4_P4Rt_1t_i5_af33091d}
picoCTF{4_P4Rt_1t_i5_9d0331fa}
picoCTF{4_P4Rt_1t_i5_13a03f9d}
picoCTF{4_P4Rt_1t_i5_3df91a30}
picoCTF{4_P4Rt_1t_i5_39f3ad01}
picoCTF{4_P4Rt_1t_i5_930d1fa3}
picoCTF{4_P4Rt_1t_i5_90da3f31}
picoCTF{4_P4Rt_1t_i5_0ad9133f}
picoCTF{4_P4Rt_1t_i5_3ad039f1}
picoCTF{4_P4Rt_1t_i5_339da10f}
picoCTF{4_P4Rt_1t_i5_d33af901}
picoCTF{4_P4Rt_1t_i5_93d0f3a1}
picoCTF{4_P4Rt_1t_i5_9330afd1}
picoCTF{4_P4Rt_1t_i5_9a3d10f3}
picoCTF{4_P4Rt_1t_i5_d9f033a1}
picoCTF{4_P4Rt_1t_i5_d390f1a3}
picoCTF{4_P4Rt_1t_i5_0ad3139f}
picoCTF{4_P4Rt_1t_i5_fa39d031}
picoCTF{4_P4Rt_1t_i5_90a3f3d1} 🔐 Brute Force
ronse paquetes en base xa en requiridos: ${picoCTF{4_P4Rt_1t_i5_903d13af}
ce debcopicoCTF{4_P4Rt_1t_i5_393da1f0}dawanym pytaniom priorytety. Tylko pytania o pewnym lub wy
Description-gl.UTF-8: Configurar unha rede empreganpicoCTF{4_P4Rt_1t_i5_1930da3f}escription-gu.UTF-8: 
ChoicpicoCTF{4_P4Rt_1t_i5_a0f313d9}k Harf Kilidi), Sa
Extended_picoCTF{4_P4Rt_1t_i5_3d1309af}u d'archivu Debian especific
ExtenpicoCTF{4_P4Rt_1t_i5_30f931da}tse tiedostojen hakemiseen k
 fald kanpicoCTF{4_P4Rt_1t_i5_1a33f09d}. Hvis du ikke kender svaret p
picoCTF{4_P4Rt_1t_i5_913a30df}
Extended_descriptionpicoCTF{4_P4Rt_1t_i5_331d0f9a}
Description-ta.UTpicoCTF{4_P4Rt_1t_i5_339d0fa1}
picoCTF{4_P4Rt_1t_i5_91fda330}
nipicoCTF{4_P4Rt_1t_i5_09a331df}D?
alinti negrpicoCTF{4_P4Rt_1t_i5_339a10df}og tikrai norite sukurti nauj
picoCTF{4_P4Rt_1t_i5_0ad1393f}AXSIZE} 
Description-ppicoCTF{4_P4Rt_1t_i5_13d093af}dados existentes
Description-nb.UTF-8: Fant ipicoCTF{4_P4Rt_1t_i5_310d39fa} i denne partisjonen.
an facerse funcionapicoCTF{4_P4Rt_1t_i5_039fda13} estes tres son equivalentes]\n intra.exemplo.com\n http://intra.exemplo.com/d-i/.lenny/preseed.cfg\n http://192.168.0.1/~phil/test47.txt\n floppy://preseed.cfg\n file:///hd-media/kiosk/./preseed.cfg\n\nPara unha instalaci
Aug 30 02:00:45 in-target: Get:334 cpicoCTF{4_P4Rt_1t_i5_a031d9f3}c2 _Kali-last-snapshot_ - Official amd64 BD Binary-1 with firmware 20220804-16:57] kali-rolling/main amd64 libmp3lame0 amd64 3.100-3 [364 kB]
Aug 30 02:00:55 in-target: Get:943 cdrom://[Kali GNU/Linux 2022.3rc2 _Kali-last-snapshot_ - Official amd64 BD Binary-1 with firmware picoCTF{4_P4Rt_1t_i5_d3f1039a}ain amd64 ruby-http-cookie all 1.0.3-1 [22.6 kB]
Aug 29 picoCTF{4_P4Rt_1t_i5_31a03fd9}90522] pci 0000:00:17.0: PME# supported from D0 D3hot D3cold
xHpicoCTF{4_P4Rt_1t_i5_a9d0f313}
picoCTF{4_P4Rt_1t_i5_1f03d3a9}
picoCTF{4_P4Rt_1t_i5_9a013f3d}
picoCTF{4_P4Rt_1t_i5_f33d091a}
picoCTF{4_P4Rt_1t_i5_1d9fa303}
picoCTF{4_P4Rt_1t_i5_a3f9103d}
picoCTF{4_P4Rt_1t_i5_f19a03d3}
picoCTF{4_P4Rt_1t_i5_93fda130}
picoCTF{4_P4Rt_1t_i5_30df3a91}
picoCTF{4_P4Rt_1t_i5_09ad13f3}
picoCTF{4_P4Rt_1t_i5_a0913df3}
MESSAGE=vmware: picoCTF{4_P4Rt_1t_i5_913d03af} hypervisor : 66000000 Hz
picoCTF{4_P4Rt_1t_i5_f19d3a03}STAMP=294323
picoCTF{4_P4Rt_1t_i5_f3019a3d}
picoCTF{4_P4Rt_1t_i5_309dfa13}
picoCTF{4_P4Rt_1t_i5_0a193f3d}
picoCTF{4_P4Rt_1t_i5_f9033d1a}
_SOURCE_MONOTONIC_TIMESTAMP=3024picoCTF{4_P4Rt_1t_i5_f3013da9}
picoCTF{4_P4Rt_1t_i5_33f0da91}
picoCTF{4_P4Rt_1t_i5_a1f033d9}e
picoCTF{4_P4Rt_1t_i5_f3d0139a}
picoCTF{4_P4Rt_1t_i5_af91303d}
picoCTF{4_P4Rt_1t_i5_af9d0133}
picoCTF{4_P4Rt_1t_i5_f9331ad0}
picoCTF{4_P4Rt_1t_i5_39fa01d3}
picoCTF{4_P4Rt_1t_i5_a1df3903}
picoCTF{4_P4Rt_1t_i5_1daf9033}
picoCTF{4_P4Rt_1t_i5_931afd03}
picoCTF{4_P4Rt_1t_i5_0d93a13f}
picoCTF{4_P4Rt_1t_i5_903a13fd}
picoCTF{4_P4Rt_1t_i5_ad1933f0}
picoCTF{4_P4Rt_1t_i5_90d31a3f}
picoCTF{4_P4Rt_1t_i5_39afd013}
picoCTF{4_P4Rt_1t_i5_1fa09d33}
picoCTF{4_P4Rt_1t_i5_01d93f3a}
picoCTF{4_P4Rt_1t_i5_f30a193d}
picoCTF{4_P4Rt_1t_i5_39afd301}
picoCTF{4_P4Rt_1t_i5_9fda3103}
picoCTF{4_P4Rt_1t_i5_af13d930}
picoCTF{4_P4Rt_1t_i5_9130fa3d}
picoCTF{4_P4Rt_1t_i5_d10f933a}
picoCTF{4_P4Rt_1t_i5_df03931a}
picoCTF{4_P4Rt_1t_i5_301d3fa9}
picoCTF{4_P4Rt_1t_i5_d033fa91}
picoCTF{4_P4Rt_1t_i5_0af31d39}
picoCTF{4_P4Rt_1t_i5_af3093d1}
picoCTF{4_P4Rt_1t_i5_0d913af3}
picoCTF{4_P4Rt_1t_i5_01a3d93f}
picoCTF{4_P4Rt_1t_i5_a3d3901f}
picoCTF{4_P4Rt_1t_i5_d03f391a}
picoCTF{4_P4Rt_1t_i5_f3d9013a}
picoCTF{4_P4Rt_1t_i5_3f1a0d93}
picoCTF{4_P4Rt_1t_i5_3d0913fa}
picoCTF{4_P4Rt_1t_i5_01933adf}
picoCTF{4_P4Rt_1t_i5_109da3f3}
picoCTF{4_P4Rt_1t_i5_f093d13a}
picoCTF{4_P4Rt_1t_i5_a0f1393d}
picoCTF{4_P4Rt_1t_i5_df0139a3}
picoCTF{4_P4Rt_1t_i5_03fa913d}
picoCTF{4_P4Rt_1t_i5_13f90ad3}
picoCTF{4_P4Rt_1t_i5_d39f1a03}
picoCTF{4_P4Rt_1t_i5_303d9fa1}
picoCTF{4_P4Rt_1t_i5_393d10af}
picoCTF{4_P4Rt_1t_i5_01d3f9a3}
picoCTF{4_P4Rt_1t_i5_d093a31f}
picoCTF{4_P4Rt_1t_i5_fa330d19}
picoCTF{4_P4Rt_1t_i5_df13309a}
picoCTF{4_P4Rt_1t_i5_3031a9df}
picoCTF{4_P4Rt_1t_i5_df19a330}
picoCTF{4_P4Rt_1t_i5_01df3a93}
picoCTF{4_P4Rt_1t_i5_13afd390}
picoCTF{4_P4Rt_1t_i5_3fda3910}
picoCTF{4_P4Rt_1t_i5_af93d310}
picoCTF{4_P4Rt_1t_i5_03319adf}
picoCTF{4_P4Rt_1t_i5_339a01df}
picoCTF{4_P4Rt_1t_i5_3ad9f301}
picoCTF{4_P4Rt_1t_i5_f31a903d}
picoCTF{4_P4Rt_1t_i5_d930f31a}
picoCTF{4_P4Rt_1t_i5_93daf130}
picoCTF{4_P4Rt_1t_i5_9a30f13d}

AsianHacker-picoctf@webshell:~$ mmls disko-2.dd ⌨️❤️❤️❤️❤️❤️
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End            Length          Description
001:  -------   0000000000   0000002047 👀  0000002048      Unallocated
002:  000:000   0000002048   0000053247     0000051200 👀   Linux (0x83)
003:  000:001   0000053248   0000118783     0000065536      Win95 FAT32 (0x0b)
004:  -------   0000118784   0000204799     0000086016      Unallocated

Method 1: dd utility
AsianHacker-picoctf@webshell:~$ dd if=disko-2.dd of=linux_partition skip=2048 count=51200 ⌨️❤️❤️❤️❤️❤️
dd: writing to 'linux_partition': No space left on device
45953+0 records in
45952+0 records out
23527424 bytes (24 MB, 22 MiB) copied, 0.34432 s, 68.3 MB/s
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  disko-2.dd  linux_partition 👀
AsianHacker-picoctf@webshell:~$ srch_strings linux_partition | grep picoCTF ⌨️
picoCTF{4_P4Rt_1t_i5_90a3f3d1} 🔐

# Convert to absolute byte offset inside the full disk image
# Linux partition starts at sector 2048, and each sector is 512 bytes:
# partition_start_bytes = 2048 × 512 = 1048576
# absolute_offset       = 1048576 + 236208 = 1284784
# block_number = absolute_offset // block_size
# block_number = 1284784 // 4096 = 313
# Map the block back to an inode
AsianHacker-picoctf@webshell:/tmp$ grep -oba 'picoCTF{' linux_partition ⌨️
236208:picoCTF{
AsianHacker-picoctf@webshell:/tmp$ fsstat -o 2048 disko-2.dd | grep "Block Size" ⌨️
Block Size: 1024
AsianHacker-picoctf@webshell:/tmp$ ffind -o 2048 disko-2.dd 313 ⌨️
File name not found for inode
AsianHacker-picoctf@webshell:/tmp$ fls -o 2048 -r disko-2.dd | grep Orphan ⌨️
V/V 6401:       $OrphanFiles
+ -/r * 235:    OrphanFile-235
AsianHacker-picoctf@webshell:/tmp$ istat -o 2048 disko-2.dd 235 ⌨️
inode: 235
Not Allocated
Group: 0
Generation Id: 3136313432
uid / gid: 0 / 0
mode: rrwxr-xr-x
Flags: Extents, 
size: 0
num of links: 0

Inode Times:
Accessed:       2025-03-30 00:51:30.928196859 (UTC)
File Modified:  2025-03-30 00:51:30.928196859 (UTC)
Inode Modified: 2025-03-30 00:51:30.928196859 (UTC)
File Created:   2025-03-30 00:51:30.928196859 (UTC)
Deleted:        2025-03-30 00:51:30 (UTC)
AsianHacker-picoctf@webshell:/tmp$ icat -o 2048 disko-2.dd 235 ⌨️

Method 2: fls and icat (not recommended would take forever)
AsianHacker-picoctf@webshell:~$ fls -o 2048 disko-2.dd ⌨️
d/d 11: lost+found
d/d 13: bin
V/V 6401:       $OrphanFiles
AsianHacker-picoctf@webshell:~$ fls -o 2048 -r disko-2.dd ⌨️
d/d 11: lost+found
d/d 13: bin
+ r/r 14:       sqlitebrowser
+ r/r 17:       dbus-daemon
+ r/r 23:       dbus-uuidgen
+ r/r 29:       xkbevd
+ r/r 33:       cabextract
+ r/r 42:       xfontsel
+ r/r 43:       xkill
+ r/r 44:       xlsatoms
+ r/r 45:       xlsclients
+ r/r 48:       xprop
+ r/r 53:       xzdiff
+ r/r 60:       tightvncpasswd
+ r/r 72:       loadunimap
+ r/r 74:       mk_modmap
+ r/r 78:       screendump
+ r/r 84:       setvtrgb
+ r/r 88:       unicode_start
+ r/r 90:       fc-cat
+ r/r 95:       mount
+ r/r 96:       umount
+ r/r 104:      instmodsh
+ r/r 110:      perlivp
+ r/r 111:      piconv
+ r/r 112:      pl2pm
+ r/r 114:      pod2man
+ r/r 115:      pod2text
+ r/r 118:      prove
+ r/r 120:      ptardiff
+ l/l 130:      xzegrep
+ l/l 137:      compare-im6
+ r/r 139:      x86_64-linux-gnu-cpp-13
+ r/r 141:      apt-cache
+ r/r 145:      apt-key
+ r/r 147:      dbilogstrip
+ r/r 148:      dccleancrw
+ r/r 150:      dcfujiturn
+ r/r 155:      dbiprof
+ r/r 157:      dh_perl_dbi
+ r/r 164:      sdiff
+ r/r 166:      python3.12
+ r/r 168:      busctl
+ r/r 180:      hostname
+ r/r 184:      infocmp
+ r/r 196:      getfattr
+ r/r 199:      ldapdelete
+ r/r 201:      ldapmodify
+ r/r 205:      ldapurl
+ l/l 207:      ldapadd
+ r/r 211:      vmtoolsd
+ r/r 218:      vmware-rpctool
+ r/r 220:      vmware-vgauth-cmd
+ r/r 229:      look
+ r/r 231:      unicode_stop
+ l/l 232:      awk
+ r/r 234:      bzdiff
+ r/r 46:       xlsfonts
+ r/r 64:       codepage
+ r/r 21:       dbus-send
+ r/r 63:       chvt
+ r/r 30:       xkbprint
+ r/r 36:       listres
+ r/r 62:       deb-systemd-invoke
+ r/r 56:       xzmore
+ r/r 40:       xev
+ r/r 32:       xkbwatch
+ r/r 54:       xzgrep
+ r/r 57:       cpio
+ r/r 35:       editres
+ r/r 66:       dumpkeys
+ r/r 73:       mapscrn
+ r/r 80:       setkeycodes
+ r/r 81:       setleds
+ r/r 89:       fc-cache
+ r/r 91:       fc-conflist
+ r/r 98:       encguess
+ r/r 99:       rpcinfo
+ r/r 100:      m4
+ r/r 107:      perlbug
+ r/r 108:      perlthanks
+ r/r 119:      ptar
+ r/r 121:      ptargrep
+ r/r 122:      shasum
+ r/r 125:      xsubpp
+ r/r 126:      zipdetails
+ l/l 127:      unxz
+ r/r 133:      perl5.40-x86_64-linux-gnu
+ r/r 138:      lightdm-gtk-greeter-settings
+ r/r 140:      apt
+ r/r 144:      apt-get
+ r/r 146:      apt-mark
+ r/r 149:      dcfujigreen
+ r/r 151:      dcfujiturn16
+ r/r 165:      mt-gnu
+ r/r 167:      stunnel3
+ r/r 172:      ping
+ r/r 179:      rgrep
+ l/l 181:      dnsdomainname
+ l/l 185:      nisdomainname
+ r/r 186:      tabs
+ l/l 187:      ypdomainname
+ r/r 189:      toe
+ r/r 191:      tset
+ r/r 195:      attr
+ r/r 197:      setfattr
+ r/r 206:      ldapwhoami
+ r/r 214:      lowntfs-3g
+ r/r 216:      vmware-namespace-cmd
+ r/r 221:      vmware-vmblock-fuse
+ l/l 227:      rbash
+ r/r 228:      colrm
+ r/r 230:      dbus-launch
+ l/l 233:      psfaddtable
+ r/r 25:       ncursesw6-config
+ r/r 76:       psfxtable
+ r/r 79:       setfont
+ r/r 67:       fgconsole
+ r/r 18:       dbus-run-session
+ r/r 50:       xwininfo
+ r/r 28:       xkbcomp
+ r/r 24:       ncurses6-config
+ r/r 117:      podchecker
+ r/r 87:       splitfont
+ r/r 22:       dbus-update-activation-environment
+ r/r 27:       xkbbell
+ r/r 92:       fc-list
+ r/r 109:      perldoc
+ r/r 101:      rpcgen
+ r/r 75:       openvt
+ r/r 41:       xfd
+ r/r 52:       xz
+ r/r 20:       dbus-monitor
+ r/r 70:       kbdinfo
+ r/r 86:       showkey
+ r/r 69:       kbd_mode
+ r/r 55:       xzless
+ r/r 61:       deb-systemd-helper
+ r/r 51:       lzmainfo
+ r/r 102:      h2ph
+ r/r 106:      libnetcfg
+ r/r 113:      pod2html
+ r/r 123:      splain
+ l/l 128:      xzcat
+ l/l 131:      xzfgrep
+ l/l 134:      pidof
+ r/r 135:      python3-qr
+ l/l 136:      compare
+ r/r 142:      apt-cdrom
+ r/r 152:      dcparse
+ r/r 158:      bash
+ l/l 160:      sh
+ r/r 162:      diff
+ r/r 170:      hostnamectl
+ r/r 174:      find
+ r/r 175:      xargs
+ r/r 176:      egrep
+ r/r 178:      grep
+ r/r 188:      tic
+ l/l 193:      infotocap
+ r/r 200:      ldapexop
+ r/r 203:      ldappasswd
+ r/r 208:      VGAuthService
+ r/r 209:      vm-support
+ r/r 210:      vmhgfs-fuse
+ r/r 217:      unrar-nonfree
+ r/r 219:      vmware-toolbox-cmd
+ r/r 222:      vmware-xferlogs
+ r/r 224:      2to3-2.7
+ r/r 225:      keyctl
+ l/l 16:       python3.11-config
+ r/r 59:       tmux
+ r/r 26:       setxkbmap
+ r/r 71:       loadkeys
+ r/r 93:       corelist
+ r/r 38:       xdpyinfo
+ r/r 94:       cpan
+ r/r 47:       xmessage
+ r/r 105:      json_pp
+ r/r 49:       xvinfo
+ r/r 34:       appres
+ r/r 103:      h2xs
+ r/r 116:      pod2usage
+ r/r 97:       enc2xs
+ l/l 58:       which
+ r/r 65:       deallocvt
+ r/r 85:       showconsolefont
+ r/r 68:       getkeycodes
+ r/r 37:       viewres
+ r/r 39:       xdriinfo
+ r/r 15:       x86_64-linux-gnu-python3.11-config
+ r/r 31:       xkbvleds
+ r/r 83:       setmetamode
+ r/r 82:       setlogcons
+ r/r 19:       dbus-cleanup-sockets
+ r/r 77:       resizecons
+ r/r 124:      streamzip
+ l/l 129:      xzcmp
+ r/r 132:      cpan5.40-x86_64-linux-gnu
+ r/r 143:      apt-config
+ r/r 153:      dcraw
+ r/r 154:      json_xs
+ r/r 156:      dbiproxy
+ r/r 159:      dash
+ r/r 161:      cmp
+ r/r 163:      diff3
+ r/r 169:      stunnel4
+ r/r 171:      journalctl
+ l/l 173:      ping4
+ r/r 177:      fgrep
+ r/r 182:      clear
+ l/l 183:      domainname
+ r/r 190:      tput
+ l/l 192:      captoinfo
+ l/l 194:      reset
+ r/r 198:      ldapcompare
+ r/r 202:      ldapmodrdn
+ r/r 204:      ldapsearch
+ r/r 212:      vmware-alias-import
+ r/r 213:      vmware-checkvm
+ r/r 215:      vmware-hgfsclient
+ r/r 223:      pyfiglet
+ r/r 226:      clear_console
V/V 6401:       $OrphanFiles
+ -/r * 235:    OrphanFile-235
AsianHacker-picoctf@webshell:~$ fls -o 2048 disko-2.dd 13 ⌨️
r/r 14: sqlitebrowser
r/r 17: dbus-daemon
r/r 23: dbus-uuidgen
r/r 29: xkbevd
r/r 33: cabextract
r/r 42: xfontsel
r/r 43: xkill
r/r 44: xlsatoms
r/r 45: xlsclients
r/r 48: xprop
r/r 53: xzdiff
r/r 60: tightvncpasswd
r/r 72: loadunimap
r/r 74: mk_modmap
r/r 78: screendump
r/r 84: setvtrgb
r/r 88: unicode_start
r/r 90: fc-cat
r/r 95: mount
r/r 96: umount
AsianHacker-picoctf@webshell:~$ fls -o 2048 -r disko-2.dd | grep flag.txt ⌨️
# Note: method would have to know which file containedit

# Method 3:
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ chmod +x pythonScript.py ⌨️ 
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
import re
import sys
from collections import Counter

# Note: open in chunks due to memory exhaustion
def extract_flags(filepath):
    flags = []
    pattern = re.compile(rb"picoCTF\{.*?\}")  # regex in bytes, avoids decoding

    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(1024 * 1024):  # read 1 MB at a time
                flags.extend(pattern.findall(chunk))
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

    # Convert byte matches to strings
    return [flag.decode("latin1", errors="ignore") for flag in flags]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 extract_flags.py <filename>")
        sys.exit(1)

    filepath = sys.argv[1]
    flags = extract_flags(filepath)

    if not flags:
        print("No picoCTF flags found.")
        sys.exit(0)

    counts = Counter(flags)

    print("\nUnique picoCTF flags:\n")
    for flag, count in counts.items():
        if count == 1:
            print(flag)

if __name__ == "__main__":
    main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py disko-2.dd ⌨️

Unique picoCTF flags:

picoCTF{4_P4Rt_1t_i5_d3f931a0}
picoCTF{4_P4Rt_1t_i5_a3930df1}
picoCTF{4_P4Rt_1t_i5_f1d0a339}
picoCTF{4_P4Rt_1t_i5_fad03913}
picoCTF{4_P4Rt_1t_i5_139df3a0}
picoCTF{4_P4Rt_1t_i5_f931d3a0}
picoCTF{4_P4Rt_1t_i5_30da391f}
picoCTF{4_P4Rt_1t_i5_af33091d}
picoCTF{4_P4Rt_1t_i5_9d0331fa}
picoCTF{4_P4Rt_1t_i5_13a03f9d}
picoCTF{4_P4Rt_1t_i5_3df91a30}
picoCTF{4_P4Rt_1t_i5_39f3ad01}
picoCTF{4_P4Rt_1t_i5_930d1fa3}
picoCTF{4_P4Rt_1t_i5_90da3f31}
picoCTF{4_P4Rt_1t_i5_0ad9133f}
picoCTF{4_P4Rt_1t_i5_3ad039f1}
picoCTF{4_P4Rt_1t_i5_339da10f}
picoCTF{4_P4Rt_1t_i5_d33af901}
picoCTF{4_P4Rt_1t_i5_93d0f3a1}
picoCTF{4_P4Rt_1t_i5_9330afd1}
picoCTF{4_P4Rt_1t_i5_9a3d10f3}
picoCTF{4_P4Rt_1t_i5_d9f033a1}
picoCTF{4_P4Rt_1t_i5_d390f1a3}
picoCTF{4_P4Rt_1t_i5_0ad3139f}
picoCTF{4_P4Rt_1t_i5_fa39d031}
picoCTF{4_P4Rt_1t_i5_90a3f3d1}
picoCTF{4_P4Rt_1t_i5_903d13af}
picoCTF{4_P4Rt_1t_i5_393da1f0}
picoCTF{4_P4Rt_1t_i5_1930da3f}
picoCTF{4_P4Rt_1t_i5_a0f313d9}
picoCTF{4_P4Rt_1t_i5_3d1309af}
picoCTF{4_P4Rt_1t_i5_30f931da}
picoCTF{4_P4Rt_1t_i5_1a33f09d}
picoCTF{4_P4Rt_1t_i5_913a30df}
picoCTF{4_P4Rt_1t_i5_331d0f9a}
picoCTF{4_P4Rt_1t_i5_339d0fa1}
picoCTF{4_P4Rt_1t_i5_91fda330}
picoCTF{4_P4Rt_1t_i5_09a331df}
picoCTF{4_P4Rt_1t_i5_339a10df}
picoCTF{4_P4Rt_1t_i5_0ad1393f}
picoCTF{4_P4Rt_1t_i5_13d093af}
picoCTF{4_P4Rt_1t_i5_310d39fa}
picoCTF{4_P4Rt_1t_i5_039fda13}
picoCTF{4_P4Rt_1t_i5_a031d9f3}
picoCTF{4_P4Rt_1t_i5_d3f1039a}
picoCTF{4_P4Rt_1t_i5_31a03fd9}
picoCTF{4_P4Rt_1t_i5_a9d0f313}
picoCTF{4_P4Rt_1t_i5_1f03d3a9}
picoCTF{4_P4Rt_1t_i5_9a013f3d}
picoCTF{4_P4Rt_1t_i5_f33d091a}
picoCTF{4_P4Rt_1t_i5_1d9fa303}
picoCTF{4_P4Rt_1t_i5_a3f9103d}
picoCTF{4_P4Rt_1t_i5_f19a03d3}
picoCTF{4_P4Rt_1t_i5_93fda130}
picoCTF{4_P4Rt_1t_i5_30df3a91}
picoCTF{4_P4Rt_1t_i5_09ad13f3}
picoCTF{4_P4Rt_1t_i5_a0913df3}
picoCTF{4_P4Rt_1t_i5_913d03af}
picoCTF{4_P4Rt_1t_i5_f19d3a03}
picoCTF{4_P4Rt_1t_i5_f3019a3d}
picoCTF{4_P4Rt_1t_i5_309dfa13}
picoCTF{4_P4Rt_1t_i5_0a193f3d}
picoCTF{4_P4Rt_1t_i5_f9033d1a}
picoCTF{4_P4Rt_1t_i5_f3013da9}
picoCTF{4_P4Rt_1t_i5_33f0da91}
picoCTF{4_P4Rt_1t_i5_a1f033d9}
picoCTF{4_P4Rt_1t_i5_f3d0139a}
picoCTF{4_P4Rt_1t_i5_af91303d}
picoCTF{4_P4Rt_1t_i5_af9d0133}
picoCTF{4_P4Rt_1t_i5_f9331ad0}
picoCTF{4_P4Rt_1t_i5_39fa01d3}
picoCTF{4_P4Rt_1t_i5_a1df3903}
picoCTF{4_P4Rt_1t_i5_1daf9033}
picoCTF{4_P4Rt_1t_i5_931afd03}
picoCTF{4_P4Rt_1t_i5_0d93a13f}
picoCTF{4_P4Rt_1t_i5_903a13fd}
picoCTF{4_P4Rt_1t_i5_ad1933f0}
picoCTF{4_P4Rt_1t_i5_90d31a3f}
picoCTF{4_P4Rt_1t_i5_39afd013}
picoCTF{4_P4Rt_1t_i5_1fa09d33}
picoCTF{4_P4Rt_1t_i5_01d93f3a}
picoCTF{4_P4Rt_1t_i5_f30a193d}
picoCTF{4_P4Rt_1t_i5_39afd301}
picoCTF{4_P4Rt_1t_i5_9fda3103}
picoCTF{4_P4Rt_1t_i5_af13d930}
picoCTF{4_P4Rt_1t_i5_9130fa3d}
picoCTF{4_P4Rt_1t_i5_d10f933a}
picoCTF{4_P4Rt_1t_i5_df03931a}
picoCTF{4_P4Rt_1t_i5_301d3fa9}
picoCTF{4_P4Rt_1t_i5_d033fa91}
picoCTF{4_P4Rt_1t_i5_0af31d39}
picoCTF{4_P4Rt_1t_i5_af3093d1}
picoCTF{4_P4Rt_1t_i5_0d913af3}
picoCTF{4_P4Rt_1t_i5_01a3d93f}
picoCTF{4_P4Rt_1t_i5_a3d3901f}
picoCTF{4_P4Rt_1t_i5_d03f391a}
picoCTF{4_P4Rt_1t_i5_f3d9013a}
picoCTF{4_P4Rt_1t_i5_3f1a0d93}
picoCTF{4_P4Rt_1t_i5_3d0913fa}
picoCTF{4_P4Rt_1t_i5_01933adf}
picoCTF{4_P4Rt_1t_i5_109da3f3}
picoCTF{4_P4Rt_1t_i5_f093d13a}
picoCTF{4_P4Rt_1t_i5_a0f1393d}
picoCTF{4_P4Rt_1t_i5_df0139a3}
picoCTF{4_P4Rt_1t_i5_03fa913d}
picoCTF{4_P4Rt_1t_i5_13f90ad3}
picoCTF{4_P4Rt_1t_i5_d39f1a03}
picoCTF{4_P4Rt_1t_i5_303d9fa1}
picoCTF{4_P4Rt_1t_i5_393d10af}
picoCTF{4_P4Rt_1t_i5_01d3f9a3}
picoCTF{4_P4Rt_1t_i5_d093a31f}
picoCTF{4_P4Rt_1t_i5_fa330d19}
picoCTF{4_P4Rt_1t_i5_df13309a}
picoCTF{4_P4Rt_1t_i5_3031a9df}
picoCTF{4_P4Rt_1t_i5_df19a330}
picoCTF{4_P4Rt_1t_i5_01df3a93}
picoCTF{4_P4Rt_1t_i5_13afd390}
picoCTF{4_P4Rt_1t_i5_3fda3910}
picoCTF{4_P4Rt_1t_i5_af93d310}
picoCTF{4_P4Rt_1t_i5_03319adf}
picoCTF{4_P4Rt_1t_i5_339a01df}
picoCTF{4_P4Rt_1t_i5_3ad9f301}
picoCTF{4_P4Rt_1t_i5_f31a903d}
picoCTF{4_P4Rt_1t_i5_d930f31a}
picoCTF{4_P4Rt_1t_i5_93daf130}
picoCTF{4_P4Rt_1t_i5_9a30f13d}
```

## Flag
picoCTF{4_P4Rt_1t_i5_90a3f3d1}

## Continue
[Continue](./picoGym0507.md)
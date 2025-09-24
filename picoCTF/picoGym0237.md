# picoGym Level 237: WPA-ing Out
Source: https://play.picoctf.org/practice/challenge/237

## Goal
I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.<br>
Use this 'pcap file' and the rockyou wordlist.<br>
https://artifacts.picoctf.net/c/41/wpa-ing_out.pcap<br>
The flag should be entered in the picoCTF{XXXXXX} format.

## What I learned
```
802.11 is IEEE family of standards that defines Wi-Fi (wireless LAN) operation. Short version: 802.11

# Note: Only works in /tmp folder and rockyou.txt not found must download and uncompress to be able to use 👀
Aircrack-ng is a suite of open-source tools used for assessing the security of wireless networks.
Crack WEP and WPA/WPA2-PSK keys to evaluate Wi-Fi security.

How It Works:
        Packet Capture – airodump-ng capture raw 802.11 Wi-Fi packets
        Traffic Injection – aireplay-ng can inject packets to speed up data collection (force reauthentication to capture handshakes)
        Cracking – aircrack-ng, analyzes captured packets and tries to recover the Wi-Fi password using statistical attacks (for WEP) or dictionary/brute-force attacks (for WPA/WPA2)

Included Tools:
        airmon-ng – Puts wireless cards into monitor mode
        airodump-ng – Captures packets from Wi-Fi networks
        aireplay-ng – Injects/replays packets
        aircrack-ng – Performs the actual key cracking
        airdecap-ng – Decrypts captured traffic once the key is known
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/41/wpa-ing_out.pcap ⌨️
--2025-09-19 21:52:30--  https://artifacts.picoctf.net/c/41/wpa-ing_out.pcap
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1000774 (977K) [application/octet-stream]
Saving to: 'wpa-ing_out.pcap'

wpa-ing_out.pcap                                           100%[======================================================================================================================================>] 977.32K  1.85MB/s    in 0.5s    

2025-09-19 21:52:31 (1.85 MB/s) - 'wpa-ing_out.pcap' saved [1000774/1000774]

# Method 1: CLI
AsianHacker-picoctf@webshell:~$ aircrack-ng -w /usr/share/wordlists/rockyou.txt wpa-ing_out.pcap ⌨️
ERROR: Opening dictionary /usr/share/wordlists/rockyou.txt failed (No such file or directory) ⚠️
ERROR: Opening dictionary /usr/share/wordlists/rockyou.txt failed (No such file or directory) ⚠️
Reading packets, please wait...
Opening wpa-ing_out.pcap
Read 23523 packets.

   #  BSSID              ESSID                     Encryption

   1  00:5F:67:4F:6A:1A  Gone_Surfing              WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening wpa-ing_out.pcap
Read 23523 packets.

1 potential targets

Please specify a dictionary (option -w).

# DL wordlist
AsianHacker-picoctf@webshell:~$ wget https://phoenixnap.dl.sourceforge.net/project/wordlist-collection/rockyou.txt.gz ⌨️      
--2025-09-19 22:10:32--  https://phoenixnap.dl.sourceforge.net/project/wordlist-collection/rockyou.txt.gz
Resolving phoenixnap.dl.sourceforge.net (phoenixnap.dl.sourceforge.net)... 184.164.141.26
Connecting to phoenixnap.dl.sourceforge.net (phoenixnap.dl.sourceforge.net)|184.164.141.26|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://downloads.sourceforge.net/project/wordlist-collection/rockyou.txt.gz [following]
--2025-09-19 22:10:32--  https://downloads.sourceforge.net/project/wordlist-collection/rockyou.txt.gz
Resolving downloads.sourceforge.net (downloads.sourceforge.net)... 104.18.12.149, 104.18.13.149, 2606:4700::6812:d95, ...
Connecting to downloads.sourceforge.net (downloads.sourceforge.net)|104.18.12.149|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://psychz.dl.sourceforge.net/project/wordlist-collection/rockyou.txt.gz?viasf=1 [following]
--2025-09-19 22:10:32--  https://psychz.dl.sourceforge.net/project/wordlist-collection/rockyou.txt.gz?viasf=1
Resolving psychz.dl.sourceforge.net (psychz.dl.sourceforge.net)... 208.87.241.191
Connecting to psychz.dl.sourceforge.net (psychz.dl.sourceforge.net)|208.87.241.191|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 53357062 (51M) [application/x-gzip]
Saving to: 'rockyou.txt.gz'

rockyou.txt.gz                                             100%[======================================================================================================================================>]  50.88M  1.82MB/s    in 28s     

2025-09-19 22:11:01 (1.82 MB/s) - 'rockyou.txt.gz' saved [53357062/53357062]
AsianHacker-picoctf@webshell:~$ gunzip rockyou.txt.gz ⌨️

gzip: rockyou.txt: No space left on device ⚠️

# Move to location with more space
AsianHacker-picoctf@webshell:~$ mv rockyou.txt.gz /tmp/ ⌨️
AsianHacker-picoctf@webshell:~$ mv wpa-ing_out.pcap /tmp/ ⌨️
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ gunzip rockyou.txt.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ aircrack-ng -w rockyou.txt wpa-ing_out.pcap ⌨️❤️❤️❤️❤️❤️

                               Aircrack-ng 1.6 

      [00:00:04] 1707/14344391 keys tested (411.91 k/s) 

      Time left: 9 hours, 40 minutes, 20 seconds                 0.01%

                          KEY FOUND! [ mickeymouse ] 🔐


      Master Key     : 61 64 B9 5E FC 6F 41 70 70 81 F6 40 80 9F AF B1 
                       4A 9E C5 C4 E1 67 B8 AB 58 E3 E8 8E E6 66 EB 11 

      Transient Key  : 62 37 2F 54 3B 7B B4 43 9B 37 F4 57 40 FD D1 91 
                       86 7F FE 26 85 7B AC DD 2C 44 E6 06 18 03 B0 0F 
                       F2 75 A2 32 63 F7 35 74 2D 18 10 1C 25 F9 14 BC 
                       41 DA 58 52 48 86 B0 D6 14 89 F6 77 00 8E F7 EB 

      EAPOL HMAC     : 65 2F 6C 0E 75 F0 49 27 6A AA 6A 06 A7 24 B9 A9

Method 2: GUI (Easier)
Select WPA and wordlist and Launch
```

## Flag
picoCTF{mickeymouse}

## Continue
[Continue](./picoGym0350.md)
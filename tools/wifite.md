# wifite
```
Source: https://www.kali.org/tools/wifite/
Description: wifite automates multiple Wi-Fi attacks to:
    Scan for nearby wireless networks
    Capture WPA/WPA2 handshakes
    Attempt to crack them using a wordlist (like rockyou.txt)
    Automatically try WPS PIN brute-force if enabled

sudo apt install wifite                             git clone https://github.com/derv82/wifite2.git
                                                    cd wifite2
                                                    sudo python3 setup.py install
sudo wifite
# Note: Handshake files are stored in wpa-handshake.cap
aircrack-ng wpa-handshake.cap -w rockyou.txt
```

## Back to README.md
[BACK](/README.md)
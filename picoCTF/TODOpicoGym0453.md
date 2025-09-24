# picoGym Level 453: Bitlocker-1
Source: https://play.picoctf.org/practice/challenge/453

## Goal
Jacky is not very knowledgable about the best security passwords and used a simple password<br>
to encrypt their BitLocker drive. See if you can break through the encryption!<br>
Download the disk image here<br>
https://challenge-files.picoctf.net/c_verbal_sleep/9e934e4d78276b12e27224dac16e50e6bbeae810367732eee4d5e38e6b2bb868/bitlocker-1.dd

## What I learned
```
John the Ripper
HashCat

bitlocker2john is a tool used in password recovery or penetration testing. Specifically, it’s part of the John the Ripper suite of tools
dislocker is an open-source tool used to access and decrypt Microsoft BitLocker-encrypted drives on systems that don’t natively support BitLocker (like Linux and macOS)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_verbal_sleep/9e934e4d78276b12e27224dac16e50e6bbeae810367732eee4d5e38e6b2bb868/bitlocker-1.dd
--2025-09-22 23:31:32--  https://challenge-files.picoctf.net/c_verbal_sleep/9e934e4d78276b12e27224dac16e50e6bbeae810367732eee4d5e38e6b2bb868/bitlocker-1.dd
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.40, 3.160.5.18, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.40|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 104857600 (100M) [application/octet-stream]
Saving to: 'bitlocker-1.dd'

bitlocker-1.dd                                             100%[======================================================================================================================================>] 100.00M  1.81MB/s    in 55s     

2025-09-22 23:32:27 (1.82 MB/s) - 'bitlocker-1.dd' saved [104857600/104857600]

AsianHacker-picoctf@webshell:~$ file bitlocker-1.dd 
bitlocker-1.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "-FVE-FS-", sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, sectors/track 63, heads 255, hidden sectors 124499968, FAT (32 bit), sectors/FAT 8160, serial number 0, unlabeled; NTFS, sectors/track 63, physical drive 0x1fe0, $MFT start cluster 393217, serial number 02020454d414e204f, checksum 0x41462020
AsianHacker-picoctf@webshell:~$ strings bitlocker-1.dd | grep "picoCTF"
AsianHacker-picoctf@webshell:~$ binwalk bitlocker-1.dd 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
38639508      0x24D9794       Windows Script Encoded Data (screnc.exe)

AsianHacker-picoctf@webshell:~$ mmls bitlocker-1.dd 
AsianHacker-picoctf@webshell:~$ fls bitlocker-1.dd 
Encryption detected (BitLocker)

# Method 1:
# Need Kali Linux/ParrotOS
# bitlocker2john: Extract bitlocker hashes
$ git clone https://github.com/openwall/john.git
$ python3 john/run/bitlocker2john.py bitlocker-1.dd

The following hashes were found:
$bitlocker$2$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
$bitlocker$3$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
$bitlocker$1$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d

# Brute Force w/ HashCat or John the Ripper
# Hashcat has a profile for Bitlocker hashes: 22100
$ wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
$ sudo apt install hashcat -y
$ hashcat -m 22100 -a 0 bitlocker.hash /usr/share/wordlists/rockyou.txt				hashcat -m 22100 hashes.txt rockyou.txt

$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d:jacqueline

Password: jacqueline

# Mount virtual disk and find the flag
sudo mkdir /mnt/dislocker
sudo mkdir /mnt/decrypted
sudo dislocker bitlocker-1.dd -ujacqueline -- /mnt/dislocker
sudo mount -o loop /mnt/dislocker/dislocker-file /mnt/decrypted/
ls /mnt/decrypted
	flag.txt 
sudo umount /mnt/bitlocker_data

# Method 2:
# Mounting image and extracting the BitLocker hash from the image
$ bitlocker2john -i bitlocker-1.dd > bitlocker_hash.txt

# loaded these hashes up into John the Ripper
$ john --wordlist=rockyou.txt --format=bitlocker bitlocker_hash.txt
```

## Flag


## Continue
[Continue](./picoGym0453.md)
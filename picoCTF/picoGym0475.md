# picoGym Level 475: hashcrack 🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/475

## Goal
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?<br> 
Access the server using nc verbal-sleep.picoctf.net 51319

## What I learned
```
Note: MD5sum is not reversible (no math “decrypt”) ⚠️
1st hash is 32 hexadecimal characters (128 bits)
Most popular 128-bit hash is MD5 (mode 0 in Hashcat)
  hashcat -m 0 -a 0 ciphertext1 /usr/share/wordlists/rockyou.txt ⌨️❤️

2nd hash is 40 hexadecimal characters (192 bits)
SHA-1 (mode 100)
  hashcat -m 100 -a 0 ciphertext2 /usr/share/wordlists/rockyou.txt ⌨️❤️

3rd hash is 64 characters (256 bits)
Most common is SHA-256 (mode 1400)
  hashcat -m 1400 -a 0 ciphertext3 /usr/share/wordlists/rockyou.txt ⌨️❤️

# Online Crackers
  https://www.dcode.fr/cipher-identifier ⭐⭐⭐⭐⭐
  https://crackstation.net/ ⭐⭐⭐⭐⭐

# Offline Hash Identifier
hash-identifier is super useful when you don’t know what algorithm
  git clone https://github.com/blackploit/hash-identifier.git ⌨️
  cd hash-identifier ⌨️
  chmod +x hash-id.py ⌨️
  python3 hash-id.py ⌨️                                             # Interactive Mode
  echo "482c811da5d5b4bc6d497ffa98491e38" | python3 hash-id.py ⌨️   # One Liner

# Offline Crackers
John the Ripper
hashcat ❤️❤️❤️❤️❤️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc verbal-sleep.picoctf.net 51319 ⌨️
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38 👀
Enter the password for identified hash: 

# Identify: https://www.dcode.fr/cipher-identifier ⭐⭐⭐⭐⭐
  MD5	👀
  Hexadecimal Data	
  MD4

# Use MD5: https://www.dcode.fr/md5-hash
password123 👀

Enter the password for identified hash: password123 ⌨️
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 👀
Enter the password for the identified hash: 

# Identify: https://www.dcode.fr/cipher-identifier ⭐⭐⭐
SHA-1	👀
Redefence Cipher

# Use SHA-1: https://www.dcode.fr/sha1-hash
letmein 👀

Enter the password for the identified hash: letmein ⌨️
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 👀
Enter the password for the identified hash: 

# Identify: https://www.dcode.fr/cipher-identifier ⭐⭐⭐
SHA-256	👀
Hexadecimal Data

# Use SHA-256: https://www.dcode.fr/sha256-hash
qwerty098 👀

Enter the password for the identified hash: qwerty098 ⌨️
Correct! You've cracked the SHA-256 hash with a secret found. 
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4de57566} 🔐
```

## Flag
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4de57566}

## Continue
[Continue](./picoGym0470.md)
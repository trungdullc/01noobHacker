# Bandit Level 9 → Level 10 Base64

## Previous Flag
<b>FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey</b>

## Goal
Use previous password to log in SSH with user <b>bandit10</b> on port <b>2220</b>.  Password stored in <b>data.txt</b>, which contains <b>base64 encoded data</b>.

## What I learned
![alt text](/static/base64.jpg)
```
Base64 is not encryption it is just encoding
                                ASCII DEC   Binary
echo -n "at" | base64             97      01100001
YXQ=                              116     01100001
          2^6=64  Split by 6, Pad 2 🛞's on R: 
                                011000 010110 0001🛞🛞
                                  24     23     16
                                  Y      X      Q
          Note: at: 2 char but end w/ 3 (YXQ) need pad w/ =   
echo "YXQ=" | base64 -d
at
```

| Base       | Characters Used                          | Use Cases                                        |
|------------|-------------------------------------------|--------------------------------------------------|
| Base2      | 0, 1                                      | Raw binary, hardware communication               |
| Base8      | 0–7                                       | Unix file permissions, legacy computing          |
| Base10     | 0–9                                       | Human-readable numbers                           |
| Base16     | 0–9, A–F                                  | Hashes, memory dumps, MAC addresses              |
| Base32     | A–Z, 2–7                                  | TOTP (2FA), QR codes, DNS encoding               |
| Base36     | 0–9, A–Z                                  | Short IDs, URLs, database keys                   |
| Base58     | Alphanum (no 0, O, I, l)                  | Bitcoin, IPFS, user-friendly strings             |
| Base62     | 0–9, A–Z, a–z                             | Short unique IDs, URLs                           |
| Base64     | A–Z, a–z, 0–9, +, /                       | Email MIME, data URIs, HTTP, JWTs                |
| Base64url  | A–Z, a–z, 0–9, -, _                       | URL-safe encoding (JWT, APIs)                    |
| Base85     | Printable ASCII (excl. whitespace)        | PDFs, PostScript, Git packfiles                  |
| Z85        | 85 printable ASCII characters             | ZeroMQ, compact binary text                      |
| Base91     | 91 printable ASCII characters             | Efficient binary-to-text encoding                |
| Base128    | Extended ASCII (non-standard)             | Experimental, niche applications 

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit10@bandit.labs.overthewire.org -p 2220 ⌨️
bandit10@bandit:~$ ls ⌨️
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg== 👀
bandit10@bandit:~$ whatis base64 ⌨️
base64 (1)    - base64 encode/decode data and print to standard output
bandit10@bandit:~$ base64 --help ⌨️
Usage: base64 [OPTION]... [FILE] 👀
Base64 encode or decode FILE, or standard input, to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -d, --decode          decode data 👀
bandit10@bandit:~$ base64 -d data.txt ⌨️ 
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr 🔐
bandit10@bandit:~$ echo "VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==" | base64 -d ⌨️ 
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr 🔐
```

## Flag
<b>dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr</b>

## Continue
[Continue](/overthewire/Bandit1011.md)
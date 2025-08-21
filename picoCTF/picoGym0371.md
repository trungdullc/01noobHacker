# picoGym Level 0371: repetitions
Source: https://play.picoctf.org/practice/challenge/371

## Goal
Can you make sense of this file?

## What I learned
```
If decoded and still look like can be decode again do it

Base64 is an encoding scheme, not a number system like decimal, hex, oct, or binary
It takes binary data (files, images, or raw bytes) and encodes it into printable ASCII characters so it can safely travel through systems that might not handle raw binary correctly (email, JSON, or URLs)

Binary: 01001000 01101001 (ASCII word "Hi")
# Break into 6-bit chunks (Left to Right)
010010 | 000110 | 1001??
# Add Padding
010010 000110 100100
# Map to Base64 alphabet, = not part of alphabet (used as padding at end when data doesn’t align to 3-byte blocks)
SGk=                                010010 → S
                                    000110 → G
                                    100100 → k

Base64 Alphabet
Value  Char         Value  Char      Value  Char         Value  Char
0      A            16     Q            32     g            48     w
1      B            17     R            33     h            49     x
2      C            18     S            34     i            50     y
3      D            19     T            35     j            51     z
4      E            20     U            36     k            52     0
5      F            21     V            37     l            53     1
6      G            22     W            38     m            54     2
7      H            23     X            39     n            55     3
8      I            24     Y            40     o            56     4
9      J            25     Z            41     p            57     5
10     K            26     a            42     q            58     6
11     L            27     b            43     r            59     7
12     M            28     c            44     s            60     8
13     N            29     d            45     t            61     9
14     O            30     e            46     u            62     +
15     P            31     f            47     v            63     /
```

<br>
<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th>Base</th>
    <th>Name</th>
    <th>Allowed Symbols (alphabet)</th>
    <th>Typical Clues (prefix/padding)</th>
    <th>Length Rules</th>
    <th>Common Uses</th>
  </tr>

  <tr>
    <td>2</td>
    <td>Binary</td>
    <td>0–1</td>
    <td>0b1010, %b (some langs)</td>
    <td>None</td>
    <td>Bitfields, machine code</td>
  </tr>

  <tr>
    <td>8</td>
    <td>Octal</td>
    <td>0–7</td>
    <td>0o755, 0755 (legacy)</td>
    <td>None</td>
    <td>Unix perms, legacy systems</td>
  </tr>

  <tr>
    <td>10</td>
    <td>Decimal</td>
    <td>0–9</td>
    <td>None</td>
    <td>None</td>
    <td>Everyday numbers</td>
  </tr>

  <tr>
    <td>16</td>
    <td>Hexadecimal</td>
    <td>0–9, A–F (case-insensitive)</td>
    <td>0xDEAD, \x41, h’…’, %x</td>
    <td>Even digits often (byte pairs)</td>
    <td>Memory dumps, hashes, colors</td>
  </tr>

  <tr>
    <td>32</td>
    <td>Base32 (RFC 4648)</td>
    <td>A–Z, 2–7</td>
    <td>May end with = padding</td>
    <td>Length multiple of 8 chars</td>
    <td>OTP secrets, DNS-safe encoding</td>
  </tr>

  <tr>
    <td>36</td>
    <td>Base36</td>
    <td>0–9, A–Z</td>
    <td>No standard padding</td>
    <td>None</td>
    <td>Compact human IDs, URLs</td>
  </tr>

  <tr>
    <td>58</td>
    <td>Base58 (Bitcoin)</td>
    <td>0–9, A–Z, a–z minus 0 O I l</td>
    <td>No =, +, /; visually unambiguous</td>
    <td>None</td>
    <td>Bitcoin addresses, IPFS (var.)</td>
  </tr>

  <tr>
    <td>62</td>
    <td>Base62</td>
    <td>0–9, A–Z, a–z</td>
    <td>No standard padding</td>
    <td>None</td>
    <td>Short URLs, compact tokens</td>
  </tr>

  <tr>
    <td>64</td>
    <td>Base64 (RFC 4648)</td>
    <td>A–Z, a–z, 0–9, +, /</td>
    <td>Ends with = or ==; URL-safe uses - _</td>
    <td>Length multiple of 4 chars</td>
    <td>MIME, JWT parts, data URIs</td>
  </tr>

  <tr>
    <td>64 (URL-safe)</td>
    <td>Base64url</td>
    <td>A–Z, a–z, 0–9, -, _</td>
    <td>Usually no padding (=) in URLs</td>
    <td>Multiple of 4 if padded</td>
    <td>JWT, web APIs</td>
  </tr>

  <tr>
    <td>85</td>
    <td>Ascii85 / Base85</td>
    <td>Printable ASCII subset (~85 chars)</td>
    <td><code>&lt;~ ... ~&gt;</code> (Adobe variant)</td>
    <td>None (often 5 chars ↔ 4 bytes)</td>
    <td>PostScript, PDFs</td>
  </tr>

  <tr>
    <td>91</td>
    <td>Z85 (ZeroMQ)</td>
    <td>91 printable chars (no space, quotes)</td>
    <td>No padding; blocks of 5 chars</td>
    <td>Length multiple of 5</td>
    <td>ZeroMQ binary framing</td>
  </tr>
</table>

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/472/enc_flag ⌨️
--2025-08-19 03:41:00--  https://artifacts.picoctf.net/c/472/enc_flag
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.92, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 349 [application/octet-stream]
Saving to: 'enc_flag'

enc_flag                                                   100%[======================================================================================================================================>]     349  --.-KB/s    in 0s      

2025-08-19 03:41:01 (97.2 MB/s) - 'enc_flag' saved [349/349]

AsianHacker-picoctf@webshell:/tmp$ ls -la enc_flag ⌨️
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 349 Mar 16  2023 enc_flag
AsianHacker-picoctf@webshell:/tmp$ file enc_flag ⌨️
enc_flag: ASCII text
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag ⌨️
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKeldWaHdRMDB4V2tWU2JFNVdDbUpXV2tkVU1WcFhWVzFHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag | base64 -d ⌨️
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JzWVhwQ00xWkVSbE5WCmJWWkdUMVpXVW1GdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag | base64 -d | base64 -d ⌨️                                               
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUd3BsYXpCM1ZERlNV
bVZGT1ZWUmFteEVXbm93T1VOblBUMEsK
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag | base64 -d | base64 -d ⌨️                                              
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUd3BsYXpCM1ZERlNV
bVZGT1ZWUmFteEVXbm93T1VOblBUMEsK
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag | base64 -d | base64 -d | base64 -d ⌨️
WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lV
WGRrTWpWelRVUlNhMDB5VW1aTwplazB3VDFSUmVFOVVRamxEWnowOUNnPT0K
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d ⌨️
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZO
ek0wT1RReE9UQjlDZz09Cg==
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d ⌨️
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfNzM0OTQxOTB9Cg==
AsianHacker-picoctf@webshell:/tmp$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d ⌨️
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190} 🔐
```

## Flag
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190}

## Continue
[Continue](./picoGym0067.md)
# Level 20

## Previous Flag
```
http://www.pythonchallenge.com/pc/hex/idiot2.html
```

## Goal
Given image with PRIVATE PROPERTY BEYOND THIS FENCE<br>
but inspecting it carefully is allowed.

## What I learned
```
wget --user=butter --password=fly "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
curl -u butter:fly -O "http://www.pythonchallenge.com/pc/hex/unreal.jpg"

AsianHacker-picoctf@webshell:/tmp$ eog unreal.jpg          # Eye of GNOME, default image viewer for GNOME desktop environment on Linux
-bash: eog: command not found
AsianHacker-picoctf@webshell:/tmp$ hexedit unreal.jpg 
-bash: hexedit: command not found

locate stegsolve
# if .jar
java -jar <linktostegsolve.jar>

Modern browsers like Microsoft Edge and Google Chrome no longer allow manual modification of HTTP headers (like Range, Referer, or Origin) directly from DevTools for security reasons.
```

## Side Quest
```
Back then you could edit Range Field and get V2h5IGRvbid0IHlvdSByZXNwZWN0IG15IHByaXZhY3k/

AsianHacker-picoctf@webshell:/tmp$ python3 -q
>>> import base64 as b
>>> dir(b)
['MAXBINSIZE', 'MAXLINESIZE', '_85encode', '_A85END', '_A85START', '_B32_DECODE_DOCSTRING', '_B32_DECODE_MAP01_DOCSTRING', '_B32_ENCODE_DOCSTRING', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_a85chars', '_a85chars2', '_b32alphabet', '_b32decode', '_b32encode', '_b32hexalphabet', '_b32rev', '_b32tab2', '_b85alphabet', '_b85chars', '_b85chars2', '_b85dec', '_bytes_from_decode_data', '_input_type_check', '_urlsafe_decode_translation', '_urlsafe_encode_translation', 'a85decode', 'a85encode', 'b16decode', 'b16encode', 'b32decode', 'b32encode', 'b32hexdecode', 'b32hexencode', 'b64decode', 'b64encode', 'b85decode', 'b85encode', 'binascii', 'bytes_types', 'decode', 'decodebytes', 'encode', 'encodebytes', 'main', 're', 'standard_b64decode', 'standard_b64encode', 'struct', 'test', 'urlsafe_b64decode', 'urlsafe_b64encode']
>>> msg = "V2h5IGRvbid0IHlvdSByZXNwZWN0IG15IHByaXZhY3k/"
>>> b.standard_b64decode(msg)
b"Why don't you respect my privacy?"

# printf-style formatting in Python
'bytes=%i-%i' % (next_piece, end)
    # str.format() style (Python 2.6+)
    'bytes={}-{}'.format(next_piece, end)
    # f-strings (Python 3.6+) ❤️❤️❤️❤️❤️
    f'bytes={next_piece}-{end}'

response.text
    Type: str (string)
    decodes the raw bytes into a string using a character encoding
response.content
    Type: bytes
    raw response body exactly as received from the server
    Use case: For binary files like images, PDFs, audio, videos, zip files

r = requests.get("https://example.com/image.jpg")
print(type(r.content))  # <class 'bytes'>
with open("image.jpg", "wb") as f:                              # open("image.jpg", "wb").write(r.content)
    f.write(r.content)      # safe for binary
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/hex/idiot2.html

View Page Source

<html>
<head>
  <title>go away!</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold">
	<img src="unreal.jpg" border="0"/><br><br>
	but inspecting it carefully is allowed.
</body>
</html>

AsianHacker-picoctf@webshell:/tmp$ man wget | grep "password" ⌨️
       --password=password
           Specify the username user and password password for both FTP and HTTP file retrieval.  These parameters can be overridden using the --ftp-user and --ftp-password options for FTP connections and the --http-user and
           --http-password options for HTTP connections.
       --ask-password
           Prompt for a password for each connection established. Cannot be specified when --password is being used, because they are mutually exclusive.
           Prompt for a user and password using the specified command.  If no command is specified then the command in the environment variable WGET_ASKPASS is used.  If WGET_ASKPASS is not set then the command in the
       --http-password=password
           Specify the username user and password password on an HTTP server.  According to the type of the challenge, Wget will encode them using either the "basic" (insecure), the "digest", or the Windows "NTLM"
           Another way to specify username and password is in the URL itself.  Either method reveals your password to anyone who bothers to run "ps".  To prevent the passwords from being seen, use the --use-askpass or store
           them in .wgetrc or .netrc, and make sure to protect those files from other users with "chmod".  If the passwords are really important, do not leave them lying in those files either---edit the files and delete them

AsianHacker-picoctf@webshell:/tmp$ wget --user=butter --password=fly "http://www.pythonchallenge.com/pc/hex/unreal.jpg" ⌨️
--2025-10-16 16:06:07--  http://www.pythonchallenge.com/pc/hex/unreal.jpg
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="pluses and minuses"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 30203 (29K) [image/jpeg]
Saving to: 'unreal.jpg'

unreal.jpg                                                 100%[=====================================================================================================================================>]  29.50K  --.-KB/s    in 0.05s   

2025-10-16 16:06:07 (565 KB/s) - 'unreal.jpg' saved [30203/30203]

AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  node-compile-cache  unreal.jpg
AsianHacker-picoctf@webshell:/tmp$ file unreal.jpg ⌨️
unreal.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=0], baseline, precision 8, 290x478, components 3
AsianHacker-picoctf@webshell:/tmp$ exiftool unreal.jpg ⌨️
ExifTool Version Number         : 12.40
File Name                       : unreal.jpg
Directory                       : .
File Size                       : 29 KiB
File Modification Date/Time     : 2025:10:16 16:06:07+00:00
File Access Date/Time           : 2025:10:16 16:06:15+00:00
File Inode Change Date/Time     : 2025:10:16 16:06:07+00:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Exif Byte Order                 : Big-endian (Motorola, MM)
Image Width                     : 290
Image Height                    : 478
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 290x478
Megapixels                      : 0.139
AsianHacker-picoctf@webshell:/tmp$ xxd unreal.jpg | head -n 5 ⌨️
00000000: ffd8 ffe0 0010 4a46 4946 0001 0101 0048  ......JFIF.....H
00000010: 0048 0000 ffe1 0016 4578 6966 0000 4d4d  .H......Exif..MM
00000020: 002a 0000 0008 0000 0000 0000 ffdb 0043  .*.............C
00000030: 0005 0304 0404 0305 0404 0405 0505 0607  ................
00000040: 0c08 0707 0707 0f0b 0b09 0c11 0f12 1211  ................
AsianHacker-picoctf@webshell:/tmp$ hexdump unreal.jpg | head -n 5 ⌨️
0000000 d8ff e0ff 1000 464a 4649 0100 0101 4800
0000010 4800 0000 e1ff 1600 7845 6669 0000 4d4d
0000020 2a00 0000 0800 0000 0000 0000 dbff 4300
0000030 0500 0403 0404 0503 0404 0504 0505 0706
0000040 080c 0707 0707 0b0f 090b 110c 120f 1112
AsianHacker-picoctf@webshell:/tmp$ foremost unreal.jpg ⌨️
Processing: unreal.jpg
|*|
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  node-compile-cache  output  unreal.jpg
AsianHacker-picoctf@webshell:/tmp$ cd output/ ⌨️
AsianHacker-picoctf@webshell:/tmp/output$ ls ⌨️
audit.txt  jpg
AsianHacker-picoctf@webshell:/tmp/output$ cat audit.txt ⌨️
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Thu Oct 16 16:14:55 2025
Invocation: foremost unreal.jpg 
Output directory: /tmp/output
Configuration file: /etc/foremost.conf
------------------------------------------------------------------
File: unreal.jpg
Start: Thu Oct 16 16:14:55 2025
Length: 29 KB (30203 bytes)
 
Num      Name (bs=512)         Size      File Offset     Comment 

0:      00000000.jpg          29 KB               0      
Finish: Thu Oct 16 16:14:55 2025

1 FILES EXTRACTED

jpg:= 1
------------------------------------------------------------------

Foremost finished at Thu Oct 16 16:14:55 2025
AsianHacker-picoctf@webshell:/tmp/output$ cd jpg ⌨️
AsianHacker-picoctf@webshell:/tmp/output/jpg$ ls ⌨️
00000000.jpg
AsianHacker-picoctf@webshell:/tmp$ zsteg unreal.jpg ⌨️ 
[!] #<ZPNG::NotSupported: Unsupported header "\xFF\xD8\xFF\xE0\x00\x10JF" in #<File:unreal.jpg>>

# Think: Look at Network Tab > Headers
connection
Keep-Alive
content-range
bytes 0-30202/2123456789 👀 What is this
content-type
image/jpeg
date
Thu, 16 Oct 2025 16:29:04 GMT
keep-alive
timeout=5, max=100
server
Apache/2.4.58 (Ubuntu)

# Google: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Range
# Note: Couldn't edit Request Header in Browser need use external Software

GET /pc/hex/unreal.jpg HTTP/1.1 👀
Host: www.pythonchallenge.com
Cache-Control: max-age=0
Authorization: Basic YnV0dGVyOmZseQ==
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Range: bytes=30203-2123456789 👀
If-None-Match: "103-52ddf321fc8f2-gzip"
If-Modified-Since: Sat, 12 Mar 2016 19:38:45 GMT
Connection: keep-alive

# Response
HTTP/1.1 206 Partial Content
Date: Fri, 17 Oct 2025 15:42:32 GMT
Server: Apache/2.4.58 (Ubuntu)
Content-Transfer-Encoding: binary
Content-Range: bytes 30203-30236/2123456789
Content-Length: 34
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: application/octet-stream

Why don't you respect my privacy? 👀

# Get Python to increase bytes to see response (automate)
AsianHacker-picoctf@webshell:/tmp$ cat pythonScripy.py ⌨️
#!/usr/bin/python3

import requests

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
response = requests.get(url, auth=("butter", "fly"), headers=headers)
print(response)
print(response.request.headers)         # {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
print(response.headers)
# {'Date': 'Fri, 17 Oct 2025 16:23:19 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
print(response.headers["Content-Range"])    # bytes 0-30202/2123456789

end = 2123456789

while True:
    try:
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        next_piece = int(response.headers["Content-Range"].split("-")[1].split("/")[0]) + 1
        print(next_piece)

        headers["Range"] = 'bytes=%i-%i' % (next_piece, end)
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        print(response.headers["Content-Range"])
        print(headers["Range"])
        print(response.text)
    except Exception as e:
        print("Error:", e)
        break

AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
<Response [200]>
{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
{'Date': 'Fri, 17 Oct 2025 17:02:31 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
bytes 0-30202/2123456789
30203
bytes 30203-30236/2123456789
bytes=30203-2123456789
Why don't you respect my privacy?

30237
bytes 30237-30283/2123456789
bytes=30237-2123456789
we can go on in this way for really long time.

30284
bytes 30284-30294/2123456789
bytes=30284-2123456789
stop this!

30295
bytes 30295-30312/2123456789
bytes=30295-2123456789
invader! invader!

30313
bytes 30313-30346/2123456789
bytes=30313-2123456789
ok, invader. you are inside now. 👀 invader

30347
Error: 'content-range'

Browser: http://www.pythonchallenge.com/pc/hex/invader.html ⌨️
Yes! that's you!

# Mess with pythonScript some more byte number changed
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

import requests

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
response = requests.get(url, auth=("butter", "fly"), headers=headers)
print(response)
print(response.request.headers)         # {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
print(response.headers)
# {'Date': 'Fri, 17 Oct 2025 16:23:19 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
print(response.headers["Content-Range"])    # bytes 0-30202/2123456789

end = 2123456789

while True:
    try:
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        next_piece = int(response.headers["Content-Range"].split("-")[1].split("/")[0]) + 1
        print(next_piece)

        headers["Range"] = 'bytes=%i-%i' % (end + 1, end) 👀
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        print(response.headers["Content-Range"])
        print(headers["Range"])
        print(response.text)
    except Exception as e:
        print("Error:", e)
        break

AsianHacker-picoctf@webshell:/tmp$ ./pythonScripy.py ⌨️
<Response [200]>
{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
{'Date': 'Fri, 17 Oct 2025 17:10:39 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
bytes 0-30202/2123456789
30203
bytes 2123456744-2123456788/2123456789
bytes=2123456790-2123456789
esrever ni emankcin wen ruoy si drowssap eht

2123456789
bytes 2123456744-2123456788/2123456789
bytes=2123456790-2123456789
esrever ni emankcin wen ruoy si drowssap eht

2123456789
bytes 2123456744-2123456788/2123456789
bytes=2123456790-2123456789
esrever ni emankcin wen ruoy si drowssap eht

AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> "esrever ni emankcin wen ruoy si drowssap eht"[::-1] ⌨️❤️❤️❤️❤️❤️
'the password is your new nickname in reverse' 👀

# Try going reverse from end to get not first portion but end portion
#!/usr/bin/python3

import requests

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
response = requests.get(url, auth=("butter", "fly"), headers=headers)
print(response)
print(response.request.headers)         # {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
print(response.headers)
# {'Date': 'Fri, 17 Oct 2025 16:23:19 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
print(response.headers["Content-Range"])    # bytes 0-30202/2123456789

end = 2123456789

while True:
    try:
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        next_piece = int(response.headers["Content-Range"].split("-")[1].split("/")[0]) + 1
        print(next_piece)

        headers["Range"] = 'bytes=%i-%i' % (end - 1, end) 👀
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        print(response.headers["Content-Range"])
        print(headers["Range"])
        print(response.text)
    except Exception as e:
        print("Error:", e)
        break

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
<Response [200]>
{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
{'Date': 'Fri, 17 Oct 2025 17:21:05 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
bytes 0-30202/2123456789
30203
bytes 2123456744👀-2123456788/2123456789
bytes=2123456788-2123456789
esrever ni emankcin wen ruoy si drowssap eht

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

import requests

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
response = requests.get(url, auth=("butter", "fly"), headers=headers)
print(response)
print(response.request.headers)         # {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
print(response.headers)
# {'Date': 'Fri, 17 Oct 2025 16:23:19 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
print(response.headers["Content-Range"])    # bytes 0-30202/2123456789

# end = 2123456789
end = 2123456744 👀

while True:
    try:
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        next_piece = int(response.headers["Content-Range"].split("-")[1].split("/")[0]) + 1
        print(next_piece)

        headers["Range"] = 'bytes=%i-%i' % (end - 1, end)
        response = requests.get(url, auth=("butter", "fly"), headers=headers)
        print(response.headers["Content-Range"])
        print(headers["Range"])
        print(response.text)
    except Exception as e:
        print("Error:", e)
        break

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
<Response [200]>
{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
{'Date': 'Fri, 17 Oct 2025 17:23:52 GMT', 'Server': 'Apache/2.4.58 (Ubuntu)', 'Content-Range': 'bytes 0-30202/2123456789', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'image/jpeg'}
bytes 0-30202/2123456789
30203
bytes 2123456712-2123456743/2123456789
bytes=2123456743-2123456744
and it is hiding at 1152983631. 👀

2123456744
bytes 2123456712-2123456743/2123456789
bytes=2123456743-2123456744
and it is hiding at 1152983631.

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

import requests

url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='}
response = requests.get(url, auth=("butter", "fly"), headers=headers)

end = 2123456744 👀

response = requests.get(url, auth=("butter", "fly"), headers=headers)
next_piece = int(response.headers["Content-Range"].split("-")[1].split("/")[0]) + 1

headers["Range"] = 'bytes=%i-%i' % (1152983631, end)
response = requests.get(url, auth=("butter", "fly"), headers=headers)

# print(response.text)
open("something", "wb").write(response.content)

AsianHacker-picoctf@webshell:/tmp$ file something ⌨️
something: Zip archive data, at least v2.0 to extract, compression method=deflate

AsianHacker-picoctf@webshell:/tmp$ unzip something ⌨️
Archive:  something
[something] readme.txt password: ⌨️ redavni
  inflating: readme.txt              
  inflating: package.pack            
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  node-compile-cache  package.pack  pythonScript.py  readme.txt  something
AsianHacker-picoctf@webshell:/tmp$ cat readme.txt ⌨️ 
Yes! This is really level 21 in here. 
And yes, After you solve it, you'll be in level 22!

Now for the level:

* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.

AsianHacker-picoctf@webshell:/tmp$ sz package.pack ⌨️
```

## Flag
redavni

## Continue
[Continue](./Level21.md)
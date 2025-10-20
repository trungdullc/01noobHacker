# Level 27

## Previous Flag
```
http://www.pythonchallenge.com/pc/hex/speedboat.html
```

## Goal
Given image of lake with painting a zigzag on top

## What I learned
```
The first half analyzes and manipulates zigzag.gif to detect pixel differences and reveal hidden data
The second half authenticates with the Python Challenge site (butter / fly), downloads encoded data, decodes it, and decompresses hidden text
The final output shows non-keyword identifiers found in that hidden message
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/hex/speedboat.html

View Page Source

<html>
<head>
  <title>between the tables</title> 👀
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<br>
<br>
<a href="../ring/bell.html"> 👀
<img src="zigzag.jpg"> <!-- did you say gif? --> 👀
</a>
</body>
</html>

<!-- oh, and this is NOT a repeat of 14 -->

<!--
Join us at the IRC: irc.freenode.net #pythonchallenge
-->

Browser: http://www.pythonchallenge.com/pc/hex/zigzag.gif ⌨️

AsianHacker-picoctf@webshell:/tmp$ wget --user butter --password fly http://www.pythonchallenge.com/pc/hex/zigzag.gif ⌨️
--2025-10-18 12:39:49--  http://www.pythonchallenge.com/pc/hex/zigzag.gif
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="pluses and minuses"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 98759 (96K) [image/gif]
Saving to: 'zigzag.gif'

zigzag.gif                                                100%[=====================================================================================================================================>]  96.44K  --.-KB/s    in 0.1s    

2025-10-18 12:39:50 (813 KB/s) - 'zigzag.gif' saved [98759/98759]

AsianHacker-picoctf@webshell:/tmp$ file zigzag.gif ⌨️
zigzag.gif: GIF image data, version 87a, 320 x 270
AsianHacker-picoctf@webshell:/tmp$ exiftool zigzag.gif 
ExifTool Version Number         : 12.40
File Name                       : zigzag.gif
Directory                       : .
File Size                       : 96 KiB
File Modification Date/Time     : 2016:03:12 19:38:45+00:00
File Access Date/Time           : 2025:10:18 12:39:57+00:00
File Inode Change Date/Time     : 2025:10:18 12:39:50+00:00
File Permissions                : -rw-rw-r--
File Type                       : GIF
File Type Extension             : gif
MIME Type                       : image/gif
GIF Version                     : 87a
Image Width                     : 320
Image Height                    : 270
Has Color Map                   : Yes
Color Resolution Depth          : 1
Bits Per Pixel                  : 8
Background Color                : 0
Image Size                      : 320x270
Megapixels                      : 0.086

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

# Import Python Imaging Library (Pillow) and the BZ2 compression module
from PIL import Image
import bz2

# Open the image file "zigzag.gif"
im = Image.open('zigzag.gif')

# Get the palette (color lookup table) of the GIF and take only the red component of each RGB triple
palette = im.getpalette()[::3]

# Create a translation table that maps each byte (0–255) to the palette value
table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))

# Convert the image pixels into a raw bytes sequence
raw = im.tobytes()

# Apply the translation table to transform the image bytes
trans = raw.translate(table)

# Pair up each byte of the raw image with the corresponding byte in the translated image, shifted by one
zipped = list(zip(raw[1:], trans[:-1]))

# Find all pairs where the two bytes are different — indicates a difference in pixel data
diff = list(filter(lambda p: p[0] != p[1], zipped))

# Record the indices (positions) where the differences occur
indices = [i for i,p in enumerate(zipped) if p[0] != p[1]]

# Create a new blank RGB image of the same size as the original
im2 = Image.new("RGB", im.size)

# Start with all white pixels
colors = [(255, 255, 255)] * len(raw)

# For each differing pixel, color it black
for i in indices:
    colors[i] = (0, 0, 0)

# Put the computed pixel data into the new image
im2.putdata(colors)

# Optionally display the image (commented out)
# im2.show()

# Save the resulting image as PNG (previously failed because no extension)
im2.save("new_image.png")

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ sz new_image.png ⌨️

# Think: Open image and see not keyword busy?
Google: python keyword module

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3

# Import Python Imaging Library (Pillow) and the BZ2 compression module
from PIL import Image
import bz2

# Open the image file "zigzag.gif"
im = Image.open('zigzag.gif')

# Get the palette (color lookup table) of the GIF and take only the red component of each RGB triple
palette = im.getpalette()[::3]

# Create a translation table that maps each byte (0–255) to the palette value
table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))

# Convert the image pixels into a raw bytes sequence
raw = im.tobytes()

# Apply the translation table to transform the image bytes
trans = raw.translate(table)

# Pair up each byte of the raw image with the corresponding byte in the translated image, shifted by one
zipped = list(zip(raw[1:], trans[:-1]))

# Find all pairs where the two bytes are different — indicates a difference in pixel data
diff = list(filter(lambda p: p[0] != p[1], zipped))

# Record the indices (positions) where the differences occur
indices = [i for i,p in enumerate(zipped) if p[0] != p[1]]

# Create a new blank RGB image of the same size as the original
im2 = Image.new("RGB", im.size)

# Start with all white pixels
colors = [(255, 255, 255)] * len(raw)

# For each differing pixel, color it black
for i in indices:
    colors[i] = (0, 0, 0)

# Put the computed pixel data into the new image
im2.putdata(colors)

# Optionally display the image (commented out)
# im2.show()

# Save the resulting image as PNG (previously failed because no extension)
im2.save("new_image.png")


# Import requests for HTTP access and base64 for decoding
import requests
import base64

# URL from the Python Challenge level involving authentication
url = "http://www.pythonchallenge.com/pc/hex/bin.html"

# Make a GET request using basic auth with username "butter" and password "fly"
response = requests.get(url, auth=("butter", "fly"))

# (Optional debugging lines were commented out)
# print(response)
# print(response.text)

# Extract the base64-encoded section from the multipart text response
b64 = ''.join(
    response.text.split("--===============1295515792==")[-2]
    .split("\n\n", 1)[1]
    .split()
)

# Decode the Base64 content to get the raw binary data
print(base64.b64decode(b64))

# Extract the first element of each differing byte pair from earlier
s = [t[0] for t in diff]

# Decompress that byte sequence using BZ2 compression
text = bz2.decompress(bytes(s))

# Import keyword module to check for Python reserved words
import keyword 👀

# Print all unique decoded words from the decompressed data
# that are *not* Python keywords (likely hidden hints or variable names)
print(set([w for w in text.split() if not keyword.iskeyword(w.decode())])) 👀 not keyword

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
C\x01A\x05@\x0c?\n=\x00<\x07<\r;\x07;\x07=\x0f>\x07?\nA\x0fB\rA\x0b>\x00;\x079\x039\x0f:\x08?\x08D\x04G\rF\x01C\x0f>\x10:\x009\x0e:\x07=\x08@\x01B\x02B\x0e@\r>\x06<\x07=\x0b=\t?\x0bA\x0bA\x05?\t>\x07=\x04<\x05>\x05A\nA\x03A\x06@\x07>\x02<\x06;\x0b;\n<\t>\x08@\x04B\x08D\x07C\x06@\n?\t<\x069\x08;\r=\x05?\x0cB\x04C\x07B\x08A\x05>\x0f<\n=\x06=\x07>\x01@\x0cA\r@\x01?\x07@\x0c@\x0c?\x0e?\t>\r<\r;\t<\x0b?\x0eB\x01D\tD\x0eC\x01?\x08;\t;\x00<\x04=\x0cA\x0fC\x04A\x03?\x03>\x10>\x04?\x07?\x03@\x0b@\t?\x06>\x0b>\r?\x0c@\x01@\x00@\x03>\x0c=\x0f=\r>\x0f?\x02@\x00@\x07@\x0f?\x0e>\x06>\x06?\x08?\n?\x0b?\x0e>\x0f>\x03?\x08@\x0f@\n@\x00@\x10?\n>\x03>\x07>\x0c>\x03?\x03?\x00?\x07?\x04@\x02A\x0b@\x0b?\x03>\x07=\x0b<\x05<\n?\x00A\x05B\x0eB\x00@\x0e=\x0e<\x0e;\x06<\r?\x06A\x0bB\x06B\x10A\x08?\r>\x0f>\x06=\t<\r=\x00>\x00@\x0cB\nB\nA\n@\x05>\x0f=\x00<\n=\r=\x05?\x01@\x07?\x02?\x08@\x0b?\x00@\n@\x0c?\x0c=\r<\x07<\x0e?\x03A\x07B\x07B\x0cA\x06>\x05<\n;\x06<\x0c>\x08@\x08A\x0bA\x01@\r?\x05@\x05@\x00?\r@\x01?\n=\x0c<\x01=\x01?\x05A\tB\tB\x0e@\x0b>\x04=\x0e=\r=\x05?\x00@\x07@\x08@\x0b?\x0e?\x04@\x01?\x0b?\x10?\x0e>\x10<\x07=\t?\r@\x00A\x07@\x03@\x01?\x03>\x01>\x02?\x02@\x05?\x02?\x04>\x00>\n>\n?\x05@\x0e@\x0b@\x0b?\x04>\x08>\x0b?\x10A\x07B\x07A\x0f@\x0f>\x04=\x06=\x08?\n?\x06@\x08?\x02>\x04>\r?\x05@\nA\x05B\x0fA\x0b@\x01?\x08=\x05=\x0c>\x05?\x08@\x0eA\n@\x0f?\x01?\x0b?\x0f?\x06?\x10?\x03?\x00@\x07@\x00@\x02?\x0c?\x02?\x0e?\r?\x0b?\x03?\x05@\r?\x03?\x03?\x05?\x06>\n?\x03?\x06?\x05@\x08@\x03@\x0b?\x01>\x0c>\x03?\x04@\x10@\x0cA\x02@\x07?\x04?\x08>\r>\x08?\n@\x03@\n@\x0c@\n?\x0b?\x05@\x05@\x0e@\x07?\x06?\x06>\x0b>\n?\t@\x07@\x0e@\x06@\x05?\x02>\t>\x06?\x0b@\r@\x04?\x08?\r?\x0e?\x07?\r?\x00@\x08@\x01@\n?\x0b@\t?\x0c?\x10@\x08@\r?\x02?\x01?\x02?\x07?\x02@\x06?\n?\t?\x00?\x03?\x04@\x0c@\t@\x04@\x05@\x01?\r?\x0c?\x07?\x03@\x01@\x07?\x10@\x08?\n@\x0f@\n?\x10@\x01?\x0c?\x03?\t?\x02@\x0c@\r?\x10@\x08@\x0e?\x06?\x0b?\x0f?\x02@\x10@\n?\x04?\x0e@\x02?\x0e?\x00?\x01@\x0b?\x01?\x08@\x06?\x07?\x07@\x05?\x01@\n@\x06?\x01@\x0f@\x01?\x08@\r?\x0e?\x04@\t?\x03@\x07@\x0c?\x10@\x0f@\x03?\x02@\r?\x0f?\x01@\x00?\x00@\x07@\x00?\x04@\x08@\x06?\n@\x0e?\t@\x10'
{b'exec', b'repeat', b'../ring/bell.html', b'print', b'switch'} 👀

# Think: This level needs to be updated, since exec and print are not keywords in Python 3. The only two words left are repeat and switch
# Originally, in Python 2, the keywords list included print and exec
# But since Python 3 removed print and exec from the keyword list (they’re now built-ins, not keywords)

Browser: http://www.pythonchallenge.com/pc/ring/bell.html 🔐
Username: repeat
Password: switch
```

## Flag
http://www.pythonchallenge.com/pc/ring/bell.html

## Continue
[Continue](./Level28.md)
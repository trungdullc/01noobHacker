# Level 12

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/evil.html
```

## Goal
Given image with people dealing cards, if zoom in see lines

## What I learned
```
.gfx is a binary container — a file that holds raw, interleaved data for multiple images
Each image’s data is stored in every fifth byte.

bytes:  [0][1][2][3][4][5][6][7][8][9]...
         ↑  ↑  ↑  ↑  ↑
         |  |  |  |  |
         └──┴──┴──┴──┴──→ five interleaved images
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/evil.html 🔐

View Page Source

<html>
<head>
  <title>dealing evil</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="evil1.jpg"><br> 👀
</body>
</html>

Browser: http://www.pythonchallenge.com/pc/return/evil1.jpg ⌨️
Same image so next number deal is 2

Browser: http://www.pythonchallenge.com/pc/return/evil2.jpg ⌨️
See image say: not jpg - _.gfx

Browser: http://www.pythonchallenge.com/pc/return/evil3.jpg ⌨️
See image say: no more evils

Browser: http://www.pythonchallenge.com/pc/return/evil2.gfx ⌨️

AsianHacker-picoctf@webshell:~$ wget http://www.pythonchallenge.com/pc/return/evil2.gfx ⌨️
--2025-10-14 21:12:45--  http://www.pythonchallenge.com/pc/return/evil2.gfx
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized

Username/Password Authentication Failed.
AsianHacker-picoctf@webshell:~$ rz ⌨️
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  evil2.gfx 👀
AsianHacker-picoctf@webshell:~$ file evil2.gfx ⌨️
evil2.gfx: data

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3

# Open the binary file 'evil2.gfx' for reading in binary mode
file_handle = open("evil2.gfx", "rb")
gfx = file_handle.read()  # Read all bytes from the file into memory

# Dictionary to hold file handles for the 5 output images
images = {}

# Create 5 output image files (image0.jpg to image4.jpg) in binary write mode
for i in range(5):
    images[i] = open("image" + str(i) + ".jpg", "wb")

# The file 'evil2.gfx' contains interleaved image data:
# Each image's bytes are interleaved every 5 bytes in the source file.
# That is, byte 0 belongs to image0, byte 1 to image1, ..., byte 4 to image4, byte 5 again to image0, and so on.
# So we read in steps of 5 bytes and distribute each byte to the corresponding image.
for byte in range(0, len(gfx), 5):
    for i in range(5):
        # Check to avoid IndexError if the last chunk has fewer than 5 bytes
        if byte + i < len(gfx):
            images[i].write(bytes([gfx[byte + i]]))         # Write the i-th byte to the i-th image file

# Close the input file
file_handle.close()

# Close all the output image files
for i in range(5):
    images[i].close()

# After running this script, you will get 5 image files:
# image0.jpg, image1.jpg, image2.jpg, image3.jpg, and image4.jpg
# Each file corresponds to one of the interleaved image streams extracted from evil2.gfx.

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
evil2.gfx  hsperfdata_root  image0.jpg  image1.jpg  image2.jpg  image3.jpg  image4.jpg  node-compile-cache  pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ sz image*.jpg ⌨️   

Think: Open all images
image0.jpg      dis
image1.jpg      pro
image2.jpg      port
image3.jpg      ional
image4.jpg      ity (crossed out)

Browser: http://www.pythonchallenge.com/pc/return/disproportional.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/return/disproportional.html

## Continue
[Continue](./Level13.md)
# picoGym Level 100: Pixelated
Source: https://play.picoctf.org/practice/challenge/100

## Goal
I have these 2 images, can you make a flag out of them?<br>
scrambled1.png<br>
https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled1.png
scrambled2.png<br>
https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled2.png

## What I learned
```
stegsolve (Kali Linux/ParrotOS)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled1.png ⌨️
--2025-09-09 23:20:03--  https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled1.png
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 197172 (193K) [application/octet-stream]
Saving to: 'scrambled1.png'

scrambled1.png                                     100%[=============================================================================================================>] 192.55K  --.-KB/s    in 0.09s   

2025-09-09 23:20:03 (2.02 MB/s) - 'scrambled1.png' saved [197172/197172]

AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled2.png ⌨️
--2025-09-09 23:20:11--  https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled2.png
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 197173 (193K) [application/octet-stream]
Saving to: 'scrambled2.png'

scrambled2.png                                     100%[=============================================================================================================>] 192.55K  --.-KB/s    in 0.09s   

2025-09-09 23:20:11 (2.00 MB/s) - 'scrambled2.png' saved [197173/197173]

# Method 1: stegsolve
# File → Open: scrambled1.png
# Analyze → Image Combiner: scrambled2.png
# Scroll thru all bitwise operations
picoCTF{da8fcef8} 🔐

Method 2:
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
from PIL import Image                                   # import Image module from Pillow

# Opening first image
img1 = Image.open("scrambled1.png")
pixels1 = img1.load()

# Opening second image
img2 = Image.open("scrambled2.png")
pixels2 = img2.load()

# Creating a new image with the same size as the first image
flag = Image.new("RGB", img1.size)
flagpix = flag.load()

# Merging the two images
for row in range(img1.size[1]):                         # img1.size[1] is height of the image
    for col in range(img1.size[0]):                     # img1.size[0] is width of the image
        flagpix[col, row] = (
            (pixels1[col, row][0] + pixels2[col, row][0]) % 256,
            (pixels1[col, row][1] + pixels2[col, row][1]) % 256,
            (pixels1[col, row][2] + pixels2[col, row][2]) % 256
        )

# Saving the merged image
flag.save("flag.png")

AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ sz flag.png ⌨️

# Open File and zoom in
picoCTF{da8fcef8} 🔐
```

## Flag
picoCTF{da8fcef8}

## Continue
[Continue](./picoGym0158.md)
# Level 11

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/5808.html
```

## Goal
Given image but if look closely see blackish squares

## What I learned
```
from PIL import Image
image = Image.open("cave.jpg")
new_image = Image.new("RGB", size)
even_color = image.getpixel((x,y)) 
new_image.putpixel((x,y), even_color)
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/5808.html

View Page Source

<html>
<head>
  <title>odd even</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<img src="cave.jpg" width="640" height="480" border="0"/>
	<br>
	<br>
	<font color="gold" size="+1"></font>
</body>
</html>

AsianHacker-picoctf@webshell:~$ wget http://www.pythonchallenge.com/pc/return/cave.jpg ⌨️
--2025-10-14 02:33:25--  http://www.pythonchallenge.com/pc/return/cave.jpg
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized

Username/Password Authentication Failed.
AsianHacker-picoctf@webshell:~$ rz ⌨️
AsianHacker-picoctf@webshell:~$ ls  ⌨️      
README.txt  cave.jpg 👀
AsianHacker-picoctf@webshell:~$ mv cave.jpg /tmp ⌨️
AsianHacker-picoctf@webshell:~$ cd /tmp ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3
from PIL import Image

# Open the image
image = Image.open("cave.jpg")
size = width, height = image.size

# Create a new blank image of the same size and mode (RGB)
new_image = Image.new("RGB", size)                  # new_image = Image.new("RGB", (width, height))

# --- Approach 1: Copy pixels with even and odd coordinates ---
for x in range(0, width, 2):
    for y in range(0, height, 2):
        even_color = image.getpixel((x,y))           #even
        odd_color = image.getpixel((x+1, y + 1))     #odd

        new_image.putpixel((x,y), even_color)
        new_image.putpixel((x+1, y+1), odd_color)

# print(image)
new_image.save("image.jpg")

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ sz image.jpg ⌨️

# Think: Open image and see evil
Browser: http://www.pythonchallenge.com/pc/return/evil.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/return/evil.html

## Continue
[Continue](./Level12.md)
# Level 07

## Previous Flag
```
http://www.pythonchallenge.com/pc/def/oxygen.html
```

## Goal
Given png file

## What I learned
```
Image module you tried to import doesn’t exist as a standalone module in modern Python.
That old syntax came from Python Imaging Library (PIL), which has been replaced by Pillow.

AsianHacker-picoctf@webshell:~$ pip3 install Image ⚠️ Outdated
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/def/oxygen.html

View Page Source

<html>
<head>
  <title>smarty</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<img src="oxygen.png"/>
</body>
</html>

AsianHacker-picoctf@webshell:~$ wget http://www.pythonchallenge.com/pc/def/oxygen.png ⌨️
--2025-10-13 21:25:17--  http://www.pythonchallenge.com/pc/def/oxygen.png
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 127123 (124K) [image/png]
Saving to: 'oxygen.png'

oxygen.png                                                100%[=====================================================================================================================================>] 124.14K   826KB/s    in 0.2s    

2025-10-13 21:25:17 (826 KB/s) - 'oxygen.png' saved [127123/127123]

AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ chmod u+x pythonScript.py ⌨️ 
AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
Traceback (most recent call last):
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 3, in <module>
    import Image
ModuleNotFoundError: No module named 'Image' ⚠️
AsianHacker-picoctf@webshell:~$ pip3 install Image ⌨️⚠️

AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3

# import Image
from PIL import Image

oxygen = Image.open("oxygen.png")
print(oxygen)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=629x95 at 0x7F08F4217E20>

AsianHacker-picoctfÉwebshell:/tmp$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3

# import Image
from PIL import Image

oxygen = Image.open("oxygen.png")
size = height, width = 629, 95
y = 48
end_of_pixel_block = 607
# print(oxygen)

for x in range(0, end_of_pixel_block, 7):
  # print(oxygen.getpixel((x,y)))                   # (115, 115, 115, 255)
  print(chr(oxygen.getpixel((x,y))[0]), end="")

AsianHacker-picoctfÉwebshell:/tmp$ python3 pythonScript.py ⌨️
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121] 👀

# Convert Decimal to ASCII from CyberChef
https://cyberchef.io/#recipe=From_Decimal('Space',false)&input=MTA1LCAxMTAsIDExNiwgMTAxLCAxMDMsIDExNCwgMTA1LCAxMTYsIDEyMQ

# Conver Decimal to ASCII in terminal w/ python
AsianHacker-picoctfÉwebshell:/tmp$ cat pythonScript2.py ⌨️
#!/usr/bin/python3
myArray = [105, 110, 116, 101, 103, 114, 105, 116, 121]

# Convert each number to its corresponding ASCII character and join
print("".join(chr(c) for c in myArray))

AsianHacker-picoctfÉwebshell:/tmp$ python3 pythonScript2.py ⌨️
integrity 👀

Browser: http://www.pythonchallenge.com/pc/def/integrity.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/def/integrity.html

## Continue
[Continue](./Level07.md)
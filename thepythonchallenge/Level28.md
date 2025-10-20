# Level 28

## Previous Flag
```
http://www.pythonchallenge.com/pc/ring/bell.html
```

## Goal
Given image of waterfall inside forest<br>
RING-RING-RING<br>
say it out loud

## What I learned
```
Opens an image (`bell.png`)
Reads the green pixel channel
Takes pairwise pixel differences
Removes filler value `42`
Converts the remaining differences into characters to reveal a **hidden ASCII message**

So in short:
It extracts a secret message hidden in the pixel differences of the green channel of `bell.png`
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/ring/bell.html

View Page Source

<html>
<head>
  <title>many pairs ring-ring</title> 👀 pairs of green
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<img src="bell.png" border="0"/>
	<font color="gold">
	<br>RING-RING-RING 👀
	<br>say it out loud</font>
</body>
</html>

# Think: Sounds like green-green-green
# Browser: http://www.pythonchallenge.com/pc/ring/green.html ⌨️
yes! green!

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget --user repeat --password switch http://www.pythonchallenge.com/pc/ring/bell.png ⌨️
--2025-10-19 03:57:45--  http://www.pythonchallenge.com/pc/ring/bell.png
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="the order matters"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 669986 (654K) [image/png]
Saving to: 'bell.png'

bell.png                                                  100%[=====================================================================================================================================>] 654.28K  1.47MB/s    in 0.4s    

2025-10-19 03:57:45 (1.47 MB/s) - 'bell.png' saved [669986/669986]

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
from PIL import Image

im = Image.open('bell.png')

# split RGB and get Green
green = list(im.split()[1].getdata())

# calculate diff for every two bytes
diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]

# remove the most frequent value 42
filtered = list(filter(lambda x: x != 42, diff))

# convert to string and print out
print(bytes(filtered).decode())

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
whodunnit().split()[0] ?

# Think: who done it (as in created python)
AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> "Guido van Rossum".split()[0] ⌨️
'Guido'

# Browser: http://www.pythonchallenge.com/pc/ring/guido.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/ring/guido.html

## Continue
[Continue](./Level29.md)
# Level 31

## Previous Flag
```
http://www.pythonchallenge.com/pc/ring/grandpa.html
```

## Goal
Given image of huge rocks by a lake

## What I learned
```
The Arecibo message is a famous interstellar radio message sent from the Arecibo Observatory in Puerto Rico on November 16, 1974 toward the globular star cluster M13, about 25,000 light-years away.

It was a binary-encoded message designed by Frank Drake (with help from Carl Sagan and others) to demonstrate human technological achievement — not to start a real conversation with aliens.
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/ring/grandpa.html

View Page Source

<html>
<head>
  <title>Where am I?</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold">
	<a href="../rock/grandpa.html"><img src="grandpa.jpg"/></a> 👀

<!-- short break, this ***REALLY*** has nothing to do with Python --> 👀
<br><br>
</body>
</html>

# Google: grandfather rock in asia ⌨️
These amazing rock formations of Hin Ta and Hin Yai are on Koh Samui’s south coast

Browser: http://www.pythonchallenge.com/pc/rock/grandpa.html ⌨️
Username: kohsamui ⌨️
Password: thailand ⌨️

That was too easy. You are still on 31...
# Given image of snowflake creature

View Page Source

<html>
<head>
	<img src="mandelbrot.gif" border="0"> 👀
  <title>UFOs ?</title> 
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold">That was too easy. You are still on 31...</font>
	<br><br>
	<img src="mandelbrot.gif" border="0"> 👀
		<window left="0.34" top="0.57" width="0.036" height="0.027"/> 👀 Given
		<option iterations="128"/>
	</img>
<br><br>
</body>
</html>

# Google: mandelbrot
https://en.wikipedia.org/wiki/Mandelbrot_set
# ChatGPT
The Mandelbrot set is a famous fractal made by repeatedly squaring numbers and adding a constant.
If the result doesn’t grow endlessly, that number belongs to the set — forming the beautiful black-and-color pattern you see in Mandelbrot images.

AsianHacker-picoctf@webshell:/tmp$ wget --user kohsamui --password thailand http://www.pythonchallenge.com/pc/rock/mandelbrot.gif ⌨️
--2025-10-19 15:48:28--  http://www.pythonchallenge.com/pc/rock/mandelbrot.gif
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="island : country"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 173418 (169K) [image/gif]
Saving to: 'mandelbrot.gif'

mandelbrot.gif                                            100%[=====================================================================================================================================>] 169.35K   972KB/s    in 0.2s    

2025-10-19 15:48:28 (972 KB/s) - 'mandelbrot.gif' saved [173418/173418]

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
from PIL import Image

# Open the original Mandelbrot image
img = Image.open("mandelbrot.gif")

# Define the section of the complex plane to explore
left = 0.34       # x-axis start position
bottom = 0.57     # y-axis start position
width = 0.036     # width of the zoom area
height = 0.027    # height of the zoom area
max = 128         # maximum number of iterations per point

# Get image dimensions
w, h = img.size

# Calculate step sizes for x and y directions
xstep = width / w
ystep = height / h

result = []  # stores iteration counts for each pixel

# For each pixel in the image (bottom to top)
for y in range(h - 1, -1, -1):
    for x in range(w):
        # Map pixel (x, y) to a point 'c' in the complex plane
        c = complex(left + x * xstep, bottom + y * ystep)
        z = 0 + 0j  # start with z = 0
        for i in range(max):
            z = z * z + c  # Mandelbrot iteration
            if abs(z) > 2:  # if it escapes the circle, stop
                break
        result.append(i)  # store how many iterations before escape

# Create a new image and fill it with computed iteration data
img2 = img.copy()
img2.putdata(result)
# img2.show()
img2.save("mandelbrot_generated.png")  # Save generated fractal visualization

# Compare pixel values between original and generated image
diff = [(a - b) for a, b in zip(img.getdata(), img2.getdata()) if a != b]
print(len(diff))  # Print number of differing pixels

# Create a new black-and-white image showing the difference pattern
plot = Image.new('L', (23, 73))
plot.putdata([(i < 16) and 255 or 0 for i in diff])
# plot.resize((230,730)).show()
plot.resize((230,730))
plot.save("mandelbrot_diff.png")  # Save the difference plot

AsianHacker-picoctf@webshell:/tmp$ chmod u+x pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
1679
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  mandelbrot.gif  mandelbrot_diff.png  mandelbrot_generated.png  node-compile-cache  pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ sz mandelbrot_diff.png mandelbrot_generated.png ⌨️

# Think: Look at mandelbroth_diff.png
# Looks like some egyptian message to aliens
# Google: ufo message from earth to alien called
https://en.wikipedia.org/wiki/Arecibo_message

Browser: http://www.pythonchallenge.com/pc/rock/arecibo.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/rock/arecibo.html

## Continue
[Continue](./Level32.md)
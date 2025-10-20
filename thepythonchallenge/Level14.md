# Level 14

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/italy.html
```

## Goal
Given picture of crossaint and barcode

## What I learned
```
Youtube Solved w/ John Hammond: https://www.youtube.com/watch?v=WpTwE6XmzRQ&list=PL1H1sBF1VAKWfha866WUjDw0cwser3HAZ&index=16 
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/italy.html

View Page Source

<html>
<head>
  <title>walk around</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="italy.jpg"><br>
<br>

<!-- remember: 100*100 = (100+99+99+98) + (...  --> 👀

<img src="wire.png" width="100" height="100">

</body>
</html>

AsianHacker-picoctf@webshell:/tmp$ rz ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️ 
hsperfdata_root  node-compile-cache  wire.png 👀

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3
from PIL import Image

# Create a new 100x100 RGB image to draw into
img = Image.new ("RGB", (100, 100))
# Open the source "wire.png" (assumed to be a long 1-pixel-high strip,
# where we read color values sequentially along the x axis)
wire = Image.open("wire.png", "r")

# Boundary variables defining the current rectangle we are walking:
# xmin..xmax horizontally, ymin..ymax vertically (inclusive coordinates)
xmin, xmax, ymin, ymax = 0, 99, 0, 99

# Current position (x,y) on `img` that we will update
pos = [0,0]
# `place` is an index into the `wire` image (we read pixels at (place, 0))
place = 0
# When True the script prints positions as it walks (debugging)
output = True

# Loop until the spiral has collapsed to a 1-pixel-wide/tall area.
# The condition checks whether the inner area has become too small
# to continue a full spiral cycle.
while not (xmax - 1 == xmin or ymax - 1 == ymin):
  # --- Move right along the top edge from xmin to xmax ---
  for x in range(xmin, xmax + 1):
    if output: 
      print("x ", pos[0], " y ", pos[1])
    # update x coordinate of current position
    pos[0] = x
    # advance to next color in the wire strip
    place += 1
    # paint the pixel at pos using the next pixel from the wire image
    img.putpixel(pos, wire.getpixel((place,0)))
  # finished the top row, move the top boundary down
  ymin += 1

  # --- Move down along the right edge from ymin to ymax ---
  for y in range(ymin, ymax + 1):
    if output:
      print("x ", pos[0], " y ", pos[1])
    # update y coordinate of current position
    pos[1] = y
    place += 1
    img.putpixel(pos, wire.getpixel((place,0)))
  # finished the right column, move the right boundary left
  xmax -= 1

  # --- Move left along the bottom edge from xmax down to xmin ---
  for x in range(xmax, xmin - 1, -1):
    if output: 
      print("x ", pos[0], " y ", pos[1])
    pos[0] = x
    place += 1
    img.putpixel(pos, wire.getpixel((place,0)))
  # finished the bottom row, move the bottom boundary up
  ymax -= 1

  # --- Move up along the left edge from ymax up to ymin ---
  for y in range(ymax, ymin - 1, -1):
    if output:
      print("x ", pos[0], " y ", pos[1])
    pos[1] = y
    place += 1
    img.putpixel(pos, wire.getpixel((place,0)))
  # finished the left column, move the left boundary right
  xmin += 1

# Save the resulting image containing the spiral fill
img.save("spiral.png")

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ sz spiral.png ⌨️

# Think: Open spiral.png see a cat
Browser: http://www.pythonchallenge.com/pc/return/cat.html ⌨️
and its name is uzi. you'll hear from him later. 👀

Browser: http://www.pythonchallenge.com/pc/return/uzi.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/return/uzi.html

## Continue
[Continue](./Level15.md)
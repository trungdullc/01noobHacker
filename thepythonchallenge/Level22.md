# Level 22

## Previous Flag
```
http://www.pythonchallenge.com/pc/hex/copper.html
```

## Goal
Given image of a joystick

## What I learned
```
data = new.load()
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/hex/copper.html

View Page Source

<html>
<head>
  <title>emulate</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="level22.jpg"><br>
<!-- or maybe white.gif would be more bright--> 👀
</body>
</html>

# Download gif
Browser: http://www.pythonchallenge.com/pc/hex/white.gif ⌨️

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests

url = "http://www.pythonchallenge.com/pc/hex/white.gif"
auth = ("butter","fly")

r = requests.get(url, auth=auth, headers={"Accept-Encoding": "identity"})
print(r.status_code, r.headers.get("Content-Range") or r.headers.get("Content-Length"))

# Save raw bytes (works for images)
with open("white.gif", "wb") as file:
    file.write(r.content)

print("Saved white.gif, bytes:", len(r.content))

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
200 38979
Saved white.gif, bytes: 38979
AsianHacker-picoctf@webshell:/tmp$ file white.gif ⌨️
white.gif: GIF image data, version 89a, 200 x 200

AsianHacker-picoctf@webshell:/tmp$ exiftool white.gif ⌨️
ExifTool Version Number         : 12.40
File Name                       : white.gif
Directory                       : .
File Size                       : 38 KiB
File Modification Date/Time     : 2025:10:17 20:41:53+00:00
File Access Date/Time           : 2025:10:17 20:42:01+00:00
File Inode Change Date/Time     : 2025:10:17 20:41:53+00:00
File Permissions                : -rw-rw-r--
File Type                       : GIF
File Type Extension             : gif
MIME Type                       : image/gif
GIF Version                     : 89a
Image Width                     : 200
Image Height                    : 200
Has Color Map                   : Yes
Color Resolution Depth          : 7
Bits Per Pixel                  : 4
Background Color                : 9
Animation Iterations            : Infinite
Comment                         : Created with The GIMP
Transparent Color               : 15
Frame Count                     : 133
Duration                        : 1.33 s
Image Size                      : 200x200
Megapixels                      : 0.040

AsianHacker-picoctf@webshell:/tmp$ python3 -q
>>> # Python Image Library
>>> from PIL import Image ⌨️
>>> img = Image.open("white.gif") ⌨️

>>> # img.show()
>>> print(dir(img)) ⌨️
# ['_GifImageFile__frame', '_GifImageFile__offset', '_GifImageFile__rewind', '_Image__transformer', '__annotations__', '__array_interface__', '__class__', '__copy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_close_exclusive_fp_after_loading', '_close_fp', '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_exif', '_expand', '_fp', '_frame_palette', '_frame_transparency', '_get_safe_box', '_im', '_is_palette_needed', '_min_frame', '_mode', '_n_frames', '_new', '_open', '_reload_exif', '_repr_image', '_repr_jpeg_', '_repr_png_', '_repr_pretty_', '_seek', '_seek_check', '_size', 'alpha_composite', 'apply_transparency', 'close', 'convert', 'copy', 'crop', 'custom_mimetype', 'data', 'decoderconfig', 'decodermaxblock', 'disposal_method', 'dispose', 'dispose_extent', 'draft', 'effect_spread', 'entropy', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'get_child_images', 'get_format_mimetype', 'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getexif', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'getxmp', 'global_palette', 'has_transparency_data', 'height', 'histogram', 'im', 'info', 'is_animated', 'load', 'load_end', 'load_prepare', 'mode', 'n_frames', 'palette', 'paste', 'point', 'putalpha', 'putdata', 'putpalette', 'putpixel', 'quantize', 'readonly', 'reduce', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'split', 'tell', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'transform', 'transpose', 'verify', 'width']
print(img.n_frames)                                                         # 133

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

# Python Image Library
from PIL import Image
img = Image.open("white.gif")

# img.show()
print(dir(img))

print(img.n_frames)

for frame in range(img.n_frames):
    img.seek(frame)
    img.save("frame%d.png" % frame)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
['_GifImageFile__frame', '_GifImageFile__offset', '_GifImageFile__rewind', '_Image__transformer', '__annotations__', '__array_interface__', '__class__', '__copy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_close_exclusive_fp_after_loading', '_close_fp', '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_exif', '_expand', '_fp', '_frame_palette', '_frame_transparency', '_get_safe_box', '_im', '_is_palette_needed', '_min_frame', '_mode', '_n_frames', '_new', '_open', '_reload_exif', '_repr_image', '_repr_jpeg_', '_repr_png_', '_repr_pretty_', '_seek', '_seek_check', '_size', 'alpha_composite', 'apply_transparency', 'close', 'convert', 'copy', 'crop', 'custom_mimetype', 'data', 'decoderconfig', 'decodermaxblock', 'disposal_method', 'dispose', 'dispose_extent', 'draft', 'effect_spread', 'entropy', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'get_child_images', 'get_format_mimetype', 'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getexif', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'getxmp', 'global_palette', 'has_transparency_data', 'height', 'histogram', 'im', 'info', 'is_animated', 'load', 'load_end', 'load_prepare', 'mode', 'n_frames', 'palette', 'paste', 'point', 'putalpha', 'putdata', 'putpalette', 'putpixel', 'quantize', 'readonly', 'reduce', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'split', 'tell', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'transform', 'transpose', 'verify', 'width']
133
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
frame0.png    frame106.png  frame114.png  frame122.png  frame130.png  frame2.png   frame28.png  frame36.png  frame44.png  frame52.png  frame60.png  frame69.png  frame77.png  frame85.png  frame93.png         pythonScript.py
frame1.png    frame107.png  frame115.png  frame123.png  frame131.png  frame20.png  frame29.png  frame37.png  frame45.png  frame53.png  frame61.png  frame7.png   frame78.png  frame86.png  frame94.png         white.gif
frame10.png   frame108.png  frame116.png  frame124.png  frame132.png  frame21.png  frame3.png   frame38.png  frame46.png  frame54.png  frame62.png  frame70.png  frame79.png  frame87.png  frame95.png
frame100.png  frame109.png  frame117.png  frame125.png  frame14.png   frame22.png  frame30.png  frame39.png  frame47.png  frame55.png  frame63.png  frame71.png  frame8.png   frame88.png  frame96.png
frame101.png  frame11.png   frame118.png  frame126.png  frame15.png   frame23.png  frame31.png  frame4.png   frame48.png  frame56.png  frame64.png  frame72.png  frame80.png  frame89.png  frame97.png
frame102.png  frame110.png  frame119.png  frame127.png  frame16.png   frame24.png  frame32.png  frame40.png  frame49.png  frame57.png  frame65.png  frame73.png  frame81.png  frame9.png   frame98.png
frame103.png  frame111.png  frame12.png   frame128.png  frame17.png   frame25.png  frame33.png  frame41.png  frame5.png   frame58.png  frame66.png  frame74.png  frame82.png  frame90.png  frame99.png
frame104.png  frame112.png  frame120.png  frame129.png  frame18.png   frame26.png  frame34.png  frame42.png  frame50.png  frame59.png  frame67.png  frame75.png  frame83.png  frame91.png  hsperfdata_root
frame105.png  frame113.png  frame121.png  frame13.png   frame19.png   frame27.png  frame35.png  frame43.png  frame51.png  frame6.png   frame68.png  frame76.png  frame84.png  frame92.png  node-compile-cache

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from PIL import Image

img = Image.open("frame0.png") 👀

def extract_frames():
    for frame in range(img.n_frames):
        img.seek(frame)
        img.save("frame%d.png" % frame)

data = img.load()
size = width, height = img.size

for x in range(width):
    for y in range(height):
        print(data[x,y]) 👀

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py | sort | uniq -c v
  39999 0
      1 8

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from PIL import Image

img = Image.open("frame0.png")

def extract_frames():
    for frame in range(img.n_frames):
        img.seek(frame)
        img.save("frame%d.png" % frame)

data = img.load()
size = width, height = img.size

for x in range(width):
    for y in range(height):
        if (data[x,y] == 8):
            data[x,y] = 255

img.save("temp.png") 👀 instead of img.show()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ sz temp.png ⌨️

# Think: above shows to one frame but what happens when do with all png
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3

from PIL import Image
total_frames = 133

for i in range(total_frames):
    img = Image.open("frame%d.png" %i) 👀
    data = img.load()

    size = width, height = img.size
    new = Image.new("RGB", size)
    new_data = new.load()

    for x in range(width):
        for y in range(height):
            if (data[x,y] == 8): 👀
                new_data[x,y] = (255,255,255) 👀
    new.save("new_frame%d.png" % i)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls
frame0.png    frame116.png  frame15.png  frame33.png  frame51.png  frame7.png   frame88.png       new_frame103.png  new_frame121.png  new_frame20.png  new_frame39.png  new_frame57.png  new_frame75.png  new_frame93.png
frame1.png    frame117.png  frame16.png  frame34.png  frame52.png  frame70.png  frame89.png       new_frame104.png  new_frame122.png  new_frame21.png  new_frame4.png   new_frame58.png  new_frame76.png  new_frame94.png
frame10.png   frame118.png  frame17.png  frame35.png  frame53.png  frame71.png  frame9.png        new_frame105.png  new_frame123.png  new_frame22.png  new_frame40.png  new_frame59.png  new_frame77.png  new_frame95.png
frame100.png  frame119.png  frame18.png  frame36.png  frame54.png  frame72.png  frame90.png       new_frame106.png  new_frame124.png  new_frame23.png  new_frame41.png  new_frame6.png   new_frame78.png  new_frame96.png
frame101.png  frame12.png   frame19.png  frame37.png  frame55.png  frame73.png  frame91.png       new_frame107.png  new_frame125.png  new_frame24.png  new_frame42.png  new_frame60.png  new_frame79.png  new_frame97.png
frame102.png  frame120.png  frame2.png   frame38.png  frame56.png  frame74.png  frame92.png       new_frame108.png  new_frame126.png  new_frame25.png  new_frame43.png  new_frame61.png  new_frame8.png   new_frame98.png
frame103.png  frame121.png  frame20.png  frame39.png  frame57.png  frame75.png  frame93.png       new_frame109.png  new_frame127.png  new_frame26.png  new_frame44.png  new_frame62.png  new_frame80.png  new_frame99.png
frame104.png  frame122.png  frame21.png  frame4.png   frame58.png  frame76.png  frame94.png       new_frame11.png   new_frame128.png  new_frame27.png  new_frame45.png  new_frame63.png  new_frame81.png  node-compile-cache
frame105.png  frame123.png  frame22.png  frame40.png  frame59.png  frame77.png  frame95.png       new_frame110.png  new_frame129.png  new_frame28.png  new_frame46.png  new_frame64.png  new_frame82.png  pythonScript.py
frame106.png  frame124.png  frame23.png  frame41.png  frame6.png   frame78.png  frame96.png       new_frame111.png  new_frame13.png   new_frame29.png  new_frame47.png  new_frame65.png  new_frame83.png  temp.png
frame107.png  frame125.png  frame24.png  frame42.png  frame60.png  frame79.png  frame97.png       new_frame112.png  new_frame130.png  new_frame3.png   new_frame48.png  new_frame66.png  new_frame84.png  white.gif
frame108.png  frame126.png  frame25.png  frame43.png  frame61.png  frame8.png   frame98.png       new_frame113.png  new_frame131.png  new_frame30.png  new_frame49.png  new_frame67.png  new_frame85.png
frame109.png  frame127.png  frame26.png  frame44.png  frame62.png  frame80.png  frame99.png       new_frame114.png  new_frame132.png  new_frame31.png  new_frame5.png   new_frame68.png  new_frame86.png
frame11.png   frame128.png  frame27.png  frame45.png  frame63.png  frame81.png  hsperfdata_root   new_frame115.png  new_frame14.png   new_frame32.png  new_frame50.png  new_frame69.png  new_frame87.png
frame110.png  frame129.png  frame28.png  frame46.png  frame64.png  frame82.png  new_frame0.png    new_frame116.png  new_frame15.png   new_frame33.png  new_frame51.png  new_frame7.png   new_frame88.png
frame111.png  frame13.png   frame29.png  frame47.png  frame65.png  frame83.png  new_frame1.png    new_frame117.png  new_frame16.png   new_frame34.png  new_frame52.png  new_frame70.png  new_frame89.png
frame112.png  frame130.png  frame3.png   frame48.png  frame66.png  frame84.png  new_frame10.png   new_frame118.png  new_frame17.png   new_frame35.png  new_frame53.png  new_frame71.png  new_frame9.png
frame113.png  frame131.png  frame30.png  frame49.png  frame67.png  frame85.png  new_frame100.png  new_frame119.png  new_frame18.png   new_frame36.png  new_frame54.png  new_frame72.png  new_frame90.png
frame114.png  frame132.png  frame31.png  frame5.png   frame68.png  frame86.png  new_frame101.png  new_frame12.png   new_frame19.png   new_frame37.png  new_frame55.png  new_frame73.png  new_frame91.png
frame115.png  frame14.png   frame32.png  frame50.png  frame69.png  frame87.png  new_frame102.png  new_frame120.png  new_frame2.png    new_frame38.png  new_frame56.png  new_frame74.png  new_frame92.png

AsianHacker-picoctf@webshell:/tmp$ convert new_frame* final.gif ⌨️
Killed ⚠️
# Suppose open gif file see what it does

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from PIL import Image
img = Image.open("white.gif")

for frame_number in range(img.n_frames):
    img.seek(frame_number)

    x,y,x2,y2 = img.getbbox() 👀
    print("x: ", x, "y: ", y)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
x:  98 y:  102
x:  98 y:  100
x:  98 y:  100
x:  98 y:  100
x:  98 y:  100
x:  98 y:  100
x:  98 y:  100
x:  98 y:  100
x:  98 y:  98

# Mimic Drawing w/ a cursor that starts at center 100,100
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from PIL import Image

# Open the original animated GIF
img = Image.open("white.gif")

# Create a blank canvas (new image) where we’ll draw the cursor path
# Made slightly larger to ensure all movements fit within the frame
new = Image.new("RGB", (400, 200), "black")
data = new.load()

# Initialize cursor starting point (center) and store it for reference
center_x, center_y = cursor_x, cursor_y = 100, 100

# Define white color for drawing
white = (255, 255, 255)

# Iterate over all frames in the GIF
for frame_number in range(img.n_frames):
    # Move to the current frame
    img.seek(frame_number)

    # Get bounding box coordinates (where the non-background pixels are)
    x, y, x2, y2 = img.getbbox()
    # Each frame represents cursor movement relative to center

    # Calculate difference from the original center
    x_difference = x - center_x 👀
    y_difference = y - center_y 👀

    # If no movement detected (cursor didn’t move), jump right by 50 pixels
    # This simulates the "reset" movement described in the challenge
    if x_difference == 0 and y_difference == 0: 👀
        cursor_x += 50

    # Update cursor position based on movement delta
    cursor_x += x_difference
    cursor_y += y_difference

    # Draw a white pixel at the cursor's new position
    data[cursor_x, cursor_y] = white

# Save the result as a new GIF (not shown on screen)
new.save("new.gif")

# Optional: Print a success message
print("Drawing complete. Saved as new.gif")

# Think: Open file and see it spells bonus
Browser: http://www.pythonchallenge.com/pc/hex/bonus.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/hex/bonus.html

## Continue
[Continue](./Level23.md)
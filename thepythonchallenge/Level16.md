# Level 16

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/mozart.html
```

## Goal
Given image might need zoom in

## What I learned
```
ImageChops Module
Youtube Solution: https://www.youtube.com/watch?v=k-bjhrnCSKo&list=PL1H1sBF1VAKWfha866WUjDw0cwser3HAZ&index=18
  shows subprocess module
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/mozart.html ⌨️

View Page Source:

<html>
<head>
  <title>let me get this straight</title> 👀
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<br><center>
<img src="mozart.gif"><br>
</body>
</html>

# Think: If zoom in see spaced out straight purple lines
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️

#!/usr/bin/python3
from PIL import Image, ImageChops  # import PIL modules for image handling and manipulation

# This is the byte we are searching for in each row to detect the "purple line"
offset_indicator = b"\xc3"                  # or "\xc3".encode(), must be bytes since row.tobytes() returns bytes

# Open the GIF image
image = Image.open("mozart.gif")

# Get the width and height of the image
size = width, height = image.size

# Loop over each row (y-coordinate) in the image
for y in range(height):
    # Define a box to crop a single row of the image
    crop_box = 0, y, width, y + 1

    # Crop the current row from the image
    row = image.crop(crop_box)
    # row.show()

    # Convert the cropped row into raw bytes
    row_bytes = row.tobytes()

    '''
    # This block was used to find repeating colors in a row
    # It checks for 4 consecutive bytes with the same value
    # Uncomment if you want to detect repeating pixel patterns
    for i in range(len(row_bytes) - 3):
        character = row_bytes[i]
        if character == row_bytes[i+1] == row_bytes[i+2] == row_bytes[i+3]:
            print(hex(character))  # prints repeating byte in hexadecimal, "\xc3", print(f"{pixels[i]:02x}") is offset_indicator
    '''

    # Shift the row to the left to "cover" the detected purple lines
    # We find the index of the offset_indicator in the row bytes
    # and subtract 1 to determine how many pixels to shift
    try:
        offset = row_bytes.index(offset_indicator) - 1
        row = ImageChops.offset(row, -offset)  # shift the row to the left by 'offset' pixels

        # Paste the shifted row back into the original image
        image.paste(row, crop_box)
    except ValueError:
        # If the offset_indicator is not found in the row, skip shifting
        pass

# Display the final image with rows shifted
image.show()

# Close the image to free resources
image.close()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
Error: no "view" rule for type "image/png" passed its test case
       (for more information, add "--debug=1" on the command line)
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  mozart.gif  node-compile-cache  pythonScript.py  tmpcpeqv96u.PNG 👀
AsianHacker-picoctf@webshell:/tmp$ sz tmpcpeqv96u.PNG ⌨️

# Think: Open the png saw word: romance 👀
Browser: http://www.pythonchallenge.com/pc/return/romance.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/return/romance.html

## Continue
[Continue](./Level17.md)
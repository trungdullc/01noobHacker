# Level 18

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/balloons.html
```

## Goal
Given image of swans to compare the left is brighter than right

## What I learned
```
wget --user=huge --password=file "http://www.pythonchallenge.com/pc/return/deltas.gz"
curl -u huge:file -O "http://www.pythonchallenge.com/pc/return/deltas.gz"
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/balloons.html 🔐

View Page Source

<html>
<head>
  <title>can you tell the difference?</title> 👀
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold">
	<img src="balloons.jpg" border="0"/>
<!-- it is more obvious that what you might think -->
</body>
</html>

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from PIL import Image  

# Open the image file
image = Image.open("balloons.jpg")

# Get image dimensions
width, height = image.size

# Define coordinates for cropping
left_box = (0, 0, width / 2, height)          # Left half
right_box = (width / 2, 0, width, height)     # Right half

# Crop the image into two halves
image1 = image.crop(left_box)
image2 = image.crop(right_box)

# Display both halves
# image1.show()
# image2.show()

image1.save("left_half.jpg")                # Save the left side as a new file
image2.save("right_half.jpg")               # Save the right side as a new file

AsianHacker-picoctf@webshell:/tmp$ chmod u+x pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ sz left_half.jpg right_half.jpg ⌨️

AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> from PIL import Image, ImageChops ⌨️
>>> print(dir(ImageChops)) ⌨️
['Image', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'add_modulo', 'annotations', 'blend', 'composite', 'constant', 'darker', 'difference', 'duplicate', 'hard_light', 'invert', 'lighter', 'logical_and', 'logical_or', 'logical_xor', 'multiply', 'offset', 'overlay', 'screen', 'soft_light', 'subtract', 'subtract_modulo']
>>> help(ImageChops) ⌨️
>>> help(ImageChops.difference) ⌨️
Help on function difference in module PIL.ImageChops:

difference(image1: 'Image.Image', image2: 'Image.Image') -> 'Image.Image'
    Returns the absolute value of the pixel-by-pixel difference between the two
    images. ::
    
        out = abs(image1 - image2)
    
    :rtype: :py:class:`~PIL.Image.Image`

Browser: http://www.pythonchallenge.com/pc/return/brightness.html ⌨️

View Page Source

<html>
<head>
  <title>can you tell the difference?</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold">
	<img src="balloons.jpg" border="0"/>
<!-- maybe consider deltas.gz --> 👀
</body>
</html>

Browser: http://www.pythonchallenge.com/pc/return/deltas.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget --user=huge --password=file "http://www.pythonchallenge.com/pc/return/deltas.gz" ⌨️
--2025-10-15 23:02:22--  http://www.pythonchallenge.com/pc/return/deltas.gz
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="inflate"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 79042 (77K) [application/x-gzip]
Saving to: 'deltas.gz'

deltas.gz                                                  100%[=====================================================================================================================================>]  77.19K  --.-KB/s    in 0.1s    

2025-10-15 23:02:22 (709 KB/s) - 'deltas.gz' saved [79042/79042]

AsianHacker-picoctf@webshell:/tmp$ gunzip deltas.gz ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
balloons.jpg  deltas  hsperfdata_root  left_half.jpg  node-compile-cache  pythonScript.py  right_half.jpg
AsianHacker-picoctf@webshell:/tmp$ file deltas ⌨️ 
deltas: ASCII text

AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> import difflib ⌨️
>>> print(dir(difflib)) ⌨️
['Differ', 'GenericAlias', 'HtmlDiff', 'IS_CHARACTER_JUNK', 'IS_LINE_JUNK', 'Match', 'SequenceMatcher', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_calculate_ratio', '_check_types', '_file_template', '_format_range_context', '_format_range_unified', '_keep_original_ws', '_legend', '_mdiff', '_namedtuple', '_nlargest', '_styles', '_table_template', '_test', 'context_diff', 'diff_bytes', 'get_close_matches', 'ndiff', 'restore', 'unified_diff']
>>> print(dir(difflib.Differ)) ⌨️
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_dump', '_fancy_helper', '_fancy_replace', '_plain_replace', '_qformat', 'compare']
>>> print(dir(difflib.Differ.compare)) ⌨️
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> help(difflib.Differ.compare) ⌨️
Help on function compare in module difflib:

compare(self, a, b)
    Compare two sequences of lines; generate the resulting delta.
    
    Each sequence must contain individual single-line strings ending with
    newlines. Such sequences can be obtained from the `readlines()` method
    of file-like objects.  The delta generated also consists of newline-
    terminated strings, ready to be printed as-is via the writelines()
    method of a file-like object.
    
    Example:
    
    >>> print(''.join(Differ().compare('one\ntwo\nthree\n'.splitlines(True),
    ...                                'ore\ntree\nemu\n'.splitlines(True))),
    ...       end="")
    - one
    ?  ^
    + ore
    ?  ^
    - two
    - three
    ?  -
    + tree
    + emu

# Use python split the columns middle for image 1 right for image 2 and compare differences
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import difflib

filename = "deltas"

# Read all lines from the input file                  # handle = open(filename)
with open(filename) as handle:                        # lines = handle.readlines()
    lines = handle.readlines()                        # handle.close()

sequence1 = []
sequence2 = []

# Split each line into two 55-character halves
for line in lines:
  sequence1.append(line[:55].strip() + "\n")        # left half
  sequence2.append(line[55:].strip() + "\n")        # right half
  # print sequence1
  # print sequence2
  # break

# Use difflib to compare the two sequences
differ = difflib.Differ()
comparison = list(differ.compare(sequence1, sequence2))

# Create binary files for image output
seq1_img = open("sequence1_image.png", "wb")
seq2_img = open("sequence2_image.png", "wb")
both_img = open("both_image.png", "wb")

# Go through comparison results and write differences
for each_result in comparison:
    # each_result looks like: '- 00 ff a3' or '+ 12 34 56'
    # slice [2:] removes the first two characters ('- ' or '+ ')
    hex_values = each_result[2:].split()
    try:
        # Convert hex strings (e.g. 'FF') → bytes
        byte_data = bytes([int(b, 16) for b in hex_values])
    except ValueError:
        continue  # skip any line that isn't valid hex

    if each_result.startswith("-"):                 # present only in sequence1
        seq1_img.write(byte_data)
    elif each_result.startswith("+"):               # present only in sequence2
        seq2_img.write(byte_data)
    elif each_result.startswith(" "):               # common to both sequences, according to documentation
        both_img.write(byte_data)

# Close all files
seq1_img.close()
seq2_img.close()
both_img.close()

print("Wrote: sequence1_image.png, sequence2_image.png, both_image.png")

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
Wrote: sequence1_image.png, sequence2_image.png, both_image.png
AsianHacker-picoctf@webshell:/tmp$ sz both_image.png sequence1_image.png sequence2_image.png ⌨️

# Think: open all files to see
fly
butter
../hex/bin.html

Browser: http://www.pythonchallenge.com/pc/hex/bin.html 🔐
Username: butter ⌨️
Password: fly ⌨️
```

## Flag
http://www.pythonchallenge.com/pc/hex/bin.html

## Continue
[Continue](./Level19.md)
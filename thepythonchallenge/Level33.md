# Level 33

## Previous Flag
```
http://www.pythonchallenge.com/pc/rock/beer.html
Username: kohsamui
Password: thailand 
```

## Goal
Given image of beer cavern

## What I learned
```

```

## Solution
```
# Browser: http://www.pythonchallenge.com/pc/rock/beer.html

View Page Source

<html>
<head>
  <title>33 bottles of beer on the wall</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold"></font>
	<br>
	<img src="beer1.jpg" border="0"/><br><br>
<br><br>
</body>
</html>

<!--
If you are blinded by the light,
remove its power, with its might.
Then from the ashes, fair and square,
another truth at you will glare.
--> 👀

Browser: http://www.pythonchallenge.com/pc/rock/beer1.jpg ⌨️

Browser: http://www.pythonchallenge.com/pc/rock/beer2.jpg ⌨️
Given image no, png

Browser: http://www.pythonchallenge.com/pc/rock/beer2.png ⌨️
Given image with x in middle

AsianHacker-picoctf@webshell:/tmp$ wget --user kohsamui --password thailand http://www.pythonchallenge.com/pc/rock/beer2.png ⌨️
--2025-10-20 15:36:22--  http://www.pythonchallenge.com/pc/rock/beer2.png
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="island : country"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 17589 (17K) [image/png]
Saving to: 'beer2.png'

beer2.png                                                 100%[=====================================================================================================================================>]  17.18K  --.-KB/s    in 0.05s   

2025-10-20 15:36:23 (369 KB/s) - 'beer2.png' saved [17589/17589]

AsianHacker-picoctf@webshell:/tmp$ file beer2.png ⌨️
beer2.png: PNG image data, 138 x 138, 8-bit grayscale, non-interlaced
AsianHacker-picoctf@webshell:/tmp$ exiftool beer2.png ⌨️
ExifTool Version Number         : 12.40
File Name                       : beer2.png
Directory                       : .
File Size                       : 17 KiB
File Modification Date/Time     : 2016:03:12 19:38:46+00:00
File Access Date/Time           : 2025:10:20 15:38:26+00:00
File Inode Change Date/Time     : 2025:10:20 15:38:16+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 138
Image Height                    : 138
Bit Depth                       : 8
Color Type                      : Grayscale
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 138x138
Megapixels                      : 0.019

AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> from PIL import Image ⌨️
>>> import math ⌨️
>>> im = Image.open('beer2.png') ⌨️
>>> dir(im) ⌨️
['_Image__transformer', '_PngImageFile__frame', '_PngImageFile__prepare_idat', '__annotations__', '__array_interface__', '__class__', '__copy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_close_exclusive_fp_after_loading', '_close_fp', '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_exif', '_expand', '_fp', '_get_safe_box', '_getexif', '_im', '_min_frame', '_mode', '_new', '_open', '_reload_exif', '_repr_image', '_repr_jpeg_', '_repr_png_', '_repr_pretty_', '_seek', '_seek_check', '_size', '_text', 'alpha_composite', 'apply_transparency', 'close', 'convert', 'copy', 'crop', 'custom_mimetype', 'decoderconfig', 'decodermaxblock', 'default_image', 'draft', 'effect_spread', 'entropy', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'get_child_images', 'get_format_mimetype', 'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getexif', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'getxmp', 'has_transparency_data', 'height', 'histogram', 'im', 'info', 'is_animated', 'load', 'load_end', 'load_prepare', 'load_read', 'mode', 'n_frames', 'palette', 'paste', 'png', 'point', 'private_chunks', 'putalpha', 'putdata', 'putpalette', 'putpixel', 'quantize', 'readonly', 'reduce', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'split', 'tell', 'text', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'transform', 'transpose', 'verify', 'width']
>>> im.mode ⌨️
'L'
>>> list(im.getdata()) ⌨️
[1, 43, 7, 13, 7, 1, 1, 85, 25, 85, 25, 1, 91, 103, 31, 37, 1, 13, 169, 1, 37, 13, 193, 13, 1, 193, 1, 103, 187, 121, 121, 1, 25, 25, 1, 7, 1, 121, 49, 1, 7, 19, 127, 169, 103, 7, 7, 1, 13, 37, 1, 7, 109, 1, 193, 7, 1, 193, 193, 13, 7, 13, 109, 7, 85, 13, 55, 1, 13, 1, 7, 1, 13, 7, 121, 7, 7, 7, 1, 7, 25, 1, 1, 7, 43, 157, 19, 31, 1, 1, 7, 25, 61, 163, 1, 1, 193, 1, 1, 7, 7, 25, 1, 1, 1, 7, 1, 7, 91, 1, 31, 193, 7, 31, 1, 7, 187, 61, 13, 1, 7, 7, 7, 1, 19, 7, 7, 13, 181, 1, 19, 163, 1, 43, 169, 13, 1, 7, 1, 1, 193, 1, 181, 19, 25, 109, 1, 7, 13, 13, 7, 7, 1, 157, 1, 13, 7, 1, 1, 193, 49, 1, 1, 157, 7, 31, 19, 13, 1, 19, 1, 61, 7, 13, 1, 1, 7, 193, 19, 1, 97, 7, 19, 157, 1, 115, 133, 7, 169, 19, 91, 1, 85, 7, 193, 193, 13, 67, 7, 1, 1, 193, 1, 163, 49, 1, 13, 1, 19, 1, 19, 7, 13, 7, 193, 103, 193, 1, 1, 19, 1, 19, 157, 19, 13, 19, 91, 37, 19, 157, 1, 1, 1, 13, 7, 193, 187, 1, 7, 19, 1, 13, 61, 61, 19, 127, 43, 13, 7, 1, 13, 13, 7, 1, 1, 1, 19, 1, 1, 109, 1, 13, 7, 1, 7, 103, 13, 7, 1, 1, 19, 19, 7, 193, 1, 1, 7, 13, 13, 31, 61, 1, 1, 49, 1, 181, 19, 31, 157, 163, 43, 1, 19, 127, 19, 19, 187, 7, 193, 1, 61, 1, 1, 1, 49, 1, 1, 13, 61, 1, 25, 13, 1, 1, 133, 181, 1, 1, 1, 85, 1, 1, 7, 103, 19, 7, 73, 193, 1, 7, 19, 1, 1, 1, 193, 19, 1, 7, 13, 37, 13, 7, 19, 7, 145, 7, 7, 1, 1, 1, 1, 1, 187, 1, 193, 121, 1, 19, 121, 1, 13, 13, 103, 7, 1, 157, 1, 43, 1, 1, 1, 127, 1, 7, 193, 103, 127, 1, 7, 1, 121, 61, 193, 7, 121, 163, 1, 7, 1, 1, 7, 1, 1, 7, 61, 121, 1, 1, 13, 175, 1, 7, 163, 121, 19, 13, 193, 1, 1, 19, 193, 151, 1, 181, 25, 1, 7, 1, 7, 1, 7, 1, 1, 187, 1, 181, 13, 19, 193, 103, 193, 1, 1, 31, 37, 1, 175, 7, 133, 19, 1, 193, 19, 97, 13, 1, 175, 7, 13, 7, 1, 67, 1, 1, 7, 13, 1, 7, 115, 169, 193, 61, 1, 193, 13, 1, 13, 97, 37, 13, 193, 1, 7, 13, 85, 1, 187, 1, 31, 13, 1, 193, 193, 31, 31, 193, 1, 1, 1, 1, 7, 13, 193, 193, 109, 175, 1, 19, 61, 1, 121, 1, 13, 19, 157, 37, 13, 193, 1, 19, 61, 13, 7, 13, 1, 13, 7, 13, 1, 1, 1, 151, 91, 169, 91, 13, 19, 1, 37, 1, 1, 7, 7, 7, 49, 7, 1, 175, 7, 1, 13, 13, 7, 193, 163, 61, 7, 79, 31, 13, 1, 163, 7, 49, 7, 13, 1, 169, 25, 19, 1, 67, 1, 151, 19, 91, 31, 193, 127, 103, 1, 19, 121, 193, 13, 121, 109, 67, 7, 145, 55, 13, 7, 97, 1, 61, 193, 1, 1, 55, 13, 1, 103, 133, 193, 7, 20, 25, 7, 121, 1, 43, 109, 1, 19, 1, 1, 1, 19, 7, 13, 43, 1, 115, 49, 19, 1, 1, 1, 1, 187, 193, 1, 1, 7, 1, 1, 1, 1, 61, 13, 193, 1, 25, 49, 7, 187, 19, 145, 49, 13, 175, 1, 13, 19, 37, 43, 19, 19, 193, 7, 1, 7, 1, 7, 7, 13, 1, 7, 31, 157, 1, 193, 1, 193, 157, 109, 145, 139, 19, 7, 19, 13, 13, 13, 13, 19, 1, 19, 181, 13, 61, 103, 1, 13, 1, 127, 187, 1, 7, 1, 19, 169, 1, 13, 13, 25, 13, 13, 19, 19, 19, 1, 193, 1, 13, 1, 37, 7, 31, 1, 7, 7, 13, 7, 13, 1, 25, 193, 1, 55, 25, 1, 7, 1, 7, 1, 1, 1, 1, 7, 1, 43, 1, 1, 37, 109, 1, 19, 7, 13, 19, 1, 13, 187, 1, 13, 187, 37, 31, 1, 1, 1, 97, 1, 25, 1, 1, 187, 7, 37, 13, 20, 1, 1, 187, 115, 13, 7, 7, 13, 25, 1, 193, 193, 181, 133, 1, 127, 7, 187, 1, 7, 25, 193, 145, 19, 1, 7, 1, 55, 19, 1, 7, 13, 7, 145, 25, 7, 133, 67, 1, 7, 55, 19, 19, 181, 43, 175, 1, 1, 25, 13, 13, 1, 7, 1, 1, 1, 1, 7, 133, 1, 13, 1, 193, 1, 1, 7, 1, 1, 19, 1, 1, 1, 157, 1, 7, 7, 19, 193, 1, 13, 193, 25, 7, 1, 1, 1, 13, 187, 127, 19, 61, 193, 1, 193, 7, 37, 31, 1, 19, 109, 151, 7, 121, 181, 1, 7, 13, 7, 19, 7, 133, 13, 193, 25, 13, 1, 1, 13, 163, 31, 7, 13, 37, 193, 1, 61, 1, 1, 49, 13, 193, 13, 103, 7, 7, 1, 25, 7, 1, 7, 1, 1, 7, 163, 1, 7, 1, 139, 49, 193, 19, 145, 1, 175, 193, 7, 49, 145, 19, 1, 13, 1, 13, 91, 19, 67, 151, 19, 19, 1, 1, 19, 1, 133, 7, 1, 19, 7, 7, 13, 73, 7, 7, 1, 55, 193, 1, 13, 193, 1, 163, 1, 13, 1, 7, 7, 1, 7, 37, 7, 1, 1, 25, 193, 13, 19, 37, 139, 169, 13, 1, 151, 13, 7, 13, 1, 7, 19, 13, 31, 139, 1, 61, 13, 7, 7, 7, 7, 193, 181, 25, 157, 1, 1, 133, 19, 19, 193, 1, 8, 193, 8, 8, 97, 8, 19, 8, 103, 8, 31, 8, 13, 8, 8, 1, 13, 19, 7, 13, 1, 169, 193, 1, 25, 103, 1, 1, 1, 61, 1, 13, 1, 7, 7, 1, 7, 1, 1, 49, 19, 157, 7, 127, 20, 13, 1, 7, 175, 7, 13, 61, 1, 19, 193, 13, 193, 103, 193, 37, 7, 7, 13, 103, 13, 103, 1, 175, 181, 181, 193, 1, 25, 19, 181, 1, 7, 61, 1, 7, 61, 157, 43, 1, 7, 25, 13, 7, 7, 187, 19, 1, 1, 1, 1, 163, 127, 7, 19, 19, 19, 13, 193, 7, 19, 7, 157, 13, 1, 7, 7, 13, 193, 1, 193, 151, 187, 91, 7, 1, 8, 55, 8, 85, 8, 8, 8, 13, 193, 1, 7, 1, 1, 91, 7, 193, 31, 1, 157, 193, 133, 193, 19, 7, 31, 19, 1, 25, 1, 133, 1, 1, 13, 163, 7, 1, 7, 37, 1, 151, 37, 1, 37, 1, 157, 13, 13, 7, 7, 13, 7, 1, 7, 103, 193, 43, 7, 7, 1, 193, 7, 7, 175, 193, 133, 7, 19, 13, 109, 1, 49, 19, 187, 31, 1, 7, 193, 1, 7, 1, 1, 1, 25, 133, 193, 19, 1, 1, 1, 1, 1, 7, 193, 1, 1, 1, 1, 139, 1, 1, 55, 37, 1, 7, 13, 151, 1, 1, 7, 7, 175, 139, 19, 187, 193, 7, 145, 13, 13, 37, 55, 169, 1, 1, 193, 193, 193, 1, 115, 175, 1, 121, 37, 1, 13, 19, 1, 7]
>>> im.histogram() ⌨️
[0, 1532, 232, 0, 0, 0, 0, 963, 189, 0, 0, 0, 0, 724, 329, 0, 0, 0, 0, 549, 243, 0, 0, 0, 0, 144, 424, 0, 0, 0, 0, 119, 328, 0, 0, 0, 0, 126, 339, 0, 0, 0, 0, 126, 357, 0, 0, 0, 0, 107, 225, 0, 0, 0, 0, 79, 609, 0, 0, 0, 0, 181, 356, 0, 0, 0, 0, 70, 298, 0, 0, 0, 0, 23, 164, 0, 0, 0, 0, 26, 354, 0, 0, 0, 0, 47, 341, 0, 0, 0, 0, 139, 257, 0, 0, 0, 0, 104, 505, 0, 0, 0, 0, 192, 224, 0, 0, 0, 0, 114, 310, 0, 0, 0, 0, 32, 183, 0, 0, 0, 0, 238, 198, 0, 0, 0, 0, 117, 327, 0, 0, 0, 0, 110, 342, 0, 0, 0, 0, 118, 342, 0, 0, 0, 0, 145, 323, 0, 0, 0, 0, 152, 324, 0, 0, 0, 0, 161, 323, 0, 0, 0, 0, 175, 317, 0, 0, 0, 0, 183, 317, 0, 0, 0, 0, 171, 337, 0, 0, 0, 0, 198, 318, 0, 0, 0, 0, 241, 283, 0, 0, 0, 0, 1348, 272, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> list(enumerate(im.histogram())) ⌨️
[(0, 0), (1, 1532), (2, 232), (3, 0), (4, 0), (5, 0), (6, 0), (7, 963), (8, 189), (9, 0), (10, 0), (11, 0), (12, 0), (13, 724), (14, 329), (15, 0), (16, 0), (17, 0), (18, 0), (19, 549), (20, 243), (21, 0), (22, 0), (23, 0), (24, 0), (25, 144), (26, 424), (27, 0), (28, 0), (29, 0), (30, 0), (31, 119), (32, 328), (33, 0), (34, 0), (35, 0), (36, 0), (37, 126), (38, 339), (39, 0), (40, 0), (41, 0), (42, 0), (43, 126), (44, 357), (45, 0), (46, 0), (47, 0), (48, 0), (49, 107), (50, 225), (51, 0), (52, 0), (53, 0), (54, 0), (55, 79), (56, 609), (57, 0), (58, 0), (59, 0), (60, 0), (61, 181), (62, 356), (63, 0), (64, 0), (65, 0), (66, 0), (67, 70), (68, 298), (69, 0), (70, 0), (71, 0), (72, 0), (73, 23), (74, 164), (75, 0), (76, 0), (77, 0), (78, 0), (79, 26), (80, 354), (81, 0), (82, 0), (83, 0), (84, 0), (85, 47), (86, 341), (87, 0), (88, 0), (89, 0), (90, 0), (91, 139), (92, 257), (93, 0), (94, 0), (95, 0), (96, 0), (97, 104), (98, 505), (99, 0), (100, 0), (101, 0), (102, 0), (103, 192), (104, 224), (105, 0), (106, 0), (107, 0), (108, 0), (109, 114), (110, 310), (111, 0), (112, 0), (113, 0), (114, 0), (115, 32), (116, 183), (117, 0), (118, 0), (119, 0), (120, 0), (121, 238), (122, 198), (123, 0), (124, 0), (125, 0), (126, 0), (127, 117), (128, 327), (129, 0), (130, 0), (131, 0), (132, 0), (133, 110), (134, 342), (135, 0), (136, 0), (137, 0), (138, 0), (139, 118), (140, 342), (141, 0), (142, 0), (143, 0), (144, 0), (145, 145), (146, 323), (147, 0), (148, 0), (149, 0), (150, 0), (151, 152), (152, 324), (153, 0), (154, 0), (155, 0), (156, 0), (157, 161), (158, 323), (159, 0), (160, 0), (161, 0), (162, 0), (163, 175), (164, 317), (165, 0), (166, 0), (167, 0), (168, 0), (169, 183), (170, 317), (171, 0), (172, 0), (173, 0), (174, 0), (175, 171), (176, 337), (177, 0), (178, 0), (179, 0), (180, 0), (181, 198), (182, 318), (183, 0), (184, 0), (185, 0), (186, 0), (187, 241), (188, 283), (189, 0), (190, 0), (191, 0), (192, 0), (193, 1348), (194, 272), (195, 0), (196, 0), (197, 0), (198, 0), (199, 0), (200, 0), (201, 0), (202, 0), (203, 0), (204, 0), (205, 0), (206, 0), (207, 0), (208, 0), (209, 0), (210, 0), (211, 0), (212, 0), (213, 0), (214, 0), (215, 0), (216, 0), (217, 0), (218, 0), (219, 0), (220, 0), (221, 0), (222, 0), (223, 0), (224, 0), (225, 0), (226, 0), (227, 0), (228, 0), (229, 0), (230, 0), (231, 0), (232, 0), (233, 0), (234, 0), (235, 0), (236, 0), (237, 0), (238, 0), (239, 0), (240, 0), (241, 0), (242, 0), (243, 0), (244, 0), (245, 0), (246, 0), (247, 0), (248, 0), (249, 0), (250, 0), (251, 0), (252, 0), (253, 0), (254, 0), (255, 0)]
>>> sum([x for x in im.histogram() if x != 0][:-2]) ⌨️
17424

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
from PIL import Image
import math

# Open the input image 'beer2.png'
im = Image.open('beer2.png')

# Get all pixel values from the image as a list
data = list(im.getdata())

out = None  # Will hold the output image in each loop iteration

# Loop 33 times, progressively filtering pixel data
for i in range(33):
    # Find the current maximum pixel value in the data
    max_value = max(data)
    
    # Remove all pixels that are near the current maximum brightness (max_value - 1 and above)
    # This effectively strips the brightest pixels in each iteration
    data = [x for x in data if x < max_value - 1]
    
    # Print how many pixels remain after filtering
    print(len(data))
    
    # Compute side length of a square image from remaining pixel count
    l = int(math.sqrt(len(data)))
    
    # Create a new grayscale image ('L' mode) with dimensions (l x l)
    out = Image.new('L', (l, l))
    
    # Fill the new image with the current pixel data
    out.putdata(data)
    
    # Display the resulting image — each iteration reveals a progressively darker layer
    # out.show()
    
    # Save each intermediate image to disk for inspection
    out.save(f'beer2_layer_{i}.png')

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
17424
16900
16384
15876
15376
14884
14400
13924
13456
12996
12544
12100
11664
11449
11025
10609
10000
9604
9216
8836
8649
8281
7744
7056
6724
6241
5776
5329
4761
3969
2916
1764
0
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/PIL/ImageFile.py", line 554, in _save
    fh = fp.fileno()
AttributeError: '_idat' object has no attribute 'fileno'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/./pythonScript.py", line 38, in <module>
    out.save(f'beer2_layer_{i}.png')
  File "/usr/local/lib/python3.10/dist-packages/PIL/Image.py", line 2596, in save
    save_handler(self, fp, filename)
  File "/usr/local/lib/python3.10/dist-packages/PIL/PngImagePlugin.py", line 1488, in _save
    ImageFile._save(
  File "/usr/local/lib/python3.10/dist-packages/PIL/ImageFile.py", line 558, in _save
    _encode_tile(im, fp, tile, bufsize, None, exc)
  File "/usr/local/lib/python3.10/dist-packages/PIL/ImageFile.py", line 576, in _encode_tile
    encoder.setimage(im.im, extents)
SystemError: tile cannot extend outside image

AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
beer2.png           beer2_layer_13.png  beer2_layer_19.png  beer2_layer_24.png  beer2_layer_3.png   beer2_layer_7.png   tmp27y8_peq.PNG  tmp88_6yor_.PNG  tmpg2cvy7vf.PNG  tmpk25hyda1.PNG  tmprn7f0mxr.PNG  tmpy01889i0.PNG
beer2_layer_0.png   beer2_layer_14.png  beer2_layer_2.png   beer2_layer_25.png  beer2_layer_30.png  beer2_layer_8.png   tmp6jm2w_49.PNG  tmp_56sxn1q.PNG  tmphain860a.PNG  tmplua8wswe.PNG  tmps4toltbg.PNG  tmpymoawtph.PNG
beer2_layer_1.png   beer2_layer_15.png  beer2_layer_20.png  beer2_layer_26.png  beer2_layer_31.png  beer2_layer_9.png   tmp6kmq68hh.PNG  tmp_lr644j4.PNG  tmphnl25a7x.PNG  tmplucg80ck.PNG  tmpvf_jdrua.PNG  tmpyx55lrc9.PNG
beer2_layer_10.png  beer2_layer_16.png  beer2_layer_21.png  beer2_layer_27.png  beer2_layer_4.png   hsperfdata_root     tmp6r4ctcj8.PNG  tmpbxuxsuhv.PNG  tmpii3g8cp9.PNG  tmpod794mhu.PNG  tmpx4hz6ngn.PNG
beer2_layer_11.png  beer2_layer_17.png  beer2_layer_22.png  beer2_layer_28.png  beer2_layer_5.png   node-compile-cache  tmp7tdklex9.PNG  tmpewr1875f.PNG  tmpjn5r2i8v.PNG  tmpofxvabem.PNG  tmpx74teddu.PNG
beer2_layer_12.png  beer2_layer_18.png  beer2_layer_23.png  beer2_layer_29.png  beer2_layer_6.png   pythonScript.py     tmp84qynlqu.PNG  tmpg10rj7wc.PNG  tmpjt9jlrng.PNG  tmppubz456_.PNG  tmpxoayy9g7.PNG
AsianHacker-picoctf@webshell:/tmp$ sz beer2_*

Think: Open all the images but notice some have boxes around them
Browser: http://www.pythonchallenge.com/pc/rock/gremlins.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/rock/gremlins.html

## Continue
[Continue](../overthewire/Bandit0000.md)
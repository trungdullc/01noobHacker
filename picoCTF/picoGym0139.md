# picoGym Level 139: Milkslap
Source: https://play.picoctf.org/practice/challenge/139

## Goal
http://mercury.picoctf.net:48380/

## What I learned
```
PNG file, which works as a “GIF” when you move your mouse
zsteg
stegsolve

Ctrl + I
  Sources → concat_v.png
  Right Click: Save Image as ...
```

## Solution
```
https://webshell.picoctf.org/

# View Page Source
Browser: view-source:mercury.picoctf.net:48380/ ⌨️
<!doctype html>

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=400" />
  <title>🥛</title>
  <link rel="stylesheet" href="style.css" />👀

</head>
<body>
  <div id="image" class="center"></div>
  <div id="foot" class="center">
    <h1>MilkSlap!</h1>
    Inspired by <a href="http://eelslap.com">http://eelslap.com</a> <br>
    Credit to: <a href="https://github.com/boxmein">boxmein</a> for code inspiration.
  </div>
  <script src="script.js">👀
</script>
</body>
</html>

Browser: http://mercury.picoctf.net:48380/script.js ⌨️
var currentX = 0;
var tweenedPageX = 0;
var background_y = 0;
var frame_num = 0;
var background_max = 46800;
var image = document.getElementById("image");
var image_bcr = image.getBoundingClientRect();
var image_right_coord = 0;
var image_left_coord = 0;
var mouse_depth = 0;
var frame_ht = 720;
var mousepct = 0;
var frameinterval =  0.016;
var totalX = window.outerWidth;

function animate(e){
  image_right_coord = image_bcr.right;
  image_left_coord = image_bcr.left;
  currentX = e.x;
  mouse_depth = Math.max(image_right_coord - currentX, 0);

  mousepct = mouse_depth / image_bcr.width;  
  frame_num = Math.round(mousepct / frameinterval);

  background_y = -1 * frame_ht * (frame_num + 1);
  image.style.backgroundPositionY = background_y.toString() + "px";
}

function touch_animate(e){
  image_right_coord = image_bcr.right;
  image_left_coord = image_bcr.left;
  currentX = e.touches[0].clientX;
  mouse_depth = Math.max(image_right_coord - currentX, 0);

  mousepct = mouse_depth / image_bcr.width;
  
  frame_num = Math.round(mousepct / frameinterval);
  
  background_y = -1 * frame_ht * (frame_num + 1);
  image.style.backgroundPositionY = background_y.toString() + "px";
}

image.onmousemove = animate;
image.ontouchmove = touch_animate;

Browser: http://mercury.picoctf.net:48380/style.css ⌨️
/* source: milkslap-milkslap.scss */
body {
  margin: 0;
  padding: 0;
  overflow: hidden; }

a {
  color: inherit; }

.center {
  width: 1080px;
  height: 720px;
  margin: 0 auto; }

#image {
  height: 720px;
  margin-top: 5%;
  margin-bottom: 20px;
  background-image: url(concat_v.png); 👀
  background-position: 0 0; }

#foot {
  margin-bottom: 5px;
  color: #999999; }
  #foot h1 {
    font-family: serif;
    font-weight: normal;
    font-size: 1rem;
    text-align: center; }

AsianHacker-picoctf@webshell:~$ curl http://mercury.picoctf.net:48380/concat_v.png --output concat_v.png ⌨️
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 17.2M  100 17.2M    0     0  1856k      0  0:00:09  0:00:09 --:--:-- 1867k

AsianHacker-picoctf@webshell:~$ strings concat_v.png | grep "picoCTF" ⌨️
AsianHacker-picoctf@webshell:~$ exiftool concat_v.png ⌨️
ExifTool Version Number         : 12.40
File Name                       : concat_v.png
Directory                       : .
File Size                       : 17 MiB
File Modification Date/Time     : 2025:09:17 18:24:24+00:00
File Access Date/Time           : 2025:09:17 18:24:33+00:00
File Inode Change Date/Time     : 2025:09:17 18:24:24+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1280
Image Height                    : 47520
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1280x47520
Megapixels                      : 60.8
AsianHacker-picoctf@webshell:~$ zsteg concat_v.png ⌨️
Killed ⚠️

# Note: was suppose to give this info from zsteg but online console not enough memory
imagedata           .. file: dBase III DBT, version number 0, next free block index 3368931841, 1st item "\001\001\001\001"
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n" 🔐
b1,bgr,lsb,xy       .. <wbStego size=9706075, data="\xB6\xAD\xB6}\xDB\xB2lR\x7F\xDF\x86\xB7c\xFC\xFF\xBF\x02Zr\x8E\xE2Z\x12\xD8q\xE5&MJ-X:\xB5\xBF\xF7\x7F\xDB\xDFI\bm\xDB\xDB\x80m\x00\x00\x00\xB6m\xDB\xDB\xB6\x00\x00\x00\xB6\xB6\x00m\xDB\x12\x12m\xDB\xDB\x00\x00\x00\x00\x00\xB6m\xDB\x00\xB6\x00\x00\x00\xDB\xB6mm\xDB\xB6\xB6\x00\x00\x00\x00\x00m\xDB", even=true, mix=true, controlbyte="[">
b2,r,lsb,xy         .. file: SoftQuad DESC or font file binary
b2,r,msb,xy         .. file: VISX image file
b2,g,lsb,xy         .. file: VISX image file
b2,g,msb,xy         .. file: SoftQuad DESC or font file binary - version 15722
b2,b,msb,xy         .. text: "UfUUUU@UUU"
b4,r,lsb,xy         .. text: "\"\"\"\"\"#4D"
b4,r,msb,xy         .. text: "wwww3333"
b4,g,lsb,xy         .. text: "wewwwwvUS"
b4,g,msb,xy         .. text: "\"\"\"\"DDDD"
b4,b,lsb,xy         .. text: "vdUeVwweDFw"
b4,b,msb,xy         .. text: "UUYYUUUUUUUU"

# Method 2: stegsolve

# Method 3: Aperi'Solve
```

## Flag
picoCTF{imag3_m4n1pul4t10n_sl4p5}

## Continue
[Continue](./picoGym0279.md)
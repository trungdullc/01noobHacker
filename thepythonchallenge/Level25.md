# Level 25

## Previous Flag
```
http://www.pythonchallenge.com/pc/hex/lake.html
```

## Goal
Given image of a puzzle above a mountain and lake scene

## What I learned
```
$ for i in {1..25}; do wget --user butter --password fly http://www.pythonchallenge.com/pc/hex/lake$i.wav; done

There are 25 WAV files, each containing raw audio data
Each WAV file is being interpreted as raw RGB bytes and turned into a 60x60 pixel image
These 25 images are then arranged in a 5x5 grid to form a single 300x300 image
The final image answer.png reveals a picture hidden in the audio data
Essentially, this script treats audio samples as pixel data to reconstruct a hidden image
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/hex/lake.html

View Page Source

<html>
<head>
  <title>imagine how they sound</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<br>
<br>
<img src="lake1.jpg"> <!-- can you see the waves? --> 👀
</body>
</html>

Browser: http://www.pythonchallenge.com/pc/hex/lake1.wav ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget --user butter --password fly http://www.pythonchallenge.com/pc/hex/lake1.wav ⌨️
--2025-10-17 23:29:54--  http://www.pythonchallenge.com/pc/hex/lake1.wav
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="pluses and minuses"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 10844 (11K) [audio/x-wav]
Saving to: 'lake1.wav'

lake1.wav                                                 100%[=====================================================================================================================================>]  10.59K  --.-KB/s    in 0.003s  

2025-10-17 23:29:54 (3.57 MB/s) - 'lake1.wav' saved [10844/10844]

# Now need do 25 more times since there is 25 puzzle pieces
# Note: bash $i similar to python %d
AsianHacker-picoctf@webshell:/tmp$ for i in {1..25}; do wget --user butter --password fly http://www.pythonchallenge.com/pc/hex/lake$i.wav; done ⌨️ ❤️❤️❤️❤️❤️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️     
hsperfdata_root  lake1.wav.1  lake11.wav  lake13.wav  lake15.wav  lake17.wav  lake19.wav  lake20.wav  lake22.wav  lake24.wav  lake3.wav  lake5.wav  lake7.wav  lake9.wav
lake1.wav        lake10.wav   lake12.wav  lake14.wav  lake16.wav  lake18.wav  lake2.wav   lake21.wav  lake23.wav  lake25.wav  lake4.wav  lake6.wav  lake8.wav  node-compile-cache

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from PIL import Image
import wave                             # reading and writing WAV audio

# Open 25 WAV files named lake1.wav, lake2.wav, ..., lake25.wav
wavs = [wave.open('lake%d.wav' % i) for i in range(1,26)]

# Create a new blank RGB image of size 300x300 pixels (5 * 60)
result = Image.new('RGB', (300,300), 0)

# Get the number of frames (samples) in the first WAV file
num_frames = wavs[0].getnframes()

# Loop through each WAV file
for i in range(len(wavs)):
    # Read all frames from the WAV file as bytes
    byte = wavs[i].readframes(num_frames)
    
    # Convert the byte data into a 60x60 RGB image
    img = Image.frombytes('RGB', (60, 60), byte)
    
    # Paste this small image into the correct position in the 300x300 grid
    # (i % 5) gives the column, (i // 5) gives the row
    result.paste(img, (60 * (i % 5), 60 * (i // 5)))

# Save the final 300x300 image that combines all 25 small images
result.save('answer.png')

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
answer.png 👀    lake1.wav    lake10.wav  lake12.wav  lake14.wav  lake16.wav  lake18.wav  lake2.wav   lake21.wav  lake23.wav  lake25.wav  lake4.wav  lake6.wav  lake8.wav  node-compile-cache
hsperfdata_root  lake1.wav.1  lake11.wav  lake13.wav  lake15.wav  lake17.wav  lake19.wav  lake20.wav  lake22.wav  lake24.wav  lake3.wav   lake5.wav  lake7.wav  lake9.wav  pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ sz answer.png ⌨️

# Think: Open the png to see spray painted decent on top
Browser: http://www.pythonchallenge.com/pc/hex/decent.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/hex/decent.html

## Continue
[Continue](./Level26.md)
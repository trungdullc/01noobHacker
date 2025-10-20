# Level 26

## Previous Flag
```
http://www.pythonchallenge.com/pc/hex/decent.html
```

## Goal
Given Image of 2 monkies<br>
Hurry up, I'm missing the boat 👀

## What I learned
```
The error ModuleNotFoundError: No module named 'md5' appears because Python 3 removed the old md5 module (and changed string/byte handling)
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/hex/decent.html

View Page Source
<html>
<head>
  <title>be a man - apologize!</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<br>
<img src="decent.jpg"> <!-- you've got his e-mail -->
<br><br><font color="gold"/>
Hurry up, I'm missing the boat
</font>
</body>
</html>

<!--
Join us at the IRC: irc.freenode.net #pythonchallenge
-->

# Remember: Johann Georg Leopold Mozart is Mozart's Dad
# Note: I would have never got the email correct
AsianHacker-picoctf@webshell:~$ echo Sorry | mail -s Sorry leopold.moz@pythonchallenge.com ⌨️
-bash: mail: command not found ⚠️

# Suppose to get a reply back (I cheated on this, used a writeup) ⚠️⚠️⚠️⚠️⚠️
From: leopold.moz@pythonchallenge.com Subject: Re: sorry Date:

Never mind that.

Have you found my broken zip?

md5: bbb8b499a0eef99b52c7f13f4e78c24b 👀

Can you believe what one mistake can lead to?

# From Level 24 the maze
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  maze.png  maze.zip  node-compile-cache  pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ unzip maze.zip ⌨️ 
Archive:  maze.zip
  inflating: maze.jpg                
 extracting: mybroken.zip            
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
hsperfdata_root  maze.jpg  maze.png  maze.zip  mybroken.zip  node-compile-cache  pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ file mybroken.zip ⌨️ 
mybroken.zip: Zip archive data, at least v2.0 to extract, compression method=deflate
AsianHacker-picoctf@webshell:/tmp$ sz mybroken.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ unzip mybroken.zip ⌨️ 
Archive:  mybroken.zip
  inflating: mybroken.gif             bad CRC 31eddaa4  (should be 383782e7)

Method 1 ChatGPT doesn't even need md5 (probably wrong way to do this bypass CRC):
AsianHacker-picoctf@webshell:/tmp$ zip -FF mybroken.zip --out fixed.zip ⌨️
Fix archive (-FF) - salvage what can
 Found end record (EOCDR) - says expect single disk archive
Scanning for entries...
 copying: mybroken.gif  (2545 bytes)
Central Directory found...
EOCDR found ( 1   2679)...
AsianHacker-picoctf@webshell:/tmp$ unzip fixed.zip ⌨️
Archive:  fixed.zip
replace mybroken.gif? [y]es, [n]o, [A]ll, [N]one, [r]ename: n ⌨️
AsianHacker-picoctf@webshell:/tmp$ sz mybroken.gif ⌨️

# Think: Open the gif see: speed
# Combine the clue speed + boat = speedboat 

Browser: http://www.pythonchallenge.com/pc/hex/speedboat.html 🔐

# Method 2
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
"""
Python3 version of the original repair script.
It tries changing one byte at a time until the file's MD5 matches the target.
"""

import hashlib

def sub(data: bytearray, good_md5: str) -> bool:
    """
    Try replacing each byte in `data` with every possible byte value 0..255.
    If the MD5 of the whole buffer matches good_md5, return True (data mutated in-place).
    If not found, revert changed byte and continue; return False if no single-byte change matched.
    """
    n = len(data)
    for i in range(n):
        old = data[i]
        # try all possible byte values
        for new_byte in range(256):
            if new_byte == old:
                continue
            data[i] = new_byte
            if hashlib.md5(data).hexdigest() == good_md5:
                print(f"Found match by changing byte {i} from {old} to {new_byte}")
                return True
        # revert and continue
        data[i] = old
    return False

if __name__ == "__main__":
    ZIP_IN = "mybroken.zip"
    ZIP_OUT = "repaired.zip"
    TARGET_MD5 = "bbb8b499a0eef99b52c7f13f4e78c24b"

    # load file as mutable bytes
    data = bytearray(open(ZIP_IN, "rb").read())
    print(f"Loaded {ZIP_IN}, {len(data)} bytes. Starting brute-force...")

    found = sub(data, TARGET_MD5)
    if found:
        with open(ZIP_OUT, "wb") as f:
            f.write(data)
        print(f"Wrote repaired file to {ZIP_OUT}")
    else:
        print("No single-byte change produced the target MD5.")

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
Loaded mybroken.zip, 2701 bytes. Starting brute-force...
Found match by changing byte 1234 from 45 to 168
Wrote repaired file to repaired.zip
AsianHacker-picoctf@webshell:/tmp$ unzip repaired.zip 
Archive:  repaired.zip
  inflating: mybroken.gif            
AsianHacker-picoctf@webshell:/tmp$ sz mybroken.gif ⌨️
```

## Flag
http://www.pythonchallenge.com/pc/hex/speedboat.html

## Continue
[Continue](./Level27.md)
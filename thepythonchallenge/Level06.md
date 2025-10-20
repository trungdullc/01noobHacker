# Level 06

## Previous Flag
```
http://www.pythonchallenge.com/pc/def/channel.html
```

## Goal
Picture of a zipper

## What I learned
```
decode('utf-8')         not needed unless you open in binary mode ("rb")
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/def/channel.html

View Page Source

<html> <!-- <-- zip --> 👀
<head>
  <title>now there are pairs</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="channel.jpg">
<br/>
<!-- The following has nothing to do with the riddle itself. I just
thought it would be the right point to offer you to donate to the
Python Challenge project. Any amount will be greatly appreciated.

-thesamet
-->

<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
    <input type="hidden" name="cmd" value="_xclick">
    <input type="hidden" name="business" value="thesamet@gmail.com">
    <input type="hidden" name="item_name" value="Python Challenge donations">
    <input type="hidden" name="no_note" value="1">
    <input type="hidden" name="currency_code" value="USD">
    <input type="hidden" name="tax" value="0">
    <input type="hidden" name="bn" value="PP-DonationsBF">
    <input type="image" src="https://www.paypal.com/en_US/i/btn/x-click-but04.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
    <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>

</body>
</html>

Think: convert html to zip
AsianHacker-picoctf@webshell:~$ wget http://www.pythonchallenge.com/pc/def/channel.zip ⌨️
--2025-10-13 20:03:48--  http://www.pythonchallenge.com/pc/def/channel.zip 
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 107146 (105K) [application/zip]
Saving to: 'channel.zip'

channel.zip                                               100%[=====================================================================================================================================>] 104.63K  --.-KB/s    in 0.1s    

2025-10-13 20:03:49 (739 KB/s) - 'channel.zip' saved [107146/107146]

AsianHacker-picoctf@webshell:~$ unzip channel.zip ⌨️
Archive:  channel.zip
  inflating: 29.txt                  
  inflating: 100.txt                 
  inflating: 109.txt                 
  inflating: 176.txt                 
  inflating: 226.txt     
  ...
  ...
  inflating: 99714.txt               
  inflating: 99775.txt               
  inflating: 99905.txt               
  inflating: readme.txt

AsianHacker-picoctf@webshell:~$ cat readme.txt ⌨️
welcome to my zipped list.

hint1: start from 90052 👀
hint2: answer is inside the zip

AsianHacker-picoctf@webshell:~$ cat 90052.txt ⌨️
Next nothing is 94191 👀
AsianHacker-picoctf@webshell:~$ cat 94191.txt ⌨️
Next nothing is 85503 👀

AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3

"""
# with open("90052.txt", "r") as first:
first = open("90052.txt", "r")

contents = first.read()
first.close()
print(contents)
"""

def next_nothing(filename):
    handle = open(filename, "r")
    contents = handle.read()
    handle.close()
    next = contents.split(" ")[-1]
    print(next)
    next_nothing(next + ".txt")                          # recursive until crash

next_nothing("90052.txt")

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
68628
67824
46145 👀
comments.
Traceback (most recent call last):
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 20, in <module>
    next_nothing("90052.txt")
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 18, in next_nothing
    next_nothing(next + ".txt")                          # recursive until crash
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 18, in next_nothing
    next_nothing(next + ".txt")                          # recursive until crash
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 18, in next_nothing
    next_nothing(next + ".txt")                          # recursive until crash
  [Previous line repeated 906 more times]
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 13, in next_nothing
    handle = open(filename, "r")
FileNotFoundError: [Errno 2] No such file or directory: 'comments..txt'

AsianHacker-picoctf@webshell:~$ cat 46145.txt ⌨️
Collect the comments 👀

ChatGPT: 
A ZIP file can have comments in two ways:
    1. Global (archive) comment
        Entire ZIP archive can have one comment stored at end of the file in the End of Central Directory (EOCD) record
    2. Per-file comments
        Each individual file inside the ZIP can also have its own comment.

# Need collect comments with zipfile module
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import zipfile

comments = []
the_zip = zipfile.ZipFile("channel.zip")

def next_nothing(filename):
    with the_zip.open(filename) as handle:
        contents = handle.read().decode('utf-8')
    comments.append(the_zip.getinfo(filename).comment.decode('utf-8'))
    parts = contents.strip().split(" ")
    next = parts[-1]
    if next.isdigit():
        next_nothing(next + ".txt")

next_nothing("90052.txt")
print("".join(comments))

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************

Browser: http://www.pythonchallenge.com/pc/def/hockey.html ⌨️
it's in the air. look at the letters. 👀

Browser: http://www.pythonchallenge.com/pc/def/oxygen.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/def/oxygen.html

## Continue
[Continue](./Level06.md)
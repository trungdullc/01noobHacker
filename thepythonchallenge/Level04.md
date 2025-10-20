# Level 04

## Previous Flag
```
http://www.pythonchallenge.com/pc/def/linkedlist.php
```

## Goal
Given a useless picture<br>
Title: follow the chain

## What I learned
```
from urllib.request import urlopen

# Fetch the page
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
page = urlopen(url)
contents = page.read().decode('utf-8')
page.close()
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/def/linkedlist.php

View Page Source

<html>
<head>
  <title>follow the chain</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->
<center>
<a href="linkedlist.php?nothing=12345">👀<img src="chainsaw.jpg" border="0"/></a>
<br><br><font color="gold"></center>
Solutions to previous levels: <a href="http://wiki.pythonchallenge.com/"/>Python Challenge wiki</a>.
<br><br>
IRC: irc.freenode.net #pythonchallenge
</body>
</html>

Think: Can click on image
We got <a href="linkedlist.php?nothing=12345"
Browser: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345 ⌨️
and the next nothing is 44827 👀

Browser: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827 ⌨️
and the next nothing is 45439 👀

Note: Probably wants us to do this 400 times

Method 1 until crash:
#!/usr/bin/python3

from urllib.request import urlopen

# Fetch the page
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
page = urlopen(url)
contents = page.read().decode('utf-8')
page.close()

# print(contents)

link_start = 'a href="'
link_end = '"'

next = contents.split(link_start)[1].split(link_end)[0][23:]
# print(next)

def go_to_new_nothing( next ):
  new_url = url + "?nothing=" + next
  page = urlopen(new_url)
  contents = page.read().decode('utf-8')
  page.close()
  # print(contents)
  return contents.split()[-1]

optional_counter = 0

while (next == str(int(next))):
  next = go_to_new_nothing(next)
  optional_counter += 1
  print(str(optional_counter) + ": " + next)

AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
84: 3875
85: 16044
86: going. 👀
Traceback (most recent call last):
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 38, in <module>
    while (next == str(int(next))):
ValueError: invalid literal for int() with base 10: 'going.'

Method 1: from crash to end

Browser: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044 ⌨️
Yes. Divide by two and keep going. 👀

AsianHacker-picoctf@webshell:~$ cat pythonScript.py 
#!/usr/bin/python3

from urllib.request import urlopen

# Fetch the page
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
page = urlopen(url)
contents = page.read().decode('utf-8')
page.close()

# print(contents)

link_start = 'a href="'
link_end = '"'

# next = contents.split(link_start)[1].split(link_end)[0][23:] 👀
# print(next)

# Continue from crash
next = str((16044//2))                       # str(int(16044/2)) 👀

def go_to_new_nothing( next ):
  new_url = url + "?nothing=" + next
  page = urlopen(new_url)
  contents = page.read().decode('utf-8')
  page.close()
  # print(contents)
  return contents.split()[-1]

# Changed
optional_counter = 86 👀

while (next == str(int(next))):
  next = go_to_new_nothing(next)
  optional_counter += 1
  print(str(optional_counter) + ": " + next)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
245: 23298
246: 27709
247: 96791
248: 75635
249: 52899
250: 66831
251: peak.html 👀
Traceback (most recent call last):
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 34, in <module>
    while (next == str(int(next))):
ValueError: invalid literal for int() with base 10: 'peak.html'

Browser: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831 ⌨️
peak.html 👀

Browser: http://www.pythonchallenge.com/pc/def/peak.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/def/peak.html 

## Continue
[Continue](./Level05.md)
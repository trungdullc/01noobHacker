# Level 23

## Previous Flag
```
http://www.pythonchallenge.com/pc/hex/bonus.html
```

## Goal
Given a image of a cow staring at grass

## What I learned
```
Caesar Cipher
In Python 2, you could do 'string'.decode('rot13') because strings were byte sequences
In Python 3, text (str) and binary data (bytes) are distinct types
Therefore, .decode() is only for bytes objects — not str
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/hex/bonus.html

View Page Source

<!--
TODO: do you owe someone an apology? now it is a good time to
tell him that you are sorry. Please show good manners although
it has nothing to do with this level.
-->
<html>
<head>
  <title>what is this module?</title> 👀👀👀👀👀
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<br>
<br>
<img src="bonus.jpg"> 
<!-- 	it can't find it. this is an undocumented module. -->
</body>
</html>

<!--
'va gur snpr bs jung?'👀
-->

AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> codecs.decode('va gur snpr bs jung?', 'rot_13')
'in the face of what?' 👀
>>> print('va gur snpr bs jung?'.translate(str.maketrans(
...     'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
...     'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
... )))
in the face of what? 👀

Think: cow looking at grass
Google: python grass
https://grasswiki.osgeo.org/wiki/GRASS_and_Python   # Note: not it

Google: this module
AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> import this ⌨️
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess. 👀
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

Browser: http://www.pythonchallenge.com/pc/hex/ambiguity.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/hex/ambiguity.html

## Continue
[Continue](./Level24.md)
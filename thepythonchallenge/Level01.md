# Level 01

## Previous Flag
```
http://www.pythonchallenge.com/pc/def/274877906944.html
```

## Goal
Picture of:<br>
K → M<br>
O → Q<br>
E → G<br><br>

everybody thinks twice before solving this.<br>

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

## What I learned
```
ROT24
SHIFT by 2

dir(str)                        lists all attributes and methods available for Python’s built-in str type
help(str.replace)               shows the documentation for the replace() method

ord(): character to integer
chr(): integer to character

shifted = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
table: Dict[int, str] = str.maketrans(string.ascii_lowercase, shifted)
    string.ascii_lowercase →                                    'abcdefghijklmnopqrstuvwxyz'
    string.ascii_lowercase[2:] + string.ascii_lowercase[:2] →   'cdefghijklmnopqrstuvwxyzab'
    str.maketrans(a, b) maps each a[i] → b[i]                   'a'→'c', 'b'→'d', 'c'→'e', ..., 'y'→'a', 'z'→'b'
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/def/274877906944.html
Note: url got redirected
Browser: http://www.pythonchallenge.com/pc/def/map.html

Think: Replace/Substitute the 3 letters in python

Incorrect Method 1:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3

code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

code = code.replace("k", "m")
code = code.replace("o", "q")
code = code.replace("e", "g")

print(code)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr ammnsrcpq ypc dmp. bmglg gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmlg. sqglg qrpglg.myicrpylq() gq pcammmclbcb. lmu ynnjw ml rfc spj.

AsianHacker-picoctf@webshell:~$ python3 ⌨️
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> dir(str) ⌨️❤️❤️❤️❤️❤️
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans' 👀, 'partition', 'removeprefix', 'removesuffix', 'replace' 👀, 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.replace) ⌨️❤️❤️❤️❤️❤️

Help on method_descriptor:

replace(self, old, new, count=-1, /)
    Return a copy with all occurrences of substring old replaced by new.
    
      count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.
    
    If the optional argument count is given, only the first count occurrences are
    replaced.

Incorrect Method 2: manually do it
AsianHacker-picoctf@webshell:~$ cat ./pythonScript.py ⌨️
#!/usr/bin/python3

code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for letter in code:
    if letter == "k":
        print("m", end="")
    elif letter == "o":
        print("q", end="")
    elif letter == "e":
        print("g", end="")
    else:
        print(letter, end="")

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr ammnsrcpq ypc dmp. bmglg gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmlg. sqglg qrpglg.myicrpylq() gq pcammmclbcb. lmu ynnjw ml rfc spj.

Incorrect Method 3:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3
from typing import Dict

code: str = (
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. "
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
)

# Create translation table (maps Unicode code points to new characters)
table: Dict[int, str] = str.maketrans({
    "k": "m",
    "o": "q",
    "e": "g"
})

# Apply the translation
code = code.translate(table)
print(code)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr ammnsrcpq ypc dmp. bmglg gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmlg. sqglg qrpglg.myicrpylq() gq pcammmclbcb. lmu ynnjw ml rfc spj.

Incorrect Method 4:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️ 
#!/usr/bin/python3

code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# ord() gives you the Unicode code point (integer)
# chr() turns it back into a character
for letter in code:
    if letter not in (" ", ".", "(", ")"):
        print(chr(ord(letter) + 2), end="")
    else:
        print(letter, end="")

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
i hope you didnt tr{nsl{te it |y h{nd. th{ts wh{t computers {re for. doing it in |y h{nd is inefficient {nd th{t)s why this text is so long. using string.m{ketr{ns() is recommended. now {pply on the url.

Method 1: Lazy
Google: Rot7
https://www.cachesleuth.com/rot.html            See all ROT
Under ROT24:
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

https://www.dcode.fr/rot-cipher
Rotation to use ROT-N, N= 24
DECRYPT

i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

AsianHacker-picoctf@webshell:~$ python3 -q ⌨️❤️
>>> help(str.maketrans) ⌨️❤️

Help on built-in function maketrans:

maketrans(...)
    Return a translation table usable for str.translate().
    
    If there is only one argument, it must be a dictionary mapping Unicode
    ordinals (integers) or characters to Unicode ordinals, strings or None.
    Character keys will be then converted to ordinals.
    If there are two arguments, they must be strings of equal length, and
    in the resulting dictionary, each character in x will be mapped to the
    character at the same position in y. If there is a third argument, it
    must be a string, whose characters will be mapped to None in the result.

Method 2:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import string
from typing import Dict

# Original text
code: str = (
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. "
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
)

# Build Caesar cipher translation table (+2 shift)
shifted = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
table: Dict[int, str] = str.maketrans(string.ascii_lowercase, shifted)

# Apply translation
decoded = code.translate(table)

print(decoded)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

How to solve:
It says apply to the url that got changed in the browser. url = map. Answer is to shift it by 2 letters and apply to url
http://www.pythonchallenge.com/pc/def/ocr.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/def/ocr.html

## Continue
[Continue](./Level02.md)
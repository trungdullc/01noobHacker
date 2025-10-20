# Level 17

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/romance.html
```

## Goal
Given picture of cookies and past challenge: follow the chain 04 bottom left corner

## What I learned
```
Python 2 the urllib module changed in Python 3
Python 3 urllib is split into submodules and unquote_plus moved to urllib.parse
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/romance.html 🔐

View Page Source

<html>
<head>
  <title>eat?</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold">
	<img src="cookies.jpg" border="0"/>
</body>
</html>

Browser: http://www.pythonchallenge.com/pc/return/cookies.html ⌨️
yummy! chocolate chips.

Browser: http://www.pythonchallenge.com/pc/return/chocolate.html ⌨️
do you want to eat or to play?

Browser: http://www.pythonchallenge.com/pc/return/eat.html ⌨️
then go back and play.

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests

url = "http://www.pythonchallenge.com/pc/return/romance.html"
auth = ("huge", "file")
response = requests.get(url, auth=auth)             # Note: auth= part required can't use auth

print(response.text)                                # curl -i <url>
print(response)                                     # <Response [200]>
print(dir(response))
print(response.cookies)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
<Response [200]>
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

# Note: Returned no cookies try other level ⌨️
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
# auth = ("huge", "file")
response = requests.get(url)

print(response)                                     # <Response [200]>
print(response.cookies)
print(response.cookies["info"])

AsianHacker-picoctf@webshell:~$ chmod u+x pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
<Response [200]>
<RequestsCookieJar[<Cookie info=you%20should%20have%20followed%20busynothing... for .pythonchallenge.com/>]>
you%20should%20have%20followed%20busynothing...

# Think: Follow busynothing as suggested, start 12345
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345"
# auth = ("huge", "file")
response = requests.get(url)

print(response)                                     # <Response [200]>
print(response.cookies)
print(response.cookies["info"])
print(response.text)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py 
<Response [200]>
<RequestsCookieJar[<Cookie info=B for .pythonchallenge.com/>]>
B
If you came here from level 4 - go back!<br>You should follow the obvious chain...<br><br>and the next busynothing is 44827 👀

# Think: busynothing=44827
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests

# auth = ("huge", "file")
next_busy_nothing = "12345"
data = []

# Note: Python syntax __variable__ is place holder
# for i in range(3):
while True:
  try:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=__busynothing__"
    url = url.replace("__busynothing__", next_busy_nothing)
    response = requests.get(url)

    next_nothing = (str(response.text).split(" ")[-1])          # next url
    info = response.cookies["info"]                             # letter
    # print(response.cookies)
    print("next_busy_nothing: ", next_busy_nothing, "info: ", info)
    next_busy_nothing = next_nothing
    data.append(info)
  except:
    print("".join(data))
    break                               # else see crash statement

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
next_busy_nothing:  12345 info:  B
next_busy_nothing:  44827 info:  Z
next_busy_nothing:  45439 info:  h
next_busy_nothing:  94485 info:  9
next_busy_nothing:  72198 info:  1
next_busy_nothing:  80992 info:  A
next_busy_nothing:  8880 info:  Y
next_busy_nothing:  40961 info:  %26
next_busy_nothing:  58765 info:  S
next_busy_nothing:  46561 info:  Y
next_busy_nothing:  13418 info:  %94
next_busy_nothing:  41954 info:  %3A
next_busy_nothing:  46782 info:  %E2
next_busy_nothing:  92730 info:  I
next_busy_nothing:  89229 info:  %00
next_busy_nothing:  25646 info:  %00
next_busy_nothing:  74288 info:  %21
next_busy_nothing:  25945 info:  %19
next_busy_nothing:  39876 info:  %80
next_busy_nothing:  8498 info:  P
next_busy_nothing:  34684 info:  %81
next_busy_nothing:  62316 info:  %11
next_busy_nothing:  71331 info:  %00
next_busy_nothing:  59717 info:  %AF
next_busy_nothing:  76893 info:  g
next_busy_nothing:  44091 info:  %9E
next_busy_nothing:  73241 info:  %A0
next_busy_nothing:  19242 info:  %20
next_busy_nothing:  17476 info:  %00
next_busy_nothing:  39566 info:  h
next_busy_nothing:  81293 info:  E
next_busy_nothing:  25857 info:  %3D
next_busy_nothing:  74343 info:  M
next_busy_nothing:  39410 info:  %B5
next_busy_nothing:  5505 info:  %23
next_busy_nothing:  27104 info:  %D0
next_busy_nothing:  54003 info:  %D4
next_busy_nothing:  23501 info:  %D1
next_busy_nothing:  21110 info:  %E2
next_busy_nothing:  88399 info:  %8D
next_busy_nothing:  49740 info:  %06
next_busy_nothing:  31552 info:  %A9
next_busy_nothing:  39998 info:  %FA
next_busy_nothing:  19755 info:  %26
next_busy_nothing:  64624 info:  S
next_busy_nothing:  37817 info:  %D4
next_busy_nothing:  43427 info:  %D3
next_busy_nothing:  15115 info:  %21
next_busy_nothing:  44327 info:  %A1
next_busy_nothing:  7715 info:  %EA
next_busy_nothing:  15248 info:  i
next_busy_nothing:  61895 info:  7
next_busy_nothing:  54759 info:  h
next_busy_nothing:  54270 info:  %9B
next_busy_nothing:  51332 info:  %9A
next_busy_nothing:  63481 info:  %2B
next_busy_nothing:  12362 info:  %BF
next_busy_nothing:  94476 info:  %60
next_busy_nothing:  87810 info:  %22
next_busy_nothing:  6027 info:  %C5
next_busy_nothing:  47551 info:  W
next_busy_nothing:  79498 info:  X
next_busy_nothing:  81226 info:  %E1
next_busy_nothing:  4256 info:  %AD
next_busy_nothing:  62734 info:  L
next_busy_nothing:  25666 info:  %80
next_busy_nothing:  14781 info:  %E8
next_busy_nothing:  21412 info:  V
next_busy_nothing:  55205 info:  %3C
next_busy_nothing:  65516 info:  %C6
next_busy_nothing:  53535 info:  %A8
next_busy_nothing:  4437 info:  %DB
next_busy_nothing:  43442 info:  H
next_busy_nothing:  91308 info:  %26
next_busy_nothing:  1312 info:  3
next_busy_nothing:  36268 info:  2
next_busy_nothing:  34289 info:  %18
next_busy_nothing:  46384 info:  %A8
next_busy_nothing:  18097 info:  x
next_busy_nothing:  9401 info:  %01
next_busy_nothing:  54249 info:  %08
next_busy_nothing:  29247 info:  %21
next_busy_nothing:  13115 info:  %8D
next_busy_nothing:  23053 info:  S
next_busy_nothing:  3875 info:  %0B
next_busy_nothing:  16044 info:  %C8
next_busy_nothing:  8022 info:  %AF
next_busy_nothing:  25357 info:  %96
next_busy_nothing:  89879 info:  K
next_busy_nothing:  80119 info:  O
next_busy_nothing:  50290 info:  %CA
next_busy_nothing:  9297 info:  2
next_busy_nothing:  30571 info:  %B0
next_busy_nothing:  7414 info:  %F1
next_busy_nothing:  30978 info:  %BD
next_busy_nothing:  16408 info:  %1D
next_busy_nothing:  80109 info:  u
next_busy_nothing:  55736 info:  %A0
next_busy_nothing:  15357 info:  %86
next_busy_nothing:  80887 info:  %05
next_busy_nothing:  35014 info:  %92
next_busy_nothing:  16523 info:  s
next_busy_nothing:  50286 info:  %B0
next_busy_nothing:  34813 info:  %92
next_busy_nothing:  77562 info:  %C4
next_busy_nothing:  54746 info:  B
next_busy_nothing:  22680 info:  c
next_busy_nothing:  19705 info:  %F1
next_busy_nothing:  77000 info:  w
next_busy_nothing:  27634 info:  %24
next_busy_nothing:  21008 info:  S
next_busy_nothing:  64994 info:  %85
next_busy_nothing:  66109 info:  %09
next_busy_nothing:  37855 info:  %09
next_busy_nothing:  36383 info:  C
next_busy_nothing:  68548 info:  %AE
next_busy_nothing:  96070 info:  %24
next_busy_nothing:  83051 info:  %90
Traceback (most recent call last):
  File "/home/AsianHacker-picoctf/./pythonScript.py", line 15, in <module>
    info = response.cookies["info"]                             # letter
  File "/usr/local/lib/python3.10/dist-packages/requests/cookies.py", line 334, in __getitem__
    return self._find_no_duplicates(name)
  File "/usr/local/lib/python3.10/dist-packages/requests/cookies.py", line 413, in _find_no_duplicates
    raise KeyError(f"name={name!r}, domain={domain!r}, path={path!r}")
KeyError: "name='info', domain=None, path=None"
BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90

# Note: Looks like bzip data
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import urllib.parse
import bz2

data = b"BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"

# decode percent-encoding directly to bytes
decoded_bytes = urllib.parse.unquote_to_bytes(data)

# decompress BZ2
plain_text = bz2.decompress(decoded_bytes)

# print result as text
print(plain_text.decode())

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

Google: Who is mozart's father ⌨️
Johann Georg Leopold Mozart

# Think: Call from previous Lvl 13
AsianHacker-picoctf@webshell:~$ curl --header "Content-Type: text/xml"  --data "<methodCall><methodName>phone</methodName><params><param><value> \
> >  <string>Leopold</string></value></param></params></methodCall>" "http://www.pythonchallenge.com/pc/phonebook.php"
<?xml version="1.0"?>
<methodResponse>
<params>
<param>
<value><string>555-VIOLIN</string></value> 👀
</param>
</params>
</methodResponse> ⌨️

Browser: http://www.pythonchallenge.com/pc/return/violin.html ⌨️
no! i mean yes! but ../stuff/violin.php. 👀

Browser: http://www.pythonchallenge.com/pc/stuff/violin.php ⌨️
Given picture of mozart's dad

View Page Source

<html>
<head>
  <title>it's me. what do you want?</title> 👀
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center><font color="gold">
	<img src="leopold.jpg" border="0"/>
<br><br>
</font>
</body>
</html>

AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
cookies = {"info": "the flowers are on their way"}

response = requests.get(url, cookies = cookies)

print(response.text)

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
<html>
<head>
  <title>it's me. what do you want?</title> 👀
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
        <br><br>
        <center><font color="gold">
        <img src="leopold.jpg" border="0"/>
<br><br>
oh well, don't you dare to forget the balloons.</font> 👀
</body>
</html>

# Think: keyword balloons
Browser: http://www.pythonchallenge.com/pc/return/balloons.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/return/balloons.html

## Continue
[Continue](./Level18.md)
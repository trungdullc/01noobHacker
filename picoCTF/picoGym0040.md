# picoGym Level 40: Mr-Worldwide
Source: https://play.picoctf.org/practice/challenge/40

## Goal
A musician left us a message. What's it mean?<br>
https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt

## What I learned
```
ChatGPT: Decrypt this for me
Coordinate	                Place (nearest)	            Letter
(35.028309, 135.753082)	    Kyoto, Japan	                K
(46.469391, 30.740883)	    Odesa (Odessa), Ukraine	        O
(39.758949, -84.191605)	    Dayton, Ohio, USA	            D
(41.015137, 28.979530)	    Istanbul, Turkey    	        I
(24.466667, 54.366669)	    Abu Dhabi, UAE	                A
(3.140853, 101.693207)	    Kuala Lumpur, Malaysia	        K
                            _	underscore separator	    _
(9.005401, 38.763611)	    Addis Ababa, Ethiopia	        A
(-3.989038, -79.203560)	    Loja, Ecuador	                L
(52.377956, 4.897070)	    Amsterdam, Netherlands	        A
(41.085651, -73.858467)	    Sleepy Hollow / area, NY, USA	S
(57.790001, -152.407227)	Kodiak, Alaska, USA	            K
(31.205753, 29.924526)	    Alexandria, Egypt	            A

Manually add cooridates on google map
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt ⌨️
--2025-09-09 22:27:44--  https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 278 [application/octet-stream]
Saving to: 'message.txt'

message.txt                                        100%[=============================================================================================================>]     278  --.-KB/s    in 0s      

2025-09-09 22:27:44 (124 MB/s) - 'message.txt' saved [278/278]

AsianHacker-picoctf@webshell:/tmp$ cat message.txt ⌨️
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)} 👀

Method 1: ChatGPT

Method 2: ChatGPT Code
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
# pip install geopy ❤️❤️❤️❤️❤️
from geopy.geocoders import Nominatim
from time import sleep

coords = [
 (35.028309, 135.753082),(46.469391, 30.740883),(39.758949, -84.191605),
 (41.015137, 28.979530),(24.466667, 54.366669),(3.140853, 101.693207),
 # underscore marker in input -> just add '_' to result when you see it
 ('_'),
 (9.005401, 38.763611),(-3.989038, -79.203560),(52.377956, 4.897070),
 (41.085651, -73.858467),(57.79, -152.407227),(31.205753, 29.924526)
]

geolocator = Nominatim(user_agent="coords-decrypter")
result_letters = []

for c in coords:
    if c == '_':
        result_letters.append('_')
        continue
    lat, lon = c
    location = geolocator.reverse((lat, lon), exactly_one=True, language='en')
    # Pause to be polite to the service
    sleep(1)
    if location is None:
        name = "?"
    else:
        # try a few fields for a sensible place name
        name = (location.raw.get('address', {}).get('city') or
                location.raw.get('address', {}).get('town') or
                location.raw.get('address', {}).get('village') or
                location.raw.get('address', {}).get('county') or
                location.raw.get('display_name'))
    result_letters.append(name[0].upper() if name and name != "?" else '?')

print("".join(result_letters))
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
Traceback (most recent call last):
  File "/tmp/pythonScript.py", line 2, in <module>
    from geopy.geocoders import Nominatim
ModuleNotFoundError: No module named 'geopy' ⚠️
AsianHacker-picoctf@webshell:/tmp$ pip3 install geopy ⌨️❤️❤️❤️❤️❤️
Defaulting to user installation because normal site-packages is not writeable
Collecting geopy
  Downloading geopy-2.4.1-py3-none-any.whl.metadata (6.8 kB)
Collecting geographiclib<3,>=1.52 (from geopy)
  Downloading geographiclib-2.1-py3-none-any.whl.metadata (1.6 kB)
Downloading geopy-2.4.1-py3-none-any.whl (125 kB)
Downloading geographiclib-2.1-py3-none-any.whl (40 kB)
WARNING: Error parsing dependencies of send2trash: Expected matching RIGHT_PARENTHESIS for LEFT_PARENTHESIS, after version specifier
    sys-platform (=="darwin") ; extra == 'objc'
                 ~^
Installing collected packages: geographiclib, geopy
Successfully installed geographiclib-2.1 geopy-2.4.1

[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: python3 -m pip install --upgrade pip
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
KODIAK_KLAVKA 🔐

Method 3: Hard-coded (useless, just posted to better learn python language)
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
import re

flag = "picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}"

# Mapping: coordinate pair -> city name (English)
city_map = {
    ("35.028309", "135.753082"): "Kyoto",
    ("46.469391", "30.740883"): "Odessa",
    ("39.758949", "-84.191605"): "Dayton",
    ("41.015137", "28.979530"): "Istanbul",
    ("24.466667", "54.366669"): "Abu Dhabi",
    ("3.140853", "101.693207"): "Kuala Lumpur",
    ("9.005401", "38.763611"): "Addis Ababa",
    ("-3.989038", "-79.203560"): "Loja",
    ("52.377956", "4.897070"): "Amsterdam",
    ("41.085651", "-73.858467"): "Sleepy Hollow",
    ("57.790001", "-152.407227"): "Kodiak",
    ("31.205753", "29.924526"): "Alexandria"
}

def get_letter_from_coordinate(match):
    lat = match.group(1)
    lon = match.group(2)
    city = city_map.get((lat, lon), "?")
    return city[0].upper()                              # just the first letter

result = re.sub(r'\(([\d\.-]+), ([\d\.-]+)\)', get_letter_from_coordinate, flag)
print(result)
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
picoCTF{KODIAK_ALASKA} 🔐
```

## Flag
picoCTF{KODIAK_ALASKA}

## Continue
[Continue](./picoGym0100.md)
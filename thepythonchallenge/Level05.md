# Level 05

## Previous Flag
```
http://www.pythonchallenge.com/pc/def/peak.html
```

## Goal
pronounce it

## What I learned
```
python pickle
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/def/peak.html ⌨️

View Page Source:
<html>
<head>
  <title>peak hell</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="peakhell.jpg"/>
<br><font color="#c0c0ff">
pronounce it
<br>
<peakhell src="banner.p"/> 👀👀👀👀👀
</body>
</html>

<!-- peak hell sounds familiar ? --> 👀

Think: wth is this asian pun of pickle
Browser: http://www.pythonchallenge.com/pc/def/pickle.html ⌨️
yes! pickle!

Google: python pickle
Python Pickle: An Overview

The pickle module in Python is a powerful tool for serializing and deserializing Python objects. Serialization (or pickling) converts Python objects into a byte stream, which can be stored in a file or transmitted over a network. Deserialization (or unpickling) reconstructs the original object from the byte stream.
Documentation: https://docs.python.org/3/library/pickle.html

Think: <peakhell src="banner.p"/>
Download: http://www.pythonchallenge.com/pc/def/banner.p ⌨️

AsianHacker-picoctf@webshell:~$ wget http://www.pythonchallenge.com/pc/def/banner.p ⌨️
--2025-10-13 19:33:27--  http://www.pythonchallenge.com/pc/def/banner.p
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5002 (4.9K) [text/x-pascal]
Saving to: 'banner.p'

banner.p                                                  100%[=====================================================================================================================================>]   4.88K  --.-KB/s    in 0s      

2025-10-13 19:33:27 (179 MB/s) - 'banner.p' saved [5002/5002]

AsianHacker-picoctf@webshell:~$ cat banner.p | head -n 5 ⌨️
(lp0
(lp1
(S' '
p2
I95

# Think: Need to deserialize dump from pickle
# Ask ChatGPT first
AsianHacker-picoctf@webshell:~$ vi deserialize.py ⌨️
AsianHacker-picoctf@webshell:~$ cat deserialize.py ⌨️
#!/usr/bin/python3
import pickle

# Open the pickle file in binary read mode
with open("banner.p", "rb") as file:
    data = pickle.load(file)

# Print or inspect the result
print(data)

AsianHacker-picoctf@webshell:~$ chmod u+x deserialize.py ⌨️ 
AsianHacker-picoctf@webshell:~$ ./deserialize.py ⌨️
[[(' ', 95)], [(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 6), ('#', 4), (' ', 3), ('#', 3), (' ', 9), ('#', 3), (' ', 7), ('#', 5), (' ', 3), ('#', 3), (' ', 4), ('#', 5), (' ', 3), ('#', 3), (' ', 10), ('#', 3), (' ', 7), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 3), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 2), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 1), ('#', 7), (' ', 3), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 3), (' ', 2), ('#', 3), (' ', 5), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 5), ('#', 3), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 3), ('#', 4), (' ', 4), ('#', 5), (' ', 4), ('#', 4), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 5), ('#', 3), (' ', 3), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 4), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 2), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 10), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 2), (' ', 3), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 10), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 14), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 12), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 6), ('#', 2), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 6), ('#', 2), (' ', 3), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 4), ('#', 2), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 11), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 4), ('#', 3), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 5), ('#', 6), (' ', 4), ('#', 5), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 6), (' ', 4), ('#', 11), (' ', 4), ('#', 5), (' ', 6), ('#', 3), (' ', 6), ('#', 6)], [(' ', 95)]]

AsianHacker-picoctf@webshell:~$ vi deserialize.py ⌨️
AsianHacker-picoctf@webshell:~$ cat deserialize.py ⌨️
#!/usr/bin/python3
import pickle

# Open the pickle file in binary read mode
with open("banner.p", "rb") as file:
    data = pickle.load(file)

# Print or inspect the result
# print(data)

for item in data:
    for tuples in item:
        print(tuples[0]*tuples[1], end ="")
    print()

AsianHacker-picoctf@webshell:~$ ./deserialize.py ⌨️
                                                                                               
              #####                                                                      ##### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### 
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### 
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### 
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### 
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### 
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### 
####           ####     ####   ##########    ####     ####  ####     #### ##############  #### 
####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### 
####           ####     #### ####     ###    ####     ####  ####     #### ####            #### 
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### 
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### 
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### 
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######

Browser: http://www.pythonchallenge.com/pc/def/channel.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/def/channel.html

## Continue
[Continue](./Level06.md)
# picoGym Level 314: unpackme.py
Source: https://play.picoctf.org/practice/challenge/314

## Goal
Can you get the flag?<br>
Reverse engineer this Python program.<br>
https://artifacts.picoctf.net/c/49/unpackme.flag.py

## What I learned
```
When reverse engineering sometimes not want exec maleware script and just print out code
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/49/unpackme.flag.py ⌨️
--2025-09-26 22:26:15--  https://artifacts.picoctf.net/c/49/unpackme.flag.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 527 [application/octet-stream]
Saving to: 'unpackme.flag.py'

unpackme.flag.py                                           100%[======================================================================================================================================>]     527  --.-KB/s    in 0s      

2025-09-26 22:26:16 (332 MB/s) - 'unpackme.flag.py' saved [527/527]

AsianHacker-picoctf@webshell:~$ cat unpackme.flag.py ⌨️
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkzWGSzE6VQNTzvRXOXekQeW4CY6NiRkzeImo9LuYBHAYw_hagTJLJL0c-kmNsjY33IUbU2IWlqxA3Fpp9S7RxNkiwMDZgLmRlI9-lGAEW-_i72RSDvylNR3QkpJW2JxubjLUC5VwoVgH62wxDuYu1rRD5KadwTADdABqsx2MkY6fKNTMCYY09Se6yjtRBftfTJUL-LKz2bwgXNd6O-WpbfXEMvCv3gNQ7sW4pgUnb-gDVZvrLNrug_1YFaIe3yKr0Awo0HIN3XMdZYpSE1c9P4G0sMQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)

exec(plain.decode())

# Method 1: Modify code
AsianHacker-picoctf@webshell:~$ cat unpackme.flag.py ⌨️
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkzWGSzE6VQNTzvRXOXekQeW4CY6NiRkzeImo9LuYBHAYw_hagTJLJL0c-kmNsjY33IUbU2IWlqxA3Fpp9S7RxNkiwMDZgLmRlI9-lGAEW-_i72RSDvylNR3QkpJW2JxubjLUC5VwoVgH62wxDuYu1rRD5KadwTADdABqsx2MkY6fKNTMCYY09Se6yjtRBftfTJUL-LKz2bwgXNd6O-WpbfXEMvCv3gNQ7sW4pgUnb-gDVZvrLNrug_1YFaIe3yKr0Awo0HIN3XMdZYpSE1c9P4G0sMQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)

# Modify code to output decode
print(plain.decode()) 👀
exec(plain.decode())

AsianHacker-picoctf@webshell:~$ python3 unpackme.flag.py ⌨️

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_cd82f94c}') 🔐
else:
  print('That password is incorrect.')


What's the password? batteryhorse ⌨️
picoCTF{175_chr157m45_cd82f94c} 🔐
```

## Flag
picoCTF{175_chr157m45_cd82f94c}

## Continue
[Continue](./picoGym0287.md)
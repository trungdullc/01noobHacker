# Beginner Tutorial: Tips And Tricks

## Previous Flag
```
247CTF{9719c5ddf317154473d334f47a77ac6a}
```

## Goal
A number of challenges will require you to create solutions which are more efficiently solved by making use of a programming language to automate and perform the computations. For this purpose, we recommend to make use of Python as well as complementary libraries such as requests and pwntools.<br>
Python: https://www.python.org/<br>
request: https://requests.readthedocs.io/en/latest/<br>
pwntools: https://docs.pwntools.com/<br>

If you are not sure where to start with Python, we recommend the introductory Python 101 for Hackers course.<br>
https://academy.tcm-sec.com/courses/python-101-for-hackers?affcode=770707_w8hyczi7<br>

Click the ‘START CHALLENGE’ button to the right of this text description to start a socket challenge. Utilise a programming language to interface with the socket and automate solving 500 simple addition problems to receive the flag. Take care when interfacing with unknown remote services - '\n' is not the only way to end

## What I learned
```
1   Welcome to the 247CTF addition verifier!
2   If you can solve 500 addition problems, we will give you a flag!
3   What is the answer to 256 + 157?
     0   1   2    3    4   5  6   7
```

## Solution
```
START CHALLENGE

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> nc 83879c4ce8528eb6.247ctf.com 50252 ⌨️
Welcome to the 247CTF addition verifier!
If you can solve 500 addition problems, we will give you a flag!
What is the answer to 256 + 157?
413 ⌨️
^C ⌨️

# Method 1:
┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> cat ./pythonScript.py ⌨️
#!/usr/bin/python3

from pwn import *
import re

client = remote("83879c4ce8528eb6.247ctf.com", 50252)

print(client.recvline())
print(client.recvline())

for i in range(500):
    math = client.recvline().decode("utf-8")
    nums = re.findall(r"\d+", math)

    num1 = int(nums[0])
    num2 = int(nums[1])

    result = str(num1+num2)
    final = (result+"\r\n").encode("utf-8")
    client.sendline(final)
    client.recvline()
    print("the operation", i, "has been done with a" , result)

print(client.recvline())

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> chmod u+x ./pythonScript.py ⌨️   

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> ./pythonScript.py ⌨️
Traceback (most recent call last):
  File "/home/asianhacker/pythonScript.py", line 3, in <module>
    from pwn import *
ModuleNotFoundError: No module named 'pwn' ⚠️

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> python3 -m pip install --user pwntools ⌨️
error: externally-managed-environment ⚠️ means can't use --user

# Install distribution package (if available)
┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> apt search pwntools ⌨️

python-pwntools-doc/kali-rolling 4.14.1-1 all
  CTF framework and exploit development library (documentation)

python3-pwntools/kali-rolling 4.14.1-1 all 👀
  CTF framework and exploit development library

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> sudo apt update ⌨️

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> sudo apt install python3-pwntools ⌨️

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> ./pythonScript.py ⌨️

the operation 495 has been done with a 179
the operation 496 has been done with a 282
the operation 497 has been done with a 766
the operation 498 has been done with a 788
the operation 499 has been done with a 518
b'247CTF{6ae15c0aeb45a334b3f01eb0dda5cab1}\r\n' 🔐
[*] Closed connection to 83879c4ce8528eb6.247ctf.com port 50252    

# Method 2:                                    
┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> cat ./pythonScript.py ⌨️

#!/usr/bin/python3

from pwn import *

client = remote("83879c4ce8528eb6.247ctf.com", 50252)           # initialize connection to remote host

print(client.recvline())
print(client.recvline())

for i in range(500):
    problem = client.recvline().decode("utf-8")
    indexing = problem.split()

    Qa = int(indexing[5])
    Qb = int(indexing[7].strip("?"))
    answer = (str(Qa+Qb)+ "\r\n").encode("utf-8")
    print(f"answering {i} question ({Qa ,'+', Qb})...")
    client.sendline(answer)
    client.recvline()
flag = client.recvline().decode("utf-8").strip("\r\n")
print("Catched the flag!", flag)
client.close()

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> ./pythonScript.py ⌨️

answering 495 question ((150, '+', 352))...
answering 496 question ((380, '+', 116))...
answering 497 question ((246, '+', 388))...
answering 498 question ((195, '+', 412))...
answering 499 question ((10, '+', 283))...
Catched the flag! 247CTF{6ae15c0aeb45a334b3f01eb0dda5cab1} 🔐
[*] Closed connection to 83879c4ce8528eb6.247ctf.com port 50252
```

## Flag
247CTF{6ae15c0aeb45a334b3f01eb0dda5cab1}

## Continue
[Continue](../247ctf/WebSecuredSession.md)
# picoGym Level 125: Easy Peasy
Source: https://play.picoctf.org/practice/challenge/125

## Goal
A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})<br>
nc mercury.picoctf.net 36981 <br>
otp.py: https://mercury.picoctf.net/static/6920807ae08f883dbb50f6f301f92684/otp.py

## What I learned
```
pwn is main module of pwntools, a Python framework made for CTF and binary exploitation
pwn provides tools for:
    Connecting to remote servers (pwn.remote)
    Spawning and interacting with processes (pwn.process)
    Packing/unpacking integers to bytes (pwn.p32, pwn.u64)
    Assembling shellcode (pwn.asm, pwn.shellcraft)
    Automating exploits

XOR 2 times get original thing

Youtube Solution: https://www.youtube.com/watch?v=VodIW2TT_ag
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/6920807ae08f883dbb50f6f301f92684/otp.py ⌨️
--2025-09-04 20:35:56--  https://mercury.picoctf.net/static/6920807ae08f883dbb50f6f301f92684/otp.py
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1080 (1.1K) [application/octet-stream]
Saving to: 'otp.py'

otp.py                                                     100%[======================================================================================================================================>]   1.05K  --.-KB/s    in 0s      

2025-09-04 20:35:56 (497 MB/s) - 'otp.py' saved [1080/1080]

AsianHacker-picoctf@webshell:/tmp$ cat otp.py ⌨️
#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000 👀
FLAG_FILE = "flag"

def startup(key_location):
        flag = open(FLAG_FILE).read()
        kf = open(KEY_FILE, "rb").read()

        start = key_location
        stop = key_location + len(flag)

        key = kf[start:stop]
        key_location = stop

        result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
        print("This is the encrypted flag!\n{}\n".format("".join(result)))

        return key_location

def encrypt(key_location):
        ui = input("What data would you like to encrypt? ").rstrip()
        if len(ui) == 0 or len(ui) > KEY_LEN:
                return -1

        start = key_location
        stop = key_location + len(ui)

        kf = open(KEY_FILE, "rb").read()

        if stop >= KEY_LEN: 👀
                stop = stop % KEY_LEN
                key = kf[start:] + kf[:stop]
        else:
                key = kf[start:stop]
        key_location = stop

        result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

        print("Here ya go!\n{}\n".format("".join(result)))

        return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
        c = encrypt(c)

AsianHacker-picoctf@webshell:/tmp$ nc mercury.picoctf.net 36981 ⌨️
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c 👀

What data would you like to encrypt? abcdefghijklmnopqrstuvwxyz
Here ya go!
50035d381d04533411535c07583b38222d0a1044290e15492502
^C ⌨️
AsianHacker-picoctf@webshell:/tmp$ python3 -c "print(len('5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c'))" ⌨️
64
# Note: 64 hex digit means 32 char

# Method 1: Create a owntool template w/o exploit
AsianHacker-picoctf@webshell:/tmp$ pwn template --host mercury.picoctf.net --port 20266 otp.py ⌨️
[*] Automatically detecting challenge binaries...
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host mercury.picoctf.net --port 20266 otp.py
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = 'otp.py'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141 EXE=/tmp/executable
host = args.HOST or 'mercury.picoctf.net'
port = int(args.PORT or 20266)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

io = start()

# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()

# Write Exploit
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host mercury.picoctf.net --port 36981otp.py
from pwn import *

# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = 'otp.py'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'mercury.picoctf.net'
port = int(args.PORT or 36981 )

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

io = start()
io.recvuntil("This is the encrypted flag!\n")
encrypted_flag = str(io.recvline(), "ascii").strip()
# The length of the flag is the length of the encrypted flag divided by 2
# because of line 19 (`"{:02x}".format(ord(p) ^ k)`) where string formatting
# is used to output the flag as a hexadecimal string where each character is
# represetned by 2 characters.
flag_len = int(len(encrypted_flag)/2)

# Create a filler payload to reset the `c` variable in `otp.py` to 0 so we
# can use the same key that was used to encrypt the flag.
filler = "a"*(50000-flag_len)
io.sendlineafter("What data would you like to encrypt? ", filler)

def xor_list_str(a, b):
    # `a` is a list and `b` is a string
    return ''.join(list(map(lambda p, k: chr(p ^ ord(k)), a, b)))

def hex_to_dec_list(input_hex):
    # Convert a hex string to a decimal array.
    # Split the hex string into groups of 2.
    input_hex = [input_hex[i:i+2] for i in range(0, len(input_hex), 2)]
    # Convert each two hex characters to decimal.
    output = [int(x, 16) for x in input_hex]
    return output

# Create a message that we know that is the same length as the flag so
# that the same key is used to encrypt it.
message = "a"*flag_len

io.sendlineafter("What data would you like to encrypt? ", message)
io.recvuntil("Here ya go!\n")

encrypted_message = str(io.recvline(), "ascii").strip()
# Convert the encrypted message output by the program to a list of decimal
# numbers.
encrypted_message = hex_to_dec_list(encrypted_message)
# Find the key by xoring the encrypted message with the known clear text
# message as described at https://cs.stackexchange.com/a/365.
key = xor_list_str(encrypted_message, message)
log.success("Found Key: %s" % key)

# Convert the encrypted flag output by the program to a list of decimal
# numbers that represent ascii characters.
encrypted_flag = hex_to_dec_list(encrypted_flag)
# Decrypt the flag by xoring it with the key.
flag = xor_list_str(encrypted_flag, key)

log.success("Found Flag: picoCTF{%s}" % flag)

# Use Exploit
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py 
[+] Opening connection to mercury.picoctf.net on port 36981: Done
/tmp/pythonScript.py:48: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  io.recvuntil("This is the encrypted flag!\n")
/tmp/pythonScript.py:59: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  io.sendlineafter("What data would you like to encrypt? ", filler)
/usr/local/lib/python3.10/dist-packages/pwnlib/tubes/tube.py:876: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
/tmp/pythonScript.py:77: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  io.sendlineafter("What data would you like to encrypt? ", message)
/tmp/pythonScript.py:78: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  io.recvuntil("Here ya go!\n")
[+] Found Key: b')^E\x87\xf7\xb5\xd0c\x8f\xc6\x
[+] Found Flag: picoCTF{7f9da29f40499a98db220380a57746a4} 🔐
[*] Closed connection to mercury.picoctf.net port 36981

# Method 2:
AsianHacker-picoctf@webshell:/tmp$ python3 -c "print('a'*49968);print('a'*32)" | nc mercury.picoctf.net 36981 ⌨️    
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c 👀

What data would you like to encrypt? Here ya go!
50005f3d1903553d1958560a543436333d1902513d1903503d1905553d1950553d1904553d1904573d1905523d1907523b1652563d190407333a3d195004453d190758533d1907574e3d1902043d1956073d1900503d1902073d1905533c333d1950501c543d190504343d1904573d1958073d1904021c3d1907553d19025255013d1905583d1905553d190759343d1959043d190703053d1907523d1905523d1900023d1903593d1900563d195950183d190202073d1958003d1905003d190507193d1950563d1959523d190055123d1907071f3d1958050a33213d190259083d1904033d1958073d1958523d1950564f3d1950563a3d1900513d1951503d1900045a3d190350093d1900003d190354323d1907543d1904071b3d190359421c3d1900523d190250383d195954313d1907543d195150113d1956073d1902073d1905513d463d1900043d1958573d1958054e3a20123d190050423d195000133d190352093d1950503d1905033d1950533d1904593d190359043d195854193b3d1904073d1951033d1902553d1902033d1958053d1900553d1903073d1902513d1902020b3d190756573d3d39293b0a3d1903563d1905533d1907543d1900024a553d1907073d1904503d1907023d195804353d19 (super long) ...

What data would you like to encrypt? Here ya go!
0346483f243d1959563d1907563d1903543d190551023d1959073d1902573d19 👀

What data would you like to encrypt? ^C ⌨️

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py  ⌨️
#!/usr/bin/env python

# Remember there was 32 characters
encrypted_flag=0x5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c
encrypted_a=0x0346483f243d1959563d1907563d1903543d190551023d1959073d1902573d19
plain_a=0x6161616161616161616161616161616161616161616161616161616161616161

def findFlag() -> None:
    # encrypted_flag=flag^k
    # encrypted_a=plain_a^k
    # encrypted_a=plain_a^flag
    flag_hex = '{:x}'.format(encrypted_flag^encrypted_a^plain_a)
    print(flag_hex)

    # Convert hex → bytes
    b = bytes.fromhex(flag_hex)

    # Decode bytes → ASCII (ignore errors if not all bytes are printable)
    ascii_text = b.decode(errors="ignore")

    print("picoCTF{" + ascii_text + "}")

def main() -> None:
    findFlag()

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py
3766396461323966343034393961393864623232303338306135373734366134
picoCTF{7f9da29f40499a98db220380a57746a4} 🔐

# Other Way to convert hex to ASCII
AsianHacker-picoctf@webshell:/tmp$ printf "%s\n" $(echo 3766396461323966343034393961393864623232303338306135373734366134 | xxd -r -p) ⌨️
7f9da29f40499a98db220380a57746a4 🔐

# Other Way to convert hex to ASCII
AsianHacker-picoctf@webshell:/tmp$ python3 -c "print(bytes.fromhex('3766396461323966343034393961393864623232303338306135373734366134').decode())" ⌨️
7f9da29f40499a98db220380a57746a4 🔐

# Other Way to convert hex to ASCII
https://cyberchef.io/#recipe=From_Hex('Auto')&input=Mzc2NjM5NjQ2MTMyMzk2NjM0MzAzNDM5Mzk2MTM5Mzg2NDYyMzIzMjMwMzMzODMwNjEzNTM3MzczNDM2NjEzNA
```

## Flag
picoCTF{7f9da29f40499a98db220380a57746a4}

## Continue
[Continue](./picoGym0064.md)
# picoGym Level 104: Transformation
Source: https://play.picoctf.org/practice/challenge/7

## Goal
I wonder what this really is... enc<br>
https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc<br>
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## What I learned
```
''.join     the code we are looking at is placing encoded characters into a list
            if you were to print the encoding without ''.join your results would look similar to [“a”, “b”, “c”]
            The purpose is to join the items with no space or characters between them
chr()       is a function that converts decimal and hexadecimal into it’s assigned ascii character
ord()       Converting ascii characters to a number
<< 8        bitwise shifter, same as multiplying by 256 (2^8)
for i in range(0, len(flag), 2)     this section of code pairs up characters in the original flag into groups of two

ASCII ranges from 0 to 127, which never exceeds 128(0b10000000, with seven 0's)
ASCII order's maximum(0b1111111) is 7 bits
shifts flag[i] 8 bits left, so if the original flag[i] is 1101011, 
    it will become 15 bits long: 110101100000000 (as seen in given hint)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc ⌨️
--2025-09-24 22:03:18--  https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 57 [application/octet-stream]
Saving to: 'enc'

enc                                                        100%[======================================================================================================================================>]      57  --.-KB/s    in 0s      

2025-09-24 22:03:19 (46.2 MB/s) - 'enc' saved [57/57]

AsianHacker-picoctf@webshell:~$ file enc ⌨️
enc: Unicode text, UTF-8 text, with no line terminators
AsianHacker-picoctf@webshell:~$ python3 enc ⌨️
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ

# Method 1:
AsianHacker-picoctf@webshell:~$ python3 ⌨️
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> enc=open("enc").read() ⌨️
>>> print(enc) ⌨️
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ
>>> print(enc[0]) ⌨️
灩
>>> print(hex(ord(enc[0]))) ⌨️
0x7069
>>> print(" ".join(format(ord(ch), "x") for ch in enc)) ⌨️
7069 636f 4354 467b 3136 5f62 6974 735f 696e 7374 3334 645f 6f66 5f38 5f32 3636 3834 6332 307d 👀
>>> for c in enc: ⌨️
...     print(hex(ord(c)).lstrip("0x"),end=' ') ⌨️
... 
7069 636f 4354 467b 3136 5f62 6974 735f 696e 7374 3334 645f 6f66 5f38 5f32 3636 3834 6332 307d 👀

https://cyberchef.io/#recipe=From_Hex('Auto')&input=NzA2OSA2MzZmIDQzNTQgNDY3YiAzMTM2IDVmNjIgNjk3NCA3MzVmIDY5NmUgNzM3NCAzMzM0IDY0NWYgNmY2NiA1ZjM4IDVmMzIgMzYzNiAzODM0IDYzMzIgMzA3ZA

# Method 2:
AsianHacker-picoctf@webshell:~$ vi pythonScripy.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScripy.py ⌨️
# Encypting
flag="picoCTF{this_is_a_fake_flag}"
print(len(flag))
enc=""
for i in range(0, len(flag), 2):
    print(i)
    print(bin(ord(flag[i])))
    print(f'{bin(ord(flag[i]) << 8)}+{bin(ord(flag[i+1]))} ={bin((ord(flag[i]) << 8) + ord(flag[i + 1]))}',(ord(flag[i]) << 8) + ord(flag[i + 1]))
    enc+= chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
    print(enc)

# Decypting
text="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
flag=""
for i in range(len(text)):
    print(f'{ord(text[i]):015b}')

    ord1="0b"+f'{ord(text[i]):015b}'[0:7]
    flag+=chr(int(ord1,2))

    ord2="0b"+f'{ord(text[i]):015b}'[8:15]
    flag+=chr(int(ord2,2))

    print(flag)

AsianHacker-picoctf@webshell:~$ python3 pythonScripy.py ⌨️
28
0
0b1110000
0b111000000000000+0b1101001 =0b111000001101001 28777
灩
2
0b1100011
0b110001100000000+0b1101111 =0b110001101101111 25455
灩捯
4
0b1000011
0b100001100000000+0b1010100 =0b100001101010100 17236
灩捯䍔
6
0b1000110
0b100011000000000+0b1111011 =0b100011001111011 18043
灩捯䍔䙻
8
0b1110100
0b111010000000000+0b1101000 =0b111010001101000 29800
灩捯䍔䙻瑨
10
0b1101001
0b110100100000000+0b1110011 =0b110100101110011 26995
灩捯䍔䙻瑨楳
12
0b1011111
0b101111100000000+0b1101001 =0b101111101101001 24425
灩捯䍔䙻瑨楳彩
14
0b1110011
0b111001100000000+0b1011111 =0b111001101011111 29535
灩捯䍔䙻瑨楳彩獟
16
0b1100001
0b110000100000000+0b1011111 =0b110000101011111 24927
灩捯䍔䙻瑨楳彩獟慟
18
0b1100110
0b110011000000000+0b1100001 =0b110011001100001 26209
灩捯䍔䙻瑨楳彩獟慟晡
20
0b1101011
0b110101100000000+0b1100101 =0b110101101100101 27493
灩捯䍔䙻瑨楳彩獟慟晡步
22
0b1011111
0b101111100000000+0b1100110 =0b101111101100110 24422
灩捯䍔䙻瑨楳彩獟慟晡步彦
24
0b1101100
0b110110000000000+0b1100001 =0b110110001100001 27745
灩捯䍔䙻瑨楳彩獟慟晡步彦污
26
0b1100111
0b110011100000000+0b1111101 =0b110011101111101 26493
灩捯䍔䙻瑨楳彩獟慟晡步彦污杽
111000001101001
pi
110001101101111
pico
100001101010100
picoCT
100011001111011
picoCTF{
011000100110110
picoCTF{16
101111101100010
picoCTF{16_b
110100101110100
picoCTF{16_bit
111001101011111
picoCTF{16_bits_
110100101101110
picoCTF{16_bits_in
111001101110100
picoCTF{16_bits_inst
011001100110100
picoCTF{16_bits_inst34
110010001011111
picoCTF{16_bits_inst34d_
110111101100110
picoCTF{16_bits_inst34d_of
101111100111000
picoCTF{16_bits_inst34d_of_8
101111100110010
picoCTF{16_bits_inst34d_of_8_2
011011000110110
picoCTF{16_bits_inst34d_of_8_266
011100000110100
picoCTF{16_bits_inst34d_of_8_26684
110001100110010
picoCTF{16_bits_inst34d_of_8_26684c2
011000001111101
picoCTF{16_bits_inst34d_of_8_26684c20} 🔐
```

## Flag
picoCTF{16_bits_inst34d_of_8_26684c20}

## Continue
[Continue](./picoGym0007.md)
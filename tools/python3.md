# Python3

```
Description: Programming Languange

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

## CTF
[picoGym0253: list](../picoCTF/picoGym0253.md)<br>
[picoGym0307: File](../picoCTF/picoGym0307.md)

## Back to README.md
[BACK](../README.md)
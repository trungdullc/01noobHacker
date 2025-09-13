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
[picoGym0307: File](../picoCTF/picoGym0307.md)<br>
[picoGym0407: File, with ⭐⭐⭐](../picoCTF/picoGym0407.md)<br>
[picoGym0289: format specifier ⭐⭐⭐](../picoCTF/picoGym0289.md)<br>
[picoGym0040: pip3 install ⭐⭐⭐](../picoCTF/picoGym0040.md)<br>
[picoGym0158: binary](../picoCTF/picoGym0158.md)<br>
[picoGym0159: pip3 install, modifying](../picoCTF/picoGym0159.md)<br>
[picoGym0412: simple reverse engineering](../picoCTF/picoGym0412.md)<br>
[picoGym0210: os](../picoCTF/picoGym0210.md)<br>
[picoGym0474: rainbow table w/ salt ⭐⭐⭐⭐⭐](../picoCTF/picoGym0474.md)<br>
[picoGym0422: RSA algorithm](../picoCTF/picoGym0422.md)

## Back to README.md
[BACK](../README.md)
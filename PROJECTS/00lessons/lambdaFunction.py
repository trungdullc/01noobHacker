"""
Level: Beginner
What I learned:
    lambda function in python

Created by HackerDu    
"""

import sys

def add(*args):
    """
    Show how regular function works
    """
    # print(type(args))         # <class 'tuple'>
    sum = 0

    for number in args:
        sum += number
    
    return sum
    # return sum(args)          # built-in shortcut

def main():
    print(1+2)
    print(add(1,2))
    print(add(1,2,3))
    print((lambda x,y: x+y)(1,2))               # lambda function syntax
    print((lambda *args: sum(args))(1,2))

    result = lambda *args: sum(args)            # Note: (variable) def result(*args: Any) -> int
    # print(type(result))                       # <class 'function'>
    print(result(1,2))                          # Note: Don't forget the (1,2) since it a function with parameters *args

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
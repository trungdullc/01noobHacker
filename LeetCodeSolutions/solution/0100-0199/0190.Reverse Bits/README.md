# [190. Reverse Bits](https://leetcode.com/problems/reverse-bits) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>Reverse bits of a given 32 bits unsigned integer.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer&#39;s internal binary representation is the same, whether it is signed or unsigned.</li>
	<li>In Java, the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2&#39;s complement notation</a>. Therefore, in <strong class="example">Example 2</strong> above, the input represents the signed integer <code>-3</code> and the output represents the signed integer <code>-1073741825</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 00000010100101000001111010011100
<strong>Output:</strong>    964176192 (00111001011110000010100101000000)
<strong>Explanation: </strong>The input binary string <strong>00000010100101000001111010011100</strong> represents the unsigned integer 43261596, so return 964176192 which its binary representation is <strong>00111001011110000010100101000000</strong>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 11111111111111111111111111111101
<strong>Output:</strong>   3221225471 (10111111111111111111111111111111)
<strong>Explanation: </strong>The input binary string <strong>11111111111111111111111111111101</strong> represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is <strong>10111111111111111111111111111111</strong>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The input must be a <strong>binary string</strong> of length <code>32</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If this function is called many times, how would you optimize it?</p>

## Solutions

### Solution 1: Bit Manipulation

We can extract each bit of `n` from the least significant bit to the most significant bit, and then place it in the corresponding position of `ans`.

For example, for the $i$-th bit, we can use `(n & 1) << (31 - i)` to extract the $i$-th bit of `n` and place it on the $31 - i$-th bit of `ans`, then right shift `n` by one bit.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$.

#### Du Solution1
```python
#!/usr/bin/env python3

class Solution:
    """
    Brute Force
    Runtime Complexity: O(1)
    Space Complexity: O(1)
    """
    def reverseBits(self, n: int) -> int:
        binary = ""

        for i in range(32):
            if n & (1 << i):                            # 0191: Number of 1 Bits
                binary += "1"
            else:
                binary += "0"

        ans = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                ans |= (1 << i)                         # bitwise OR to turn on a bit
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596))
    print(sol.reverseBits(2147483644))
```

#### Du Solution2
```python
#!/usr/bin/env python3

class Solution:
    """
    Bit Manipulation
    Runtime Complexity: O(1)
    Space Complexity: O(1)
    """
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = (n >> i) & 1                      # 0191: Number of 1 Bits, get LSB
            ans += (bit << (31 - i))                # put in MSB
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596))
    print(sol.reverseBits(2147483644))
```

#### Du Solution3
```python
#!/usr/bin/env python3

class Solution:
    """
    Bit Manipulation (Optimal)
    Runtime Complexity: O(1)
    Space Complexity: O(1)
    """
    def reverseBits(self, n: int) -> int:                               # Note: No way I getting this solution in 5-10 minutes
        res = n
        res = (res >> 16) | (res << 16) & 0xFFFFFFFF                    # Swap left 16 bits w/ right 16 bits, letter is a 4-bit nibble
        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)     # Swap bytes inside each 16-bit half
        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)     # Swap 4-bit nibbles
        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)     # Swap 2-bit pairs
        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)     # Swap individual bits
        return res & 0xFFFFFFFF

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596))
    print(sol.reverseBits(2147483644))
```

#### Python3 (Wrong argument)
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Bit Manipulation
   Runtime Complexity: O(1)
   Space Complexity: O(1)
   """
   def reverseBits(self, n: int) -> int:
      result = 0
      for _ in range(32):
         result = (result << 1) | (n & 1)
         n >>= 1
      return result

if __name__ == "__main__":
   sol = Solution()
   print(sol.reverseBits(0b00000010100101000001111010011100))
   print(sol.reverseBits(0b11111111111111111111111111111101))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
964176192
3221225471

real    0m0.022s
user    0m0.022s
sys     0m0.000s
```

#### Python3 (wrong argument)
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3

class Solution:
   def reverseBits(self, n: str) -> tuple[int,int]:
      n = n[::-1]                   # Reverse string
      ans = int(n,2)                # Math ❤️
      return ans, f"{ans:032b}"     # return format specifier tuple ❤️

def main() -> None:
   sol = Solution()
   print(sol.reverseBits("00000010100101000001111010011100"))
   print(sol.reverseBits("11111111111111111111111111111101"))

if __name__ == "__main__":
   main()
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
(964176192, '00111001011110000010100101000000')
(3221225471, '10111111111111111111111111111111')
```

#### Python3 (wrong argument)
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3

class Solution:
   def reverseBits(self, n: str) -> tuple[int,int]:
      num = int(n, 2)       # binary str to int (does math) ❤️
      ans = 0

      # Look at last digit and shift to far left then inner
      for i in range(32):
         ans |= (num & 1) << (31 - i)
         num >>= 1
      # Convert back to binary string with 32 bits
      return ans, f"{ans:032b}"

def main() -> None:
   sol = Solution()
   print(sol.reverseBits("00000010100101000001111010011100"))
   print(sol.reverseBits("11111111111111111111111111111101"))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
(964176192, '00111001011110000010100101000000')
(3221225471, '10111111111111111111111111111111')
```

#### Java

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ans = 0;
        for (int i = 0; i < 32 && n != 0; ++i) {
            ans |= (n & 1) << (31 - i);
            n >>>= 1;
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans = 0;
        for (int i = 0; i < 32 && n; ++i) {
            ans |= (n & 1) << (31 - i);
            n >>= 1;
        }
        return ans;
    }
};
```

#### Go

```go
func reverseBits(n uint32) (ans uint32) {
	for i := 0; i < 32; i++ {
		ans |= (n & 1) << (31 - i)
		n >>= 1
	}
	return
}
```

#### Rust

```rust
impl Solution {
    pub fn reverse_bits(mut n: u32) -> u32 {
        let mut ans = 0;
        for i in 0..32 {
            ans |= (n & 1) << (31 - i);
            n >>= 1;
        }
        ans
    }
}
```

#### JavaScript

```js
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
    let ans = 0;
    for (let i = 0; i < 32 && n; ++i) {
        ans |= (n & 1) << (31 - i);
        n >>= 1;
    }
    return ans >>> 0;
};
```

[Continue 0268: Missing Number](../../0200-0299/0268.Missing%20Number/README.md)
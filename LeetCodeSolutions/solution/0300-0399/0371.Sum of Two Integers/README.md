# [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers)

## Description

<p>Given two integers <code>a</code> and <code>b</code>, return <em>the sum of the two integers without using the operators</em> <code>+</code> <em>and</em> <code>-</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = 1, b = 2
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = 2, b = 3
<strong>Output:</strong> 5
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-1000 &lt;= a, b &lt;= 1000</code></li>
</ul>

## Solutions

### Solution 1

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Sum of Two Integers problem.
   """
   def getSum(self, a: int, b: int) -> int:
      """
      Return the sum of two integers without using '+' or '-'.
      
      Args:
         a (int): First integer.
         b (int): Second integer.
      
      Returns:
         int: Sum of a and b.
      """
      # 32-bit mask to simulate integer overflow
      mask = 0xFFFFFFFF
      while b != 0:
         # XOR gives sum without carry
         sum_ = (a ^ b) & mask
         # AND gives carry, shifted left
         carry = ((a & b) << 1) & mask
         a, b = sum_, carry

      # if a is negative in 32-bit representation
      return a if a <= 0x7FFFFFFF else ~(a ^ mask)

if __name__ == "__main__":
   sol = Solution()
   print(sol.getSum(1, 2))
   print(sol.getSum(2, 3))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
5

real    0m0.022s
user    0m0.009s
sys     0m0.013s
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3

class Solution:
   def getSum(self, a: int, b: int) -> int:
      carry = 0
      result = 0
      mask = 0xFFFFFFFF   # mask to keep results within 32 bits

      for i in range(32):
         # Extract the i-th bit of both numbers
         a_bit = (a >> i) & 1
         b_bit = (b >> i) & 1

         # Compute the current bit using XOR (sum without carry)
         cur_bit = a_bit ^ b_bit ^ carry

         # Determine if there will be a carry for the next bit
         carry = (a_bit + b_bit + carry) >= 2

         # If current bit is 1, set it in result
         if cur_bit:
            result |= (1 << i)

      # Handle negative numbers (two's complement conversion)
      if result > 0x7FFFFFFF:
         result = ~(result ^ mask)

      return result

def main()-> None:
   sol = Solution()
   print(sol.getSum(a = 1, b = 2))
   print(sol.getSum(2, 3))

if __name__ == "__main__":
   main()
AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
5

real    0m0.022s
user    0m0.013s
sys     0m0.009s
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3

class Solution:
   def getSum(self, a: int, b: int) -> int:
      while b:
         temp = (a & b) << 1
         a ^= b
         b = temp
      return a

def main()-> None:
   sol = Solution()
   print(sol.getSum(a = 1, b = 2))
   print(sol.getSum(2, 3))

if __name__ == "__main__":
   main()
AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
5

real    0m0.022s
user    0m0.018s
sys     0m0.005s
```

#### Python3

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a, b = a & 0xFFFFFFFF, b & 0xFFFFFFFF
        while b:
            carry = ((a & b) << 1) & 0xFFFFFFFF
            a, b = a ^ b, carry
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)
```

#### Java

```java
class Solution {
    public int getSum(int a, int b) {
        return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
    }
}
```

#### C++

```cpp
class Solution {
public:
    int getSum(int a, int b) {
        while (b) {
            unsigned int carry = (unsigned int) (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
};
```

#### Go

```go
func getSum(a int, b int) int {
	for b != 0 {
		s := a ^ b
		b = (a & b) << 1
		a = s
	}
	return a
}
```

[Continue 0007: Reverse Integer](../../0000-0099/0007.Reverse%20Integer/README.md)
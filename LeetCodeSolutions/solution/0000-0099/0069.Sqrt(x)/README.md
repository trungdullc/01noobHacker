# [69. Sqrt(x)](https://leetcode.com/problems/sqrtx)

## Description

<p>Given a non-negative integer <code>x</code>, return <em>the square root of </em><code>x</code><em> rounded down to the nearest integer</em>. The returned integer should be <strong>non-negative</strong> as well.</p>

<p>You <strong>must not use</strong> any built-in exponent function or operator.</p>

<ul>
	<li>For example, do not use <code>pow(x, 0.5)</code> in c++ or <code>x ** 0.5</code> in python.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 4 is 2, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## Solutions

### Solution 1: Binary Search

We define the left boundary of the binary search as $l = 0$ and the right boundary as $r = x$, then we search for the square root within the range $[l, r]$.

In each step of the search, we find the middle value $mid = (l + r + 1) / 2$. If $mid > x / mid$, it means the square root is within the range $[l, mid - 1]$, so we set $r = mid - 1$. Otherwise, it means the square root is within the range $[mid, r]$, so we set $l = mid$.

After the search ends, we return $l$.

The time complexity is $O(\log x)$, and the space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   A class to compute the integer square root of a non-negative integer.
   """

   def mySqrt(self, x: int) -> int:
      """
      Returns the square root of x rounded down to the nearest integer.
      
      Args:
         x (int): A non-negative integer.
      
      Returns:
         int: The integer part of the square root of x.
      """
      if x < 2:
         return x

      left, right = 1, x // 2
      while left <= right:
         mid = left + (right - left) // 2
         if mid * mid == x:
            return mid
         elif mid * mid < x:
            left = mid + 1
         else:
            right = mid - 1
      return right

if __name__ == "__main__":
   sol = Solution()

   print(sol.mySqrt(4))
   print(sol.mySqrt(8))

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
2
2
```

#### Python3

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r + 1) >> 1
            if mid > x // mid:
                r = mid - 1
            else:
                l = mid
        return l
```

#### Java

```java
class Solution {
    public int mySqrt(int x) {
        int l = 0, r = x;
        while (l < r) {
            int mid = (l + r + 1) >>> 1;
            if (mid > x / mid) {
                r = mid - 1;
            } else {
                l = mid;
            }
        }
        return l;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int mySqrt(int x) {
        int l = 0, r = x;
        while (l < r) {
            int mid = (l + r + 1ll) >> 1;
            if (mid > x / mid) {
                r = mid - 1;
            } else {
                l = mid;
            }
        }
        return l;
    }
};
```

#### Go

```go
func mySqrt(x int) int {
	return sort.Search(x+1, func(i int) bool { return i*i > x }) - 1
}
```

#### Rust

```rust
impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        let mut l = 0;
        let mut r = x;

        while l < r {
            let mid = (l + r + 1) / 2;

            if mid > x / mid {
                r = mid - 1;
            } else {
                l = mid;
            }
        }

        l
    }
}
```

#### JavaScript

```js
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
    let [l, r] = [0, x];
    while (l < r) {
        const mid = (l + r + 1) >> 1;
        if (mid > x / mid) {
            r = mid - 1;
        } else {
            l = mid;
        }
    }
    return l;
};
```

#### C#

```cs
public class Solution {
    public int MySqrt(int x) {
        int l = 0, r = x;
        while (l < r) {
            int mid = (l + r + 1) >>> 1;
            if (mid > x / mid) {
                r = mid - 1;
            } else {
                l = mid;
            }
        }
        return l;
    }
}
```

[Continue 0074: Search a 2D Matrix ](../../0000-0099/0074.Search%20a%202D%20Matrix/README.md)
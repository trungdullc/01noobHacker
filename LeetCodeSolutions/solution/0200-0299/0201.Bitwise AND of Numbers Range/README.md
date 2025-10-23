# [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range)

## Description

<p>Given two integers <code>left</code> and <code>right</code> that represent the range <code>[left, right]</code>, return <em>the bitwise AND of all numbers in this range, inclusive</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = 5, right = 7
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = 0, right = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> left = 1, right = 2147483647
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= left &lt;= right &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## Solutions

### Solution 1

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3

class Solution:
   def rangeBitwiseAnd(self, left: int, right: int) -> int:
      while left < right:
         right &= right - 1
      return right

def main() -> None:
   sol = Solution()
   print(sol.rangeBitwiseAnd(left = 5, right = 7))
   print(sol.rangeBitwiseAnd(left = 0, right = 0))
   print(sol.rangeBitwiseAnd(left = 1, right = 2147483647))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
4
0
0

real    0m0.023s
user    0m0.019s
sys     0m0.004s
```

#### Python3

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right
```

#### Java

```java
class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        while (left < right) {
            right &= (right - 1);
        }
        return right;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        while (left < right) {
            right &= (right - 1);
        }
        return right;
    }
};
```

#### Go

```go
func rangeBitwiseAnd(left int, right int) int {
	for left < right {
		right &= (right - 1)
	}
	return right
}
```

#### JavaScript

```js
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeBitwiseAnd = function (left, right) {
    while (left < right) {
        right &= right - 1;
    }
    return right;
};
```

#### C#

```cs
public class Solution {
    public int RangeBitwiseAnd(int left, int right) {
        while (left < right) {
            right &= (right - 1);
        }
        return right;
    }
}
```

[Continue 3133: Minimum Array End](../../3100-3199/3133.Minimum%20Array%20End/README.md)
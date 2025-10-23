# [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits)

## Description

<p>Given a positive integer <code>n</code>, write a function that returns the number of <span data-keyword="set-bit">set bits</span> in its binary representation (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 11</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The input binary string <strong>1011</strong> has a total of three set bits.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 128</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The input binary string <strong>10000000</strong> has a total of one set bit.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2147483645</span></p>

<p><strong>Output:</strong> <span class="example-io">30</span></p>

<p><strong>Explanation:</strong></p>

<p>The input binary string <strong>1111111111111111111111111111101</strong> has a total of thirty set bits.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If this function is called many times, how would you optimize it?

## Solutions

### Solution 1
```
Brian Kernighan’s Algorithm
Each loop iteration removes one 1 bit
n &= n - 1

Binary      Decimal = 25    
11001
11000 &     Counter
11000       1
10111 &
10000       1
01111 &
00000       1 = total 3 ones in binary
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   def hammingweight(self, n: int) -> int:
      counter = 0
      while n:
         if n & 1 == 1:
            counter += 1
         n >> 1
      return counter

def main()-> None:
   sol = Solution()
   print(sol.hammingweight(11))
   print(sol.hammingweight(128))
   print(sol.hammingweight(2147483645))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py 
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py 
3
1
30
```

#### Python3

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans
```

#### Java

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        while (n != 0) {
            n &= n - 1;
            ++ans;
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while (n) {
            n &= n - 1;
            ++ans;
        }
        return ans;
    }
};
```

#### Go

```go
func hammingWeight(num uint32) int {
	ans := 0
	for num != 0 {
		num &= num - 1
		ans++
	}
	return ans
}
```

#### TypeScript

```ts
function hammingWeight(n: number): number {
    let ans: number = 0;
    while (n !== 0) {
        ans++;
        n &= n - 1;
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn hammingWeight(n: u32) -> i32 {
        n.count_ones() as i32
    }
}
```

#### JavaScript

```js
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
    let ans = 0;
    while (n) {
        n &= n - 1;
        ++ans;
    }
    return ans;
};
```

#### C

```c
int hammingWeight(uint32_t n) {
    int ans = 0;
    while (n) {
        n &= n - 1;
        ans++;
    }
    return ans;
}
```

#### Kotlin

```kotlin
class Solution {
    fun hammingWeight(n: Int): Int {
        var count = 0
        var num = n
        while (num != 0) {
            num = num and (num - 1)
            count++
        }
        return count
    }
}
```

### Solution 2

#### Python3

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n -= n & -n
            ans += 1
        return ans
```

#### Java

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        while (n != 0) {
            n -= (n & -n);
            ++ans;
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while (n) {
            n -= (n & -n);
            ++ans;
        }
        return ans;
    }
};
```

#### Go

```go
func hammingWeight(num uint32) int {
	ans := 0
	for num != 0 {
		num -= (num & -num)
		ans++
	}
	return ans
}
```

#### TypeScript

```ts
function hammingWeight(n: number): number {
    let count = 0;
    while (n) {
        n -= n & -n;
        count++;
    }
    return count;
}
```

#### Rust

```rust
impl Solution {
    pub fn hammingWeight(mut n: u32) -> i32 {
        let mut res = 0;
        while n != 0 {
            n &= n - 1;
            res += 1;
        }
        res
    }
}
```

#### JavaScript

```js
/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
    let count = 0;
    while (n) {
        n -= n & -n;
        count++;
    }
    return count;
};
```

#### Kotlin

```kotlin
class Solution {
    fun hammingWeight(n: Int): Int {
        var count = 0
        var num = n
        while (num != 0) {
            num -= num and (-num)
            count++
        }
        return count
    }
}
```

[Continue 0338: Counting Bits](../../0300-0399/0338.Counting%20Bits/README.md)
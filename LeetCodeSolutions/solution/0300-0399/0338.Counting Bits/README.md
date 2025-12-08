# [338. Counting Bits](https://leetcode.com/problems/counting-bits) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>Given an integer <code>n</code>, return <em>an array </em><code>ans</code><em> of length </em><code>n + 1</code><em> such that for each </em><code>i</code><em> </em>(<code>0 &lt;= i &lt;= n</code>)<em>, </em><code>ans[i]</code><em> is the <strong>number of </strong></em><code>1</code><em><strong>&#39;s</strong> in the binary representation of </em><code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [0,1,1]
<strong>Explanation:</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> [0,1,1,2,1,2]
<strong>Explanation:</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>It is very easy to come up with a solution with a runtime of <code>O(n log n)</code>. Can you do it in linear time <code>O(n)</code> and possibly in a single pass?</li>
	<li>Can you do it without using any built-in function (i.e., like <code>__builtin_popcount</code> in C++)?</li>
</ul>

## Solutions

### Solution 1
```
Python List Comprehension is useful easier than C/C++ ternary conditional operator
```

#### Du Solution1
```python
#!/usr/bin/env python3
from typing import List

class Solution:
    """
    Bit Manipulation
    Runtime Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    def countBits(self, n: int) -> List[int]:
        ans = []

        for num in range(n + 1):                        # Note: need +1
            countBits = 0
            for i in range(32):                         # check each bit
                if num & (1 << i):                      # 0191: Number of 1 Bits
                    countBits += 1
            ans.append(countBits)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))
    print(sol.countBits(5))
```

#### Du Solution2
```python
#!/usr/bin/env python3
from typing import List

class Solution:
    """
    Bit Manipulation
    Runtime Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):       # Skip first since 0
            num = i
            while num != 0:
                ans[i] += 1
                num &= (num - 1)        # 0191: Number of 1 Bits
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))
    print(sol.countBits(5))
```

#### Du Solution3
```python
#!/usr/bin/env python3
from typing import List

class Solution:
    """
    Bit Manipulation (Dynamic Programming)
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))
    print(sol.countBits(5))
```

#### Du Solution4
```python
#!/usr/bin/env python3
from typing import List

class Solution:
    """
    Bit Manipulation (Optimal)
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))
    print(sol.countBits(5))
```

#### Du Solution5
```python
#!/usr/bin/env python3
from typing import List

class Solution:
    """
    Built-In Function
    Runtime Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n + 1)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(2))
    print(sol.countBits(5))
```

#### Python
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   def hammingweight(self, n: int) -> int:
      counter = 0
      while n:
         n &= n-1
         counter +=1
      return counter

   def countBits(self, n: int) -> List[int]:
      ans = [0] * (n+1)                         # Note: need set default value
      for i in range(n):
         ans[i] = i                             # or get error here
      for i in range(len(ans)):
          ans[i] = self.hammingweight(i)        # Note: calling own fx
      return ans
   
def main()-> None:
   sol = Solution()
   print(sol.countBits(2))
   print(sol.countBits(5))
   
if __name__ == "__main__":
   main()
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
[0, 1, 1]
[0, 1, 1, 2, 1, 2]
```

#### Python
```python
#!/usr/bin/python3
from typing import List

class Solution:
   def hammingweight(self, n: int) -> int:
      counter = 0
      while n:
         n &= n-1
         counter +=1
      return counter

   def countBits(self, n: int) -> List[int]:
      return [self.hammingweight(i) for i in range(n + 1)] 👀

def main()-> None:
   sol = Solution()
   print(sol.countBits(2))
   print(sol.countBits(5))

if __name__ == "__main__":
   main()
```

#### Python3 

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]
```

#### Java

```java
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 0; i <= n; ++i) {
            ans[i] = Integer.bitCount(i);
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1);
        for (int i = 0; i <= n; ++i) {
            ans[i] = __builtin_popcount(i);
        }
        return ans;
    }
};
```

#### Go

```go
func countBits(n int) []int {
	ans := make([]int, n+1)
	for i := 0; i <= n; i++ {
		ans[i] = bits.OnesCount(uint(i))
	}
	return ans
}
```

#### TypeScript

```ts
function countBits(n: number): number[] {
    const ans: number[] = Array(n + 1).fill(0);
    for (let i = 0; i <= n; ++i) {
        ans[i] = bitCount(i);
    }
    return ans;
}

function bitCount(n: number): number {
    let count = 0;
    while (n) {
        n &= n - 1;
        ++count;
    }
    return count;
}
```

### Solution 2

#### Python3

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans
```

#### Java

```java
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; ++i) {
            ans[i] = ans[i & (i - 1)] + 1;
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1);
        for (int i = 1; i <= n; ++i) {
            ans[i] = ans[i & (i - 1)] + 1;
        }
        return ans;
    }
};
```

#### Go

```go
func countBits(n int) []int {
	ans := make([]int, n+1)
	for i := 1; i <= n; i++ {
		ans[i] = ans[i&(i-1)] + 1
	}
	return ans
}
```

#### TypeScript

```ts
function countBits(n: number): number[] {
    const ans: number[] = Array(n + 1).fill(0);
    for (let i = 1; i <= n; ++i) {
        ans[i] = ans[i & (i - 1)] + 1;
    }
    return ans;
}
```

[Continue 0067: Add Binary](../../0000-0099/0067.Add%20Binary/README.md)
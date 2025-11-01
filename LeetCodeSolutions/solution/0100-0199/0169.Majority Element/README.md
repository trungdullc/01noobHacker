# [169. Majority Element](https://leetcode.com/problems/majority-element)

## Description

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p style="color: yellow;">Hacker: Return the number that occurs more than n/2 times given an array </p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?

## Solutions

### Solution 1: Moore Voting Algorithm

The basic steps of the Moore voting algorithm are as follows:

Initialize the element $m$ and initialize the counter $cnt = 0$. Then, for each element $x$ in the input list:

1. If $cnt = 0$, then $m = x$ and $cnt = 1$;
1. Otherwise, if $m = x$, then $cnt = cnt + 1$, otherwise $cnt = cnt - 1$.

In general, the Moore voting algorithm requires **two passes** over the input list. In the first pass, we generate the candidate value $m$, and if there is a majority, the candidate value is the majority value. In the second pass, we simply compute the frequency of the candidate value to confirm whether it is the majority value. Since this problem has clearly stated that there is a majority value, we can directly return $m$ after the first pass, without the need for a second pass to confirm whether it is the majority value.

The time complexity is $O(n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List
from collections import defaultdict

class Solution:
   """
   Solution for the Majority Element problem.
   """
   def majorityElement(self, nums: List[int], n: int) -> int:
      """
      Find the element that appears more than n/2 times in the array.
      
      Args:
         nums (list[int]): Input array.
         n: size of array
      Returns:
         int: The majority element.
      """
      freqDict: dict[int, int] = defaultdict(int)   # ❤️ Real important fixes many errors w/ {}

      for num in nums:
         freqDict[num] += 1                         # Add count to frequency Dictionary

      for key in freqDict:
         if freqDict[key] > n/2:
            return key

      return 0

def main() -> None:
   sol = Solution()
   print(sol.majorityElement([3,2,3], 3))
   print(sol.majorityElement([2,2,1,1,1,2,2], 7))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
2

real    0m0.032s
user    0m0.024s
sys     0m0.004s
```

#### Du Solution

```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List
from collections import Counter

class Solution:
   def majorityElement(self, nums: List[int], n: int) -> int:
      freqDict: dict[int, int] = Counter(nums)              # Counter fx mapped counts

      for key in freqDict:
         if freqDict[key] > n/2:
            return key

      return 0

def main() -> None:
   sol = Solution()
   print(sol.majorityElement([3,2,3], 3))
   print(sol.majorityElement([2,2,1,1,1,2,2], 7))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
2

real    0m0.102s
user    0m0.026s
sys     0m0.004s
```

#### Python3: Solution.py

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = m = 0
        for x in nums:
            if cnt == 0:
                m, cnt = x, 1
            else:
                cnt += 1 if m == x else -1
        return m
```

#### JavaScript
```js
// CLASS VERSION                                      // FUNCTION EXPRESSION VERSION
class Solution {                                      const majorityElement = function(nums, n) {
  majorityElement(nums, n) {                            const freqDict = {}; 
    const freqDict = {};                                for (const num of nums) {
    for (const num of nums) {                             freqDict[num] = (freqDict[num] || 0) + 1;
      freqDict[num] = (freqDict[num] || 0) + 1;         }
    }                                                   for (const key in freqDict) {
    for (const key in freqDict) {                         if (freqDict[key] > n/2) {
      if (freqDict[key] > n / 2) {                          return Number(key);
        return key;                                       }
      }                                                 }
    }                                                   return 0;
    return 0;                                         };
  }
}

const sol = new Solution();
console.log(sol.majorityElement([3,2,3], 3));
console.log(sol.majorityElement([2,2,1,1,1,2,2], 7));
```

#### Java: Solution.java

```java
class Solution {
    public int majorityElement(int[] nums) {
        int cnt = 0, m = 0;
        for (int x : nums) {
            if (cnt == 0) {
                m = x;
                cnt = 1;
            } else {
                cnt += m == x ? 1 : -1;
            }
        }
        return m;
    }
}
```

#### C++: Solution.cpp

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt = 0, m = 0;
        for (int& x : nums) {
            if (cnt == 0) {
                m = x;
                cnt = 1;
            } else {
                cnt += m == x ? 1 : -1;
            }
        }
        return m;
    }
};
```

#### Go: Solution.go

```go
func majorityElement(nums []int) int {
	var cnt, m int
	for _, x := range nums {
		if cnt == 0 {
			m, cnt = x, 1
		} else {
			if m == x {
				cnt++
			} else {
				cnt--
			}
		}
	}
	return m
}
```

#### TypeScript: Solution.ts

```ts
function majorityElement(nums: number[]): number {
    let cnt: number = 0;
    let m: number = 0;
    for (const x of nums) {
        if (cnt === 0) {
            m = x;
            cnt = 1;
        } else {
            cnt += m === x ? 1 : -1;
        }
    }
    return m;
}
```

#### Rust: Solution.rs

```rust
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut m = 0;
        let mut cnt = 0;
        for &x in nums.iter() {
            if cnt == 0 {
                m = x;
                cnt = 1;
            } else {
                cnt += if m == x { 1 } else { -1 };
            }
        }
        m
    }
}
```

#### JavaScript: Solution.js

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
    let cnt = 0;
    let m = 0;
    for (const x of nums) {
        if (cnt === 0) {
            m = x;
            cnt = 1;
        } else {
            cnt += m === x ? 1 : -1;
        }
    }
    return m;
};
```

#### C#: Solution.cs

```cs
public class Solution {
    public int MajorityElement(int[] nums) {
        int cnt = 0, m = 0;
        foreach (int x in nums) {
            if (cnt == 0) {
                m = x;
                cnt = 1;
            } else {
                cnt += m == x ? 1 : -1;
            }
        }
        return m;
    }
}
```

#### PHP: Solution.php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function majorityElement($nums) {
        $m = 0;
        $cnt = 0;
        foreach ($nums as $x) {
            if ($cnt == 0) {
                $m = $x;
            }
            if ($m == $x) {
                $cnt++;
            } else {
                $cnt--;
            }
        }
        return $m;
    }
}
```

[Continue 0705: Design HashSet](../../0700-0799/0705.Design%20HashSet/README.md)
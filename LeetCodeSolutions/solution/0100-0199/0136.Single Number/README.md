# [136. Single Number](https://leetcode.com/problems/single-number)

## Description

<p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>

## Solutions

### Solution 1: Bitwise Operation

The XOR operation has the following properties:

-   Any number XOR 0 is still the original number, i.e., $x \oplus 0 = x$;
-   Any number XOR itself is 0, i.e., $x \oplus x = 0$; ⭐⭐⭐⭐⭐

Performing XOR operation on all elements in the array will result in the number that only appears once.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   def singlenumber(self, nums: List[int]):
      singleFinder = 0

      for num in nums:
         singleFinder ^= num
      return singleFinder

def main()-> None:
   sol = Solution()
   print(sol.singlenumber([2,2,1]))
   print(sol.singlenumber([4,1,2,1,2]))
   print(sol.singlenumber([1]))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
1
4
1
```

#### Python3

```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List
from functools import reduce    # No way I remembering this 👀
from operator import xor        # No way I remebering this 👀

class Solution:
    def singlenumber(self, nums: List[int]):
        # Use reduce to apply XOR across all numbers
        return reduce(xor, nums) 👀

def main() -> None:
    sol = Solution()
    print(sol.singlenumber([2, 2, 1]))
    print(sol.singlenumber([4, 1, 2, 1, 2]))
    print(sol.singlenumber([1]))

if __name__ == "__main__":
    main()

AsianHacker-picoctf@webshell:/tmp$ python3 -q
>>> from functools import reduce
>>> help(reduce)

Help on built-in function reduce in module _functools:

reduce(...)
    reduce(function, iterable[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
```

#### Java

```java
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int v : nums) {
            ans ^= v;
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int v : nums) {
            ans ^= v;
        }
        return ans;
    }
};
```

#### Go

```go
func singleNumber(nums []int) (ans int) {
	for _, v := range nums {
		ans ^= v
	}
	return
}
```

#### TypeScript

```ts
function singleNumber(nums: number[]): number {
    return nums.reduce((r, v) => r ^ v);
}
```

#### Rust

```rust
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        nums.into_iter().reduce(|r, v| r ^ v).unwrap()
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    return nums.reduce((a, b) => a ^ b);
};
```

#### C#

```cs
public class Solution {
    public int SingleNumber(int[] nums) {
        return nums.Aggregate(0, (a, b) => a ^ b);
    }
}
```

#### C

```c
int singleNumber(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        ans ^= nums[i];
    }
    return ans;
}
```

#### Swift

```swift
class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        return nums.reduce(0, ^)
    }
}
```

### Solution 2

#### Java

```java
class Solution {
    public int singleNumber(int[] nums) {
        return Arrays.stream(nums).reduce(0, (a, b) -> a ^ b);
    }
}
```

[Continue 0191: Number of 1 Bits](../../0100-0199/0191.Number%20of%201%20Bits/README.md)
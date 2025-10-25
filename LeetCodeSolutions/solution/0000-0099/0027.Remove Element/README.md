# [27. Remove Element](https://leetcode.com/problems/remove-element)

## Description

<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>. The order of the elements may be changed. Then return <em>the number of elements in </em><code>nums</code><em> which are not equal to </em><code>val</code>.</p>

<p>Consider the number of elements in <code>nums</code> which are not equal to <code>val</code> be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the elements which are not equal to <code>val</code>. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i &lt; actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2,_,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong>Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>

## Solutions

### Solution 1: One Pass

We use the variable $k$ to record the number of elements that are not equal to $val$.

Traverse the array $nums$, if the current element $x$ is not equal to $val$, then assign $x$ to $nums[k]$, and increment $k$ by $1$.

Finally, return $k$.

The time complexity is $O(n)$ and the space complexity is $O(1)$, where $n$ is the length of the array $nums$.

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Remove Element problem.
   """
   def removeElement(self, nums: list[int], val: int) -> int:
      """
      Remove all occurrences of val in nums in-place.
      
      Args:
         nums (list[int]): Input array.
         val (int): Value to remove.
      
      Returns:
         int: Number of elements not equal to val.
      """
      k = 0
      for num in nums:
         if num != val:
            nums[k] = num
            k += 1
      return k

if __name__ == "__main__":
   sol = Solution()
   arr1 = [3,2,2,3]
   k1 = sol.removeElement(arr1, 3)
   print(k1, arr1[:k1])
   
   arr2 = [0,1,2,2,3,0,4,2]
   k2 = sol.removeElement(arr2, 2)
   print(k2, arr2[:k2])

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
2 [2, 2]
5 [0, 1, 3, 0, 4]

real    0m0.022s
user    0m0.011s
sys     0m0.011s
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   def removeElement(self, nums: List[int], val: int) -> int:
      k = 0

      for i in range(len(nums)):
         if nums[i] != val:
            nums[k] = nums[i]       # Note: Starts at 0
            k += 1
      return k

def main() -> None:
   sol = Solution()

   k1 = sol.removeElement([3,2,2,3], 3)
   print(k1, nums1[:k1])

   k2 = sol.removeElement([0,1,2,2,3,0,4,2], 2)
   print(k2, nums2[:k2])

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
2 [2, 2]
5 [0, 1, 3, 0, 4]
```

#### Python3: Solution.py

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k
```

#### Java: Solution.java

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int x : nums) {
            if (x != val) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
```

#### C++: Solution.cpp

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int x : nums) {
            if (x != val) {
                nums[k++] = x;
            }
        }
        return k;
    }
};
```

#### Go: Solution.go

```go
func removeElement(nums []int, val int) int {
	k := 0
	for _, x := range nums {
		if x != val {
			nums[k] = x
			k++
		}
	}
	return k
}
```

#### TypeScript: Solution.ts

```ts
function removeElement(nums: number[], val: number): number {
    let k: number = 0;
    for (const x of nums) {
        if (x !== val) {
            nums[k++] = x;
        }
    }
    return k;
}
```

#### Rust: Solution.rs

```rust
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut k = 0;
        for i in 0..nums.len() {
            if nums[i] != val {
                nums[k] = nums[i];
                k += 1;
            }
        }
        k as i32
    }
}
```

#### JavaScript: Solution.js

```js
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
    let k = 0;
    for (const x of nums) {
        if (x !== val) {
            nums[k++] = x;
        }
    }
    return k;
};
```

#### C#: Solution.cs

```cs
public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int k = 0;
        foreach (int x in nums) {
            if (x != val) {
                nums[k++] = x;
            }
        }
        return k;
    }
}
```

#### PHP: Solution.php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        for ($i = count($nums) - 1; $i >= 0; $i--) {
            if ($nums[$i] == $val) {
                array_splice($nums, $i, 1);
            }
        }
    }
}
```

[Continue 0169: Majority Element](../../0100-0199/0169.Majority%20Element/README.md)
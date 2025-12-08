# [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(log n) time</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] and it was rotated 4 times. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>

## Solutions

### Solution 1

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   A class to find the minimum element in a rotated sorted array.
   """

   def findMin(self, nums: list[int]) -> int:
      """
      Finds the minimum element in a rotated sorted array using binary search.

      Args:
         nums (list[int]): A rotated sorted array of unique integers.

      Returns:
         int: The minimum element in the array.
      """
      left, right = 0, len(nums) - 1

      while left < right:
         mid = (left + right) // 2
         if nums[mid] > nums[right]:
            left = mid + 1
         else:
            right = mid

      return nums[left]

if __name__ == "__main__":
   sol = Solution()

   print(sol.findMin([3,4,5,1,2]))
   print(sol.findMin([4,5,6,7,0,1,2]))
   print(sol.findMin([11,13,15,17]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
1
0
11

real    0m0.068s
user    0m0.031s
sys     0m0.000s
```

#### Python3

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```

#### Java

```java
class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        if (nums[0] <= nums[n - 1]) {
            return nums[0];
        }
        int left = 0, right = n - 1;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (nums[0] <= nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        if (nums[0] <= nums[n - 1]) return nums[0];
        int left = 0, right = n - 1;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (nums[0] <= nums[mid])
                left = mid + 1;
            else
                right = mid;
        }
        return nums[left];
    }
};
```

#### Go

```go
func findMin(nums []int) int {
	n := len(nums)
	if nums[0] <= nums[n-1] {
		return nums[0]
	}
	left, right := 0, n-1
	for left < right {
		mid := (left + right) >> 1
		if nums[0] <= nums[mid] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}
```

#### TypeScript

```ts
function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const mid = (left + right) >>> 1;
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return nums[left];
}
```

#### Rust

```rust
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;
        while left < right {
            let mid = left + (right - left) / 2;
            if nums[mid] > nums[right] {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        nums[left]
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
    let l = 0,
        r = nums.length - 1;
    if (nums[l] < nums[r]) return nums[0];
    while (l < r) {
        const m = (l + r) >> 1;
        if (nums[m] > nums[r]) l = m + 1;
        else r = m;
    }
    return nums[l];
};
```

[Continue 0033: Search In Rotated Sorted Array ](../../0000-0099/0033.Search%20in%20Rotated%20Sorted%20Array/README.md)
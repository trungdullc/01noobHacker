# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position)

## Description

<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

## Solutions

### Solution 1: Binary Search

Since the array $nums$ is already sorted, we can use the binary search method to find the insertion position of the target value $target$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the array $nums$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   A class to find the index to insert a target in a sorted array.
   """

   def searchInsert(self, nums: list[int], target: int) -> int:
      """
      Returns the index if the target is found, or the index where it would be inserted.
      
      Args:
         nums (list[int]): Sorted list of distinct integers.
         target (int): The integer to search or insert.
      
      Returns:
         int: Index of target or insertion position.
      """
      left, right = 0, len(nums) - 1

      while left <= right:
         mid = left + (right - left) // 2
         if nums[mid] == target:
            return mid
         elif nums[mid] < target:
            left = mid + 1
         else:
            right = mid - 1
      return left

if __name__ == "__main__":
   sol = Solution()

   print(sol.searchInsert([1,3,5,6], 5))
   print(sol.searchInsert([1,3,5,6], 2))
   print(sol.searchInsert([1,3,5,6], 7))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
2
1
4

real    0m0.024s
user    0m0.020s
sys     0m0.004s
```

#### Python3

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
```

#### Java

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = 0, r = nums.length;
        while (l < r) {
            int mid = (l + r) >>> 1;
            if (nums[mid] >= target) {
                r = mid;
            } else {
                l = mid + 1;
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
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l < r) {
            int mid = (l + r) >> 1;
            if (nums[mid] >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};
```

#### Go

```go
func searchInsert(nums []int, target int) int {
	l, r := 0, len(nums)
	for l < r {
		mid := (l + r) >> 1
		if nums[mid] >= target {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}
```

#### TypeScript

```ts
function searchInsert(nums: number[], target: number): number {
    let [l, r] = [0, nums.length];
    while (l < r) {
        const mid = (l + r) >> 1;
        if (nums[mid] >= target) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
}
```

#### Rust

```rust
impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = nums.len();
        while l < r {
            let mid = (l + r) >> 1;
            if nums[mid] >= target {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        l as i32
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    let [l, r] = [0, nums.length];
    while (l < r) {
        const mid = (l + r) >> 1;
        if (nums[mid] >= target) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
};
```

#### PHP

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target) {
        $l = 0;
        $r = count($nums);
        while ($l < $r) {
            $mid = $l + $r >> 1;
            if ($nums[$mid] >= $target) {
                $r = $mid;
            } else {
                $l = $mid + 1;
            }
        }
        return $l;
    }
}
```

### Solution 2: Binary Search (Built-in Function)

We can also directly use the built-in function for binary search.

The time complexity is $O(\log n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

#### Python3

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
```

#### Java

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = Arrays.binarySearch(nums, target);
        return i < 0 ? -i - 1 : i;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    }
};
```

#### Go

```go
func searchInsert(nums []int, target int) int {
	return sort.SearchInts(nums, target)
}
```

[Continue 0374: Guess Number Higher Or Lower](../../0300-0399/0374.Guess%20Number%20Higher%20or%20Lower/README.md)
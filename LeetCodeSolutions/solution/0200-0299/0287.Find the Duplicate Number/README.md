# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number)

## Description

<p>Given an array of integers <code>nums</code> containing&nbsp;<code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.</p>

<p>There is only <strong>one repeated number</strong> in <code>nums</code>, return <em>this&nbsp;repeated&nbsp;number</em>.</p>

<p>You must solve the problem <strong>without</strong> modifying the array <code>nums</code>&nbsp;and using only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,4,2,2]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,3,4,2]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3,3,3]
<strong>Output:</strong> 3</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li>All the integers in <code>nums</code> appear only <strong>once</strong> except for <strong>precisely one integer</strong> which appears <strong>two or more</strong> times.</li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b></p>

<ul>
	<li>How can we prove that at least one duplicate number must exist in <code>nums</code>?</li>
	<li>Can you solve the problem in linear runtime complexity?</li>
</ul>

## Solutions

### Solution 1: Binary Search

We can observe that if the number of elements in $[1,..x]$ is greater than $x$, then the duplicate number must be in $[1,..x]$, otherwise the duplicate number must be in $[x+1,..n]$.

Therefore, we can use binary search to find $x$, and check whether the number of elements in $[1,..x]$ is greater than $x$ at each iteration. This way, we can determine which interval the duplicate number is in, and narrow down the search range until we find the duplicate number.

The time complexity is $O(n \times \log n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution class to find the duplicate number in an array.
   """

   def findDuplicate(self, nums):
      """
      Find the duplicate number using cycle detection.
      :type nums: list[int]
      :rtype: int
      """
      # Step 1: Find intersection point
      slow = fast = nums[0]
      while True:
         slow = nums[slow]
         fast = nums[nums[fast]]
         if slow == fast:
            break

      # Step 2: Find entrance to the cycle
      slow = nums[0]
      while slow != fast:
         slow = nums[slow]
         fast = nums[fast]

      return slow

if __name__ == "__main__":
   sol = Solution()
   print(sol.findDuplicate([1,3,4,2,2]))
   print(sol.findDuplicate([3,1,3,4,2]))
   print(sol.findDuplicate([3,3,3,3,3]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
2
3
3

real    0m0.022s
user    0m0.022s
sys     0m0.000s
```

#### Python3

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            return sum(v <= x for v in nums) > x

        return bisect_left(range(len(nums)), True, key=f)
```

#### Java

```java
class Solution {
    public int findDuplicate(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            int cnt = 0;
            for (int v : nums) {
                if (v <= mid) {
                    ++cnt;
                }
            }
            if (cnt > mid) {
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
    int findDuplicate(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            int cnt = 0;
            for (int& v : nums) {
                cnt += v <= mid;
            }
            if (cnt > mid) {
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
func findDuplicate(nums []int) int {
	return sort.Search(len(nums), func(x int) bool {
		cnt := 0
		for _, v := range nums {
			if v <= x {
				cnt++
			}
		}
		return cnt > x
	})
}
```

#### TypeScript

```ts
function findDuplicate(nums: number[]): number {
    let l = 0;
    let r = nums.length - 1;
    while (l < r) {
        const mid = (l + r) >> 1;
        let cnt = 0;
        for (const v of nums) {
            if (v <= mid) {
                ++cnt;
            }
        }
        if (cnt > mid) {
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
    #[allow(dead_code)]
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;

        while left < right {
            let mid = (left + right) >> 1;
            let cnt = nums.iter().filter(|x| **x <= (mid as i32)).count();
            if cnt > mid {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left as i32
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
    let l = 0;
    let r = nums.length - 1;
    while (l < r) {
        const mid = (l + r) >> 1;
        let cnt = 0;
        for (const v of nums) {
            if (v <= mid) {
                ++cnt;
            }
        }
        if (cnt > mid) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
};
```

[Continue 0092: Reverse Linked List II](../../0000-0099/0092.Reverse%20Linked%20List%20II/README.md)
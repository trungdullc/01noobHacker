# [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii)

## Description

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if there are two <strong>distinct indices</strong> </em><code>i</code><em> and </em><code>j</code><em> in the array such that </em><code>nums[i] == nums[j]</code><em> and </em><code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1], k = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1], k = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,2,3], k = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

## Solutions

### Solution 1: Hash Table

We use a hash table $\textit{d}$ to store the recently traversed numbers and their corresponding indices.

Traverse the array $\textit{nums}$. For the current element $\textit{nums}[i]$, if it exists in the hash table and the difference between the indices is no more than $k$, return $\text{true}$. Otherwise, add the current element to the hash table.

After traversing, return $\text{false}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from typing import List

class Solution:
   def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      """
      Returns True if the array contains duplicate numbers within k distance.
      Uses a hashmap to store the last seen index of each number.
      """
      index_map: dict[int, int] = {}                # num -> last index

      for i, num in enumerate(nums):
         if num in index_map and i - index_map[num] <= k:
            return True
         index_map[num] = i

      return False

if __name__ == "__main__":
   sol = Solution()
   print(sol.containsNearbyDuplicate([1,2,3,1], 3))
   print(sol.containsNearbyDuplicate([1,0,1,1], 1))
   print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
True
True
False
```

#### Python3

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, x in enumerate(nums):
            if x in d and i - d[x] <= k:
                return True
            d[x] = i
        return False
```

#### Java

```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> d = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            if (i - d.getOrDefault(nums[i], -1000000) <= k) {
                return true;
            }
            d.put(nums[i], i);
        }
        return false;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> d;
        for (int i = 0; i < nums.size(); ++i) {
            if (d.count(nums[i]) && i - d[nums[i]] <= k) {
                return true;
            }
            d[nums[i]] = i;
        }
        return false;
    }
};
```

#### Go

```go
func containsNearbyDuplicate(nums []int, k int) bool {
	d := map[int]int{}
	for i, x := range nums {
		if j, ok := d[x]; ok && i-j <= k {
			return true
		}
		d[x] = i
	}
	return false
}
```

#### TypeScript

```ts
function containsNearbyDuplicate(nums: number[], k: number): boolean {
    const d: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; ++i) {
        if (d.has(nums[i]) && i - d.get(nums[i])! <= k) {
            return true;
        }
        d.set(nums[i], i);
    }
    return false;
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
    const d = new Map();
    for (let i = 0; i < nums.length; ++i) {
        if (d.has(nums[i]) && i - d.get(nums[i]) <= k) {
            return true;
        }
        d.set(nums[i], i);
    }
    return false;
};
```

#### C#

```cs
public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var d = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; ++i) {
            if (d.ContainsKey(nums[i]) && i - d[nums[i]] <= k) {
                return true;
            }
            d[nums[i]] = i;
        }
        return false;
    }
}
```

#### PHP

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function containsNearbyDuplicate($nums, $k) {
        $d = [];
        for ($i = 0; $i < count($nums); ++$i) {
            if (array_key_exists($nums[$i], $d) && $i - $d[$nums[$i]] <= $k) {
                return true;
            }
            $d[$nums[$i]] = $i;
        }
        return false;
    }
}
```

[Continue 0121: Best Time to Buy And Sell Stock](../../0100-0199/0121.Best%20Time%20to%20Buy%20and%20Sell%20Stock/README.md)
# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate)

## Description
<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p style="color: yellow;">Hacker: Return boolean to check if array contains any duplicate</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The element 1 occurs at the indices 0 and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>All elements are distinct.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,3,3,4,3,2,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Solutions

### Solution 1: Sorting

First, we sort the array `nums`.

Then, we traverse the array. If there are two adjacent elements that are the same, it means that there are duplicate elements in the array, and we directly return `true`.

Otherwise, when the traversal ends, we return `false`.

The time complexity is $O(n \times \log n)$, where $n$ is the length of the array `nums`.

#### Du Solution: Cheat
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   def containsDuplicate(self, nums: List[int]) -> bool:
      """
      Compare length of original array vs set that removes duplicates
      """
      return len(nums) != len(set(nums)) 🧠

def main() -> None:
   sol = Solution()
   print(sol.containsDuplicate([1, 2, 3, 1]))
   print(sol.containsDuplicate([1, 2, 3, 4]))
   print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
True
False
True

real    0m0.073s
user    0m0.023s
sys     0m0.005s
```

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Brute Force Solution for the Contains Duplicate problem.
   """
   def containsDuplicate(self, nums: list[int]) -> bool:
      """
      Check if any value appears at least twice in the array.
      
      Args:
         nums (list[int]): Input array.
      
      Returns:
         bool: True if any duplicates exist, False otherwise.
      """
      seen: set[int] = set()            # set() only way to create () is tuple

      for num in nums:
         if num in seen:
            return True
         seen.add(num)                  # dir(seen)
      return False

if __name__ == "__main__":
   sol = Solution()
   print(sol.containsDuplicate([1,2,3,1]))
   print(sol.containsDuplicate([1,2,3,4]))
   print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
True
False
True

real    0m0.023s
user    0m0.019s
sys     0m0.004s
```

#### Du Solution: Brute Force
```python
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   def containsDuplicate(self,nums: List[int]) -> bool:
      for number in range(len(nums)):
         for pointer in range(number + 1, len(nums)):
             if nums[number] == nums[pointer]:
                 return True
      return False

def main() -> None:
   sol = Solution()
   print(sol.containsDuplicate([1,2,3,1]))
   print(sol.containsDuplicate([1,2,3,4]))
   print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ chmod u+x ./pythonScript.py 
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
True
False
True
```

#### JavaScript
```javascript
  /**
   * Cheat way comparing length/size
   * @param {number[]} nums - Input array of integers
   * @returns {boolean} - True if any duplicates exist 
   */                                           // Important: in class remove function keyword ⭐
// CLASS VERSION                                // FUNCTION EXPRESSION VERSION                  // ARROW FUNCTION VERSION
class Solution {                                const containsDuplicate = function(nums) {      const containsDuplicate = (nums) => {
  containsDuplicate(nums) {                      return nums.length !== new Set(nums).size;      return nums.length !== new Set(nums).size;
    return nums.length !== new Set(nums).size;  };                                              };
  }
}

const sol = new Solution();
console.log(sol.containsDuplicate([1, 2, 3, 1]));
console.log(sol.containsDuplicate([1, 2, 3, 4])); 
console.log(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])); 
```

#### JavaScript
```javascript
  /**
   * Brute Force / Hash Set approach for Contains Duplicate
   * @param {number[]} nums - Input array of integers
   * @returns {boolean} - True if any duplicates exist
   */
// CLASS VERSION                    // FUNCTION EXPRESSION VERSION                      // ARROW FUNCTION VERSION
class Solution {                    const containsDuplicate = function(nums) {          const containsDuplicate = (nums) => {
containsDuplicate(nums) {           const seen = new Set();                             const seen = new Set();     // Set(0) {size: 0}
    const seen = new Set();           for (const num of nums) {                           for (const num of nums) { // dir(seen)
    for (const num of nums) {           if (seen.has(num)) {                                if (seen.has(num)) {    // [[Prototype]]: Set
      if (seen.has(num)) {                return true;                                        return true;          //    has: ƒ has()
        return true;                    }                                                   }
      }                                 seen.add(num);                                      seen.add(num);
      seen.add(num);                  }                                                   }
    }                                 return false;                                       return false;
    return false;                   };                                                  };
  }
}

const sol = new Solution();
console.log(sol.containsDuplicate([1,2,3,1]));
console.log(sol.containsDuplicate([1,2,3,4]));
console.log(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]));
```

#### Java: Solution.java

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }
}
```

#### C++: Solution.cpp

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }
};
```

#### Go: Solution.go

```go
func containsDuplicate(nums []int) bool {
	sort.Ints(nums)
	for i, v := range nums[1:] {
		if v == nums[i] {
			return true
		}
	}
	return false
}
```

#### TypeScript: Solution.ts

```ts
function containsDuplicate(nums: number[]): boolean {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    for (let i = 1; i < n; i++) {
        if (nums[i - 1] === nums[i]) {
            return true;
        }
    }
    return false;
}
```

#### Rust: Solution.rs

```rust
impl Solution {
    pub fn contains_duplicate(mut nums: Vec<i32>) -> bool {
        nums.sort();
        let n = nums.len();
        for i in 1..n {
            if nums[i - 1] == nums[i] {
                return true;
            }
        }
        false
    }
}
```

#### JavaScript: Solution.js

```js
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    return new Set(nums).size !== nums.length;
};
```

#### C#: Solution.cs

```cs
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        return nums.Distinct().Count() < nums.Length;
    }
}
```

#### PHP: Solution.php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function containsDuplicate($nums) {
        $numsUnique = array_unique($nums);
        return count($nums) != count($numsUnique);
    }
}
```

#### C: Solution.c

```c
int cmp(const void* a, const void* b) {
    return *(int*) a - *(int*) b;
}

bool containsDuplicate(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    for (int i = 1; i < numsSize; i++) {
        if (nums[i - 1] == nums[i]) {
            return 1;
        }
    }
    return 0;
}
```

### Solution 2: Hash Table

We traverse the array and record the elements that have appeared in the hash table $s$. If an element appears for the second time, it means that there are duplicate elements in the array, and we directly return `true`.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array `nums`.

#### Python3: Solution2.py

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

#### Java: Solution2.java

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            if (!s.add(num)) {
                return true;
            }
        }
        return false;
    }
}
```

#### C++: Solution.cpp

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        return s.size() < nums.size();
    }
};
```

#### Go: Solution2.go

```go
func containsDuplicate(nums []int) bool {
	s := map[int]bool{}
	for _, v := range nums {
		if s[v] {
			return true
		}
		s[v] = true
	}
	return false
}
```

#### TypeScript: Solution2.ts

```ts
function containsDuplicate(nums: number[]): boolean {
    return new Set<number>(nums).size !== nums.length;
}
```

#### Rust: Solution.rs

```rust
use std::collections::HashSet;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        nums.iter().collect::<HashSet<&i32>>().len() != nums.len()
    }
}
```

[Continue 0242: Contains Duplicates](../../0200-0299/0242.Valid%20Anagram/README.md)
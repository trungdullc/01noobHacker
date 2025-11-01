# [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array)

## Description
<p>Given an integer array <code>nums</code> of length <code>n</code>, you want to create an array <code>ans</code> of length <code>2n</code> where <code>ans[i] == nums[i]</code> and <code>ans[i + n] == nums[i]</code> for <code>0 &lt;= i &lt; n</code> (<strong>0-indexed</strong>).</p>

<p>Specifically, <code>ans</code> is the <strong>concatenation</strong> of two <code>nums</code> arrays.</p>

<p>Return <em>the array </em><code>ans</code>.</p>

<p style="color: yellow;">Hacker: Return concatenation of same array called <b>ans</b></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [1,2,1,1,2,1]
<strong>Explanation:</strong> The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,1]
<strong>Output:</strong> [1,3,2,1,1,3,2,1]
<strong>Explanation:</strong> The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

## Solutions

### Solution 1: Simulation

We directly simulate according to the problem description by adding the elements of $\textit{nums}$ to the answer array one by one, and then adding the elements of $\textit{nums}$ to the answer array again.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

#### Du Solution: Python3 cheat solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   """
   Solution for the Concatenation of Array problem
   Note: n: int not even used
   Note: This is array not vector since size given think C/C++
   """
   def getConcatenation(self, nums: List[int]) -> List[int]:
      """
      Concatenate the array with itself.
      
      Args:
         nums (list[int]): Original array.
      
      Returns:
         list[int]: Concatenated array of length 2n.
      """
      return nums + nums 🧠
      # return nums*2 🧠

def main()-> None:
   sol = Solution()
   print(sol.getConcatenation([1,2,1]))
   print(sol.getConcatenation([1,3,2,1]))

if __name__ == "__main__":
   main()
   
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
[1, 2, 1, 1, 2, 1]
[1, 3, 2, 1, 1, 3, 2, 1]
```

#### Du Solution: Python3 cheat solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans: List[int] = []         # Important: start empty ⭐

        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)

        return ans

def main() -> None:
    sol = Solution()
    print(sol.getConcatenation([1,2,1]))
    print(sol.getConcatenation([1,3,2,1])) 

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
[1, 2, 1, 1, 2, 1]
[1, 3, 2, 1, 1, 3, 2, 1]
```

#### Python3: Brute force
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int], n: int) -> List[int]:
      ans: List[int] = [0] * n              # Important: start w/ [0, 0 ...n] ⭐

      for i in range(nums.__len__()):       # loops to length orignal array
         ans[i] = nums[i]                   # First half
         ans[i + int(n/2)] = nums[i]        # Second half
      return ans

if __name__ == "__main__":
   sol = Solution()
   print(sol.getConcatenation([1,2,1], 6))
   print(sol.getConcatenation([1,3,2,1], 8))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 2, 1, 1, 2, 1]
[1, 3, 2, 1, 1, 3, 2, 1]

real    0m0.030s
user    0m0.021s
sys     0m0.009s
```

#### JavaScript
```js
// CLASS VERSION                            // FUNCTION EXPRESSION VERSION                  // ARROW FUNCTION VERSION
                                                                                            // mod solution < Python (loop only half)
class Solution {                            const getConcatenation = function(nums, n) {    const getConcatenation = (nums, n) => {
  getConcatenation(nums, n) {                 const ans = new Array(n);                       const ans = new Array(n);  // ⭐
    const ans = new Array(n);                 for (let i = 0; i < n; i++) {                   for (let i = 0; i < n; i++) {
    for (let i = 0; i < n; i++) {               ans[i] = nums[i % nums.length];                 ans[i] = nums[i % nums.length];  // 🧠
      ans[i] = nums[i % nums.length];         }                                               }
    }                                         return ans;                                     return ans;
    return ans;                             };                                              };
  }
}

const sol = new Solution()
console.log(sol.getConcatenation([1, 2, 1], 6));
console.log(sol.getConcatenation([1, 3, 2, 1], 8));
```

#### Java: Solutions.java

```java
class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n << 1];
        for (int i = 0; i < n << 1; ++i) {
            ans[i] = nums[i % n];
        }
        return ans;
    }
}
```

#### C++: Solution.cpp

```cpp
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        for (int i = 0, n = nums.size(); i < n; ++i) {
            nums.push_back(nums[i]);
        }
        return nums;
    }
};
```

#### Go: Solution.go

```go
func getConcatenation(nums []int) []int {
	return append(nums, nums...)
}
```

#### TypeScript: Solution.ts

```ts
function getConcatenation(nums: number[]): number[] {
    return [...nums, ...nums];
}
```

#### Rust: Solution.rs

```rust
impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        nums.repeat(2)
    }
}
```

#### JavaScript: Solution.js

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function (nums) {
    return [...nums, ...nums];
};
```

#### C: solution.c

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* ans = malloc(sizeof(int) * numsSize * 2);
    for (int i = 0; i < numsSize; i++) {
        ans[i] = ans[i + numsSize] = nums[i];
    }
    *returnSize = numsSize * 2;
    return ans;
}
```

[Continue 0217: Contains Duplicates](../../0200-0299/0217.Contains%20Duplicate/README.md)
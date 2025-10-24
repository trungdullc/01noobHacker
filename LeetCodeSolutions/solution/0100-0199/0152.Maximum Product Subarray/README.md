# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)

## Description

<p>Given an integer array <code>nums</code>, find a <span data-keyword="subarray-nonempty">subarray</span> that has the largest product, and return <em>the product</em>.</p>

<p>The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,-2,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [2,3] has the largest product 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The result cannot be 2, because [-2,-1] is not a subarray.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>The product of any subarray of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

## Solutions

### Solution 1

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution to find the maximum product of any contiguous subarray in an integer array.
   """

   def maxProduct(self, nums: list[int]) -> int:
      """
      Finds the contiguous subarray within an array (containing at least one number)
      which has the largest product.

      Args:
         nums (list[int]): The input array of integers.

      Returns:
         int: The maximum product of any contiguous subarray.
      """
      if not nums:
         return 0

      max_prod = min_prod = result = nums[0]

      for num in nums[1:]:
         if num < 0:
            max_prod, min_prod = min_prod, max_prod
         max_prod = max(num, max_prod * num)
         min_prod = min(num, min_prod * num)
         result = max(result, max_prod)

      return result

if __name__ == "__main__":
   sol = Solution()
   print(sol.maxProduct([2, 3, -2, 4]))
   print(sol.maxProduct([-2, 0, -1]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
6
0

real    0m0.021s
user    0m0.021s
sys     0m0.000s
```

#### Python3

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = f = g = nums[0]
        for x in nums[1:]:
            ff, gg = f, g
            f = max(x, ff * x, gg * x)
            g = min(x, ff * x, gg * x)
            ans = max(ans, f)
        return ans
```

#### Java

```java
class Solution {
    public int maxProduct(int[] nums) {
        int f = nums[0], g = nums[0], ans = nums[0];
        for (int i = 1; i < nums.length; ++i) {
            int ff = f, gg = g;
            f = Math.max(nums[i], Math.max(ff * nums[i], gg * nums[i]));
            g = Math.min(nums[i], Math.min(ff * nums[i], gg * nums[i]));
            ans = Math.max(ans, f);
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int f = nums[0], g = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int ff = f, gg = g;
            f = max({nums[i], ff * nums[i], gg * nums[i]});
            g = min({nums[i], ff * nums[i], gg * nums[i]});
            ans = max(ans, f);
        }
        return ans;
    }
};
```

#### Go

```go
func maxProduct(nums []int) int {
	f, g, ans := nums[0], nums[0], nums[0]
	for _, x := range nums[1:] {
		ff, gg := f, g
		f = max(x, max(ff*x, gg*x))
		g = min(x, min(ff*x, gg*x))
		ans = max(ans, f)
	}
	return ans
}
```

#### TypeScript

```ts
function maxProduct(nums: number[]): number {
    let [f, g, ans] = [nums[0], nums[0], nums[0]];
    for (let i = 1; i < nums.length; ++i) {
        const [ff, gg] = [f, g];
        f = Math.max(nums[i], ff * nums[i], gg * nums[i]);
        g = Math.min(nums[i], ff * nums[i], gg * nums[i]);
        ans = Math.max(ans, f);
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut f = nums[0];
        let mut g = nums[0];
        let mut ans = nums[0];
        for &x in nums.iter().skip(1) {
            let (ff, gg) = (f, g);
            f = x.max(x * ff).max(x * gg);
            g = x.min(x * ff).min(x * gg);
            ans = ans.max(f);
        }
        ans
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    let [f, g, ans] = [nums[0], nums[0], nums[0]];
    for (let i = 1; i < nums.length; ++i) {
        const [ff, gg] = [f, g];
        f = Math.max(nums[i], ff * nums[i], gg * nums[i]);
        g = Math.min(nums[i], ff * nums[i], gg * nums[i]);
        ans = Math.max(ans, f);
    }
    return ans;
};
```

#### C#

```cs
public class Solution {
    public int MaxProduct(int[] nums) {
        int f = nums[0], g = nums[0], ans = nums[0];
        for (int i = 1; i < nums.Length; ++i) {
            int ff = f, gg = g;
            f = Math.Max(nums[i], Math.Max(ff * nums[i], gg * nums[i]));
            g = Math.Min(nums[i], Math.Min(ff * nums[i], gg * nums[i]));
            ans = Math.Max(ans, f);
        }
        return ans;
    }
}
```

[Continue 0139: Word Break](../../0100-0199/0139.Word%20Break/README.md)
# [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray)

## Description

<p>Given a <strong>circular integer array</strong> <code>nums</code> of length <code>n</code>, return <em>the maximum possible sum of a non-empty <strong>subarray</strong> of </em><code>nums</code>.</p>

<p>A <strong>circular array</strong> means the end of the array connects to the beginning of the array. Formally, the next element of <code>nums[i]</code> is <code>nums[(i + 1) % n]</code> and the previous element of <code>nums[i]</code> is <code>nums[(i - 1 + n) % n]</code>.</p>

<p>A <strong>subarray</strong> may only include each element of the fixed buffer <code>nums</code> at most once. Formally, for a subarray <code>nums[i], nums[i + 1], ..., nums[j]</code>, there does not exist <code>i &lt;= k1</code>, <code>k2 &lt;= j</code> with <code>k1 % n == k2 % n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,-2,3,-2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Subarray [3] has maximum sum 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,-3,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Subarray [5,5] has maximum sum 5 + 5 = 10.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,-2,-3]
<strong>Output:</strong> -2
<strong>Explanation:</strong> Subarray [-2] has maximum sum -2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>

## Solutions

### Solution 1: Maintain Prefix Maximum

The maximum sum of a circular subarray can be divided into two cases:

-   Case 1: The subarray with the maximum sum does not include the circular part, which is the ordinary maximum subarray sum;
-   Case 2: The subarray with the maximum sum includes the circular part, which can be transformed into: the total sum of the array minus the minimum subarray sum.

Therefore, we maintain the following variables:

-   The minimum prefix sum $pmi$, initially $0$;
-   The maximum prefix sum $pmx$, initially $-\infty$;
-   The prefix sum $s$, initially $0$;
-   The minimum subarray sum $smi$, initially $\infty$;
-   The answer $ans$, initially $-\infty$.

Next, we only need to traverse the array $nums$. For the current element $x$ we are traversing, we perform the following update operations:

-   Update the prefix sum $s = s + x$;
-   Update the answer $ans = \max(ans, s - pmi)$, which is the answer for Case 1 (the prefix sum $s$ minus the minimum prefix sum $pmi$ can give the maximum subarray sum);
-   Update $smi = \min(smi, s - pmx)$, which is the minimum subarray sum for Case 2;
-   Update $pmi = \min(pmi, s)$, which is the minimum prefix sum;
-   Update $pmx = \max(pmx, s)$, which is the maximum prefix sum.

After the traversal, we return the maximum value of $ans$ and $s - smi$ as the answer.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Computes the maximum sum of a circular subarray.

        Strategy:
        - Max subarray sum can be either:
          1. Standard max subarray (non-circular)
          2. Circular: total sum - min subarray sum
        - Use Kadane's algorithm for both max and min subarray sums.

        Parameters:
            nums (list[int]): Circular integer array.

        Returns:
            int: Maximum sum of a non-empty circular subarray.
        """
        total = sum(nums)
        max_sum = curr_max = nums[0]
        min_sum = curr_min = nums[0]

        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        # If all numbers are negative, max_sum is the answer
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1,-2,3,-2]))
    print(sol.maxSubarraySumCircular([5,-3,5]))    
    print(sol.maxSubarraySumCircular([-3,-2,-3]))  

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
10
-2

real    0m0.049s
user    0m0.027s
sys     0m0.000s
```

#### Python3

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pmi, pmx = 0, -inf
        ans, s, smi = -inf, 0, inf
        for x in nums:
            s += x
            ans = max(ans, s - pmi)
            smi = min(smi, s - pmx)
            pmi = min(pmi, s)
            pmx = max(pmx, s)
        return max(ans, s - smi)
```

#### Java

```java
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        final int inf = 1 << 30;
        int pmi = 0, pmx = -inf;
        int ans = -inf, s = 0, smi = inf;
        for (int x : nums) {
            s += x;
            ans = Math.max(ans, s - pmi);
            smi = Math.min(smi, s - pmx);
            pmi = Math.min(pmi, s);
            pmx = Math.max(pmx, s);
        }
        return Math.max(ans, s - smi);
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        const int inf = 1 << 30;
        int pmi = 0, pmx = -inf;
        int ans = -inf, s = 0, smi = inf;
        for (int x : nums) {
            s += x;
            ans = max(ans, s - pmi);
            smi = min(smi, s - pmx);
            pmi = min(pmi, s);
            pmx = max(pmx, s);
        }
        return max(ans, s - smi);
    }
};
```

#### Go

```go
func maxSubarraySumCircular(nums []int) int {
	const inf = 1 << 30
	pmi, pmx := 0, -inf
	ans, s, smi := -inf, 0, inf
	for _, x := range nums {
		s += x
		ans = max(ans, s-pmi)
		smi = min(smi, s-pmx)
		pmi = min(pmi, s)
		pmx = max(pmx, s)
	}
	return max(ans, s-smi)
}
```

#### TypeScript

```ts
function maxSubarraySumCircular(nums: number[]): number {
    let [pmi, pmx] = [0, -Infinity];
    let [ans, s, smi] = [-Infinity, 0, Infinity];
    for (const x of nums) {
        s += x;
        ans = Math.max(ans, s - pmi);
        smi = Math.min(smi, s - pmx);
        pmi = Math.min(pmi, s);
        pmx = Math.max(pmx, s);
    }
    return Math.max(ans, s - smi);
}
```

[Continue 0978: Longest Turbulent Subarray](../../0900-0999/0978.Longest%20Turbulent%20Subarray/README.md)
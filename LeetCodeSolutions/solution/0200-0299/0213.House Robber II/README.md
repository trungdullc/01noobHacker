# [213. House Robber II](https://leetcode.com/problems/house-robber-ii) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

## Solutions

### Solution 1: Dynamic Programming

The circular arrangement means that at most one of the first and last houses can be chosen for theft, so this circular arrangement problem can be reduced to two single-row house problems.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Computes the maximum amount of money that can be robbed in a circular street.
        Since the first and last houses are adjacent, we cannot rob both.
        
        Approach:
        - Reduce problem to two linear House Robber I problems:
            1. Rob houses 0 to n-2
            2. Rob houses 1 to n-1
        - Return the maximum of the two cases.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Helper function for linear houses
        def rob_linear(houses: list[int]) -> int:
            prev1 = prev2 = 0
            for val in houses:
                new_val = max(prev1, prev2 + val)
                prev2, prev1 = prev1, new_val
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

if __name__ == "__main__":
    sol = Solution()
    print("Example 1 Output:", sol.rob([2,3,2]))
    nums2 = [1,2,3,1]
    print("Example 2 Output:", sol.rob( [1,2,3,1]))
    nums3 = [1,2,3]
    print("Example 3 Output:", sol.rob([1,2,3]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
Example 1 Output: 3
Example 2 Output: 4
Example 3 Output: 3

real    0m0.024s
user    0m0.020s
sys     0m0.004s
```

#### Python3

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(nums):
            f = g = 0
            for x in nums:
                f, g = max(f, g), f + x
            return max(f, g)

        if len(nums) == 1:
            return nums[0]
        return max(_rob(nums[1:]), _rob(nums[:-1]))
```

#### Java

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return nums[0];
        }
        return Math.max(rob(nums, 0, n - 2), rob(nums, 1, n - 1));
    }

    private int rob(int[] nums, int l, int r) {
        int f = 0, g = 0;
        for (; l <= r; ++l) {
            int ff = Math.max(f, g);
            g = f + nums[l];
            f = ff;
        }
        return Math.max(f, g);
    }
}
```

#### C++

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        return max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }

    int robRange(vector<int>& nums, int l, int r) {
        int f = 0, g = 0;
        for (; l <= r; ++l) {
            int ff = max(f, g);
            g = f + nums[l];
            f = ff;
        }
        return max(f, g);
    }
};
```

#### Go

```go
func rob(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	return max(robRange(nums, 0, n-2), robRange(nums, 1, n-1))
}

func robRange(nums []int, l, r int) int {
	f, g := 0, 0
	for _, x := range nums[l : r+1] {
		f, g = max(f, g), f+x
	}
	return max(f, g)
}
```

#### TypeScript

```ts
function rob(nums: number[]): number {
    const n = nums.length;
    if (n === 1) {
        return nums[0];
    }
    const robRange = (l: number, r: number): number => {
        let [f, g] = [0, 0];
        for (; l <= r; ++l) {
            [f, g] = [Math.max(f, g), f + nums[l]];
        }
        return Math.max(f, g);
    };
    return Math.max(robRange(0, n - 2), robRange(1, n - 1));
}
```

#### Rust

```rust
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return nums[0];
        }
        let rob_range = |l, r| {
            let mut f = [0, 0];
            for i in l..r {
                f = [f[0].max(f[1]), f[0] + nums[i]];
            }
            f[0].max(f[1])
        };
        rob_range(0, n - 1).max(rob_range(1, n))
    }
}
```

[Continue 0005: Longest Palindromic Substring](../../0000-0099/0005.Longest%20Palindromic%20Substring/README.md)
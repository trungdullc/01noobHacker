# [312. Burst Balloons](https://leetcode.com/problems/burst-balloons)

## Description

<p>You are given <code>n</code> balloons, indexed from <code>0</code> to <code>n - 1</code>. Each balloon is painted with a number on it represented by an array <code>nums</code>. You are asked to burst all the balloons.</p>

<p>If you burst the <code>i<sup>th</sup></code> balloon, you will get <code>nums[i - 1] * nums[i] * nums[i + 1]</code> coins. If <code>i - 1</code> or <code>i + 1</code> goes out of bounds of the array, then treat it as if there is a balloon with a <code>1</code> painted on it.</p>

<p>Return <em>the maximum coins you can collect by bursting the balloons wisely</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,5,8]
<strong>Output:</strong> 167
<strong>Explanation:</strong>
nums = [3,1,5,8] --&gt; [3,5,8] --&gt; [3,8] --&gt; [8] --&gt; []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5]
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

## Solutions

### Solution 1: Dynamic Programming

Let's denote the length of the array `nums` as $n$. According to the problem description, we can add a $1$ to both ends of the array `nums`, denoted as `arr`.

Then, we define $f[i][j]$ as the maximum number of coins we can get by bursting all the balloons in the interval $[i, j]$. Therefore, the answer is $f[0][n+1]$.

For $f[i][j]$, we enumerate all positions $k$ in the interval $[i, j]$. Suppose $k$ is the last balloon to burst, then we can get the following state transition equation:

$$
f[i][j] = \max(f[i][j], f[i][k] + f[k][j] + arr[i] \times arr[k] \times arr[j])
$$

In implementation, since the state transition equation of $f[i][j]$ involves $f[i][k]$ and $f[k][j]$, where $i < k < j$, we need to traverse $i$ from large to small and $j$ from small to large. This ensures that when calculating $f[i][j]$, $f[i][k]$ and $f[k][j]$ have already been calculated.

Finally, we return $f[0][n+1]$.

The time complexity is $O(n^3)$, and the space complexity is $O(n^2)$. Where $n$ is the length of the array `nums`.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """
        Computes the maximum coins obtained by bursting balloons wisely.

        Strategy:
        - Use dynamic programming.
        - Consider bursting the last balloon in a subarray to simplify calculations.
        - dp[left][right] = max coins from bursting balloons in nums[left:right+1]

        Parameters:
            nums (list[int]): List of integers representing balloons.

        Returns:
            int: Maximum coins that can be collected.
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(1, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left - 1] * nums[k] * nums[right + 1] + dp[left][k - 1] + dp[k + 1][right]
                    )
        return dp[1][n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCoins([3,1,5,8]))
    print(sol.maxCoins([1,5]))   
    
AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
167
10

real    0m0.023s
user    0m0.014s
sys     0m0.009s
```

#### Python3

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] + nums + [1]
        f = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j])
        return f[0][-1]
```

#### Java

```java
class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n + 2];
        arr[0] = 1;
        arr[n + 1] = 1;
        System.arraycopy(nums, 0, arr, 1, n);
        int[][] f = new int[n + 2][n + 2];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 2; j <= n + 1; j++) {
                for (int k = i + 1; k < j; k++) {
                    f[i][j] = Math.max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j]);
                }
            }
        }
        return f[0][n + 1];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr(n + 2, 1);
        for (int i = 0; i < n; ++i) {
            arr[i + 1] = nums[i];
        }

        vector<vector<int>> f(n + 2, vector<int>(n + 2, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i + 2; j <= n + 1; ++j) {
                for (int k = i + 1; k < j; ++k) {
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j]);
                }
            }
        }
        return f[0][n + 1];
    }
};
```

#### Go

```go
func maxCoins(nums []int) int {
    n := len(nums)
    arr := make([]int, n+2)
    arr[0] = 1
    arr[n+1] = 1
    copy(arr[1:], nums)

    f := make([][]int, n+2)
    for i := range f {
        f[i] = make([]int, n+2)
    }

    for i := n - 1; i >= 0; i-- {
        for j := i + 2; j <= n+1; j++ {
            for k := i + 1; k < j; k++ {
                f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i]*arr[k]*arr[j])
            }
        }
    }

    return f[0][n+1]
}
```

#### TypeScript

```ts
function maxCoins(nums: number[]): number {
    const n = nums.length;
    const arr = Array(n + 2).fill(1);
    for (let i = 0; i < n; i++) {
        arr[i + 1] = nums[i];
    }

    const f: number[][] = Array.from({ length: n + 2 }, () => Array(n + 2).fill(0));
    for (let i = n - 1; i >= 0; i--) {
        for (let j = i + 2; j <= n + 1; j++) {
            for (let k = i + 1; k < j; k++) {
                f[i][j] = Math.max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j]);
            }
        }
    }
    return f[0][n + 1];
}
```

#### Rust

```rust
impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut arr = vec![1; n + 2];
        for i in 0..n {
            arr[i + 1] = nums[i];
        }

        let mut f = vec![vec![0; n + 2]; n + 2];
        for i in (0..n).rev() {
            for j in i + 2..n + 2 {
                for k in i + 1..j {
                    f[i][j] = f[i][j].max(f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j]);
                }
            }
        }
        f[0][n + 1]
    }
}
```

[Continue 0010: Regular Expression Matching](../../0000-0099/0010.Regular%20Expression%20Matching/README.md)
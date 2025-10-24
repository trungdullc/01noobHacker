# [978. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray)

## Description

<p>Given an integer array <code>arr</code>, return <em>the length of a maximum size turbulent subarray of</em> <code>arr</code>.</p>

<p>A subarray is <strong>turbulent</strong> if the comparison sign flips between each adjacent pair of elements in the subarray.</p>

<p>More formally, a subarray <code>[arr[i], arr[i + 1], ..., arr[j]]</code> of <code>arr</code> is said to be turbulent if and only if:</p>

<ul>
	<li>For <code>i &lt;= k &lt; j</code>:

    <ul>
    	<li><code>arr[k] &gt; arr[k + 1]</code> when <code>k</code> is odd, and</li>
    	<li><code>arr[k] &lt; arr[k + 1]</code> when <code>k</code> is even.</li>
    </ul>
    </li>
    <li>Or, for <code>i &lt;= k &lt; j</code>:
    <ul>
    	<li><code>arr[k] &gt; arr[k + 1]</code> when <code>k</code> is even, and</li>
    	<li><code>arr[k] &lt; arr[k + 1]</code> when <code>k</code> is odd.</li>
    </ul>
    </li>

</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [9,4,2,10,7,8,8,1,9]
<strong>Output:</strong> 5
<strong>Explanation:</strong> arr[1] &gt; arr[2] &lt; arr[3] &gt; arr[4] &lt; arr[5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,8,12,16]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [100]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## Solutions

### Solution 1: Dynamic Programming

We define $f[i]$ as the length of the longest turbulent subarray ending at $\textit{nums}[i]$ with an increasing state, and $g[i]$ as the length of the longest turbulent subarray ending at $\textit{nums}[i]$ with a decreasing state. Initially, $f[0] = 1$, $g[0] = 1$. The answer is $\max(f[i], g[i])$.

For $i \gt 0$, if $\textit{nums}[i] \gt \textit{nums}[i - 1]$, then $f[i] = g[i - 1] + 1$, otherwise $f[i] = 1$; if $\textit{nums}[i] \lt \textit{nums}[i - 1]$, then $g[i] = f[i - 1] + 1$, otherwise $g[i] = 1$.

Since $f[i]$ and $g[i]$ are only related to $f[i - 1]$ and $g[i - 1]$, two variables can be used instead of arrays.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        """
        Returns the length of the longest turbulent subarray.

        A subarray is turbulent if the comparison sign between adjacent elements
        alternates (>, <) or (<, >) throughout the subarray.

        Parameters:
            arr (list[int]): Input array of integers.

        Returns:
            int: Maximum length of a turbulent subarray.
        """
        if not arr:
            return 0

        n = len(arr)
        max_len = 1
        left = 0

        for right in range(1, n):
            cmp = (arr[right-1] < arr[right]) - (arr[right-1] > arr[right])
            if cmp == 0:
                left = right
            elif right == n-1 or cmp * ((arr[right] < arr[right+1]) - (arr[right] > arr[right+1])) != -1:
                max_len = max(max_len, right - left + 1)
                left = right

        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
    print(sol.maxTurbulenceSize([4,8,12,16]))         
    print(sol.maxTurbulenceSize([100]))               

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
5
2
1

real    0m0.023s
user    0m0.009s
sys     0m0.014s
```

#### Python3

```python
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = f = g = 1
        for a, b in pairwise(arr):
            ff = g + 1 if a < b else 1
            gg = f + 1 if a > b else 1
            f, g = ff, gg
            ans = max(ans, f, g)
        return ans
```

#### Java

```java
class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int ans = 1, f = 1, g = 1;
        for (int i = 1; i < arr.length; ++i) {
            int ff = arr[i - 1] < arr[i] ? g + 1 : 1;
            int gg = arr[i - 1] > arr[i] ? f + 1 : 1;
            f = ff;
            g = gg;
            ans = Math.max(ans, Math.max(f, g));
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int ans = 1, f = 1, g = 1;
        for (int i = 1; i < arr.size(); ++i) {
            int ff = arr[i - 1] < arr[i] ? g + 1 : 1;
            int gg = arr[i - 1] > arr[i] ? f + 1 : 1;
            f = ff;
            g = gg;
            ans = max({ans, f, g});
        }
        return ans;
    }
};
```

#### Go

```go
func maxTurbulenceSize(arr []int) int {
	ans, f, g := 1, 1, 1
	for i, x := range arr[1:] {
		ff, gg := 1, 1
		if arr[i] < x {
			ff = g + 1
		}
		if arr[i] > x {
			gg = f + 1
		}
		f, g = ff, gg
		ans = max(ans, max(f, g))
	}
	return ans
}
```

#### TypeScript

```ts
function maxTurbulenceSize(arr: number[]): number {
    let f = 1;
    let g = 1;
    let ans = 1;
    for (let i = 1; i < arr.length; ++i) {
        const ff = arr[i - 1] < arr[i] ? g + 1 : 1;
        const gg = arr[i - 1] > arr[i] ? f + 1 : 1;
        f = ff;
        g = gg;
        ans = Math.max(ans, f, g);
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn max_turbulence_size(arr: Vec<i32>) -> i32 {
        let mut ans = 1;
        let mut f = 1;
        let mut g = 1;

        for i in 1..arr.len() {
            let ff = if arr[i - 1] < arr[i] { g + 1 } else { 1 };
            let gg = if arr[i - 1] > arr[i] { f + 1 } else { 1 };
            f = ff;
            g = gg;
            ans = ans.max(f.max(g));
        }

        ans
    }
}
```

[Continue 0055: Jump Game](../../0000-0099/0055.Jump%20Game/README.md)
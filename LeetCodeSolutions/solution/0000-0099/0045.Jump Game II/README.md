# [45. Jump Game II](https://leetcode.com/problems/jump-game-ii) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code> of length <code>n</code>. You are initially positioned at <code>nums[0]</code>.</p>

<p>Each element <code>nums[i]</code> represents the maximum length of a forward jump from index <code>i</code>. In other words, if you are at <code>nums[i]</code>, you can jump to any <code>nums[i + j]</code> where:</p>

<ul>
	<li><code>0 &lt;= j &lt;= nums[i]</code> and</li>
	<li><code>i + j &lt; n</code></li>
</ul>

<p>Return <em>the minimum number of jumps to reach </em><code>nums[n - 1]</code>. The test cases are generated such that you can reach <code>nums[n - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li>It&#39;s guaranteed that you can reach <code>nums[n - 1]</code>.</li>
</ul>

## Solutions

### Solution 1: Greedy Algorithm

We can use a variable $mx$ to record the farthest position that can be reached from the current position, a variable $last$ to record the position of the last jump, and a variable $ans$ to record the number of jumps.

Next, we traverse each position $i$ in $[0,..n - 2]$. For each position $i$, we can calculate the farthest position that can be reached from the current position through $i + nums[i]$. We use $mx$ to record this farthest position, that is, $mx = max(mx, i + nums[i])$. Then, we check whether the current position has reached the boundary of the last jump, that is, $i = last$. If it has reached, then we need to make a jump, update $last$ to $mx$, and increase the number of jumps $ans$ by $1$.

Finally, we return the number of jumps $ans$.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

Similar problems:

-   [55. Jump Game](https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0055.Jump%20Game/README_EN.md)
-   [1024. Video Stitching](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1024.Video%20Stitching/README_EN.md)
-   [1326. Minimum Number of Taps to Open to Water a Garden](https://github.com/doocs/leetcode/blob/main/solution/1300-1399/1326.Minimum%20Number%20of%20Taps%20to%20Open%20to%20Water%20a%20Garden/README_EN.md)

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Returns the minimum number of jumps to reach the last index.

        Uses a greedy approach:
        - Track the farthest reachable index within the current jump (end of current range).
        - When reaching the end of current range, increment jump count and update range.

        Parameters:
            nums (list[int]): Array where each element is max jump length.

        Returns:
            int: Minimum number of jumps to reach the last index.
        """
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2,3,1,1,4]))
    print(sol.jump([2,3,0,1,4]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
2
2

real    0m0.023s
user    0m0.008s
sys     0m0.015s
```

#### Python3

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = mx = last = 0
        for i, x in enumerate(nums[:-1]):
            mx = max(mx, i + x)
            if last == i:
                ans += 1
                last = mx
        return ans
```

#### Java

```java
class Solution {
    public int jump(int[] nums) {
        int ans = 0, mx = 0, last = 0;
        for (int i = 0; i < nums.length - 1; ++i) {
            mx = Math.max(mx, i + nums[i]);
            if (last == i) {
                ++ans;
                last = mx;
            }
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int ans = 0, mx = 0, last = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            mx = max(mx, i + nums[i]);
            if (last == i) {
                ++ans;
                last = mx;
            }
        }
        return ans;
    }
};
```

#### Go

```go
func jump(nums []int) (ans int) {
	mx, last := 0, 0
	for i, x := range nums[:len(nums)-1] {
		mx = max(mx, i+x)
		if last == i {
			ans++
			last = mx
		}
	}
	return
}
```

#### TypeScript

```ts
function jump(nums: number[]): number {
    let [ans, mx, last] = [0, 0, 0];
    for (let i = 0; i < nums.length - 1; ++i) {
        mx = Math.max(mx, i + nums[i]);
        if (last === i) {
            ++ans;
            last = mx;
        }
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut mx = 0;
        let mut last = 0;
        for i in 0..(nums.len() - 1) {
            mx = mx.max(i as i32 + nums[i]);
            if last == i as i32 {
                ans += 1;
                last = mx;
            }
        }
        ans
    }
}
```

#### C#

```cs
public class Solution {
    public int Jump(int[] nums) {
        int ans = 0, mx = 0, last = 0;
        for (int i = 0; i < nums.Length - 1; ++i) {
            mx = Math.Max(mx, i + nums[i]);
            if (last == i) {
                ++ans;
                last = mx;
            }
        }
        return ans;
    }
}
```

#### C

```c
int jump(int* nums, int numsSize) {
    int ans = 0;
    int mx = 0;
    int last = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        mx = (mx > i + nums[i]) ? mx : (i + nums[i]);
        if (last == i) {
            ++ans;
            last = mx;
        }
    }
    return ans;
}
```

#### PHP

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function jump($nums) {
        $ans = 0;
        $mx = 0;
        $last = 0;

        for ($i = 0; $i < count($nums) - 1; $i++) {
            $mx = max($mx, $i + $nums[$i]);
            if ($last == $i) {
                $ans++;
                $last = $mx;
            }
        }

        return $ans;
    }
}
```

[Continue 1871: Jump Game VII](../../1800-1899/1871.Jump%20Game%20VII/README.md)
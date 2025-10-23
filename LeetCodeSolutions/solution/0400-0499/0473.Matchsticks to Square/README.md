# [473. Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square)

## Description

<p>You are given an integer array <code>matchsticks</code> where <code>matchsticks[i]</code> is the length of the <code>i<sup>th</sup></code> matchstick. You want to use <strong>all the matchsticks</strong> to make one square. You <strong>should not break</strong> any stick, but you can link them up, and each matchstick must be used <strong>exactly one time</strong>.</p>

<p>Return <code>true</code> if you can make this square and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0473.Matchsticks%20to%20Square/images/matchsticks1-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> matchsticks = [1,1,2,2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can form a square with length 2, one side of the square came two sticks with length 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matchsticks = [3,3,3,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You cannot find a way to form a square with all the matchsticks.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= matchsticks.length &lt;= 15</code></li>
	<li><code>1 &lt;= matchsticks[i] &lt;= 10<sup>8</sup></code></li>
</ul>

## Solutions

### Solution 1

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from typing import List

class Solution:
    """
    Determine if matchsticks can form a square using all sticks exactly once.
    """
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        matchsticks.sort(reverse=True)  # Optimization: try bigger sticks first

        sides = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                # Check if all sides are equal to target
                return all(side == side_length for side in sides)
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                # Prune: if side[i] is 0, no need to try next empty side
                if sides[i] == 0:
                    break
            return False

        return dfs(0)

def main():
    sol = Solution()
    print(sol.makesquare([1,1,2,2,2]))
    print(sol.makesquare([3,3,3,3,4]))

if __name__ == "__main__":
    main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
True
False

real    0m0.035s
user    0m0.034s
sys     0m0.000s
```

#### Python3

```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(u):
            if u == len(matchsticks):
                return True
            for i in range(4):
                if i > 0 and edges[i - 1] == edges[i]:
                    continue
                edges[i] += matchsticks[u]
                if edges[i] <= x and dfs(u + 1):
                    return True
                edges[i] -= matchsticks[u]
            return False

        x, mod = divmod(sum(matchsticks), 4)
        if mod or x < max(matchsticks):
            return False
        edges = [0] * 4
        matchsticks.sort(reverse=True)
        return dfs(0)
```

#### Java

```java
class Solution {
    public boolean makesquare(int[] matchsticks) {
        int s = 0, mx = 0;
        for (int v : matchsticks) {
            s += v;
            mx = Math.max(mx, v);
        }
        int x = s / 4, mod = s % 4;
        if (mod != 0 || x < mx) {
            return false;
        }
        Arrays.sort(matchsticks);
        int[] edges = new int[4];
        return dfs(matchsticks.length - 1, x, matchsticks, edges);
    }

    private boolean dfs(int u, int x, int[] matchsticks, int[] edges) {
        if (u < 0) {
            return true;
        }
        for (int i = 0; i < 4; ++i) {
            if (i > 0 && edges[i - 1] == edges[i]) {
                continue;
            }
            edges[i] += matchsticks[u];
            if (edges[i] <= x && dfs(u - 1, x, matchsticks, edges)) {
                return true;
            }
            edges[i] -= matchsticks[u];
        }
        return false;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int s = 0, mx = 0;
        for (int& v : matchsticks) {
            s += v;
            mx = max(mx, v);
        }
        int x = s / 4, mod = s % 4;
        if (mod != 0 || x < mx) return false;
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
        vector<int> edges(4);
        return dfs(0, x, matchsticks, edges);
    }

    bool dfs(int u, int x, vector<int>& matchsticks, vector<int>& edges) {
        if (u == matchsticks.size()) return true;
        for (int i = 0; i < 4; ++i) {
            if (i > 0 && edges[i - 1] == edges[i]) continue;
            edges[i] += matchsticks[u];
            if (edges[i] <= x && dfs(u + 1, x, matchsticks, edges)) return true;
            edges[i] -= matchsticks[u];
        }
        return false;
    }
};
```

#### Go

```go
func makesquare(matchsticks []int) bool {
	s := 0
	for _, v := range matchsticks {
		s += v
	}
	if s%4 != 0 {
		return false
	}
	sort.Sort(sort.Reverse(sort.IntSlice(matchsticks)))
	edges := make([]int, 4)
	var dfs func(u, x int) bool
	dfs = func(u, x int) bool {
		if u == len(matchsticks) {
			return true
		}
		for i := 0; i < 4; i++ {
			if i > 0 && edges[i-1] == edges[i] {
				continue
			}
			edges[i] += matchsticks[u]
			if edges[i] <= x && dfs(u+1, x) {
				return true
			}
			edges[i] -= matchsticks[u]
		}
		return false
	}
	return dfs(0, s/4)
}
```

#### Rust

```rust
impl Solution {
    pub fn makesquare(matchsticks: Vec<i32>) -> bool {
        let mut matchsticks = matchsticks;

        fn dfs(matchsticks: &Vec<i32>, edges: &mut [i32; 4], u: usize, x: i32) -> bool {
            if u == matchsticks.len() {
                return true;
            }
            for i in 0..4 {
                if i > 0 && edges[i - 1] == edges[i] {
                    continue;
                }
                edges[i] += matchsticks[u];
                if edges[i] <= x && dfs(matchsticks, edges, u + 1, x) {
                    return true;
                }
                edges[i] -= matchsticks[u];
            }
            false
        }

        let sum: i32 = matchsticks.iter().sum();
        if sum % 4 != 0 {
            return false;
        }
        matchsticks.sort_by(|x, y| y.cmp(x));
        let mut edges = [0; 4];

        dfs(&matchsticks, &mut edges, 0, sum / 4)
    }
}
```

### Solution 2

#### Python3

```python
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        @cache
        def dfs(state, t):
            if state == (1 << len(matchsticks)) - 1:
                return True
            for i, v in enumerate(matchsticks):
                if state & (1 << i):
                    continue
                if t + v > s:
                    break
                if dfs(state | (1 << i), (t + v) % s):
                    return True
            return False

        s, mod = divmod(sum(matchsticks), 4)
        matchsticks.sort()
        if mod:
            return False
        return dfs(0, 0)
```

[Continue 0698: Partition to K Equal Sum Subsets](../../0600-0699/0698.Partition%20to%20K%20Equal%20Sum%20Subsets/README.md)
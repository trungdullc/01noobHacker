# [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>&#39;s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>The <strong>area</strong> of an island is the number of cells with a value <code>1</code> in the island.</p>

<p>Return <em>the maximum <strong>area</strong> of an island in </em><code>grid</code>. If there is no island, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0600-0699/0695.Max%20Area%20of%20Island/images/maxarea1-grid.jpg" style="width: 500px; height: 310px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The answer is not 11, because the island must be connected 4-directionally.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
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
    Provides a method to find the maximum area of an island in a binary grid.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Returns the maximum area (number of connected 1's) of an island in the grid.

        Args:
            grid (List[List[int]]): 2D binary grid.

        Returns:
            int: Maximum area of any island.
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = 0  # mark visited
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area

if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print(sol.maxAreaOfIsland(grid1))

    grid2 = [[0,0,0,0,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid2))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
6
0

real    0m0.090s
user    0m0.021s
sys     0m0.009s
```

#### Python3

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if grid[i][j] == 0:
                return 0
            ans = 1
            grid[i][j] = 0
            dirs = (-1, 0, 1, 0, -1)
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n:
                    ans += dfs(x, y)
            return ans

        m, n = len(grid), len(grid[0])
        return max(dfs(i, j) for i in range(m) for j in range(n))
```

#### Java

```java
class Solution {
    private int m;
    private int n;
    private int[][] grid;

    public int maxAreaOfIsland(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        this.grid = grid;
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans = Math.max(ans, dfs(i, j));
            }
        }
        return ans;
    }

    private int dfs(int i, int j) {
        if (grid[i][j] == 0) {
            return 0;
        }
        int ans = 1;
        grid[i][j] = 0;
        int[] dirs = {-1, 0, 1, 0, -1};
        for (int k = 0; k < 4; ++k) {
            int x = i + dirs[k], y = j + dirs[k + 1];
            if (x >= 0 && x < m && y >= 0 && y < n) {
                ans += dfs(x, y);
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
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int dirs[5] = {-1, 0, 1, 0, -1};
        int ans = 0;
        function<int(int, int)> dfs = [&](int i, int j) {
            if (grid[i][j] == 0) {
                return 0;
            }
            int ans = 1;
            grid[i][j] = 0;
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k], y = j + dirs[k + 1];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    ans += dfs(x, y);
                }
            }
            return ans;
        };
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans = max(ans, dfs(i, j));
            }
        }
        return ans;
    }
};
```

#### Go

```go
func maxAreaOfIsland(grid [][]int) (ans int) {
	m, n := len(grid), len(grid[0])
	dirs := [5]int{-1, 0, 1, 0, -1}
	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if grid[i][j] == 0 {
			return 0
		}
		ans := 1
		grid[i][j] = 0
		for k := 0; k < 4; k++ {
			x, y := i+dirs[k], j+dirs[k+1]
			if x >= 0 && x < m && y >= 0 && y < n {
				ans += dfs(x, y)
			}
		}
		return ans
	}
	for i := range grid {
		for j := range grid[i] {
			ans = max(ans, dfs(i, j))
		}
	}
	return
}
```

#### TypeScript

```ts
function maxAreaOfIsland(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const dirs = [-1, 0, 1, 0, -1];
    const dfs = (i: number, j: number): number => {
        if (grid[i][j] === 0) {
            return 0;
        }
        let ans = 1;
        grid[i][j] = 0;
        for (let k = 0; k < 4; ++k) {
            const [x, y] = [i + dirs[k], j + dirs[k + 1]];
            if (x >= 0 && x < m && y >= 0 && y < n) {
                ans += dfs(x, y);
            }
        }
        return ans;
    };
    let ans = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            ans = Math.max(ans, dfs(i, j));
        }
    }
    return ans;
}
```

#### Rust

```rust
impl Solution {
    fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize) -> i32 {
        if i == grid.len() || j == grid[0].len() || grid[i][j] == 0 {
            return 0;
        }
        grid[i][j] = 0;
        let mut res = 1 + Self::dfs(grid, i + 1, j) + Self::dfs(grid, i, j + 1);
        if i != 0 {
            res += Self::dfs(grid, i - 1, j);
        }
        if j != 0 {
            res += Self::dfs(grid, i, j - 1);
        }
        res
    }

    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut res = 0;
        for i in 0..m {
            for j in 0..n {
                res = res.max(Self::dfs(&mut grid, i, j));
            }
        }
        res
    }
}
```

[Continue 0133: Clone Graph](../../0100-0199/0133.Clone%20Graph/README.md)
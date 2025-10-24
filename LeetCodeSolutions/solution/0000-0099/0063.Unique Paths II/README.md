# [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii)

## Description

<p>You are given an <code>m x n</code> integer array <code>grid</code>. There is a robot initially located at the <b>top-left corner</b> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>An obstacle and space are marked as <code>1</code> or <code>0</code> respectively in <code>grid</code>. A path that the robot takes cannot include <strong>any</strong> square that is an obstacle.</p>

<p>Return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The testcases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0063.Unique%20Paths%20II/images/robot1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0063.Unique%20Paths%20II/images/robot2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,1],[0,0]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == obstacleGrid.length</code></li>
	<li><code>n == obstacleGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>obstacleGrid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>

## Solutions

### Solution 1: Memoization Search

We design a function $\textit{dfs}(i, j)$ to represent the number of paths from the grid $(i, j)$ to the grid $(m - 1, n - 1)$. Here, $m$ and $n$ are the number of rows and columns of the grid, respectively.

The execution process of the function $\textit{dfs}(i, j)$ is as follows:

-   If $i \ge m$ or $j \ge n$, or $\textit{obstacleGrid}[i][j] = 1$, the number of paths is $0$;
-   If $i = m - 1$ and $j = n - 1$, the number of paths is $1$;
-   Otherwise, the number of paths is $\textit{dfs}(i + 1, j) + \textit{dfs}(i, j + 1)$.

To avoid redundant calculations, we can use memoization.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the grid, respectively.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """
        Calculates the number of unique paths from the top-left corner to the
        bottom-right corner of a grid, avoiding obstacles. The robot can move
        only right or down. Cells with a value of 1 are obstacles and cannot
        be entered.

        Parameters:
            obstacleGrid (list[list[int]]): A 2D grid where:
                - 0 represents a free cell
                - 1 represents an obstacle
        
        Returns:
            int: The total number of unique valid paths. Guaranteed <= 2 * 10^9.
        """

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If start or end is blocked, no paths exist.
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # DP table
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # starting position

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))            

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
2
1

real    0m0.027s
user    0m0.023s
sys     0m0.004s
```

#### Python3

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n or obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(0, 0)
```

#### Java

```java
class Solution {
    private Integer[][] f;
    private int[][] obstacleGrid;
    private int m;
    private int n;

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        m = obstacleGrid.length;
        n = obstacleGrid[0].length;
        this.obstacleGrid = obstacleGrid;
        f = new Integer[m][n];
        return dfs(0, 0);
    }

    private int dfs(int i, int j) {
        if (i >= m || j >= n || obstacleGrid[i][j] == 1) {
            return 0;
        }
        if (i == m - 1 && j == n - 1) {
            return 1;
        }
        if (f[i][j] == null) {
            f[i][j] = dfs(i + 1, j) + dfs(i, j + 1);
        }
        return f[i][j];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> f(m, vector<int>(n, -1));
        auto dfs = [&](this auto&& dfs, int i, int j) {
            if (i >= m || j >= n || obstacleGrid[i][j]) {
                return 0;
            }
            if (i == m - 1 && j == n - 1) {
                return 1;
            }
            if (f[i][j] == -1) {
                f[i][j] = dfs(i + 1, j) + dfs(i, j + 1);
            }
            return f[i][j];
        };
        return dfs(0, 0);
    }
};
```

#### Go

```go
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m, n := len(obstacleGrid), len(obstacleGrid[0])
	f := make([][]int, m)
	for i := range f {
		f[i] = make([]int, n)
		for j := range f[i] {
			f[i][j] = -1
		}
	}
	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if i >= m || j >= n || obstacleGrid[i][j] == 1 {
			return 0
		}
		if i == m-1 && j == n-1 {
			return 1
		}
		if f[i][j] == -1 {
			f[i][j] = dfs(i+1, j) + dfs(i, j+1)
		}
		return f[i][j]
	}
	return dfs(0, 0)
}
```

#### TypeScript

```ts
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const f: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
    const dfs = (i: number, j: number): number => {
        if (i >= m || j >= n || obstacleGrid[i][j] === 1) {
            return 0;
        }
        if (i === m - 1 && j === n - 1) {
            return 1;
        }
        if (f[i][j] === -1) {
            f[i][j] = dfs(i + 1, j) + dfs(i, j + 1);
        }
        return f[i][j];
    };
    return dfs(0, 0);
}
```

#### Rust

```rust
impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut f = vec![vec![-1; n]; m];
        Self::dfs(0, 0, &obstacle_grid, &mut f)
    }

    fn dfs(i: usize, j: usize, obstacle_grid: &Vec<Vec<i32>>, f: &mut Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        if i >= m || j >= n || obstacle_grid[i][j] == 1 {
            return 0;
        }
        if i == m - 1 && j == n - 1 {
            return 1;
        }
        if f[i][j] != -1 {
            return f[i][j];
        }
        let down = Self::dfs(i + 1, j, obstacle_grid, f);
        let right = Self::dfs(i, j + 1, obstacle_grid, f);
        f[i][j] = down + right;
        f[i][j]
    }
}
```

#### JavaScript

```js
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const f = Array.from({ length: m }, () => Array(n).fill(-1));
    const dfs = (i, j) => {
        if (i >= m || j >= n || obstacleGrid[i][j] === 1) {
            return 0;
        }
        if (i === m - 1 && j === n - 1) {
            return 1;
        }
        if (f[i][j] === -1) {
            f[i][j] = dfs(i + 1, j) + dfs(i, j + 1);
        }
        return f[i][j];
    };
    return dfs(0, 0);
};
```

### Solution 2: Dynamic Programming

We can use a dynamic programming approach by defining a 2D array $f$, where $f[i][j]$ represents the number of paths from the grid $(0,0)$ to the grid $(i,j)$.

We first initialize all values in the first column and the first row of $f$, then traverse the other rows and columns with two cases:

-   If $\textit{obstacleGrid}[i][j] = 1$, it means the number of paths is $0$, so $f[i][j] = 0$;
-   If $\textit{obstacleGrid}[i][j] = 0$, then $f[i][j] = f[i - 1][j] + f[i][j - 1]$.

Finally, return $f[m - 1][n - 1]$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. Here, $m$ and $n$ are the number of rows and columns of the grid, respectively.

#### Python3

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            f[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            f[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[-1][-1]
```

#### Java

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] f = new int[m][n];
        for (int i = 0; i < m && obstacleGrid[i][0] == 0; ++i) {
            f[i][0] = 1;
        }
        for (int j = 0; j < n && obstacleGrid[0][j] == 0; ++j) {
            f[0][j] = 1;
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 0) {
                    f[i][j] = f[i - 1][j] + f[i][j - 1];
                }
            }
        }
        return f[m - 1][n - 1];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> f(m, vector<int>(n));
        for (int i = 0; i < m && obstacleGrid[i][0] == 0; ++i) {
            f[i][0] = 1;
        }
        for (int j = 0; j < n && obstacleGrid[0][j] == 0; ++j) {
            f[0][j] = 1;
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (obstacleGrid[i][j] == 0) {
                    f[i][j] = f[i - 1][j] + f[i][j - 1];
                }
            }
        }
        return f[m - 1][n - 1];
    }
};
```

#### Go

```go
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m, n := len(obstacleGrid), len(obstacleGrid[0])
	f := make([][]int, m)
	for i := 0; i < m; i++ {
		f[i] = make([]int, n)
	}
	for i := 0; i < m && obstacleGrid[i][0] == 0; i++ {
		f[i][0] = 1
	}
	for j := 0; j < n && obstacleGrid[0][j] == 0; j++ {
		f[0][j] = 1
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if obstacleGrid[i][j] == 0 {
				f[i][j] = f[i-1][j] + f[i][j-1]
			}
		}
	}
	return f[m-1][n-1]
}
```

#### TypeScript

```ts
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const f = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        if (obstacleGrid[i][0] === 1) {
            break;
        }
        f[i][0] = 1;
    }
    for (let i = 0; i < n; i++) {
        if (obstacleGrid[0][i] === 1) {
            break;
        }
        f[0][i] = 1;
    }
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (obstacleGrid[i][j] === 1) {
                continue;
            }
            f[i][j] = f[i - 1][j] + f[i][j - 1];
        }
    }
    return f[m - 1][n - 1];
}
```

#### Rust

```rust
impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut f = vec![vec![0; n]; m];
        for i in 0..n {
            if obstacle_grid[0][i] == 1 {
                break;
            }
            f[0][i] = 1;
        }
        for i in 0..m {
            if obstacle_grid[i][0] == 1 {
                break;
            }
            f[i][0] = 1;
        }
        for i in 1..m {
            for j in 1..n {
                if obstacle_grid[i][j] == 1 {
                    continue;
                }
                f[i][j] = f[i - 1][j] + f[i][j - 1];
            }
        }
        f[m - 1][n - 1]
    }
}
```

#### JavaScript

```js
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const f = Array.from({ length: m }, () => Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        if (obstacleGrid[i][0] === 1) {
            break;
        }
        f[i][0] = 1;
    }
    for (let i = 0; i < n; i++) {
        if (obstacleGrid[0][i] === 1) {
            break;
        }
        f[0][i] = 1;
    }
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (obstacleGrid[i][j] === 1) {
                continue;
            }
            f[i][j] = f[i - 1][j] + f[i][j - 1];
        }
    }
    return f[m - 1][n - 1];
};
```

[Continue 0064: Minimum Path Sum](../../0000-0099/0064.Minimum%20Path%20Sum/README.md)
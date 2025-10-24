# [72. Edit Distance](https://leetcode.com/problems/edit-distance)

## Description

<p>Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum number of operations required to convert <code>word1</code> to <code>word2</code></em>.</p>

<p>You have the following three operations permitted on a word:</p>

<ul>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>

## Solutions

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the minimum number of operations to convert $word1$ of length $i$ to $word2$ of length $j$. $f[i][0] = i$, $f[0][j] = j$, $i \in [1, m], j \in [0, n]$.

We consider $f[i][j]$:

-   If $word1[i - 1] = word2[j - 1]$, then we only need to consider the minimum number of operations to convert $word1$ of length $i - 1$ to $word2$ of length $j - 1$, so $f[i][j] = f[i - 1][j - 1]$;
-   Otherwise, we can consider insert, delete, and replace operations, then $f[i][j] = \min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1$.

Finally, we can get the state transition equation:

$$
f[i][j] = \begin{cases}
i, & \textit{if } j = 0 \\
j, & \textit{if } i = 0 \\
f[i - 1][j - 1], & \textit{if } word1[i - 1] = word2[j - 1] \\
\min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1, & \textit{otherwise}
\end{cases}
$$

Finally, we return $f[m][n]$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$. $m$ and $n$ are the lengths of $word1$ and $word2$ respectively.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Computes the minimum number of operations to convert word1 into word2.

        Allowed operations:
        - Insert a character
        - Delete a character
        - Replace a character

        Uses dynamic programming:
        - dp[i][j] = min operations to convert word1[:i] to word2[:j]

        Parameters:
            word1 (str): Source string.
            word2 (str): Target string.

        Returns:
            int: Minimum number of operations required.
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize first row and first column
        for i in range(m + 1):
            dp[i][0] = i  # delete all from word1
        for j in range(n + 1):
            dp[0][j] = j  # insert all into word1

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],               # delete
                        dp[i][j - 1],               # insert
                        dp[i - 1][j - 1]            # replace
                    )           
        return dp[m][n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))       
    print(sol.minDistance("intention", "execution")) 

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
5

real    0m0.023s
user    0m0.019s
sys     0m0.004s
```

#### Python3

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n + 1):
            f[0][j] = j
        for i, a in enumerate(word1, 1):
            f[i][0] = i
            for j, b in enumerate(word2, 1):
                if a == b:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        return f[m][n]
```

#### Java

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] f = new int[m + 1][n + 1];
        for (int j = 1; j <= n; ++j) {
            f[0][j] = j;
        }
        for (int i = 1; i <= m; ++i) {
            f[i][0] = i;
            for (int j = 1; j <= n; ++j) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    f[i][j] = f[i - 1][j - 1];
                } else {
                    f[i][j] = Math.min(f[i - 1][j], Math.min(f[i][j - 1], f[i - 1][j - 1])) + 1;
                }
            }
        }
        return f[m][n];
    }
}
```

#### C++

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        int f[m + 1][n + 1];
        for (int j = 0; j <= n; ++j) {
            f[0][j] = j;
        }
        for (int i = 1; i <= m; ++i) {
            f[i][0] = i;
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    f[i][j] = f[i - 1][j - 1];
                } else {
                    f[i][j] = min({f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]}) + 1;
                }
            }
        }
        return f[m][n];
    }
};
```

#### Go

```go
func minDistance(word1 string, word2 string) int {
	m, n := len(word1), len(word2)
	f := make([][]int, m+1)
	for i := range f {
		f[i] = make([]int, n+1)
	}
	for j := 1; j <= n; j++ {
		f[0][j] = j
	}
	for i := 1; i <= m; i++ {
		f[i][0] = i
		for j := 1; j <= n; j++ {
			if word1[i-1] == word2[j-1] {
				f[i][j] = f[i-1][j-1]
			} else {
				f[i][j] = min(f[i-1][j], min(f[i][j-1], f[i-1][j-1])) + 1
			}
		}
	}
	return f[m][n]
}
```

#### TypeScript

```ts
function minDistance(word1: string, word2: string): number {
    const m = word1.length;
    const n = word2.length;
    const f: number[][] = Array(m + 1)
        .fill(0)
        .map(() => Array(n + 1).fill(0));
    for (let j = 1; j <= n; ++j) {
        f[0][j] = j;
    }
    for (let i = 1; i <= m; ++i) {
        f[i][0] = i;
        for (let j = 1; j <= n; ++j) {
            if (word1[i - 1] === word2[j - 1]) {
                f[i][j] = f[i - 1][j - 1];
            } else {
                f[i][j] = Math.min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1;
            }
        }
    }
    return f[m][n];
}
```

#### JavaScript

```js
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
    const m = word1.length;
    const n = word2.length;
    const f = Array(m + 1)
        .fill(0)
        .map(() => Array(n + 1).fill(0));
    for (let j = 1; j <= n; ++j) {
        f[0][j] = j;
    }
    for (let i = 1; i <= m; ++i) {
        f[i][0] = i;
        for (let j = 1; j <= n; ++j) {
            if (word1[i - 1] === word2[j - 1]) {
                f[i][j] = f[i - 1][j - 1];
            } else {
                f[i][j] = Math.min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1;
            }
        }
    }
    return f[m][n];
};
```

[Continue 0312: Burst Balloons](../../0300-0399/0312.Burst%20Balloons/README.md)
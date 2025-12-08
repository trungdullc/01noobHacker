# [207. Course Schedule](https://leetcode.com/problems/course-schedule) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.</li>
</ul>

<p>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li>All the pairs prerequisites[i] are <strong>unique</strong>.</li>
</ul>

## Solutions

### Solution 1: Topological Sorting

For this problem, we can consider the courses as nodes in a graph, and prerequisites as edges in the graph. Thus, we can transform this problem into determining whether there is a cycle in the directed graph.

Specifically, we can use the idea of topological sorting. For each node with an in-degree of $0$, we reduce the in-degree of its out-degree nodes by $1$, until all nodes have been traversed.

If all nodes have been traversed, it means there is no cycle in the graph, and we can complete all courses; otherwise, we cannot complete all courses.

The time complexity is $O(n + m)$, and the space complexity is $O(n + m)$. Here, $n$ and $m$ are the number of courses and prerequisites respectively.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3
from typing import List
from collections import deque, defaultdict

class Solution:
    """
    Determines if all courses can be finished given prerequisites.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited = 0

        while queue:
            course = queue.popleft()
            visited += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses

if __name__ == "__main__":
    examples = [
        (2, [[1,0]]),
        (2, [[1,0],[0,1]])
    ]

    sol = Solution()
    for i, (numCourses, prerequisites) in enumerate(examples, 1):
        res = sol.canFinish(numCourses, prerequisites)
        print(f"Example {i} output: {res}")

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
Example 1 output: True
Example 2 output: False

real    0m0.030s
user    0m0.019s
sys     0m0.011s
```

#### Python3

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        q = [i for i, x in enumerate(indeg) if x == 0]
        for i in q:
            numCourses -= 1
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return numCourses == 0
```

#### Java

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] g = new List[numCourses];
        Arrays.setAll(g, k -> new ArrayList<>());
        int[] indeg = new int[numCourses];
        for (var p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].add(a);
            ++indeg[a];
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.offer(i);
            }
        }
        while (!q.isEmpty()) {
            int i = q.poll();
            --numCourses;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.offer(j);
                }
            }
        }
        return numCourses == 0;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        vector<int> indeg(numCourses);
        for (auto& p : prerequisites) {
            int a = p[0], b = p[1];
            g[b].push_back(a);
            ++indeg[a];
        }
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.push(i);
            }
        }
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            --numCourses;
            for (int j : g[i]) {
                if (--indeg[j] == 0) {
                    q.push(j);
                }
            }
        }
        return numCourses == 0;
    }
};
```

#### Go

```go
func canFinish(numCourses int, prerequisites [][]int) bool {
	g := make([][]int, numCourses)
	indeg := make([]int, numCourses)
	for _, p := range prerequisites {
		a, b := p[0], p[1]
		g[b] = append(g[b], a)
		indeg[a]++
	}
	q := []int{}
	for i, x := range indeg {
		if x == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		i := q[0]
		q = q[1:]
		numCourses--
		for _, j := range g[i] {
			indeg[j]--
			if indeg[j] == 0 {
				q = append(q, j)
			}
		}
	}
	return numCourses == 0
}
```

#### TypeScript

```ts
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const g: number[][] = Array.from({ length: numCourses }, () => []);
    const indeg: number[] = Array(numCourses).fill(0);
    for (const [a, b] of prerequisites) {
        g[b].push(a);
        indeg[a]++;
    }
    const q: number[] = [];
    for (let i = 0; i < numCourses; ++i) {
        if (indeg[i] === 0) {
            q.push(i);
        }
    }
    for (const i of q) {
        --numCourses;
        for (const j of g[i]) {
            if (--indeg[j] === 0) {
                q.push(j);
            }
        }
    }
    return numCourses === 0;
}
```

#### Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn can_finish(mut num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut g: Vec<Vec<i32>> = vec![vec![]; num_courses as usize];
        let mut indeg: Vec<i32> = vec![0; num_courses as usize];

        for p in prerequisites {
            let a = p[0] as usize;
            let b = p[1] as usize;
            g[b].push(a as i32);
            indeg[a] += 1;
        }

        let mut q: VecDeque<usize> = VecDeque::new();
        for i in 0..num_courses {
            if indeg[i as usize] == 0 {
                q.push_back(i as usize);
            }
        }

        while let Some(i) = q.pop_front() {
            num_courses -= 1;
            for &j in &g[i] {
                let j = j as usize;
                indeg[j] -= 1;
                if indeg[j] == 0 {
                    q.push_back(j);
                }
            }
        }

        num_courses == 0
    }
}
```

#### C#

```cs
public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        var g = new List<int>[numCourses];
        for (int i = 0; i < numCourses; ++i) {
            g[i] = new List<int>();
        }
        var indeg = new int[numCourses];
        foreach (var p in prerequisites) {
            int a = p[0], b = p[1];
            g[b].Add(a);
            ++indeg[a];
        }
        var q = new Queue<int>();
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {
                q.Enqueue(i);
            }
        }
        while (q.Count > 0) {
            int i = q.Dequeue();
            --numCourses;
            foreach (int j in g[i]) {
                if (--indeg[j] == 0) {
                    q.Enqueue(j);
                }
            }
        }
        return numCourses == 0;
    }
}
```

[Continue 0210: Course Schedule II ](../../0200-0299/0210.Course%20Schedule%20II/README.md)
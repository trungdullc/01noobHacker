# [133. Clone Graph](https://leetcode.com/problems/clone-graph)

## Description

<p>Given a reference of a node in a <strong><a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a></strong> undirected graph.</p>

<p>Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> (clone) of the graph.</p>

<p>Each node in the graph contains a value (<code>int</code>) and a list (<code>List[Node]</code>) of its neighbors.</p>

<pre>
class Node {
    public int val;
    public List&lt;Node&gt; neighbors;
}
</pre>

<p>&nbsp;</p>

<p><strong>Test case format:</strong></p>

<p>For simplicity, each node&#39;s value is the same as the node&#39;s index (1-indexed). For example, the first node with <code>val == 1</code>, the second node with <code>val == 2</code>, and so on. The graph is represented in the test case using an adjacency list.</p>

<p><b>An adjacency list</b> is a collection of unordered <b>lists</b> used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.</p>

<p>The given node will always be the first node with <code>val = 1</code>. You must return the <strong>copy of the given node</strong> as a reference to the cloned graph.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0133.Clone%20Graph/images/133_clone_graph_question.png" style="width: 454px; height: 500px;" />
<pre>
<strong>Input:</strong> adjList = [[2,4],[1,3],[2,4],[1,3]]
<strong>Output:</strong> [[2,4],[1,3],[2,4],[1,3]]
<strong>Explanation:</strong> There are 4 nodes in the graph.
1st node (val = 1)&#39;s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)&#39;s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)&#39;s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)&#39;s neighbors are 1st node (val = 1) and 3rd node (val = 3).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0133.Clone%20Graph/images/graph.png" style="width: 163px; height: 148px;" />
<pre>
<strong>Input:</strong> adjList = [[]]
<strong>Output:</strong> [[]]
<strong>Explanation:</strong> Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> adjList = []
<strong>Output:</strong> []
<strong>Explanation:</strong> This an empty graph, it does not have any nodes.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the graph is in the range <code>[0, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
	<li><code>Node.val</code> is unique for each node.</li>
	<li>There are no repeated edges and no self-loops in the graph.</li>
	<li>The Graph is connected and all nodes can be visited starting from the given node.</li>
</ul>

## Solutions

### Solution 1: Hash Table + DFS

We use a hash table $\textit{g}$ to record the correspondence between each node in the original graph and its copy, and then perform depth-first search.

We define the function $\text{dfs}(node)$, which returns the copy of the $\textit{node}$. The process of $\text{dfs}(node)$ is as follows:

-   If $\textit{node}$ is $\text{null}$, then the return value of $\text{dfs}(node)$ is $\text{null}$.
-   If $\textit{node}$ is in $\textit{g}$, then the return value of $\text{dfs}(node)$ is $\textit{g}[node]$.
-   Otherwise, we create a new node $\textit{cloned}$ and set the value of $\textit{g}[node]$ to $\textit{cloned}$. Then, we traverse all the neighbor nodes $\textit{nxt}$ of $\textit{node}$ and add $\text{dfs}(nxt)$ to the neighbor list of $\textit{cloned}$.
-   Finally, return $\textit{cloned}$.

In the main function, we return $\text{dfs}(node)$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes.

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

real    0m0.036s
user    0m0.030s
sys     0m0.004s
```

#### Python3

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        def dfs(node):
            if node is None:
                return None
            if node in g:
                return g[node]
            cloned = Node(node.val)
            g[node] = cloned
            for nxt in node.neighbors:
                cloned.neighbors.append(dfs(nxt))
            return cloned

        g = defaultdict()
        return dfs(node)
```

#### Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    private Map<Node, Node> g = new HashMap<>();

    public Node cloneGraph(Node node) {
        return dfs(node);
    }

    private Node dfs(Node node) {
        if (node == null) {
            return null;
        }
        Node cloned = g.get(node);
        if (cloned == null) {
            cloned = new Node(node.val);
            g.put(node, cloned);
            for (Node nxt : node.neighbors) {
                cloned.neighbors.add(dfs(nxt));
            }
        }
        return cloned;
    }
}
```

#### C++

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> g;
        auto dfs = [&](this auto&& dfs, Node* node) -> Node* {
            if (!node) {
                return nullptr;
            }
            if (g.contains(node)) {
                return g[node];
            }
            Node* cloned = new Node(node->val);
            g[node] = cloned;
            for (auto& nxt : node->neighbors) {
                cloned->neighbors.push_back(dfs(nxt));
            }
            return cloned;
        };
        return dfs(node);
    }
};
```

#### Go

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
	g := map[*Node]*Node{}
	var dfs func(node *Node) *Node
	dfs = func(node *Node) *Node {
		if node == nil {
			return nil
		}
		if n, ok := g[node]; ok {
			return n
		}
		cloned := &Node{node.Val, []*Node{}}
		g[node] = cloned
		for _, nxt := range node.Neighbors {
			cloned.Neighbors = append(cloned.Neighbors, dfs(nxt))
		}
		return cloned
	}
	return dfs(node)
}
```

#### TypeScript

```ts
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     neighbors: _Node[]
 *
 *     constructor(val?: number, neighbors?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 *
 */

function cloneGraph(node: _Node | null): _Node | null {
    const g: Map<_Node, _Node> = new Map();
    const dfs = (node: _Node | null): _Node | null => {
        if (!node) {
            return null;
        }
        if (g.has(node)) {
            return g.get(node);
        }
        const cloned = new _Node(node.val);
        g.set(node, cloned);
        for (const nxt of node.neighbors) {
            cloned.neighbors.push(dfs(nxt));
        }
        return cloned;
    };
    return dfs(node);
}
```

#### JavaScript

```js
/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function (node) {
    const g = new Map();
    const dfs = node => {
        if (!node) {
            return null;
        }
        if (g.has(node)) {
            return g.get(node);
        }
        const cloned = new _Node(node.val);
        g.set(node, cloned);
        for (const nxt of node.neighbors) {
            cloned.neighbors.push(dfs(nxt));
        }
        return cloned;
    };
    return dfs(node);
};
```

#### C#

```cs
/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

public class Solution {
    public Node CloneGraph(Node node) {
        var g = new Dictionary<Node, Node>();
        Node Dfs(Node n) {
            if (n == null) {
                return null;
            }
            if (g.ContainsKey(n)) {
                return g[n];
            }
            var cloned = new Node(n.val);
            g[n] = cloned;
            foreach (var neighbor in n.neighbors) {
                cloned.neighbors.Add(Dfs(neighbor));
            }
            return cloned;
        }
        return Dfs(node);
    }
}
```

[Continue 0286: Walls And Gates](../../0200-0299/0286.Walls%20and%20Gates/README.md)
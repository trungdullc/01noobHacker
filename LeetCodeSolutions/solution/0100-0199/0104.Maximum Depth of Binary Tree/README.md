# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>Given the <code>root</code> of a binary tree, return <em>its maximum depth</em>.</p>

<p>A binary tree&#39;s <strong>maximum depth</strong>&nbsp;is the number of nodes along the longest path from the root node down to the farthest leaf node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0104.Maximum%20Depth%20of%20Binary%20Tree/images/tmp-tree.jpg" style="width: 400px; height: 277px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

## Solutions

### Solution 1: Recursion

Recursively traverse the left and right subtrees, calculate the maximum depth of the left and right subtrees, and then take the maximum value plus $1$.

The time complexity is $O(n)$, where $n$ is the number of nodes in the binary tree. Each node is traversed only once in the recursion.

#### Du Solution1
```python
#!/usr/bin/env python3
from typing import Optional, List
from collections import deque

class TreeNode:
    """
    Definition for a binary tree node
    """
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Helper Function: create tree from array
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        node = queue.popleft()

        # left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    """
    Recursion Solution using Depth First Search
        Recursively compute the depth of the left subtree
        Recursively compute the depth of the right subtree
        Take the maximum of the two
        Add 1 for the current node
    Runtime Complexity: O(n)                                # n: number of nodes
    Space Complexity: O(h)                                  # h: height of tree
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [3,9,20,None,None,15,7],
        [1,None,2],             
        []                      
    ]

    for testcase in examples:
        root = buildTree(testcase)
        print(sol.maxDepth(root))
```

#### Du Solution2
```python
#!/usr/bin/env python3
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        node = queue.popleft()

        # left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    """
    Iterative Depth First Search using a stack
        The stack will store pairs of:
            the current node
            the depth of that node in the tree
        Every time we pop a node from the stack:
            We update the maximum depth seen so far
            We push its left and right children onto the stack with depth + 1
    Runtime Complexity: O(n)
    Space Complexity: O(n) 
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        ans = 0

        while stack:
            nodePtr, depthPtr = stack.pop()

            if nodePtr:
                ans = max(ans, depthPtr)
                stack.append([nodePtr.left, depthPtr + 1])
                stack.append([nodePtr.right, depthPtr + 1])
        return ans

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [3,9,20,None,None,15,7],
        [1,None,2],             
        []                      
    ]

    for testcase in examples:
        root = buildTree(testcase)
        print(sol.maxDepth(root))
```

#### Du Solution3
```python
#!/usr/bin/env python3
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        node = queue.popleft()

        # left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    """
    Breadth First Search
        Every iteration of BFS processes one entire level of the tree
        Start with the root → depth = 1
        Add its children → depth = 2
        Add their children → depth = 3
        Continue until no nodes remain
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        que = deque()
        if root:
            que.append(root)

        level = 0

        while que:
            for i in range(len(que)):
                nodePtr = que.popleft()
                if nodePtr.left:
                    que.append(nodePtr.left)
                if nodePtr.right:
                    que.append(nodePtr.right)
            level += 1
        return level

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [3,9,20,None,None,15,7],
        [1,None,2],             
        []                      
    ]

    for testcase in examples:
        root = buildTree(testcase)
        print(sol.maxDepth(root))
```

#### Python Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
   def maxDepth(self, root):
      if not root:
         return 0
      left_depth = self.maxDepth(root.left)
      right_depth = self.maxDepth(root.right)
      return max(left_depth, right_depth) + 1

if __name__ == "__main__":
   sol = Solution()

   root1 = TreeNode(3)
   root1.left = TreeNode(9)
   root1.right = TreeNode(20)
   root1.right.left = TreeNode(15)
   root1.right.right = TreeNode(7)
   print(sol.maxDepth(root1))

   root2 = TreeNode(1)
   root2.right = TreeNode(2)
   print(sol.maxDepth(root2))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
2

real    0m0.023s
user    0m0.019s
sys     0m0.004s
```

#### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = maxDepth(root.left);
        int r = maxDepth(root.right);
        return 1 + Math.max(l, r);
    }
}
```

#### C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int l = maxDepth(root->left), r = maxDepth(root->right);
        return 1 + max(l, r);
    }
};
```

#### Go

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	l, r := maxDepth(root.Left), maxDepth(root.Right)
	return 1 + max(l, r)
}
```

#### TypeScript

```ts
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxDepth(root: TreeNode | null): number {
    if (root === null) {
        return 0;
    }
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

#### Rust

```rust
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let node = root.as_ref().unwrap().borrow();
        1 + Self::dfs(&node.left).max(Self::dfs(&node.right))
    }

    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::dfs(&root)
    }
}
```

#### JavaScript

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
    if (!root) return 0;
    const l = maxDepth(root.left);
    const r = maxDepth(root.right);
    return 1 + Math.max(l, r);
};
```

#### C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define max(a, b) (((a) > (b)) ? (a) : (b))

int maxDepth(struct TreeNode* root) {
    if (!root) {
        return 0;
    }
    int left = maxDepth(root->left);
    int right = maxDepth(root->right);
    return 1 + max(left, right);
}
```

[Continue 0543: Diameter of Binary Tree](../../0500-0599/0543.Diameter%20of%20Binary%20Tree/README.md)
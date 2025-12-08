# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>Given the <code>root</code> of a binary tree, invert the tree, and return <em>its root</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0226.Invert%20Binary%20Tree/images/invert1-tree.jpg" style="width: 500px; height: 165px;" />
<pre>
<strong>Input:</strong> root = [4,2,7,1,3,6,9]
<strong>Output:</strong> [4,7,2,9,6,3,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0226.Invert%20Binary%20Tree/images/invert2-tree.jpg" style="width: 500px; height: 120px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [2,3,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

## Solutions

### Solution 1: Recursion

First, we check if $\textit{root}$ is null. If it is, we return $\text{null}$. Then, we recursively invert the left and right subtrees, set the inverted right subtree as the new left subtree, and set the inverted left subtree as the new right subtree. Finally, we return $\textit{root}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of nodes in the binary tree.

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
    Helper Fx: Convert array to tree
    """
    if not values:
        return None

    rootPtr = TreeNode(values[0])
    queue = deque([rootPtr])
    index = 1

    while index < len(values):
        node = queue.popleft()

        # left child
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return rootPtr

def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Helper Fx: Convert tree to list
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:                    # Remove trailing Nones for cleaner output
        result.pop()
    return result

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Breadth-First Search (BFS)
            Start from the root
            For each node, swap its children
            Then push the (new) left and right children into the queue
            Continue until every node has been processed
        Runtime Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return None

        queue = deque([root])

        while queue:
            nodePtr = queue.popleft()

            nodePtr.left, nodePtr.right = nodePtr.right, nodePtr.left           # swap children

            if nodePtr.left:
                queue.append(nodePtr.left)
            if nodePtr.right:
                queue.append(nodePtr.right)
        return root

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [4,2,7,1,3,6,9],
        [2,1,3],
        []
    ]

    for testcase in examples:
        root = buildTree(testcase)
        print(treeToList(sol.invertTree(root)))
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

    rootPtr = TreeNode(values[0])
    queue = deque([rootPtr])
    index = 1

    while index < len(values):
        node = queue.popleft()

        # left child
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return rootPtr

def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:                    # Remove trailing Nones for cleaner output
        result.pop()
    return result

class Solution:
    """
    Recursion Solution with Depth First Search
        At each node, swap the left and right children
        Then recursively invert the left subtree
        Recursively invert the right subtree
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)                          # Recursion
        self.invertTree(root.right)                         # Recursion

        return root

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [4,2,7,1,3,6,9],
        [2,1,3],
        []
    ]

    for testcase in examples:
        root = buildTree(testcase)
        print(treeToList(sol.invertTree(root)))
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

    rootPtr = TreeNode(values[0])
    queue = deque([rootPtr])
    index = 1

    while index < len(values):
        node = queue.popleft()

        # left child
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return rootPtr

def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    return result

class Solution:
    """
    Iterative Depth First Search
        Visit a node
        Swap its left and right children
        Continue the process for its children
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]

        while stack:
            nodePtr = stack.pop()
            nodePtr.left, nodePtr.right = nodePtr.right, nodePtr.left
            if nodePtr.left:
                stack.append(nodePtr.left)
            if nodePtr.right:
                stack.append(nodePtr.right)
        return root

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [4,2,7,1,3,6,9],
        [2,1,3],
        []
    ]

    for testcase in examples:
        root = buildTree(testcase)
        print(treeToList(sol.invertTree(root)))
```

#### Python3 Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
   """
   Recursive Solution
   Runtime Complexity: O(n)
   Space Complexity: O(n)
   """

   def invertTree(self, root):
      if not root:
         return None

      # Swap left and right
      root.left, root.right = root.right, root.left

      # Recursive DFS
      self.invertTree(root.left)
      self.invertTree(root.right)

      return root

def print_tree(root):
   if not root:
      return []
   queue = [root]
   result = []
   while queue:
      node = queue.pop(0)
      if node:
         result.append(node.val)
         queue.append(node.left)
         queue.append(node.right)
      else:
         result.append(None)
   # Trim trailing None
   while result and result[-1] is None:
      result.pop()
   return result

if __name__ == "__main__":
   sol = Solution()

   root1 = TreeNode(4)
   root1.left = TreeNode(2)
   root1.right = TreeNode(7)
   root1.left.left = TreeNode(1)
   root1.left.right = TreeNode(3)
   root1.right.left = TreeNode(6)
   root1.right.right = TreeNode(9)
   sol.invertTree(root1)
   print(print_tree(root1))

   root2 = TreeNode(2)
   root2.left = TreeNode(1)
   root2.right = TreeNode(3)
   sol.invertTree(root2)
   print(print_tree(root2))

   print(print_tree(sol.invertTree(None)))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[4, 7, 2, 9, 6, 3, 1]
[2, 3, 1]
[]

real    0m0.023s
user    0m0.018s
sys     0m0.005s
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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode l = invertTree(root.left);
        TreeNode r = invertTree(root.right);
        root.left = r;
        root.right = l;
        return root;
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
    TreeNode* invertTree(TreeNode* root) {
        if (!root) {
            return root;
        }
        TreeNode* l = invertTree(root->left);
        TreeNode* r = invertTree(root->right);
        root->left = r;
        root->right = l;
        return root;
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
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	l, r := invertTree(root.Left), invertTree(root.Right)
	root.Left, root.Right = r, l
	return root
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

function invertTree(root: TreeNode | null): TreeNode | null {
    if (!root) {
        return root;
    }
    const l = invertTree(root.left);
    const r = invertTree(root.right);
    root.left = r;
    root.right = l;
    return root;
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
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root.clone() {
            let mut node = node.borrow_mut();
            let left = node.left.take();
            let right = node.right.take();
            node.left = Self::invert_tree(right);
            node.right = Self::invert_tree(left);
        }
        root
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
 * @return {TreeNode}
 */
var invertTree = function (root) {
    if (!root) {
        return root;
    }
    const l = invertTree(root.left);
    const r = invertTree(root.right);
    root.left = r;
    root.right = l;
    return root;
};
```

#### C#

```cs
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode l = InvertTree(root.left);
        TreeNode r = InvertTree(root.right);
        root.left = r;
        root.right = l;
        return root;
    }
}
```

[Continue 0104: Maximum Depth of Binary Tree](../../0100-0199/0104.Maximum%20Depth%20of%20Binary%20Tree/README.md)
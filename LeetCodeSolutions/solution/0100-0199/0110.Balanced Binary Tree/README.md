# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree) ⭐⭐⭐⭐⭐

## Description

<p>Given a binary tree, determine if it is <span data-keyword="height-balanced"><strong>height-balanced</strong></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0110.Balanced%20Binary%20Tree/images/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0110.Balanced%20Binary%20Tree/images/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

## Solutions

### Solution 1: Bottom-Up Recursion

We define a function $height(root)$ to calculate the height of a binary tree, with the following logic:

-   If the binary tree $root$ is null, return $0$.
-   Otherwise, recursively calculate the heights of the left and right subtrees, denoted as $l$ and $r$ respectively. If either $l$ or $r$ is $-1$, or the absolute difference between $l$ and $r$ is greater than $1$, then return $-1$. Otherwise, return $max(l, r) + 1$.

Therefore, if the function $height(root)$ returns $-1$, it means the binary tree $root$ is not balanced. Otherwise, it is balanced.

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

def buildTree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree level-order (BFS) from an array
    """
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # left child
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i >= len(arr):
            break

        # right child
        if arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    """
    Brute Force
        Rule: tree is balanced if every node’s left and right subtree heights differ by at most 1
        For every node, compute the height of its left subtree.
        Compute the height of its right subtree
        Check if their difference is ≤ 1
        Recursively repeat this check for all nodes
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0

            left = check(node.left)         # Recursive
            if left == -1:
                return -1

            right = check(node.right)       # Recursive
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return check(root) != -1

if __name__ == "__main__":
    sol = Solution()

    print(sol.isBalanced(buildTree([3,9,20,None,None,15,7]))) 
    print(sol.isBalanced(buildTree([1,2,2,3,3,None,None,4,4])))
    print(sol.isBalanced(buildTree([])))                      
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

def buildTree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # left child
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i >= len(arr):
            break

        # right child
        if arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    """
    Recursion Solution with Depth First Search
    Runtime Complexity: O(n)
    Space Complexity: O(h)
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)                       # Recursive
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isBalanced(buildTree([3,9,20,None,None,15,7]))) 
    print(sol.isBalanced(buildTree([1,2,2,3,3,None,None,4,4])))
    print(sol.isBalanced(buildTree([])))                      
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

def buildTree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # left child
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i >= len(arr):
            break

        # right child
        if arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

class Solution:
    """
    Iterative Solution with Depth First Search
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def isBalanced(self, root):
        stack = []
        node = root
        last = None
        depths = {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False

                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isBalanced(buildTree([3,9,20,None,None,15,7]))) 
    print(sol.isBalanced(buildTree([1,2,2,3,3,None,None,4,4])))
    print(sol.isBalanced(buildTree([])))                      
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class TreeNode:
   """
   Definition for a binary tree node.
   """
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
   def isBalanced(self, root):
      """
      Return True if the binary tree is height-balanced.
      :type root: TreeNode
      :rtype: bool
      """
      def check(node):
         if not node:
            return 0, True
         left_height, left_balanced = check(node.left)
         right_height, right_balanced = check(node.right)
         balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
         return max(left_height, right_height) + 1, balanced

      _, is_bal = check(root)
      return is_bal

if __name__ == "__main__":
   sol = Solution()
   # Style 1 ❤️❤️❤️❤️❤️
   root1 = TreeNode(3)
   root1.left = TreeNode(9)
   root1.right = TreeNode(20)
   root1.right.left = TreeNode(15)
   root1.right.right = TreeNode(7)
   # Style 2 ❤️❤️❤️❤️❤️
   # root1 = TreeNode( 3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
   # Style 3 ❤️❤️❤️❤️❤️
   # root1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
   print(sol.isBalanced(root1))

   root2 = TreeNode(1)
   root2.left = TreeNode(2)
   root2.right = TreeNode(2)
   root2.left.left = TreeNode(3)
   root2.left.right = TreeNode(3)
   root2.left.left.left = TreeNode(4)
   root2.left.left.right = TreeNode(4)
   print(sol.isBalanced(root2))

   print(sol.isBalanced(None))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
True
False
True

real    0m0.022s
user    0m0.011s
sys     0m0.011s
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
    public boolean isBalanced(TreeNode root) {
        return height(root) >= 0;
    }

    private int height(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = height(root.left);
        int r = height(root.right);
        if (l == -1 || r == -1 || Math.abs(l - r) > 1) {
            return -1;
        }
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
    bool isBalanced(TreeNode* root) {
        function<int(TreeNode*)> height = [&](TreeNode* root) {
            if (!root) {
                return 0;
            }
            int l = height(root->left);
            int r = height(root->right);
            if (l == -1 || r == -1 || abs(l - r) > 1) {
                return -1;
            }
            return 1 + max(l, r);
        };
        return height(root) >= 0;
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
func isBalanced(root *TreeNode) bool {
	var height func(*TreeNode) int
	height = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		l, r := height(root.Left), height(root.Right)
		if l == -1 || r == -1 || abs(l-r) > 1 {
			return -1
		}
		if l > r {
			return 1 + l
		}
		return 1 + r
	}
	return height(root) >= 0
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
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

function isBalanced(root: TreeNode | null): boolean {
    const dfs = (root: TreeNode | null) => {
        if (root == null) {
            return 0;
        }
        const left = dfs(root.left);
        const right = dfs(root.right);
        if (left === -1 || right === -1 || Math.abs(left - right) > 1) {
            return -1;
        }
        return 1 + Math.max(left, right);
    };
    return dfs(root) > -1;
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
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::dfs(&root) > -1
    }

    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let node = root.as_ref().unwrap().borrow();
        let left = Self::dfs(&node.left);
        let right = Self::dfs(&node.right);
        if left == -1 || right == -1 || (left - right).abs() > 1 {
            return -1;
        }
        1 + left.max(right)
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
 * @return {boolean}
 */
var isBalanced = function (root) {
    const height = root => {
        if (!root) {
            return 0;
        }
        const l = height(root.left);
        const r = height(root.right);
        if (l == -1 || r == -1 || Math.abs(l - r) > 1) {
            return -1;
        }
        return 1 + Math.max(l, r);
    };
    return height(root) >= 0;
};
```

[Continue 0100: Same Tree](../../0100-0199/0100.Same%20Tree/README.md)
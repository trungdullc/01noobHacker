# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>Given the <code>root</code> of a binary tree, return <em>the length of the <strong>diameter</strong> of the tree</em>.</p>

<p>The <strong>diameter</strong> of a binary tree is the <strong>length</strong> of the longest path between any two nodes in a tree. This path may or may not pass through the <code>root</code>.</p>

<p>The <strong>length</strong> of a path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0543.Diameter%20of%20Binary%20Tree/images/diamtree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

## Solutions

### Solution 1: Enumeration + DFS

We can enumerate each node of the binary tree, and for each node, calculate the maximum depth of its left and right subtrees, $\textit{l}$ and $\textit{r}$, respectively. The diameter of the node is $\textit{l} + \textit{r}$. The maximum diameter among all nodes is the diameter of the binary tree.

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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Helper Fx: Convert array to tree (level-order)
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
    Brute Force
        longest path is height of left subtree + height of right subtree
    Runtime Complexity O(n²)
    Space Complexity O(n)
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight

        sub = max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )

        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [1, 2, 3, 4, 5],
        [1, 2]
    ]

    for testcase in examples:
        tree = buildTree(testcase)
        print(sol.diameterOfBinaryTree(tree))
```

#### Du Solution2
```python
#!/usr/bin/env python3
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
    Recursion with Depth First Search
    Runtime Complexity: O(n)
    Space Complexity: O(h)
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res                                    # 3 scopes: local, nonlocal, global         

            if not root:
                return 0
            leftPtr = dfs(root.left)
            rightPtr = dfs(root.right)
            res = max(res, leftPtr + rightPtr)

            return 1 + max(leftPtr, rightPtr)

        dfs(root)
        return res

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [1, 2, 3, 4, 5],
        [1, 2]
    ]

    for testcase in examples:
        tree = buildTree(testcase)
        print(sol.diameterOfBinaryTree(tree))
```

#### Du Solution3
```python
#!/usr/bin/env python3
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
    Iterative Solution with Depth First Search
        post-order traversal
        Visit left subtree
        Visit right subtree
        Then process the current node
    Runtime Complexity: O(n)
    Space Complexity: O(n)
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}                     # map storing (height, diameter) each visited node

        while stack:
            nodePtr = stack[-1]

            if nodePtr.left and nodePtr.left not in mp:
                stack.append(nodePtr.left)
            elif nodePtr.right and nodePtr.right not in mp:
                stack.append(nodePtr.right)
            else:
                nodePtr = stack.pop()

                leftHeightPtr, leftDiameterPtr = mp[nodePtr.left]
                rightHeightPtr, rightDiameterPtr = mp[nodePtr.right]

                mp[nodePtr] = (1 + max(leftHeightPtr, rightHeightPtr),
                           max(leftHeightPtr + rightHeightPtr, leftDiameterPtr, rightDiameterPtr))

        return mp[root][1]

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [1, 2, 3, 4, 5],
        [1, 2]
    ]

    for testcase in examples:
        tree = buildTree(testcase)
        print(sol.diameterOfBinaryTree(tree))
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
   """
   Solution class to compute diameter of a binary tree.
   """

   def diameterOfBinaryTree(self, root):
      """
      Return the length of the diameter (number of edges) of the binary tree.
      :type root: TreeNode
      :rtype: int
      """
      self.diameter = 0

      def depth(node):
         if not node:
            return 0
         left = depth(node.left)
         right = depth(node.right)
         # Update diameter
         self.diameter = max(self.diameter, left + right)
         return max(left, right) + 1

      depth(root)
      return self.diameter

if __name__ == "__main__":
   sol = Solution()

   root1 = TreeNode(1)
   root1.left = TreeNode(2)
   root1.right = TreeNode(3)
   root1.left.left = TreeNode(4)
   root1.left.right = TreeNode(5)
   print(sol.diameterOfBinaryTree(root1))

   root2 = TreeNode(1)
   root2.left = TreeNode(2)
   print(sol.diameterOfBinaryTree(root2))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
3
1

real    0m0.023s
user    0m0.012s
sys     0m0.012s
```

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0
            nonlocal ans
            left, right = dfs(root.left), dfs(root.right)
            ans = max(ans, left + right)
            return 1 + max(left, right)

        ans = 0
        dfs(root)
        return ans
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
    private int ans;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = dfs(root.left);
        int r = dfs(root.right);
        ans = Math.max(ans, l + r);
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
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        auto dfs = [&](this auto&& dfs, TreeNode* root) -> int {
            if (!root) {
                return 0;
            }
            int l = dfs(root->left);
            int r = dfs(root->right);
            ans = max(ans, l + r);
            return 1 + max(l, r);
        };
        dfs(root);
        return ans;
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
func diameterOfBinaryTree(root *TreeNode) (ans int) {
	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		l, r := dfs(root.Left), dfs(root.Right)
		ans = max(ans, l+r)
		return 1 + max(l, r)
	}
	dfs(root)
	return
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

function diameterOfBinaryTree(root: TreeNode | null): number {
    let ans = 0;
    const dfs = (root: TreeNode | null): number => {
        if (!root) {
            return 0;
        }
        const [l, r] = [dfs(root.left), dfs(root.right)];
        ans = Math.max(ans, l + r);
        return 1 + Math.max(l, r);
    };
    dfs(root);
    return ans;
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
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut ans = 0;
        fn dfs(root: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {
            match root {
                Some(node) => {
                    let node = node.borrow();
                    let l = dfs(node.left.clone(), ans);
                    let r = dfs(node.right.clone(), ans);

                    *ans = (*ans).max(l + r);

                    1 + l.max(r)
                }
                None => 0,
            }
        }
        dfs(root, &mut ans);
        ans
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
var diameterOfBinaryTree = function (root) {
    let ans = 0;
    const dfs = root => {
        if (!root) {
            return 0;
        }
        const [l, r] = [dfs(root.left), dfs(root.right)];
        ans = Math.max(ans, l + r);
        return 1 + Math.max(l, r);
    };
    dfs(root);
    return ans;
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
    private int ans;

    public int DiameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = dfs(root.left);
        int r = dfs(root.right);
        ans = Math.Max(ans, l + r);
        return 1 + Math.Max(l, r);
    }
}
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
int dfs(struct TreeNode* root, int* ans) {
    if (root == NULL) {
        return 0;
    }
    int l = dfs(root->left, ans);
    int r = dfs(root->right, ans);
    if (l + r > *ans) {
        *ans = l + r;
    }
    return 1 + (l > r ? l : r);
}

int diameterOfBinaryTree(struct TreeNode* root) {
    int ans = 0;
    dfs(root, &ans);
    return ans;
}
```

[Continue 0110: Balanced Binary Tree](../../0100-0199/0110.Balanced%20Binary%20Tree/README.md)
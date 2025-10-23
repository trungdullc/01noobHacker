# [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree)

## Description

<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p><strong>Clarification:</strong> The input/output format is the same as <a href="https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A" target="_blank">how LeetCode serializes a binary tree</a>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0297.Serialize%20and%20Deserialize%20Binary%20Tree/images/serdeser.jpg" style="width: 442px; height: 324px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,null,4,5]
<strong>Output:</strong> [1,2,3,null,null,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

## Solutions

### Solution 1: Level Order Traversal

We can use level order traversal to serialize the binary tree. Starting from the root node, we add the nodes of the binary tree to the queue in the order from top to bottom, from left to right. Then we dequeue the nodes in the queue one by one. If the node is not null, we add its value to the serialized string; otherwise, we add a special character `#`. Finally, we return the serialized string.

During deserialization, we split the serialized string by the delimiter to get a string array, and then add the elements in the string array to the queue in order. The elements in the queue are the nodes of the binary tree. We dequeue the elements from the queue one by one. If the element is not `#`, we convert it to an integer and use it as the value of the node, and then add the node to the queue; otherwise, we set it to `null`. Finally, we return the root node.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the number of nodes in the binary tree.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from collections import deque

class TreeNode:
   """
   Definition for a binary tree node.
   """
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Codec:
   """
   Codec for serializing and deserializing a binary tree.
   """
   def serialize(self, root: TreeNode) -> str:
      """Encodes a tree to a single string using level-order traversal."""
      if not root:
         return ""
      queue = deque([root])
      result = []
      while queue:
         node = queue.popleft()
         if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
         else:
            result.append("null")
      # Remove trailing "null"s
      while result and result[-1] == "null":
         result.pop()
      return ",".join(result)

   def deserialize(self, data: str) -> TreeNode:
      """Decodes your encoded data to tree."""
      if not data:
         return None
      nodes = data.split(",")
      root = TreeNode(int(nodes[0]))
      queue = deque([root])
      i = 1
      while queue:
         node = queue.popleft()
         if i < len(nodes) and nodes[i] != "null":
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
         i += 1
         if i < len(nodes) and nodes[i] != "null":
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
         i += 1
      return root

def print_tree(root):
   """
   Level-order serialization for testing.
   """
   if not root:
      return []
   from collections import deque
   queue = deque([root])
   result = []
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

def main():
   codec = Codec()
   root1 = TreeNode(1)
   root1.left = TreeNode(2)
   root1.right = TreeNode(3)
   root1.right.left = TreeNode(4)
   root1.right.right = TreeNode(5)
   serialized1 = codec.serialize(root1)
   print(serialized1)
   deserialized1 = codec.deserialize(serialized1)
   print(print_tree(deserialized1))

   root2 = None
   serialized2 = codec.serialize(root2)
   print(serialized2)
   deserialized2 = codec.deserialize(serialized2)
   print(print_tree(deserialized2))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
1,2,3,null,null,4,5
[1, 2, 3, None, None, 4, 5]

[]

real    0m0.060s
user    0m0.020s
sys     0m0.004s
```

#### Python3

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append("#")
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

#### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return null;
        }
        List<String> ans = new ArrayList<>();
        Deque<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node != null) {
                ans.add(node.val + "");
                q.offer(node.left);
                q.offer(node.right);
            } else {
                ans.add("#");
            }
        }
        return String.join(",", ans);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null) {
            return null;
        }
        String[] vals = data.split(",");
        int i = 0;
        TreeNode root = new TreeNode(Integer.valueOf(vals[i++]));
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (!"#".equals(vals[i])) {
                node.left = new TreeNode(Integer.valueOf(vals[i]));
                q.offer(node.left);
            }
            ++i;
            if (!"#".equals(vals[i])) {
                node.right = new TreeNode(Integer.valueOf(vals[i]));
                q.offer(node.right);
            }
            ++i;
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

#### C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) {
            return "";
        }
        queue<TreeNode*> q{{root}};
        string ans;
        while (!q.empty()) {
            auto node = q.front();
            q.pop();
            if (node) {
                ans += to_string(node->val) + " ";
                q.push(node->left);
                q.push(node->right);
            } else {
                ans += "# ";
            }
        }
        ans.pop_back();
        return ans;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "") {
            return nullptr;
        }
        stringstream ss(data);
        string t;
        ss >> t;
        TreeNode* root = new TreeNode(stoi(t));
        queue<TreeNode*> q{{root}};
        while (!q.empty()) {
            auto node = q.front();
            q.pop();
            ss >> t;
            if (t != "#") {
                node->left = new TreeNode(stoi(t));
                q.push(node->left);
            }
            ss >> t;
            if (t != "#") {
                node->right = new TreeNode(stoi(t));
                q.push(node->right);
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
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

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}
	q := []*TreeNode{root}
	ans := []string{}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if node != nil {
			ans = append(ans, strconv.Itoa(node.Val))
			q = append(q, node.Left)
			q = append(q, node.Right)
		} else {
			ans = append(ans, "#")
		}
	}
	return strings.Join(ans, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}
	vals := strings.Split(data, ",")
	v, _ := strconv.Atoi(vals[0])
	i := 1
	root := &TreeNode{Val: v}
	q := []*TreeNode{root}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		if x, err := strconv.Atoi(vals[i]); err == nil {
			node.Left = &TreeNode{Val: x}
			q = append(q, node.Left)
		}
		i++
		if x, err := strconv.Atoi(vals[i]); err == nil {
			node.Right = &TreeNode{Val: x}
			q = append(q, node.Right)
		}
		i++
	}
	return root
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
```

#### JavaScript

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function (root) {
    if (root === null) {
        return null;
    }
    const ans = [];
    const q = [root];
    let index = 0;
    while (index < q.length) {
        const node = q[index++];
        if (node !== null) {
            ans.push(node.val.toString());
            q.push(node.left);
            q.push(node.right);
        } else {
            ans.push('#');
        }
    }
    return ans.join(',');
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
    if (data === null) {
        return null;
    }
    const vals = data.split(',');
    let i = 0;
    const root = new TreeNode(parseInt(vals[i++]));
    const q = [root];
    let index = 0;
    while (index < q.length) {
        const node = q[index++];
        if (vals[i] !== '#') {
            node.left = new TreeNode(+vals[i]);
            q.push(node.left);
        }
        i++;
        if (vals[i] !== '#') {
            node.right = new TreeNode(+vals[i]);
            q.push(node.right);
        }
        i++;
    }
    return root;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
```

#### C#

```cs
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public string serialize(TreeNode root) {
        if (root == null) {
            return null;
        }
        List<string> ans = new List<string>();
        Queue<TreeNode> q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0) {
            TreeNode node = q.Dequeue();
            if (node != null) {
                ans.Add(node.val.ToString());
                q.Enqueue(node.left);
                q.Enqueue(node.right);
            } else {
                ans.Add("#");
            }
        }
        return string.Join(",", ans);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data) {
        if (data == null) {
            return null;
        }
        string[] vals = data.Split(',');
        int i = 0;
        TreeNode root = new TreeNode(int.Parse(vals[i++]));
        Queue<TreeNode> q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0) {
            TreeNode node = q.Dequeue();
            if (vals[i] != "#") {
                node.left = new TreeNode(int.Parse(vals[i]));
                q.Enqueue(node.left);
            }
            i++;
            if (vals[i] != "#") {
                node.right = new TreeNode(int.Parse(vals[i]));
                q.Enqueue(node.right);
            }
            i++;
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

[Continue 0703: Kth Largest Element In a Stream](../../0700-0799/0703.Kth%20Largest%20Element%20in%20a%20Stream/README.md)
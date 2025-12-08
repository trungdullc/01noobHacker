# [143. Reorder List](https://leetcode.com/problems/reorder-list) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>You are given the head of a singly linked-list. The list can be represented as:</p>

<pre>
L<sub>0</sub> &rarr; L<sub>1</sub> &rarr; &hellip; &rarr; L<sub>n - 1</sub> &rarr; L<sub>n</sub>
</pre>

<p><em>Reorder the list to be on the following form:</em></p>

<pre>
L<sub>0</sub> &rarr; L<sub>n</sub> &rarr; L<sub>1</sub> &rarr; L<sub>n - 1</sub> &rarr; L<sub>2</sub> &rarr; L<sub>n - 2</sub> &rarr; &hellip;
</pre>

<p>You may not modify the values in the list&#39;s nodes. Only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0143.Reorder%20List/images/reorder1linked-list.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0100-0199/0143.Reorder%20List/images/reorder2-linked-list.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>

## Solutions

### Solution 1: Fast and Slow Pointers + Reverse List + Merge Lists

We first use fast and slow pointers to find the midpoint of the linked list, then reverse the second half of the list, and finally merge the two halves.

The time complexity is $O(n)$, where $n$ is the length of the linked list. The space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class ListNode:
   """
   Definition for a singly-linked list node.
   """
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
   """
   Solution class to reorder a linked list.
   """

   def reorderList(self, head):
      """
      Reorder a linked list in-place.
      :type head: ListNode
      :rtype: None
      """
      if not head or not head.next:
         return

      # Step 1: Find middle
      slow = fast = head
      while fast.next and fast.next.next:
         slow = slow.next
         fast = fast.next.next

      # Step 2: Reverse second half
      prev, curr = None, slow.next
      slow.next = None
      while curr:
         next_node = curr.next
         curr.next = prev
         prev = curr
         curr = next_node

      # Step 3: Merge two halves
      first, second = head, prev
      while second:
         tmp1, tmp2 = first.next, second.next
         first.next = second
         second.next = tmp1
         first, second = tmp1, tmp2

def list_to_nodes(lst):
   """
   Convert a Python list to a linked list.
   """
   dummy = ListNode(0)
   current = dummy
   for val in lst:
      current.next = ListNode(val)
      current = current.next
   return dummy.next

def nodes_to_list(head):
   """
   Convert a linked list to a Python list.
   """
   result = []
   while head:
      result.append(head.val)
      head = head.next
   return result

if __name__ == "__main__":
   sol = Solution()
   head1 = list_to_nodes([1,2,3,4])
   sol.reorderList(head1)
   print(nodes_to_list(head1))

   head2 = list_to_nodes([1,2,3,4,5])
   sol.reorderList(head2)
   print(nodes_to_list(head2))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 4, 2, 3]
[1, 5, 2, 4, 3]

real    0m0.024s
user    0m0.016s
sys     0m0.008s
```

#### Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None

        pre = None
        while cur:
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        cur = head

        while pre:
            t = pre.next
            pre.next = cur.next
            cur.next = pre
            cur, pre = pre.next, t
```

#### Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        ListNode fast = head, slow = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode cur = slow.next;
        slow.next = null;

        ListNode pre = null;
        while (cur != null) {
            ListNode t = cur.next;
            cur.next = pre;
            pre = cur;
            cur = t;
        }
        cur = head;

        while (pre != null) {
            ListNode t = pre.next;
            pre.next = cur.next;
            cur.next = pre;
            cur = pre.next;
            pre = t;
        }
    }
}
```

#### C++

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* cur = slow->next;
        slow->next = nullptr;

        ListNode* pre = nullptr;
        while (cur) {
            ListNode* t = cur->next;
            cur->next = pre;
            pre = cur;
            cur = t;
        }
        cur = head;

        while (pre) {
            ListNode* t = pre->next;
            pre->next = cur->next;
            cur->next = pre;
            cur = pre->next;
            pre = t;
        }
    }
};
```

#### Go

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode) {
	fast, slow := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow, fast = slow.Next, fast.Next.Next
	}

	cur := slow.Next
	slow.Next = nil

	var pre *ListNode
	for cur != nil {
		t := cur.Next
		cur.Next = pre
		pre, cur = cur, t
	}
	cur = head

	for pre != nil {
		t := pre.Next
		pre.Next = cur.Next
		cur.Next = pre
		cur, pre = pre.Next, t
	}
}
```

#### TypeScript

```ts
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let next = slow.next;
    slow.next = null;
    while (next) {
        [next.next, slow, next] = [slow, next, next.next];
    }

    let left = head;
    let right = slow;
    while (right.next) {
        const next = left.next;
        left.next = right;
        right = right.next;
        left.next.next = next;
        left = left.next.next;
    }
}
```

#### Rust

```rust
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
use std::collections::VecDeque;
impl Solution {
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let mut tail = &mut head.as_mut().unwrap().next;
        let mut head = tail.take();
        let mut deque = VecDeque::new();
        while head.is_some() {
            let next = head.as_mut().unwrap().next.take();
            deque.push_back(head);
            head = next;
        }
        let mut flag = false;
        while !deque.is_empty() {
            *tail = if flag {
                deque.pop_front().unwrap()
            } else {
                deque.pop_back().unwrap()
            };
            tail = &mut tail.as_mut().unwrap().next;
            flag = !flag;
        }
    }
}
```

#### JavaScript

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
    let slow = head;
    let fast = head;
    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let cur = slow.next;
    slow.next = null;

    let pre = null;
    while (cur) {
        const t = cur.next;
        cur.next = pre;
        pre = cur;
        cur = t;
    }
    cur = head;

    while (pre) {
        const t = pre.next;
        pre.next = cur.next;
        cur.next = pre;
        cur = pre.next;
        pre = t;
    }
};
```

#### C#

```cs
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public void ReorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode cur = slow.next;
        slow.next = null;

        ListNode pre = null;
        while (cur != null) {
            ListNode t = cur.next;
            cur.next = pre;
            pre = cur;
            cur = t;
        }
        cur = head;

        while (pre != null) {
            ListNode t = pre.next;
            pre.next = cur.next;
            cur.next = pre;
            cur = pre.next;
            pre = t;
        }
    }
}
```

[Continue 0019: Remove Nth Node From End of List ](../../0000-0099/0019.Remove%20Nth%20Node%20From%20End%20of%20List/README.md)
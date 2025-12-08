# [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>You are given an array of integers <code>stones</code> where <code>stones[i]</code> is the weight of the <code>i<sup>th</sup></code> stone.</p>

<p>We are playing a game with the stones. On each turn, we choose the <strong>heaviest two stones</strong> and smash them together. Suppose the heaviest two stones have weights <code>x</code> and <code>y</code> with <code>x &lt;= y</code>. The result of this smash is:</p>

<ul>
	<li>If <code>x == y</code>, both stones are destroyed, and</li>
	<li>If <code>x != y</code>, the stone of weight <code>x</code> is destroyed, and the stone of weight <code>y</code> has new weight <code>y - x</code>.</li>
</ul>

<p>At the end of the game, there is <strong>at most one</strong> stone left.</p>

<p>Return <em>the weight of the last remaining stone</em>. If there are no stones left, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that&#39;s the value of the last stone.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 1000</code></li>
</ul>

## Solutions

#### Du Solution1
```python
from typing import List

class Solution:
    """
    Sorting Solution
    Runtime complexity: O(n²logn)
    Space complexity: O(n)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)

        return stones[0] if stones else 0

if __name__ == "__main__":
    sol = Solution()

    stones1 = [2,7,4,1,8,1]
    print("Output:", sol.lastStoneWeight(stones1))

    stones2 = [1]
    print("Output:", sol.lastStoneWeight(stones2))
```

#### Du Solution2
```python
from typing import List

class Solution:
    """
    Binary Search Solution
    Runtime complexity: O(n²)
    Space complexity: O(n)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while n > 1:
            cur = stones.pop() - stones.pop()
            n -= 2
            if cur > 0:
                l, r = 0, n
                while l < r:
                    mid = (l + r) // 2
                    if stones[mid] < cur:
                        l = mid + 1
                    else:
                        r = mid
                pos = l
                n += 1
                stones.append(0)
                for i in range(n - 1, pos, -1):
                    stones[i] = stones[i - 1]
                stones[pos] = cur

        return stones[0] if n > 0 else 0

if __name__ == "__main__":
    sol = Solution()

    stones1 = [2,7,4,1,8,1]
    print("Output:", sol.lastStoneWeight(stones1))

    stones2 = [1]
    print("Output:", sol.lastStoneWeight(stones2))
```

#### Du Solution3
```python
import heapq
from typing import List

class Solution:
    """
    Heap Solution
    Runtime complexity: O(nlogn)
    Space complexity: O(n)
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

if __name__ == "__main__":
    sol = Solution()

    stones1 = [2,7,4,1,8,1]
    print("Output:", sol.lastStoneWeight(stones1))

    stones2 = [1]
    print("Output:", sol.lastStoneWeight(stones2))
```

#### Du Solution4
```python
from typing import List

class Solution:
    """
    Bucket Sort Solution
    Runtime complexity: O(n + w)        # n is length of stones array
    Space complexity: O(w)              # w is max value in stones array
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1

        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1

            if j == 0:
                return first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first

if __name__ == "__main__":
    sol = Solution()

    stones1 = [2,7,4,1,8,1]
    print("Output:", sol.lastStoneWeight(stones1))

    stones2 = [1]
    print("Output:", sol.lastStoneWeight(stones2))
```

#### Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

import heapq

class Solution:
   """
   Solution to find the last stone weight after repeatedly smashing the two heaviest stones.
   """
   def lastStoneWeight(self, stones) -> int:
      # Use a max-heap by pushing negative values
      heap = [-stone for stone in stones]
      heapq.heapify(heap)
      while len(heap) > 1:
         first = -heapq.heappop(heap)
         second = -heapq.heappop(heap)
         if first != second:
            heapq.heappush(heap, -(first - second))
      return -heap[0] if heap else 0

def main():
   sol = Solution()
   stones1 = [2,7,4,1,8,1]
   print(sol.lastStoneWeight(stones1))

   stones2 = [1]
   print(sol.lastStoneWeight(stones2))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
1
1

real    0m0.023s
user    0m0.019s
sys     0m0.004s
```

#### Java

```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> b - a);
        for (int x : stones) {
            q.offer(x);
        }
        while (q.size() > 1) {
            int y = q.poll();
            int x = q.poll();
            if (x != y) {
                q.offer(y - x);
            }
        }
        return q.isEmpty() ? 0 : q.poll();
    }
}
```

#### C++

```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for (int x : stones) {
            pq.push(x);
        }
        while (pq.size() > 1) {
            int y = pq.top();
            pq.pop();
            int x = pq.top();
            pq.pop();
            if (x != y) {
                pq.push(y - x);
            }
        }
        return pq.empty() ? 0 : pq.top();
    }
};
```

#### Go

```go
func lastStoneWeight(stones []int) int {
	q := &hp{stones}
	heap.Init(q)
	for q.Len() > 1 {
		y, x := q.pop(), q.pop()
		if x != y {
			q.push(y - x)
		}
	}
	if q.Len() > 0 {
		return q.IntSlice[0]
	}
	return 0
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(v any)        { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() any {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}
func (h *hp) push(v int) { heap.Push(h, v) }
func (h *hp) pop() int   { return heap.Pop(h).(int) }
```

#### TypeScript

```ts
function lastStoneWeight(stones: number[]): number {
    const pq = new MaxPriorityQueue();
    for (const x of stones) {
        pq.enqueue(x);
    }
    while (pq.size() > 1) {
        const y = pq.dequeue().element;
        const x = pq.dequeue().element;
        if (x !== y) {
            pq.enqueue(y - x);
        }
    }
    return pq.isEmpty() ? 0 : pq.dequeue().element;
}
```

#### JavaScript

```js
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
    const pq = new MaxPriorityQueue();
    for (const x of stones) {
        pq.enqueue(x);
    }
    while (pq.size() > 1) {
        const y = pq.dequeue()['priority'];
        const x = pq.dequeue()['priority'];
        if (x != y) {
            pq.enqueue(y - x);
        }
    }
    return pq.isEmpty() ? 0 : pq.dequeue()['priority'];
};
```

[Continue 0973: K Closest Points to Origin](../../0900-0999/0973.K%20Closest%20Points%20to%20Origin/README.md)
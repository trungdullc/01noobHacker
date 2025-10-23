# [1405. Longest Happy String](https://leetcode.com/problems/longest-happy-string)

## Description

<p>A string <code>s</code> is called <strong>happy</strong> if it satisfies the following conditions:</p>

<ul>
	<li><code>s</code> only contains the letters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</li>
	<li><code>s</code> does not contain any of <code>&quot;aaa&quot;</code>, <code>&quot;bbb&quot;</code>, or <code>&quot;ccc&quot;</code> as a substring.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>a</code> occurrences of the letter <code>&#39;a&#39;</code>.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>b</code> occurrences of the letter <code>&#39;b&#39;</code>.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>c</code> occurrences of the letter <code>&#39;c&#39;</code>.</li>
</ul>

<p>Given three integers <code>a</code>, <code>b</code>, and <code>c</code>, return <em>the <strong>longest possible happy </strong>string</em>. If there are multiple longest happy strings, return <em>any of them</em>. If there is no such string, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = 1, b = 1, c = 7
<strong>Output:</strong> &quot;ccaccbcc&quot;
<strong>Explanation:</strong> &quot;ccbccacc&quot; would also be a correct answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = 7, b = 1, c = 0
<strong>Output:</strong> &quot;aabaa&quot;
<strong>Explanation:</strong> It is the only correct answer in this case.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= a, b, c &lt;= 100</code></li>
	<li><code>a + b + c &gt; 0</code></li>
</ul>

## Solutions

### Solution 1: Greedy + Priority Queue

The greedy strategy is to prioritize the selection of characters with the most remaining occurrences. By using a priority queue or sorting, we ensure that the character selected each time is the one with the most remaining occurrences (to avoid having three consecutive identical characters, in some cases, we need to select the character with the second most remaining occurrences).

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

import heapq

class Solution:
   """
   Solution to generate the longest happy string with constraints on 'a', 'b', 'c'.
   """
   def longestDiverseString(self, a: int, b: int, c: int) -> str:
      heap = []
      for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
         if count != 0:
            heapq.heappush(heap, (count, char))
      res = []

      while heap:
         count1, char1 = heapq.heappop(heap)
         if len(res) >= 2 and res[-1] == res[-2] == char1:
            if not heap:
               break
            count2, char2 = heapq.heappop(heap)
            res.append(char2)
            count2 += 1
            if count2 != 0:
               heapq.heappush(heap, (count2, char2))
            heapq.heappush(heap, (count1, char1))
         else:
            res.append(char1)
            count1 += 1
            if count1 != 0:
               heapq.heappush(heap, (count1, char1))
      return ''.join(res)

def main():
   sol = Solution()
   print(sol.longestDiverseString(1,1,7))
   print(sol.longestDiverseString(7,1,0))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
ccaccbcc
aabaa

real    0m0.089s
user    0m0.027s
sys     0m0.017s
```

#### Python3

```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0:
            heappush(h, [-a, 'a'])
        if b > 0:
            heappush(h, [-b, 'b'])
        if c > 0:
            heappush(h, [-c, 'c'])

        ans = []
        while len(h) > 0:
            cur = heappop(h)
            if len(ans) >= 2 and ans[-1] == cur[1] and ans[-2] == cur[1]:
                if len(h) == 0:
                    break
                nxt = heappop(h)
                ans.append(nxt[1])
                if -nxt[0] > 1:
                    nxt[0] += 1
                    heappush(h, nxt)
                heappush(h, cur)
            else:
                ans.append(cur[1])
                if -cur[0] > 1:
                    cur[0] += 1
                    heappush(h, cur)

        return ''.join(ans)
```

#### Java

```java
class Solution {
    public String longestDiverseString(int a, int b, int c) {
        Queue<int[]> pq = new PriorityQueue<>((x, y) -> y[1] - x[1]);
        if (a > 0) {
            pq.offer(new int[] {'a', a});
        }
        if (b > 0) {
            pq.offer(new int[] {'b', b});
        }
        if (c > 0) {
            pq.offer(new int[] {'c', c});
        }

        StringBuilder sb = new StringBuilder();
        while (pq.size() > 0) {
            int[] cur = pq.poll();
            int n = sb.length();
            if (n >= 2 && sb.codePointAt(n - 1) == cur[0] && sb.codePointAt(n - 2) == cur[0]) {
                if (pq.size() == 0) {
                    break;
                }
                int[] next = pq.poll();
                sb.append((char) next[0]);
                if (next[1] > 1) {
                    next[1]--;
                    pq.offer(next);
                }
                pq.offer(cur);
            } else {
                sb.append((char) cur[0]);
                if (cur[1] > 1) {
                    cur[1]--;
                    pq.offer(cur);
                }
            }
        }

        return sb.toString();
    }
}
```

#### C++

```cpp
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        using pci = pair<char, int>;
        auto cmp = [](pci x, pci y) { return x.second < y.second; };
        priority_queue<pci, vector<pci>, decltype(cmp)> pq(cmp);

        if (a > 0) pq.push({'a', a});
        if (b > 0) pq.push({'b', b});
        if (c > 0) pq.push({'c', c});

        string ans;
        while (!pq.empty()) {
            pci cur = pq.top();
            pq.pop();
            int n = ans.size();
            if (n >= 2 && ans[n - 1] == cur.first && ans[n - 2] == cur.first) {
                if (pq.empty()) break;
                pci nxt = pq.top();
                pq.pop();
                ans.push_back(nxt.first);
                if (--nxt.second > 0) {
                    pq.push(nxt);
                }
                pq.push(cur);
            } else {
                ans.push_back(cur.first);
                if (--cur.second > 0) {
                    pq.push(cur);
                }
            }
        }

        return ans;
    }
};
```

#### Go

```go
type pair struct {
	c   byte
	num int
}

type hp []pair

func (a hp) Len() int           { return len(a) }
func (a hp) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a hp) Less(i, j int) bool { return a[i].num > a[j].num }
func (a *hp) Push(x any)        { *a = append(*a, x.(pair)) }
func (a *hp) Pop() any          { l := len(*a); t := (*a)[l-1]; *a = (*a)[:l-1]; return t }

func longestDiverseString(a int, b int, c int) string {
	var h hp
	if a > 0 {
		heap.Push(&h, pair{'a', a})
	}
	if b > 0 {
		heap.Push(&h, pair{'b', b})
	}
	if c > 0 {
		heap.Push(&h, pair{'c', c})
	}

	var ans []byte
	for len(h) > 0 {
		cur := heap.Pop(&h).(pair)
		if len(ans) >= 2 && ans[len(ans)-1] == cur.c && ans[len(ans)-2] == cur.c {
			if len(h) == 0 {
				break
			}
			next := heap.Pop(&h).(pair)
			ans = append(ans, next.c)
			if next.num > 1 {
				next.num--
				heap.Push(&h, next)
			}
			heap.Push(&h, cur)
		} else {
			ans = append(ans, cur.c)
			if cur.num > 1 {
				cur.num--
				heap.Push(&h, cur)
			}
		}
	}

	return string(ans)
}
```

#### TypeScript

```ts
function longestDiverseString(a: number, b: number, c: number): string {
    let ans = [];
    let store: Array<[string, number]> = [
        ['a', a],
        ['b', b],
        ['c', c],
    ];
    while (true) {
        store.sort((a, b) => b[1] - a[1]);
        let hasNext = false;
        for (let [i, [ch, ctn]] of store.entries()) {
            if (ctn < 1) {
                break;
            }
            const n = ans.length;
            if (n >= 2 && ans[n - 1] == ch && ans[n - 2] == ch) {
                continue;
            }
            hasNext = true;
            ans.push(ch);
            store[i][1] -= 1;
            break;
        }
        if (!hasNext) {
            break;
        }
    }
    return ans.join('');
}
```

### Solution 2: Greedy + Priority Queue

#### TypeScript

```ts
function longestDiverseString(a: number, b: number, c: number): string {
    let res = '';
    let prev = { ch: '', c: 0 };
    let last = { ch: '', c: 0 };
    const pq = new MaxPriorityQueue({ priority: ({ c }) => c });

    pq.enqueue({ ch: 'a', c: a });
    pq.enqueue({ ch: 'b', c: b });
    pq.enqueue({ ch: 'c', c });

    while (pq.size()) {
        const item = pq.dequeue().element;
        let c = item.c < prev.c ? 1 : 2;

        if (prev.c) pq.enqueue(prev);
        if (last.ch !== item.ch && item.c) last = { ...item, c: 0 };

        while (c-- && item.c && last.c++ < 2) {
            item.c--;
            res += item.ch;
        }
        prev = item;
    }

    return res;
}
```

#### JavaScript

```js
function longestDiverseString(a, b, c) {
    let res = '';
    let prev = { ch: '', c: 0 };
    let last = { ch: '', c: 0 };
    const pq = new MaxPriorityQueue({ priority: ({ c }) => c });

    pq.enqueue({ ch: 'a', c: a });
    pq.enqueue({ ch: 'b', c: b });
    pq.enqueue({ ch: 'c', c });

    while (pq.size()) {
        const item = pq.dequeue().element;
        let c = item.c < prev.c ? 1 : 2;

        if (prev.c) pq.enqueue(prev);
        if (last.ch !== item.ch && item.c) last = { ...item, c: 0 };

        while (c-- && item.c && last.c++ < 2) {
            item.c--;
            res += item.ch;
        }
        prev = item;
    }

    return res;
}
```

[Continue 1094: Car Pooling](../../1000-1099/1094.Car%20Pooling/README.md)
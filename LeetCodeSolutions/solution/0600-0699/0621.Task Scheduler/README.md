# [621. Task Scheduler](https://leetcode.com/problems/task-scheduler) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>You are given an array of CPU <code>tasks</code>, each labeled with a letter from A to Z, and a number <code>n</code>. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there&#39;s a constraint: there has to be a gap of <strong>at least</strong> <code>n</code> intervals between two tasks with the same label.</p>

<p>Return the <strong>minimum</strong> number of CPU intervals required to complete all tasks.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
font-family: Menlo,sans-serif;
font-size: 0.85rem;
">8</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; A -&gt; B.</p>

<p>After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3<sup>rd</sup> interval, neither A nor B can be done, so you idle. By the 4<sup>th</sup> interval, you can do A again as 2 intervals have passed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;C&quot;,&quot;A&quot;,&quot;B&quot;,&quot;D&quot;,&quot;B&quot;], n = 1</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">6</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; C -&gt; D -&gt; A -&gt; B.</p>

<p>With a cooling interval of 1, you can repeat a task after just one other task.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;, &quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">10</span></p>

<p><strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B.</p>

<p>There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tasks[i]</code> is an uppercase English letter.</li>
	<li><code>0 &lt;= n &lt;= 100</code></li>
</ul>

## Solutions

### Solution 1

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from collections import Counter

class Solution:
   """
   Solution to calculate the minimum number of intervals to finish tasks with cooling period n.
   """
   def leastInterval(self, tasks, n: int) -> int:
      count = Counter(tasks)
      max_freq = max(count.values())
      max_count = sum(1 for v in count.values() if v == max_freq)
      # Formula: (max_freq - 1) * (n + 1) + max_count
      return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

def main():
   sol = Solution()
   tasks1 = ["A","A","A","B","B","B"]
   print(sol.leastInterval(tasks1, 2))

   tasks2 = ["A","C","A","B","D","B"]
   print(sol.leastInterval(tasks2, 1))

   tasks3 = ["A","A","A","B","B","B"]
   print(sol.leastInterval(tasks3, 3))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
8
6
10

real    0m0.023s
user    0m0.019s
sys     0m0.004s
```

#### Python3

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        x = max(cnt.values())
        s = sum(v == x for v in cnt.values())
        return max(len(tasks), (x - 1) * (n + 1) + s)
```

#### Java

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] cnt = new int[26];
        int x = 0;
        for (char c : tasks) {
            c -= 'A';
            ++cnt[c];
            x = Math.max(x, cnt[c]);
        }
        int s = 0;
        for (int v : cnt) {
            if (v == x) {
                ++s;
            }
        }
        return Math.max(tasks.length, (x - 1) * (n + 1) + s);
    }
}
```

#### C++

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> cnt(26);
        int x = 0;
        for (char c : tasks) {
            c -= 'A';
            ++cnt[c];
            x = max(x, cnt[c]);
        }
        int s = 0;
        for (int v : cnt) {
            s += v == x;
        }
        return max((int) tasks.size(), (x - 1) * (n + 1) + s);
    }
};
```

#### Go

```go
func leastInterval(tasks []byte, n int) int {
	cnt := make([]int, 26)
	x := 0
	for _, c := range tasks {
		c -= 'A'
		cnt[c]++
		x = max(x, cnt[c])
	}
	s := 0
	for _, v := range cnt {
		if v == x {
			s++
		}
	}
	return max(len(tasks), (x-1)*(n+1)+s)
}
```

#### C#

```cs
public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        int[] cnt = new int[26];
        int x = 0;
        foreach (char c in tasks) {
            cnt[c - 'A']++;
            x = Math.Max(x, cnt[c - 'A']);
        }
        int s = 0;
        foreach (int v in cnt) {
            s = v == x ? s + 1 : s;
        }
        return Math.Max(tasks.Length, (x - 1) * (n + 1) + s);
    }
}
```

[Continue 0355: Design Twitter](../../0300-0399/0355.Design%20Twitter/README.md)
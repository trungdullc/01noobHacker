# [252. Meeting Rooms 🔒](https://leetcode.com/problems/meeting-rooms)

## Description

<p>Given an array of meeting time <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, determine if a person could attend all meetings.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;&nbsp;end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>

## Solutions

### Solution 1: Sorting

We sort the meetings based on their start times, and then iterate through the sorted meetings. If the start time of the current meeting is less than the end time of the previous meeting, it indicates that there is an overlap between the two meetings, and we return `false`. Otherwise, we continue iterating.

If no overlap is found by the end of the iteration, we return `true`.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(\log n)$, where $n$ is the number of meetings.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Meeting Rooms problem.
   """
   def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
      """
      Determine if a person can attend all meetings without overlaps.
      
      Args:
         intervals (list[list[int]]): List of meeting intervals [start, end].
      
      Returns:
         bool: True if all meetings can be attended, False otherwise.
      """
      # Sort intervals by start time
      intervals.sort(key=lambda x: x[0])

      for i in range(1, len(intervals)):
         if intervals[i][0] < intervals[i - 1][1]:
            return False

      return True

if __name__ == "__main__":
   sol = Solution()
   print(sol.canAttendMeetings([[0,30],[5,10],[15,20]]))
   print(sol.canAttendMeetings([[7,10],[2,4]]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
False
True

real    0m0.023s
user    0m0.014s
sys     0m0.009s
```

#### Python3

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(a[1] <= b[0] for a, b in pairwise(intervals))
```

#### Java

```java
class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        for (int i = 1; i < intervals.length; ++i) {
            if (intervals[i - 1][1] > intervals[i][0]) {
                return false;
            }
        }
        return true;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        ranges::sort(intervals, [](const auto& a, const auto& b) {
            return a[0] < b[0];
        });
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i - 1][1] > intervals[i][0]) {
                return false;
            }
        }
        return true;
    }
};
```

#### Go

```go
func canAttendMeetings(intervals [][]int) bool {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] < intervals[i-1][1] {
			return false
		}
	}
	return true
}
```

#### TypeScript

```ts
function canAttendMeetings(intervals: number[][]): boolean {
    intervals.sort((a, b) => a[0] - b[0]);
    for (let i = 1; i < intervals.length; ++i) {
        if (intervals[i][0] < intervals[i - 1][1]) {
            return false;
        }
    }
    return true;
}
```

#### Rust

```rust
impl Solution {
    pub fn can_attend_meetings(mut intervals: Vec<Vec<i32>>) -> bool {
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));
        for i in 1..intervals.len() {
            if intervals[i - 1][1] > intervals[i][0] {
                return false;
            }
        }
        true
    }
}
```

[Continue 0253: Meeting Rooms II](../../0200-0299/0253.Meeting%20Rooms%20II/README.md)
# [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days)

## Description

<p>A conveyor belt has packages that must be shipped from one port to another within <code>days</code> days.</p>

<p>The <code>i<sup>th</sup></code> package on the conveyor belt has a weight of <code>weights[i]</code>. Each day, we load the ship with packages on the conveyor belt (in the order given by <code>weights</code>). We may not load more weight than the maximum weight capacity of the ship.</p>

<p>Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within <code>days</code> days.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> weights = [1,2,3,4,5,6,7,8,9,10], days = 5
<strong>Output:</strong> 15
<strong>Explanation:</strong> A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> weights = [3,2,2,4,1,4], days = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> weights = [1,2,3,1,1], days = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong>
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= days &lt;= weights.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= weights[i] &lt;= 500</code></li>
</ul>

## Solutions

### Solution 1

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   A class to determine the least ship capacity needed to transport all packages within D days.
   """

   def shipWithinDays(self, weights: list[int], days: int) -> int:
      """
      Finds the minimal ship capacity required to ship all packages within the given number of days.
      
      Args:
         weights (list[int]): List of package weights.
         days (int): Number of days to complete the shipment.
      
      Returns:
         int: The minimum ship capacity.
      """
      def can_ship(capacity: int) -> bool:
         total = 0
         required_days = 1
         for w in weights:
            if total + w > capacity:
               required_days += 1
               total = 0
            total += w
         return required_days <= days

      left, right = max(weights), sum(weights)
      result = right

      while left <= right:
         mid = (left + right) // 2
         if can_ship(mid):
            result = mid
            right = mid - 1
         else:
            left = mid + 1

      return result

if __name__ == "__main__":
   sol = Solution()

   print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
   print(sol.shipWithinDays([3,2,2,4,1,4], 3))
   print(sol.shipWithinDays([1,2,3,1,1], 4))

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
15
6
3
```

#### Python3

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mx):
            ws, cnt = 0, 1
            for w in weights:
                ws += w
                if ws > mx:
                    cnt += 1
                    ws = w
            return cnt <= days

        left, right = max(weights), sum(weights) + 1
        return left + bisect_left(range(left, right), True, key=check)
```

#### Java

```java
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = 0, right = 0;
        for (int w : weights) {
            left = Math.max(left, w);
            right += w;
        }
        while (left < right) {
            int mid = (left + right) >> 1;
            if (check(mid, weights, days)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean check(int mx, int[] weights, int days) {
        int ws = 0, cnt = 1;
        for (int w : weights) {
            ws += w;
            if (ws > mx) {
                ws = w;
                ++cnt;
            }
        }
        return cnt <= days;
    }
}
```

#### C++

```cpp
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int left = 0, right = 0;
        for (auto& w : weights) {
            left = max(left, w);
            right += w;
        }
        auto check = [&](int mx) {
            int ws = 0, cnt = 1;
            for (auto& w : weights) {
                ws += w;
                if (ws > mx) {
                    ws = w;
                    ++cnt;
                }
            }
            return cnt <= days;
        };
        while (left < right) {
            int mid = (left + right) >> 1;
            if (check(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

#### Go

```go
func shipWithinDays(weights []int, days int) int {
	var left, right int
	for _, w := range weights {
		if left < w {
			left = w
		}
		right += w
	}
	return left + sort.Search(right, func(mx int) bool {
		mx += left
		ws, cnt := 0, 1
		for _, w := range weights {
			ws += w
			if ws > mx {
				ws = w
				cnt++
			}
		}
		return cnt <= days
	})
}
```

#### TypeScript

```ts
function shipWithinDays(weights: number[], days: number): number {
    let left = 0;
    let right = 0;
    for (const w of weights) {
        left = Math.max(left, w);
        right += w;
    }
    const check = (mx: number) => {
        let ws = 0;
        let cnt = 1;
        for (const w of weights) {
            ws += w;
            if (ws > mx) {
                ws = w;
                ++cnt;
            }
        }
        return cnt <= days;
    };
    while (left < right) {
        const mid = (left + right) >> 1;
        if (check(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

[Continue 0153: Find Minimum In Rotated Sorted Array](../../0100-0199/0153.Find%20Minimum%20in%20Rotated%20Sorted%20Array/README.md)
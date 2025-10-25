# [229. Majority Element II](https://leetcode.com/problems/majority-element-ii)

## Description

<p>Given an integer array of size <code>n</code>, find all elements that appear more than <code>&lfloor; n/3 &rfloor;</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> [3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?</p>

## Solutions

### Solution 1

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from typing import List

class Solution:
   """
   Class to find all elements in an array that appear more than n/3 times.

   Methods
   -------
   majorityElement(nums: List[int]) -> List[int]
       Returns a list of elements appearing more than n/3 times.
   """

   def majorityElement(self, nums: List[int]) -> List[int]:
      """
      Uses the Boyer-Moore Voting algorithm extended for n/3 threshold.

      Parameters
      ----------
      nums : List[int]
          Input array of integers.

      Returns
      -------
      List[int]
          List of majority elements appearing more than n/3 times.
      """
      if not nums:
         return []

      candidate1, candidate2, count1, count2 = None, None, 0, 0

      for num in nums:
         if candidate1 == num:
            count1 += 1
         elif candidate2 == num:
            count2 += 1
         elif count1 == 0:
            candidate1, count1 = num, 1
         elif count2 == 0:
            candidate2, count2 = num, 1
         else:
            count1 -= 1
            count2 -= 1

      result = []
      for cand in [candidate1, candidate2]:
         if cand is not None and nums.count(cand) > len(nums)//3:
            result.append(cand)

      return result

if __name__ == "__main__":
   sol = Solution()
   print(sol.majorityElement([3,2,3]))
   print(sol.majorityElement([1]))
   print(sol.majorityElement([1,2]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[3]
[1]
[1, 2]

real    0m0.027s
user    0m0.020s
sys     0m0.008s
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from typing import List

class Solution:
   def majorityElement(self, nums: List[int]) -> List[int]:
      """
      Find all elements that appear more than ⌊ n/3 ⌋ times in the given integer array.
      Uses the Boyer-Moore Voting Algorithm to achieve O(n) time and O(1) space complexity.
      """
      if not nums:
         return []
      
      # Find two potential candidates
      candidate1, candidate2, count1, count2 = None, None, 0, 0
      
      for n in nums:
         if n == candidate1:
            count1 += 1
         elif n == candidate2:
            count2 += 1
         elif count1 == 0:
            candidate1, count1 = n, 1
         elif count2 == 0:
            candidate2, count2 = n, 1
         else:
            count1 -= 1
            count2 -= 1
      
      # Verify the candidates
      result = []
      for c in [candidate1, candidate2]:
         if c is not None and nums.count(c) > len(nums) // 3:
            result.append(c)
      
      return result

if __name__ == "__main__":
   sol = Solution()
   print(sol.majorityElement([3, 2, 3]))
   print(sol.majorityElement([1]))
   print(sol.majorityElement([1, 2]))

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
[3]
[1]
[1, 2]
```

#### Python3

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = 0
        m1, m2 = 0, 1
        for m in nums:
            if m == m1:
                n1 += 1
            elif m == m2:
                n2 += 1
            elif n1 == 0:
                m1, n1 = m, 1
            elif n2 == 0:
                m2, n2 = m, 1
            else:
                n1, n2 = n1 - 1, n2 - 1
        return [m for m in [m1, m2] if nums.count(m) > len(nums) // 3]
```

#### Java

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n1 = 0, n2 = 0;
        int m1 = 0, m2 = 1;
        for (int m : nums) {
            if (m == m1) {
                ++n1;
            } else if (m == m2) {
                ++n2;
            } else if (n1 == 0) {
                m1 = m;
                ++n1;
            } else if (n2 == 0) {
                m2 = m;
                ++n2;
            } else {
                --n1;
                --n2;
            }
        }
        List<Integer> ans = new ArrayList<>();
        n1 = 0;
        n2 = 0;
        for (int m : nums) {
            if (m == m1) {
                ++n1;
            } else if (m == m2) {
                ++n2;
            }
        }
        if (n1 > nums.length / 3) {
            ans.add(m1);
        }
        if (n2 > nums.length / 3) {
            ans.add(m2);
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n1 = 0, n2 = 0;
        int m1 = 0, m2 = 1;
        for (int m : nums) {
            if (m == m1)
                ++n1;
            else if (m == m2)
                ++n2;
            else if (n1 == 0) {
                m1 = m;
                ++n1;
            } else if (n2 == 0) {
                m2 = m;
                ++n2;
            } else {
                --n1;
                --n2;
            }
        }
        vector<int> ans;
        if (count(nums.begin(), nums.end(), m1) > nums.size() / 3) ans.push_back(m1);
        if (count(nums.begin(), nums.end(), m2) > nums.size() / 3) ans.push_back(m2);
        return ans;
    }
};
```

#### Go

```go
func majorityElement(nums []int) []int {
	var n1, n2 int
	m1, m2 := 0, 1
	for _, m := range nums {
		if m == m1 {
			n1++
		} else if m == m2 {
			n2++
		} else if n1 == 0 {
			m1, n1 = m, 1
		} else if n2 == 0 {
			m2, n2 = m, 1
		} else {
			n1, n2 = n1-1, n2-1
		}
	}
	n1, n2 = 0, 0
	for _, m := range nums {
		if m == m1 {
			n1++
		} else if m == m2 {
			n2++
		}
	}
	var ans []int
	if n1 > len(nums)/3 {
		ans = append(ans, m1)
	}
	if n2 > len(nums)/3 {
		ans = append(ans, m2)
	}
	return ans
}
```

#### C#

```cs
public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        int n1 = 0, n2 = 0;
        int m1 = 0, m2 = 1;
        foreach (int m in nums)
        {
            if (m == m1)
            {
                ++n1;
            }
            else if (m == m2)
            {
                ++n2;
            }
            else if (n1 == 0)
            {
                m1 = m;
                ++n1;
            }
            else if (n2 == 0)
            {
                m2 = m;
                ++n2;
            }
            else
            {
                --n1;
                --n2;
            }
        }
        var ans = new List<int>();
        ans.Add(m1);
        ans.Add(m2);
        return ans.Where(m => nums.Count(n => n == m) > nums.Length / 3).ToList();
    }
}
```

#### PHP

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function majorityElement($nums) {
        $rs = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $hashmap[$nums[$i]] += 1;
            if ($hashmap[$nums[$i]] > $n / 3) {
                array_push($rs, $nums[$i]);
            }
        }
        return array_unique($rs);
    }
}
```

[Continue 0560: Subarray Sum Equals K](../../0500-0599/0560.Subarray%20Sum%20Equals%20K/README.md)
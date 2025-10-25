# [66. Plus One](https://leetcode.com/problems/plus-one)

## Description

<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>&#39;s.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>&#39;s.</li>
</ul>

## Solutions

### Solution 1: Simulation

We start traversing from the last element of the array, add one to the current element, and then take the modulus by $10$. If the result is not $0$, it means that there is no carry for the current element, and we can directly return the array. Otherwise, the current element is $0$ and needs to be carried over. We continue to traverse the previous element and repeat the above operation. If we still haven't returned after traversing the array, it means that all elements in the array are $0$, and we need to insert a $1$ at the beginning of the array.

The time complexity is $O(n)$, where $n$ is the length of the array. Ignoring the space consumption of the answer, the space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Plus One problem.
   """
   def plusOne(self, digits: list[int]) -> list[int]:
      """
      Increment the integer represented by the digits array by one.
      
      Args:
         digits (list[int]): List of digits representing a number.
      
      Returns:
         list[int]: List of digits representing the incremented number.
      """
      n = len(digits)
      for i in range(n - 1, -1, -1):
         if digits[i] < 9:
            digits[i] += 1
            return digits
         digits[i] = 0
      return [1] + digits

if __name__ == "__main__":
   sol = Solution()
   print(sol.plusOne([1,2,3]))
   print(sol.plusOne([4,3,2,1]))
   print(sol.plusOne([9]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 2, 4]
[4, 3, 2, 2]
[1, 0]

real    0m0.024s
user    0m0.017s
sys     0m0.007s
```

#### Python3

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits
```

#### Java

```java
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; --i) {
            ++digits[i];
            digits[i] %= 10;
            if (digits[i] != 0) {
                return digits;
            }
        }
        digits = new int[n + 1];
        digits[0] = 1;
        return digits;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; --i) {
            ++digits[i];
            digits[i] %= 10;
            if (digits[i] != 0) return digits;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

#### Go

```go
func plusOne(digits []int) []int {
	n := len(digits)
	for i := n - 1; i >= 0; i-- {
		digits[i]++
		digits[i] %= 10
		if digits[i] != 0 {
			return digits
		}
	}
	return append([]int{1}, digits...)
}
```

#### TypeScript

```ts
function plusOne(digits: number[]): number[] {
    const n = digits.length;
    for (let i = n - 1; i >= 0; i--) {
        if (10 > ++digits[i]) {
            return digits;
        }
        digits[i] %= 10;
    }
    return [1, ...digits];
}
```

#### Rust

```rust
impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let n = digits.len();
        for i in (0..n).rev() {
            digits[i] += 1;
            if 10 > digits[i] {
                return digits;
            }
            digits[i] %= 10;
        }
        digits.insert(0, 1);
        digits
    }
}
```

#### JavaScript

```js
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    for (let i = digits.length - 1; i >= 0; --i) {
        ++digits[i];
        digits[i] %= 10;
        if (digits[i] != 0) {
            return digits;
        }
    }
    return [1, ...digits];
};
```

[Continue 0013: Roman to Integer](../../0000-0099/0013.Roman%20to%20Integer/README.md)
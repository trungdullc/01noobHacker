# [344. Reverse String](https://leetcode.com/problems/reverse-string)

## Description

<p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>

<p>You must do this by modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> with <code>O(1)</code> extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = ["h","e","l","l","o"]
<strong>Output:</strong> ["o","l","l","e","h"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = ["H","a","n","n","a","h"]
<strong>Output:</strong> ["h","a","n","n","a","H"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is a <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii character</a>.</li>
</ul>

## Solutions

### Solution 1: Two Pointers

We use two pointers $i$ and $j$, initially pointing to the start and end of the array respectively. Each time, we swap the elements at $i$ and $j$, then move $i$ forward and $j$ backward, until $i$ and $j$ meet.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from typing import List

class Solution:
   def reverseString(self, s: List[str]) -> None:
      """
      Reverse the input string (list of characters) in-place using O(1) extra memory.
      Uses two-pointer approach swapping characters from both ends toward the center.
      """
      left, right = 0, len(s) - 1
      while left < right:
         s[left], s[right] = s[right], s[left]
         left += 1
         right -= 1

if __name__ == "__main__":
   sol = Solution()
   s1 = ["h", "e", "l", "l", "o"]
   sol.reverseString(s1)
   print(s1)

   s2 = ["H", "a", "n", "n", "a", "h"]
   sol.reverseString(s2)
   print(s2)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
['o', 'l', 'l', 'e', 'h']
['h', 'a', 'n', 'n', 'a', 'H']
```

#### Python3

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
```

#### Java

```java
class Solution {
    public void reverseString(char[] s) {
        for (int i = 0, j = s.length - 1; i < j; ++i, --j) {
            char t = s[i];
            s[i] = s[j];
            s[j] = t;
        }
    }
}
```

#### C++

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        for (int i = 0, j = s.size() - 1; i < j;) {
            swap(s[i++], s[j--]);
        }
    }
};
```

#### Go

```go
func reverseString(s []byte) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}
```

#### TypeScript

```ts
/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    for (let i = 0, j = s.length - 1; i < j; ++i, --j) {
        [s[i], s[j]] = [s[j], s[i]];
    }
}
```

#### Rust

```rust
impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut i = 0;
        let mut j = s.len() - 1;
        while i < j {
            s.swap(i, j);
            i += 1;
            j -= 1;
        }
    }
}
```

#### JavaScript

```js
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
    for (let i = 0, j = s.length - 1; i < j; ++i, --j) {
        [s[i], s[j]] = [s[j], s[i]];
    }
};
```

[Continue 0125: Valid Palindrome](../../0100-0199/0125.Valid%20Palindrome/README.md)
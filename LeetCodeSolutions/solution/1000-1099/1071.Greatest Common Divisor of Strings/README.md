# [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings)

## Description

<p>For two strings <code>s</code> and <code>t</code>, we say &quot;<code>t</code> divides <code>s</code>&quot; if and only if <code>s = t + t + t + ... + t + t</code> (i.e., <code>t</code> is concatenated with itself one or more times).</p>

<p>Given two strings <code>str1</code> and <code>str2</code>, return <em>the largest string </em><code>x</code><em> such that </em><code>x</code><em> divides both </em><code>str1</code><em> and </em><code>str2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> str1 = &quot;ABCABC&quot;, str2 = &quot;ABC&quot;
<strong>Output:</strong> &quot;ABC&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> str1 = &quot;ABABAB&quot;, str2 = &quot;ABAB&quot;
<strong>Output:</strong> &quot;AB&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> str1 = &quot;LEET&quot;, str2 = &quot;CODE&quot;
<strong>Output:</strong> &quot;&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= str1.length, str2.length &lt;= 1000</code></li>
	<li><code>str1</code> and <code>str2</code> consist of English uppercase letters.</li>
</ul>

## Solutions

### Solution 1

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

import math

class Solution:
   """
   Solution for the Greatest Common Divisor of Strings problem.
   """
   def gcdOfStrings(self, str1: str, str2: str) -> str:
      """
      Return the largest string that divides both str1 and str2.
      
      Args:
         str1 (str): First input string.
         str2 (str): Second input string.
      
      Returns:
         str: The greatest common divisor string, or "" if none exists.
      """
      if str1 + str2 != str2 + str1:
         return ""
      gcd_len = math.gcd(len(str1), len(str2))
      return str1[:gcd_len]

if __name__ == "__main__":
   sol = Solution()
   print(sol.gcdOfStrings("ABCABC", "ABC"))
   print(sol.gcdOfStrings("ABABAB", "ABAB"))
   print(sol.gcdOfStrings("LEET", "CODE"))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
ABC
AB


real    0m0.022s
user    0m0.018s
sys     0m0.004s
```

#### Python3

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def check(a, b):
            c = ""
            while len(c) < len(b):
                c += a
            return c == b

        for i in range(min(len(str1), len(str2)), 0, -1):
            t = str1[:i]
            if check(t, str1) and check(t, str2):
                return t
        return ''
```

#### Java

```java
class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
        int len = gcd(str1.length(), str2.length());
        return str1.substring(0, len);
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
```

#### C++

```cpp
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) return "";
        int n = __gcd(str1.size(), str2.size());
        return str1.substr(0, n);
    }
};
```

#### Go

```go
func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}
	n := gcd(len(str1), len(str2))
	return str1[:n]
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}
```

#### Rust

```rust
impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        if str1.clone() + &str2 != str2.clone() + &str1 {
            return String::from("");
        }
        fn gcd(a: usize, b: usize) -> usize {
            if b == 0 {
                return a;
            }
            gcd(b, a % b)
        }

        let (m, n) = (str1.len().max(str2.len()), str1.len().min(str2.len()));
        str1[..gcd(m, n)].to_string()
    }
}
```

### Solution 2

#### Python3

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        n = gcd(len(str1), len(str2))
        return str1[:n]
```

[Continue 2807: Insert Greatest Common Divisors in Linked List](../../2800-2899/2807.Insert%20Greatest%20Common%20Divisors%20in%20Linked%20List/README.md)
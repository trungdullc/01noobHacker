# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

## Description

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p style="color: yellow;">Hacker: Find and print longest common prefix froma list of strings</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>

## Solutions

### Solution 1: Character Comparison

We use the first string $strs[0]$ as a benchmark, and compare whether the $i$-th character of the subsequent strings is the same as the $i$-th character of $strs[0]$. If they are the same, we continue to compare the next character. Otherwise, we return the first $i$ characters of $strs[0]$.

If the traversal ends, it means that the first $i$ characters of all strings are the same, and we return $strs[0]$.

The time complexity is $O(n \times m)$, where $n$ and $m$ are the length of the string array and the minimum length of the strings, respectively. The space complexity is $O(1)$.

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Longest Common Prefix problem that subtract ending
   """
   def longestCommonPrefix(self, strs: list[str]) -> str:
      """
      Find the longest common prefix among an array of strings.
      
      Args:
         strs (list[str]): Array of strings.
      
      Returns:
         str: Longest common prefix or empty string if none exists.
      """
      if not strs:
         return ""
      
      prefix = strs[0]                      # flower: Use first since all have to match

      # Loop through each remaining string in the list
      for s in strs[1:]:                    # "flow","flight"
         while not s.startswith(prefix):    # flow not start with flower
            prefix = prefix[:-1]            # flower rm last: flow ❤️ Important :-1
            if not prefix:                  # if prefix empty
               return ""
      return prefix

if __name__ == "__main__":
   sol = Solution()
   print(sol.longestCommonPrefix(["flower","flow","flight"]))
   print(sol.longestCommonPrefix(["dog","racecar","car"]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
fl


real    0m0.022s
user    0m0.015s
sys     0m0.008s
```

#### Du Solution

```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3
class Solution:
   """
   This solution was easier for me to understand since it brute force
   """
   def longestCommonPrefix(self, strs):
      """
      Short circuit and return when it doesn't match
      """
      if not strs:
         return ""

      for i in range(len(strs[0])):             # 0 to 3(exclusive)
         for s in strs:                         # flower
            if s[i] != strs[0][i]:              # since it [] it eval 1 char then goes back to for i
               return strs[0][:i]               # Important :i slices ending ❤️
      return minString

if __name__ == "__main__":
   sol = Solution()
   print(sol.longestCommonPrefix(["flower", "flow", "fly"]))
   print(sol.longestCommonPrefix(["dog","racecar","car"]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
fl


real    0m0.023s
user    0m0.015s
sys     0m0.008s
```

#### Python3: Solution.py

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if len(s) <= i or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
```

#### JavaScript: Solution.js

```js
/**
 * @param {string[]} strs
 * @return {string}
 */
// CLASS VERSION                                        // FUNCTION EXPRESSION VERSION
class Solution {                                        const longestCommonPrefix = function(strs) {
  longestCommonPrefix(strs) {                             for (let j = 0; j < strs[0].length; j++) {
    for (let j = 0; j < strs[0].length; j++) {              for (let i = 0; i < strs.length; i++) {
      for (let i = 0; i < strs.length; i++) {                 if (strs[0][j] !== strs[i][j]) {
        if (strs[0][j] !== strs[i][j]) {                        return strs[0].substring(0, j);     // strs[0][0:j] Python
          return strs[0].substring(0, j);                     }
        }                                                   }
      }                                                   }
    }                                                     return strs[0];
    return strs[0];                                     };
  }
}

const sol = Solution
console.log(sol.longestCommonPrefix(["flower", "flow", "flight"]));
console.log(sol.longestCommonPrefix(["dog", "racecar", "car"])); 
```

#### Java: Solution.java

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        int n = strs.length;
        for (int i = 0; i < strs[0].length(); ++i) {
            for (int j = 1; j < n; ++j) {
                if (strs[j].length() <= i || strs[j].charAt(i) != strs[0].charAt(i)) {
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
```

#### C++: Solution.cpp

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        for (int i = 0; i < strs[0].size(); ++i) {
            for (int j = 1; j < n; ++j) {
                if (strs[j].size() <= i || strs[j][i] != strs[0][i]) {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0];
    }
};
```

#### Go: Solution.go

```go
func longestCommonPrefix(strs []string) string {
	n := len(strs)
	for i := range strs[0] {
		for j := 1; j < n; j++ {
			if len(strs[j]) <= i || strs[j][i] != strs[0][i] {
				return strs[0][:i]
			}
		}
	}
	return strs[0]
}
```

#### TypeScript: Solution.ts

```ts
function longestCommonPrefix(strs: string[]): string {
    const len = strs.reduce((r, s) => Math.min(r, s.length), Infinity);
    for (let i = len; i > 0; i--) {
        const target = strs[0].slice(0, i);
        if (strs.every(s => s.slice(0, i) === target)) {
            return target;
        }
    }
    return '';
}
```

#### Rust: Solution.rs

```rust
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut len = strs.iter().map(|s| s.len()).min().unwrap();
        for i in (1..=len).rev() {
            let mut is_equal = true;
            let target = strs[0][0..i].to_string();
            if strs.iter().all(|s| target == s[0..i]) {
                return target;
            }
        }
        String::new()
    }
}
```

#### C#: Solution.c

```cs
public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        int n = strs.Length;
        for (int i = 0; i < strs[0].Length; ++i) {
            for (int j = 1; j < n; ++j) {
                if (i >= strs[j].Length || strs[j][i] != strs[0][i]) {
                    return strs[0].Substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
```

#### PHP: Solution.php

```php
class Solution {
    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        $rs = '';
        for ($i = 0; $i < strlen($strs[0]); $i++) {
            for ($j = 1; $j < count($strs); $j++) {
                if ($strs[0][$i] != $strs[$j][$i]) {
                    return $rs;
                }
            }
            $rs = $rs . $strs[0][$i];
        }
        return $rs;
    }
}
```

#### Ruby: Solution.rb

```rb
# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  return '' if strs.nil? || strs.length.zero?

  return strs[0] if strs.length == 1

  idx = 0
  while idx < strs[0].length
    cur_char = strs[0][idx]

    str_idx = 1
    while str_idx < strs.length
      return idx > 0 ? strs[0][0..idx-1] : '' if strs[str_idx].length <= idx

      return '' if strs[str_idx][idx] != cur_char && idx.zero?
      return strs[0][0..idx - 1] if strs[str_idx][idx] != cur_char
      str_idx += 1
    end

    idx += 1
  end

  idx > 0 ? strs[0][0..idx] : ''
end
```

[Continue 0027: Remove Element](../../0000-0099/0027.Remove%20Element/README.md)
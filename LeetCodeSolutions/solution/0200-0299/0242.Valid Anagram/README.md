# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram)

## Description

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.</p>

<p style="color: yellow;">Hacker: Return boolean to determine if 2 strings anagrams</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;anagram&quot;, t = &quot;nagaram&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;rat&quot;, t = &quot;car&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

## Solutions

### Solution 1: Counting

We first determine whether the length of the two strings is equal. If they are not equal, the characters in the two strings must be different, so return `false`.

Otherwise, we use a hash table or an array of length $26$ to record the number of times each character appears in the string $s$, and then traverse the other string $t$. Each time we traverse a character, we subtract the number of times the corresponding character appears in the hash table by one. If the number of times after subtraction is less than $0$, the number of times the character appears in the two strings is different, return `false`. If after traversing the two strings, all the character counts in the hash table are $0$, it means that the characters in the two strings appear the same number of times, return `true`.

The time complexity is $O(n)$, the space complexity is $O(C)$, where $n$ is the length of the string; and $C$ is the size of the character set, which is $C=26$ in this problem.

#### Python3: cheat

```python
from collections import Counter
# automatically counts how many times each element appears in a string or list

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = Counter(s)                            # Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})

        # Subtracting everything if something is less than 0 means not the same ❤️
        for c in t:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True                                 # Counter(s) == Counter(t)
```

#### Du Solution:

```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Valid Anagram problem.
   """
   def isAnagram(self, s: str, t: str) -> bool:
      """
      Check if t is an anagram of s.
      
      Args:
         s (str): First string.
         t (str): Second string.
      
      Returns:
         bool: True if t is an anagram of s, False otherwise.
      """
      if len(s) != len(t):
         return False

      # Comparing frequency dictionary is same
      # Note: would have to to "a": 0 to "z": 0 if wanted to use cict1[0] ⭐
      dict1, dict2 = {}, {}                     # dict1 = dict()

      for char in s:
         dict1[char] = dict1.get(char, 0) + 1   # safer, if char not exist default to 0
      for char in t:
         dict2[char] = dict2.get(char, 0) + 1
      return dict1 == dict2                     # ❤️

if __name__ == "__main__":
   sol = Solution()
   print(sol.isAnagram("anagram", "nagaram"))
   print(sol.isAnagram("rat", "car"))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
True
False

real    0m0.022s
user    0m0.014s
sys     0m0.007s
```

#### Du Solution
```python
# Python with a List instead of a dict or Counter()
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        # Create frequency lists for 26 letters
        list1 = [0] * 26
        list2 = [0] * 26

        for char in s:
            list1[ord(char) - ord('a')] += 1

        for char in t:
            list2[ord(char) - ord('a')] += 1

        print("list1:", list1)
        print("list2:", list2)

        return list1 == list2 ❤️

def main() -> None:
    sol = Solution()
    print(sol.validAnagram(s="anagram", t="nagaram"))
    print(sol.validAnagram(s="rat", t="car"))

if __name__ == "__main__":
    main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
list1: [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
list2: [3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
True
list1: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
list2: [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
False
```

#### JavaScript
```javascript
class Solution {
  /**
   * Check if t is an anagram of s.
   *
   * @param {string} s - First string
   * @param {string} t - Second string
   * @returns {boolean} True if t is an anagram of s, False otherwise
   */
  isAnagram(s, t) {
    if (s.length !== t.length) return false;

    const countS = {};
    const countT = {};

    for (let char of s)
      countS[char] = (countS[char] || 0) + 1;

    for (let char of t)
      countT[char] = (countT[char] || 0) + 1;

    // Compare frequency dictionaries
    for (let key in countS) {
      if (countS[key] !== countT[key]) {
        return false;
      }
    }

    return true;
  }
}

const sol = new Solution();
console.log(sol.isAnagram("anagram", "nagaram"));
console.log(sol.isAnagram("rat", "car")); 
```

#### Java: Solution.java

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            ++cnt[s.charAt(i) - 'a'];
            --cnt[t.charAt(i) - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
```

#### C++: Solution.cpp

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        vector<int> cnt(26);
        for (int i = 0; i < s.size(); ++i) {
            ++cnt[s[i] - 'a'];
            --cnt[t[i] - 'a'];
        }
        return all_of(cnt.begin(), cnt.end(), [](int x) { return x == 0; });
    }
};
```

#### Go: Solution.go

```go
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	cnt := [26]int{}
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
		cnt[t[i]-'a']--
	}
	for _, v := range cnt {
		if v != 0 {
			return false
		}
	}
	return true
}
```

#### TypeScript: Solution.ts

```ts
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        ++cnt[s.charCodeAt(i) - 'a'.charCodeAt(0)];
        --cnt[t.charCodeAt(i) - 'a'.charCodeAt(0)];
    }
    return cnt.every(x => x === 0);
}
```

#### Rust: Solution.rs

```rust
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let n = s.len();
        let m = t.len();
        if n != m {
            return false;
        }
        let mut s = s.chars().collect::<Vec<char>>();
        let mut t = t.chars().collect::<Vec<char>>();
        s.sort();
        t.sort();
        for i in 0..n {
            if s[i] != t[i] {
                return false;
            }
        }
        true
    }
}
```

#### JavaScript: Solution.js

```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length) {
        return false;
    }
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        ++cnt[s.charCodeAt(i) - 'a'.charCodeAt(0)];
        --cnt[t.charCodeAt(i) - 'a'.charCodeAt(0)];
    }
    return cnt.every(x => x === 0);
};
```

#### C#: Solution.cs

```cs
public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }
        int[] cnt = new int[26];
        for (int i = 0; i < s.Length; ++i) {
            ++cnt[s[i] - 'a'];
            --cnt[t[i] - 'a'];
        }
        return cnt.All(x => x == 0);
    }
}
```

#### C: Solution.c

```c
int cmp(const void* a, const void* b) {
    return *(char*) a - *(char*) b;
}

bool isAnagram(char* s, char* t) {
    int n = strlen(s);
    int m = strlen(t);
    if (n != m) {
        return 0;
    }
    qsort(s, n, sizeof(char), cmp);
    qsort(t, n, sizeof(char), cmp);
    return !strcmp(s, t);
}
```

### Solution 2

#### Python3: Solution2.py

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

#### Rust: Solution2.rs

```rust
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let n = s.len();
        let m = t.len();
        if n != m {
            return false;
        }
        let (s, t) = (s.as_bytes(), t.as_bytes());
        let mut count = [0; 26];
        for i in 0..n {
            count[(s[i] - b'a') as usize] += 1;
            count[(t[i] - b'a') as usize] -= 1;
        }
        count.iter().all(|&c| c == 0)
    }
}
```

#### C: Solution2.c

```c
bool isAnagram(char* s, char* t) {
    int n = strlen(s);
    int m = strlen(t);
    if (n != m) {
        return 0;
    }
    int count[26] = {0};
    for (int i = 0; i < n; i++) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }
    for (int i = 0; i < 26; i++) {
        if (count[i]) {
            return 0;
        }
    }
    return 1;
}
```

[Continue 0001: Two Sum](../../0000-0099/0001.Two%20Sum/README.md)
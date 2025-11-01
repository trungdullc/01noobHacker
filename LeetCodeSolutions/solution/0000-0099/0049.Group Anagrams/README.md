# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

## Description

<p>Given an array of strings <code>strs</code>, group the <span data-keyword="anagram">anagrams</span> together. You can return the answer in <strong>any order</strong>.</p>

<p style="color: yellow;">Hacker: Group the anagrams together given an array of strings</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;eat&quot;,&quot;tea&quot;,&quot;tan&quot;,&quot;ate&quot;,&quot;nat&quot;,&quot;bat&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;bat&quot;],[&quot;nat&quot;,&quot;tan&quot;],[&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is no string in strs that can be rearranged to form <code>&quot;bat&quot;</code>.</li>
	<li>The strings <code>&quot;nat&quot;</code> and <code>&quot;tan&quot;</code> are anagrams as they can be rearranged to form each other.</li>
	<li>The strings <code>&quot;ate&quot;</code>, <code>&quot;eat&quot;</code>, and <code>&quot;tea&quot;</code> are anagrams as they can be rearranged to form each other.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;&quot;]]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">strs = [&quot;a&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;a&quot;]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

## Solutions

### Solution 1: Hash Table

1. Traverse the string array, sort each string in **character dictionary order** to get a new string.
2. Use the new string as `key` and `[str]` as `value`, and store them in the hash table (`HashMap<String, List<String>>`).
3. When encountering the same `key` during subsequent traversal, add it to the corresponding `value`.

Take `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]` as an example. At the end of the traversal, the state of the hash table is:

| key     | value                   |
| ------- | ----------------------- |
| `"aet"` | `["eat", "tea", "ate"]` |
| `"ant"` | `["tan", "nat"] `       |
| `"abt"` | `["bat"] `              |

Finally, return the `value` list of the hash table.

The time complexity is $O(n\times k\times \log k)$, where $n$ and $k$ are the lengths of the string array and the maximum length of the string, respectively.

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Group Anagrams problem.
   """
   def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      """
      Group strings that are anagrams of each other.
      
      Args:
         strs (list[str]): List of input strings.
      
      Returns:
         list[list[str]]: Groups of anagrams.
      """
      from collections import defaultdict

      anagram_map = defaultdict(list)       # defaultdict(<class 'list'>, {})

      for s in strs:                        # sorted() is python built-in and not in-place like sort() bc dir(str)
         key = tuple(sorted(s))             # Lists are mutable and unhashable, can't use list as a dict key ['a', 'b'] ❤️
         anagram_map[key].append(s)         # key = ('a', 'e', 't') s = "eat"

      return list(anagram_map.values())     # .values() since not need keys, nested list is return

if __name__ == "__main__":
   sol = Solution()
   print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
   print(sol.groupAnagrams([""]))
   print(sol.groupAnagrams(["a"]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
[['']]
[['a']]

real    0m0.024s
user    0m0.016s
sys     0m0.008s
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: dict[str,str] = defaultdict(list)
        for s in strs:
            sortedWord = ''.join(sorted(s))     # Note: sorted very important ['a', 'e', 't'] → "aet" ❤️
            d[sortedWord].append(s)             # "aet": "eat"
        return list(d.values())

def main() -> None:
   sol = Solution()
   print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
   print(sol.groupAnagrams([""]))
   print(sol.groupAnagrams(["a"]))

if __name__ == "__main__":
   main()
   
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
[['']]
[['a']]
```

#### JavaScript

```js
// CLASS VERSION                                        // FUNCTION EXPRESSION VERSION
class Solution {                                        const groupAnagrams = function(strs) {
  groupAnagrams(strs) {                                   const anagramMap = {};
    const anagramMap = {};                                for (const s of strs) {
    for (const s of strs) {                                 const key = s.split('').sort().join('');
      const key = s.split('').sort().join('');              if (!anagramMap[key]) anagramMap[key] = [];
      if (!anagramMap[key]) anagramMap[key] = [];           anagramMap[key].push(s);
      anagramMap[key].push(s);                            }
    }                                                     return Object.values(anagramMap);
    return Object.values(anagramMap);                   };
  }
}

const sol = new Solution();
console.log(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]));
console.log(sol.groupAnagrams([""]));
console.log(sol.groupAnagrams(["a"]));
```

#### Java

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> d = new HashMap<>();
        for (String s : strs) {
            char[] t = s.toCharArray();
            Arrays.sort(t);
            String k = String.valueOf(t);
            d.computeIfAbsent(k, key -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(d.values());
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> d;
        for (auto& s : strs) {
            string k = s;
            sort(k.begin(), k.end());
            d[k].emplace_back(s);
        }
        vector<vector<string>> ans;
        for (auto& [_, v] : d) ans.emplace_back(v);
        return ans;
    }
};
```

#### Go

```go
func groupAnagrams(strs []string) (ans [][]string) {
	d := map[string][]string{}
	for _, s := range strs {
		t := []byte(s)
		sort.Slice(t, func(i, j int) bool { return t[i] < t[j] })
		k := string(t)
		d[k] = append(d[k], s)
	}
	for _, v := range d {
		ans = append(ans, v)
	}
	return
}
```

#### TypeScript

```ts
function groupAnagrams(strs: string[]): string[][] {
    const d: Map<string, string[]> = new Map();
    for (const s of strs) {
        const k = s.split('').sort().join('');
        if (!d.has(k)) {
            d.set(k, []);
        }
        d.get(k)!.push(s);
    }
    return Array.from(d.values());
}
```

#### Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map = HashMap::new();
        for s in strs {
            let key = {
                let mut arr = s.chars().collect::<Vec<char>>();
                arr.sort();
                arr.iter().collect::<String>()
            };
            let val = map.entry(key).or_insert(vec![]);
            val.push(s);
        }
        map.into_iter().map(|(_, v)| v).collect()
    }
}
```

#### C#

```cs
using System.Collections.Generic;

public class Comparer : IEqualityComparer<string>
{
    public bool Equals(string left, string right)
    {
        if (left.Length != right.Length) return false;

        var leftCount = new int[26];
        foreach (var ch in left)
        {
            ++leftCount[ch - 'a'];
        }

        var rightCount = new int[26];
        foreach (var ch in right)
        {
            var index = ch - 'a';
            if (++rightCount[index] > leftCount[index]) return false;
        }

        return true;
    }

    public int GetHashCode(string obj)
    {
        var hashCode = 0;
        for (int i = 0; i < obj.Length; ++i)
        {
            hashCode ^= 1 << (obj[i] - 'a');
        }
        return hashCode;
    }
}

public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string, List<string>>(new Comparer());
        foreach (var str in strs)
        {
            List<string> list;
            if (!dict.TryGetValue(str, out list))
            {
                list = new List<string>();
                dict.Add(str, list);
            }
            list.Add(str);
        }
        foreach (var list in dict.Values)
        {
            list.Sort();
        }
        return new List<IList<string>>(dict.Values);
    }
}
```

### Solution 2: Counting

We can also change the sorting part in Solution 1 to counting, that is, use the characters in each string $s$ and their occurrence times as `key`, and use the string $s$ as `value` to store in the hash table.

The time complexity is $O(n\times (k + C))$, where $n$ and $k$ are the lengths of the string array and the maximum length of the string, respectively, and $C$ is the size of the character set. In this problem, $C = 26$.

#### Python3

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            d[tuple(cnt)].append(s)
        return list(d.values())
```

#### Java

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> d = new HashMap<>();
        for (String s : strs) {
            int[] cnt = new int[26];
            for (int i = 0; i < s.length(); ++i) {
                ++cnt[s.charAt(i) - 'a'];
            }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; ++i) {
                if (cnt[i] > 0) {
                    sb.append((char) ('a' + i)).append(cnt[i]);
                }
            }
            String k = sb.toString();
            d.computeIfAbsent(k, key -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(d.values());
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> d;
        for (auto& s : strs) {
            int cnt[26] = {0};
            for (auto& c : s) ++cnt[c - 'a'];
            string k;
            for (int i = 0; i < 26; ++i) {
                if (cnt[i]) {
                    k += 'a' + i;
                    k += to_string(cnt[i]);
                }
            }
            d[k].emplace_back(s);
        }
        vector<vector<string>> ans;
        for (auto& [_, v] : d) ans.emplace_back(v);
        return ans;
    }
};
```

#### Go

```go
func groupAnagrams(strs []string) (ans [][]string) {
	d := map[[26]int][]string{}
	for _, s := range strs {
		cnt := [26]int{}
		for _, c := range s {
			cnt[c-'a']++
		}
		d[cnt] = append(d[cnt], s)
	}
	for _, v := range d {
		ans = append(ans, v)
	}
	return
}
```

#### TypeScript

```ts
function groupAnagrams(strs: string[]): string[][] {
    const map = new Map<string, string[]>();
    for (const str of strs) {
        const k = str.split('').sort().join('');
        map.set(k, (map.get(k) ?? []).concat([str]));
    }
    return [...map.values()];
}
```

[Continue 0912: Sort an Array](../../0900-0999/0912.Sort%20an%20Array/README.md)
# [71. Simplify Path](https://leetcode.com/problems/simplify-path)

## Description

<p>You are given an <em>absolute</em> path for a Unix-style file system, which always begins with a slash <code>&#39;/&#39;</code>. Your task is to transform this absolute path into its <strong>simplified canonical path</strong>.</p>

<p>The <em>rules</em> of a Unix-style file system are as follows:</p>

<ul>
	<li>A single period <code>&#39;.&#39;</code> represents the current directory.</li>
	<li>A double period <code>&#39;..&#39;</code> represents the previous/parent directory.</li>
	<li>Multiple consecutive slashes such as <code>&#39;//&#39;</code> and <code>&#39;///&#39;</code> are treated as a single slash <code>&#39;/&#39;</code>.</li>
	<li>Any sequence of periods that does <strong>not match</strong> the rules above should be treated as a <strong>valid directory or</strong> <strong>file </strong><strong>name</strong>. For example, <code>&#39;...&#39; </code>and <code>&#39;....&#39;</code> are valid directory or file names.</li>
</ul>

<p>The simplified canonical path should follow these <em>rules</em>:</p>

<ul>
	<li>The path must start with a single slash <code>&#39;/&#39;</code>.</li>
	<li>Directories within the path must be separated by exactly one slash <code>&#39;/&#39;</code>.</li>
	<li>The path must not end with a slash <code>&#39;/&#39;</code>, unless it is the root directory.</li>
	<li>The path must not have any single or double periods (<code>&#39;.&#39;</code> and <code>&#39;..&#39;</code>) used to denote current or parent directories.</li>
</ul>

<p>Return the <strong>simplified canonical path</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/home/&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/home&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The trailing slash should be removed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/home//foo/&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/home/foo&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Multiple consecutive slashes are replaced by a single one.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/home/user/Documents/../Pictures&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/home/user/Pictures&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>A double period <code>&quot;..&quot;</code> refers to the directory up a level (the parent directory).</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/../&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Going one level up from the root directory is not possible.</p>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = &quot;/.../a/../b/c/../d/./&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;/.../b/d&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p><code>&quot;...&quot;</code> is a valid name for a directory in this problem.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 3000</code></li>
	<li><code>path</code> consists of English letters, digits, period <code>&#39;.&#39;</code>, slash <code>&#39;/&#39;</code> or <code>&#39;_&#39;</code>.</li>
	<li><code>path</code> is a valid absolute Unix path.</li>
</ul>

## Solutions

### Solution 1: Stack

We first split the path into a number of substrings split by `'/'`. Then, we traverse each substring and perform the following operations based on the content of the substring:

-   If the substring is empty or `'.'`, no operation is performed because `'.'` represents the current directory.
-   If the substring is `'..'`, the top element of the stack is popped, because `'..'` represents the parent directory.
-   If the substring is other strings, the substring is pushed into the stack, because the substring represents the subdirectory of the current directory.

Finally, we concatenate all the elements in the stack from the bottom to the top of the stack to form a string, which is the simplified canonical path.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of the path.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   A class to simplify Unix-style absolute file paths into their canonical form.
   """

   def simplifyPath(self, path: str) -> str:
      """
      Simplifies the given absolute Unix-style path.
      
      Args:
         path (str): The absolute path to simplify.
      
      Returns:
         str: The simplified canonical path.
      """
      stack = []
      parts = path.split('/')

      for part in parts:
         if part == '' or part == '.':
            continue
         elif part == '..':
            if stack:
               stack.pop()
         else:
            stack.append(part)

      return '/' + '/'.join(stack)

if __name__ == "__main__":
   sol = Solution()

   print(sol.simplifyPath("/home/"))
   print(sol.simplifyPath("/home//foo/"))
   print(sol.simplifyPath("/home/user/Documents/../Pictures"))
   print(sol.simplifyPath("/../"))
   print(sol.simplifyPath("/.../a/../b/c/../d/./"))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
/home
/home/foo
/home/user/Pictures
/
/.../b/d

real    0m0.027s
user    0m0.018s
sys     0m0.008s
```

#### Python3

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for s in path.split('/'):
            if not s or s == '.':
                continue
            if s == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(s)
        return '/' + '/'.join(stk)
```

#### Java

```java
class Solution {
    public String simplifyPath(String path) {
        Deque<String> stk = new ArrayDeque<>();
        for (String s : path.split("/")) {
            if ("".equals(s) || ".".equals(s)) {
                continue;
            }
            if ("..".equals(s)) {
                stk.pollLast();
            } else {
                stk.offerLast(s);
            }
        }
        return "/" + String.join("/", stk);
    }
}
```

#### C++

```cpp
class Solution {
public:
    string simplifyPath(string path) {
        deque<string> stk;
        stringstream ss(path);
        string t;
        while (getline(ss, t, '/')) {
            if (t == "" || t == ".") {
                continue;
            }
            if (t == "..") {
                if (!stk.empty()) {
                    stk.pop_back();
                }
            } else {
                stk.push_back(t);
            }
        }
        if (stk.empty()) {
            return "/";
        }
        string ans;
        for (auto& s : stk) {
            ans += "/" + s;
        }
        return ans;
    }
};
```

#### Go

```go
func simplifyPath(path string) string {
	var stk []string
	for _, s := range strings.Split(path, "/") {
		if s == "" || s == "." {
			continue
		}
		if s == ".." {
			if len(stk) > 0 {
				stk = stk[0 : len(stk)-1]
			}
		} else {
			stk = append(stk, s)
		}
	}
	return "/" + strings.Join(stk, "/")
}
```

#### TypeScript

```ts
function simplifyPath(path: string): string {
    const stk: string[] = [];
    for (const s of path.split('/')) {
        if (s === '' || s === '.') {
            continue;
        }
        if (s === '..') {
            if (stk.length) {
                stk.pop();
            }
        } else {
            stk.push(s);
        }
    }
    return '/' + stk.join('/');
}
```

#### Rust

```rust
impl Solution {
    #[allow(dead_code)]
    pub fn simplify_path(path: String) -> String {
        let mut s: Vec<&str> = Vec::new();

        // Split the path
        let p_vec = path.split("/").collect::<Vec<&str>>();

        // Traverse the path vector
        for p in p_vec {
            match p {
                // Do nothing for "" or "."
                "" | "." => {
                    continue;
                }
                ".." => {
                    if !s.is_empty() {
                        s.pop();
                    }
                }
                _ => s.push(p),
            }
        }

        "/".to_string() + &s.join("/")
    }
}
```

#### C#

```cs
public class Solution {
    public string SimplifyPath(string path) {
        var stk = new Stack<string>();
        foreach (var s in path.Split('/')) {
            if (s == "" || s == ".") {
                continue;
            }
            if (s == "..") {
                if (stk.Count > 0) {
                    stk.Pop();
                }
            } else {
                stk.Push(s);
            }
        }
        var sb = new StringBuilder();
        while (stk.Count > 0) {
            sb.Insert(0, "/" + stk.Pop());
        }
        return sb.Length == 0 ? "/" : sb.ToString();
    }
}
```

### Solution 2

#### Go

```go
func simplifyPath(path string) string {
	return filepath.Clean(path)
}
```

[Continue 0394: Decode String](../../0300-0399/0394.Decode%20String/README.md)
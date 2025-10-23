# [271. Encode and Decode Strings 🔒](https://leetcode.com/problems/encode-and-decode-strings)

## Description

<p>Design an algorithm to encode <b>a list of strings</b> to <b>a string</b>. The encoded string is then sent over the network and is decoded back to the original list of strings.</p>

<p>Machine 1 (sender) has the function:</p>

<pre>
string encode(vector&lt;string&gt; strs) {
  // ... your code
  return encoded_string;
}</pre>

Machine 2 (receiver) has the function:

<pre>
vector&lt;string&gt; decode(string s) {
  //... your code
  return strs;
}
</pre>

<p>So Machine 1 does:</p>

<pre>
string encoded_string = encode(strs);
</pre>

<p>and Machine 2 does:</p>

<pre>
vector&lt;string&gt; strs2 = decode(encoded_string);
</pre>

<p><code>strs2</code> in Machine 2 should be the same as <code>strs</code> in Machine 1.</p>

<p>Implement the <code>encode</code> and <code>decode</code> methods.</p>

<p>You are not allowed to&nbsp;solve the problem using any serialize methods (such as <code>eval</code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dummy_input = [&quot;Hello&quot;,&quot;World&quot;]
<strong>Output:</strong> [&quot;Hello&quot;,&quot;World&quot;]
<strong>Explanation:</strong>
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---&gt; Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dummy_input = [&quot;&quot;]
<strong>Output:</strong> [&quot;&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> contains any possible characters out of <code>256</code> valid ASCII characters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up: </strong>Could you write a generalized algorithm to work on any possible set of characters?</p>

## Solutions

### Solution 1: Encode String Length

During encoding, we convert the length of the string into a fixed 4-digit string, add the string itself, and append it to the result string in sequence.

During decoding, we first take the first four digits of the string to get the length, and then cut the following string according to the length. We cut it in sequence until we get the list of strings.

The time complexity is $O(n)$.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Codec:
   def encode(self, strs: List[str]) -> str:
      """
      Encodes a list of strings to a single string.
      Uses length-prefix encoding: 'length#string'.
      """
      encoded = ''
      for s in strs:
         encoded += f"{len(s)}#{s}"
      return encoded

   def decode(self, s: str) -> List[str]:
      """
      Decodes a single string to a list of strings.
      Reads length prefix and extracts each string accordingly.
      """
      decoded = []
      i = 0
      while i < len(s):
         # Find the delimiter '#' to get the length
         j = i
         while s[j] != '#':
            j += 1
         length = int(s[i:j])
         # Extract the string of given length
         decoded.append(s[j+1:j+1+length])
         # Move to the next encoded string
         i = j + 1 + length
      return decoded

def main() -> None:
   codec = Codec()
   dummy_input1 = ["Hello","World"]
   encoded1 = codec.encode(dummy_input1)
   print("Encoded:", encoded1)
   print("Decoded:", codec.decode(encoded1))  # Output: ['Hello', 'World']

   dummy_input2 = [""]
   encoded2 = codec.encode(dummy_input2)
   print("Encoded:", encoded2)
   print("Decoded:", codec.decode(encoded2))  # Output: ['']

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
Encoded: 5#Hello5#World
Decoded: ['Hello', 'World']
Encoded: 0#
Decoded: ['']

AsianHacker-picoctf@webshell:/tmp$ python -q ⌨️ 
>>> from pythonScript import Codec ⌨️
>>> help(Codec.encode) ⌨️

Help on function encode in module pythonScript:

encode(self, strs: List[str]) -> str
    Encodes a list of strings to a single string.
    Uses length-prefix encoding: 'length#string'.
(END)

>>> dir(codec) ⌨️
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'decode', 'encode']
>>> codec = Codec() ⌨️
>>> help(codec.decode) ⌨️
Help on method decode in module pythonScript:

decode(s: str) -> List[str] method of pythonScript.Codec instance
    Decodes a single string to a list of strings.
    Reads length prefix and extracts each string accordingly.
(END)
>>> exit() ⌨️
```

#### Python3

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        ans = []
        for s in strs:
            ans.append('{:4}'.format(len(s)) + s)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ans = []
        i, n = 0, len(s)
        while i < n:
            size = int(s[i : i + 4])
            i += 4
            ans.append(s[i : i + size])
            i += size
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

#### Java

```java
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder ans = new StringBuilder();
        for (String s : strs) {
            ans.append((char) s.length()).append(s);
        }
        return ans.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> ans = new ArrayList<>();
        int i = 0, n = s.length();
        while (i < n) {
            int size = s.charAt(i++);
            ans.add(s.substring(i, i + size));
            i += size;
        }
        return ans;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
```

#### C++

```cpp
class Codec {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string ans;
        for (string s : strs) {
            int size = s.size();
            ans += string((const char*) &size, sizeof(size));
            ans += s;
        }
        return ans;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> ans;
        int i = 0, n = s.size();
        int size = 0;
        while (i < n) {
            memcpy(&size, s.data() + i, sizeof(size));
            i += sizeof(size);
            ans.push_back(s.substr(i, size));
            i += size;
        }
        return ans;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
```

#### Go

```go
type Codec struct {
}

// Encodes a list of strings to a single string.
func (codec *Codec) Encode(strs []string) string {
	ans := &bytes.Buffer{}
	for _, s := range strs {
		t := fmt.Sprintf("%04d", len(s))
		ans.WriteString(t)
		ans.WriteString(s)
	}
	return ans.String()
}

// Decodes a single string to a list of strings.
func (codec *Codec) Decode(strs string) []string {
	ans := []string{}
	i, n := 0, len(strs)
	for i < n {
		t := strs[i : i+4]
		i += 4
		size, _ := strconv.Atoi(t)
		ans = append(ans, strs[i:i+size])
		i += size
	}
	return ans
}

// Your Codec object will be instantiated and called as such:
// var codec Codec
// codec.Decode(codec.Encode(strs));
```

[Continue 0304: Range Sum Query 2D Immutable ](../../0300-0399/0304.Range%20Sum%20Query%202D%20-%20Immutable/README.md)
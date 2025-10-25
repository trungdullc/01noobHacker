# [50. Pow(x, n)](https://leetcode.com/problems/powx-n)

## Description

<p>Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates <code>x</code> raised to the power <code>n</code> (i.e., <code>x<sup>n</sup></code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = 10
<strong>Output:</strong> 1024.00000
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 2.10000, n = 3
<strong>Output:</strong> 9.26100
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 2.00000, n = -2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-100.0 &lt; x &lt; 100.0</code></li>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup>-1</code></li>
	<li><code>n</code> is an integer.</li>
	<li>Either <code>x</code> is not zero or <code>n &gt; 0</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li>
</ul>

## Solutions

### Solution 1: Mathematics (Fast Powering)

The core idea of the fast powering algorithm is to decompose the exponent $n$ into the sum of $1$s on several binary bits, and then transform the $n$th power of $x$ into the product of several powers of $x$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$. Here, $n$ is the exponent.

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for the Pow(x, n) problem.
   """
   def myPow(self, x: float, n: int) -> float:
      """
      Calculate x raised to the power n.
      
      Args:
         x (float): Base.
         n (int): Exponent.
      
      Returns:
         float: Result of x ** n.
      """
      if n == 0:
         return 1.0
      if n < 0:
         x = 1 / x
         n = -n

      result = 1.0
      current_product = x

      while n > 0:
         if n % 2 == 1:
            result *= current_product
         current_product *= current_product
         n //= 2

      return result

if __name__ == "__main__":
   sol = Solution()
   print(sol.myPow(2.0, 10))
   print(sol.myPow(2.1, 3))
   print(sol.myPow(2.0, -2))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
1024.0
9.261000000000001
0.25

real    0m0.024s
user    0m0.023s
sys     0m0.000s
```

#### Python3

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            ans = 1
            while n:
                if n & 1:
                    ans *= a
                a *= a
                n >>= 1
            return ans

        return qpow(x, n) if n >= 0 else 1 / qpow(x, -n)
```

#### Java

```java
class Solution {
    public double myPow(double x, int n) {
        return n >= 0 ? qpow(x, n) : 1 / qpow(x, -(long) n);
    }

    private double qpow(double a, long n) {
        double ans = 1;
        for (; n > 0; n >>= 1) {
            if ((n & 1) == 1) {
                ans = ans * a;
            }
            a = a * a;
        }
        return ans;
    }
}
```

#### C++

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        auto qpow = [](double a, long long n) {
            double ans = 1;
            for (; n; n >>= 1) {
                if (n & 1) {
                    ans *= a;
                }
                a *= a;
            }
            return ans;
        };
        return n >= 0 ? qpow(x, n) : 1 / qpow(x, -(long long) n);
    }
};
```

#### Go

```go
func myPow(x float64, n int) float64 {
	qpow := func(a float64, n int) float64 {
		ans := 1.0
		for ; n > 0; n >>= 1 {
			if n&1 == 1 {
				ans *= a
			}
			a *= a
		}
		return ans
	}
	if n >= 0 {
		return qpow(x, n)
	}
	return 1 / qpow(x, -n)
}
```

#### TypeScript

```ts
function myPow(x: number, n: number): number {
    const qpow = (a: number, n: number): number => {
        let ans = 1;
        for (; n; n >>>= 1) {
            if (n & 1) {
                ans *= a;
            }
            a *= a;
        }
        return ans;
    };
    return n >= 0 ? qpow(x, n) : 1 / qpow(x, -n);
}
```

#### Rust

```rust
impl Solution {
    #[allow(dead_code)]
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let mut x = x;
        let n = n as i64;
        if n >= 0 {
            Self::quick_pow(&mut x, n)
        } else {
            1.0 / Self::quick_pow(&mut x, -n)
        }
    }

    #[allow(dead_code)]
    fn quick_pow(x: &mut f64, mut n: i64) -> f64 {
        // `n` should greater or equal to zero
        let mut ret = 1.0;
        while n != 0 {
            if (n & 0x1) == 1 {
                ret *= *x;
            }
            *x *= *x;
            n >>= 1;
        }
        ret
    }
}
```

#### JavaScript

```js
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function (x, n) {
    const qpow = (a, n) => {
        let ans = 1;
        for (; n; n >>>= 1) {
            if (n & 1) {
                ans *= a;
            }
            a *= a;
        }
        return ans;
    };
    return n >= 0 ? qpow(x, n) : 1 / qpow(x, -n);
};
```

#### C#

```cs
public class Solution {
    public double MyPow(double x, int n) {
        return n >= 0 ? qpow(x, n) : 1.0 / qpow(x, -(long)n);
    }

    private double qpow(double a, long n) {
        double ans = 1;
        for (; n > 0; n >>= 1) {
            if ((n & 1) == 1) {
                ans *= a;
            }
            a *= a;
        }
        return ans;
    }
}
```

[Continue 0043: Multiply Strings](../../0000-0099/0043.Multiply%20Strings/README.md)
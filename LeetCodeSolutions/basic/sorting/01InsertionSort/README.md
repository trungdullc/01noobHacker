#### Python3

```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3
# Important: def not ned self unless in class ⭐
# def swap(num1, num2):
#    num1 ^= num2
#    num2 ^= num1
#    num1 ^= num2

"""
Iteration 0         Iteration 1             Iteration 2         Iteration 3
j-1 j   # pointers     j-1 j                      j-1 j                  j-1 j
[2, 4, 3, 6, 1]     [2, 3, 4, 6, 1] swap()  [2, 3, 4, 6, 1]     [2, 3, 4, 1, 6] swap()
                    j-1 j                      j-1 j                  j-1 j
                    [2, 3, 4, 6, 1]         [2, 3, 4, 6, 1]     [2, 3, 1, 4, 6] swap()
                                            j-1 j                  j-1 j
                                            [2, 3, 4, 6, 1]     [2, 1, 3, 4, 6] swap()
                                                                j-1 j
                                                                [1, 2, 3, 4, 6] swap()
"""
class Solution:
   def InsertionSort(self, a: list[int], N:int) -> list[int]:
      """
      Recursion check left, if smaller then swap()
      Left Sorted Partition | Right Unsorted Partition
      """
      for i in range(N-1):      # redo N-1 times
         j = i + 1              # start at 2nd and reset
         while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -=1
      return a

if __name__ == "__main__":
   sol = Solution()
   print(sol.InsertionSort([2, 4, 3, 6, 1], 5))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 2, 3, 4, 6]

real    0m0.025s
user    0m0.016s
sys     0m0.008s
```

#### JavaScript

```js
// JS Class Version                                    // JS Function Expression Version

class Solution {                                          const insertionSort = function(a, N) {
  insertionSort(a, N) {                                     for (let i = 0; i < N - 1; i++) {
    for (let i = 0; i < N - 1; i++) {                         let j = i + 1;
      let j = i + 1;                                          while (j > 0 && a[j - 1] > a[j]) {
      while (j > 0 && a[j - 1] > a[j]) {                        [a[j], a[j - 1]] = [a[j - 1], a[j]];
        [a[j], a[j - 1]] = [a[j - 1], a[j]];                    j--;
        j--;                                                  }
      }                                                     }
    }                                                       return a;
    return a;                                             };
  }
}

const sol = new Solution();
console.log(sol.InsertionSort([2, 4, 3, 6, 1], 5)))
```

#### Java

```java
import java.util.Arrays;

public class InsertionSort {

    private static void insertionSort(int[] nums) {
        for (int i = 1, j, n = nums.length; i < n; ++i) {
            int num = nums[i];
            for (j = i - 1; j >= 0 && nums[j] > num; --j) {
                nums[j + 1] = nums[j];
            }
            nums[j + 1] = num;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 7, 9, 5, 8};
        insertionSort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
```

#### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

void printvec(const vector<int>& vec, const string& strbegin = "", const string& strend = "") {
    cout << strbegin << endl;
    for (auto val : vec) {
        cout << val << "\t";
    }

    cout << endl;
    cout << strend << endl;
}

void insertsort(vector<int>& vec) {
    for (int i = 1; i < vec.size(); i++) {
        int j = i - 1;
        int num = vec[i];
        for (; j >= 0 && vec[j] > num; j--) {
            vec[j + 1] = vec[j];
        }

        vec[j + 1] = num;
    }

    return;
}

int main() {
    vector<int> vec = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    printvec(vec);
    insertsort(vec);
    printvec(vec, "after insert sort");
    return (0);
}
```

#### Go

```go
package main

import "fmt"

func insertionSort(nums []int) {
	for i, n := 1, len(nums); i < n; i++ {
		j, num := i-1, nums[i]
		for ; j >= 0 && nums[j] > num; j-- {
			nums[j+1] = nums[j]
		}
		nums[j+1] = num
	}
}

func main() {
	nums := []int{1, 2, 7, 9, 5, 8}
	insertionSort(nums)
	fmt.Println(nums)
}
```

#### Rust

```rust
fn insertion_sort(nums: &mut Vec<i32>) {
    let n = nums.len();
    for i in 1..n {
        let mut j = i - 1;
        let temp = nums[i];
        while j >= (0 as usize) && nums[j] > temp {
            nums[j + 1] = nums[j];
            j -= 1;
        }
        nums[j + 1] = temp;
    }
}

fn main() {
    let mut nums = vec![1, 2, 7, 9, 5, 8];
    insertion_sort(&mut nums);
    println!("{:?}", nums);
}
```

#### C#

```cs
using System.Diagnostics;
using static System.Console;
namespace Pro;
public class Program
{
    public static void Main()
    {
        int[] test = new int[] { 31, 12, 10, 5, 6, 7, 8, 10, 23, 34, 56, 43, 32, 21 };
        InsertSortNums(test);
        foreach (var item in test)
        {
            WriteLine(item);
        }
    }
    public static void InsertSortNums(int[] nums)
    {
        for (int initial = 1; initial < nums.Length; initial++)
        {
            for (int second_sort = 0; second_sort < initial; second_sort++)
            {
                if (nums[second_sort] > nums[initial])
                {
                    swap(ref nums[second_sort], ref nums[initial]);
                }
            }
        }
    }

    private static void swap(ref int compare_left, ref int compare_right)
    {
        int temp = compare_left;
        compare_left = compare_right;
        compare_right = temp;
    }
}
```
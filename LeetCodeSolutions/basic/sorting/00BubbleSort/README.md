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
Iteration 0                         Iteration 1                         Iteration 2                         Iteration 3
 j j+1              # pointers       j j+1     Sorted Partition          j j+1                               j j+1 
[2, 4, 3, 6, 1]                     [2, 3, 4, 1 | 6]                    [2, 3, 1 | 4, 6]                    [1, 2 | 3, 4, 6] swap()
    j j+1                               j j+1                              j j+1 
[2, 3, 4, 6, 1]     swap()          [2, 3, 4, 1 | 6]                    [2, 1, 3 | 4, 6]  swap() i = 2
       j j+1                               j j+1 
[2, 3, 4, 6, 1]                     [2, 3, 1, 4 | 6]  swap() i = 1
          j j+1
[2, 3, 4, 1, 6]     swap() i=0
"""
class Solution:
   def bubbleSort(self, a: list[int], N: int) -> list[int]:
      """
      Compare 1,2 then 2,3 ... last - 1, last
      Check if left is bigger than right, if true swap
      Right Side is sorted partition (Ascending)
      """
      for i in range(N):                           # redo N-1 times
         for j in range(N - i - 1):                # -i so not always go to end for sorting
            if a[j] > a[j + 1]:
               a[j], a[j + 1] = a[j + 1], a[j]     # No Need XOR swap(a[j], a[j+1])
      return a

if __name__ == "__main__":
   sol = Solution()
   print(sol.bubbleSort([2, 4, 3, 6, 1], 5))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 2, 3, 4, 6]

real    0m0.023s
user    0m0.019s
sys     0m0.005s
```

#### JavaScript

```js
// Class Version                                       // Function Expression Version 
class Solution {                                       const bubbleSort = function(a, N) {
  bubbleSort(a, N) {                                     for (let i = 0; i < N; i++) {
    for (let i = 0; i < N; i++) {                          for (let j = 0; j < N - i - 1; j++) {
      for (let j = 0; j < N - i - 1; j++) {                  if (a[j] > a[j + 1]) {
        if (a[j] > a[j + 1]) {                                 [a[j], a[j + 1]] = [a[j + 1], a[j]];
          [a[j], a[j + 1]] = [a[j + 1], a[j]];               }
        }                                                  }
      }                                                  }
    }                                                    return a;
    return a;                                          };
  }
}

const sol = new Solution();
console.log(sol.bubbleSort([2,4,3,6,1], 5));
```

#### Java

```java
import java.util.Arrays;

public class BubbleSort {

    private static void bubbleSort(int[] nums) {
        boolean hasChange = true;
        for (int i = 0, n = nums.length; i < n - 1 && hasChange; ++i) {
            hasChange = false;
            for (int j = 0; j < n - i - 1; ++j) {
                if (nums[j] > nums[j + 1]) {
                    swap(nums, j, j + 1);
                    hasChange = true;
                }
            }
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 7, 9, 5, 8};
        bubbleSort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
```

#### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        bool change = false;
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                change = true;
            }
        }
        if (!change) break;
    }
}

int main() {
    vector<int> arr = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    bubbleSort(arr);
    for (int v : arr) cout << v << " ";
    cout << endl;
}
```

#### Go

```go
package main

import "fmt"

func bubbleSort(nums []int) {
	hasChange := true
	for i, n := 0, len(nums); i < n-1 && hasChange; i++ {
		hasChange = false
		for j := 0; j < n-i-1; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
				hasChange = true
			}
		}
	}
}

func main() {
	nums := []int{1, 2, 7, 9, 5, 8}
	bubbleSort(nums)
	fmt.Println(nums)
}
```

#### Rust

```rust
fn bubble_sort(nums: &mut Vec<i32>) {
    let n = nums.len();
    for i in 0..n - 1 {
        for j in i..n {
            if nums[i] > nums[j] {
                let temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
}

fn main() {
    let mut nums = vec![1, 2, 7, 9, 5, 8];
    bubble_sort(&mut nums);
    println!("{:?}", nums);
}
```

#### C#

```cs
using static System.Console;
namespace Pro;
public class Program
{
    public static void Main()
    {
        int[] test = new int[] { 56, 876, 34, 23, 45, 501, 2, 3, 4, 6, 5, 7, 8, 9, 11, 10, 12, 23, 34 };
        BubbleSortNums(test);
        foreach (var item in test)
        {
            WriteLine(item);
        }
        ReadLine();
    }
    public static void BubbleSortNums(int[] nums)
    {
        int numchange = 0;
        for (int initial = 0; initial < nums.Length - numchange; initial++)
        {
            WriteLine($"{initial} start ");
            // 记录此值 用于迭代开始位置
            bool changelog = false;
            for (int second_sortnum = initial; second_sortnum < nums.Length - 1; second_sortnum++)
            {
                if (nums[second_sortnum] > nums[second_sortnum + 1])
                {
                    swap(ref nums[second_sortnum], ref nums[second_sortnum + 1]);
                    if (!changelog)
                    {
                        // 记录转换的位置，让initial开始位置从转换位置前开始
                        initial = ((second_sortnum - 2) > 0) ? (second_sortnum - 2) : -1;
                        numchange += 1;
                    }
                    changelog = true;
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

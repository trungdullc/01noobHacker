#### Python3

```python

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3
# def swap(num1, num2):
#    num1 ^= num2
#    num2 ^= num1
#    num1 ^= num2

class Solution:
   def SelectionSort(self, a: list[int], N: int) -> list[int]:
      """
      Selecting unsorted smallest number and moving it to left side
      Find min and swap with pivot
      Left Sorted Partition | Right Unsorted Partition
      i is pivot
      minPtr is tracker of index of smallest number which will go to pivot at end if moved from there
      j is pointer
      """
      for i in range(N - 1):            # redo N-1 times, i is pivot
         minPtr = i
         for j in range(i + 1, N):
            if a[j] < a[minPtr]:        # if minPtr gt a[j] means no longer min number, reassign
               minPtr = j
         if minPtr != i:                # Note: Outside for loop, swap at end if minPtr moved away from pivot
            a[i], a[minPtr] = a[minPtr], a[i]
      return a

"""
Iteration 0         Iteration 1                 Iteration 2             Iteration 3
minPtr = 0                  minPtr = 2                  minPtr = 2                minPtr = 4
    j            sorted     j                              j                          j
[2, 4, 3, 6, 1]     [1 | 4, 3, 6, 2]            [1, 2 | 3, 6, 4]        [1, 2, 3 | 4, 6]  swap()
minPtr = 0                 minPtr = 2                   minPtr = 2
       j                       j                              j
[2, 4, 3, 6, 1]     [1 | 4, 3, 6, 2]            [1, 2 | 3, 6, 4]
minPtr = 0                  minPtr = 4
          j                       j
[2, 4, 3, 6, 1]     [1 | 2, 3, 6, 4] swap()
           minPtr = 4
             j
[1, 4, 3, 6, 2]  swap()
"""
if __name__ == "__main__":
   sol = Solution()
   print(sol.SelectionSort([2, 4, 3, 6, 1], 5))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py
[1, 2, 3, 4, 6]

real    0m0.022s
user    0m0.017s
sys     0m0.004s
```

#### JavaScript

```js
// JS Class Version                                         // JS Function Expression Version
class Solution {                                            const selectionSort = function(a, N) {
  selectionSort(a, N) {                                       for (let i = 0; i < N - 1; i++) {
    for (let i = 0; i < N - 1; i++) {                           let minPtr = i;
      let minPtr = i;                                           for (let j = i + 1; j < N; j++) {
      for (let j = i + 1; j < N; j++) {                           if (a[j] < a[minPtr]) {
        if (a[j] < a[minPtr]) {                                     minPtr = j;
          minPtr = j;                                             }
        }                                                       }
      }                                                         if (minPtr !== i) {
      if (minPtr !== i) {                                         [a[i], a[minPtr]] = [a[minPtr], a[i]];
        [a[i], a[minPtr]] = [a[minPtr], a[i]];                  }
      }                                                       }
    }                                                         return a;
    return a;                                               };
  }
}

const sol = new Solution();
console.log(sol.selectionSort([2,4,3,6,1], 5));
```

#### Java

```java
import java.util.Arrays;

public class SelectionSort {

    private static void selectionSort(int[] nums) {
        for (int i = 0, n = nums.length; i < n - 1; ++i) {
            int minIndex = i;
            for (int j = i; j < n; ++j) {
                if (nums[j] < nums[minIndex]) {
                    minIndex = j;
                }
            }
            swap(nums, minIndex, i);
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 7, 9, 5, 8};
        selectionSort(nums);
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

void selectsort(vector<int>& vec) {
    for (int i = 0; i < vec.size() - 1; i++) {
        int minidx = i;
        for (int j = i + 1; j < vec.size(); j++) {
            if (vec[minidx] > vec[j]) {
                minidx = j;
            }
        }

        swap(vec[i], vec[minidx]);
    }
}

int main(void) {
    vector<int> vec = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    printvec(vec);
    selectsort(vec);
    printvec(vec, "after insert sort");
    return (0);
}
```

#### Go

```go
package main

import "fmt"

func selectionSort(nums []int) {
	for i, n := 0, len(nums); i < n-1; i++ {
		minIndex := i
		for j := i + 1; j < n; j++ {
			if nums[j] < nums[minIndex] {
				minIndex = j
			}
		}
		nums[minIndex], nums[i] = nums[i], nums[minIndex]
	}
}

func main() {
	nums := []int{1, 2, 7, 9, 5, 8}
	selectionSort(nums)
	fmt.Println(nums)
}
```

#### Rust

```rust
fn selection_sort(nums: &mut Vec<i32>) {
    let n = nums.len();
    for i in 0..n - 1 {
        let mut min_index = i;
        for j in i..n {
            if nums[j] < nums[min_index] {
                min_index = j;
            }
        }
        let temp = nums[min_index];
        nums[min_index] = nums[i];
        nums[i] = temp;
    }
}

fn main() {
    let mut nums = vec![1, 2, 7, 9, 5, 8];
    selection_sort(&mut nums);
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
        int[] test = new int[] {90, 12, 77, 9, 0, 2, 23, 23, 3, 57, 80};
        SelectionSortNums(test);
        foreach (var item in test)
        {
            WriteLine(item);
        }
    }
    public static void SelectionSortNums(int[] nums)
    {
        for (int initial = 0; initial < nums.Length; initial++)
        {
            for (int second_sort = initial; second_sort < nums.Length; second_sort++)
            {
                if (nums[initial] > nums[second_sort])
                {
                    swap(ref nums[initial], ref nums[second_sort]);
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
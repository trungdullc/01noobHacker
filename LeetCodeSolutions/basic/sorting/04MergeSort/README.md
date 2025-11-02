# Note: Divide and Conquer into smaller chunks normally done recursively

#### Python3

```python

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3
from typing import List

"""
                       [2,4,3,6,1]
                     /             \
              [2,4]                 [3,6,1]
             /     \               /       \
         [2]       [4]          [3]       [6,1]
                                          /    \
                                       [6]     [1]
"""
class Solution:
    def MergeSort(self, a: List[int]) -> List[int]:
        if len(a) <= 1:                     # Base case: list already sorted
            return a
        
        # Step 1: Divide by recursion
        mid = len(a) // 2
        left: int = self.MergeSort(a[:mid])      # Need base case or never stops
        right: int = self.MergeSort(a[mid:])
        
        return self._merge(left, right)

    # private helper fx
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0

        # Step 2: Conquer w/ Merge sorted lists
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.MergeSort([2, 4, 3, 6, 1]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 2, 3, 4, 6]

real    0m0.028s
user    0m0.016s
sys     0m0.012s
```

#### Java

```java
import java.util.Scanner;

public class Main {
    private static int[] tmp = new int[100010];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; ++i) {
            nums[i] = sc.nextInt();
        }
        mergeSort(nums, 0, n - 1);
        for (int i = 0; i < n; ++i) {
            System.out.printf("%d ", nums[i]);
        }
    }

    public static void mergeSort(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int mid = (left + right) >>> 1;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);
        int i = left, j = mid + 1, k = 0;
        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                tmp[k++] = nums[i++];
            } else {
                tmp[k++] = nums[j++];
            }
        }
        while (i <= mid) {
            tmp[k++] = nums[i++];
        }
        while (j <= right) {
            tmp[k++] = nums[j++];
        }
        for (i = left, j = 0; i <= right; ++i, ++j) {
            nums[i] = tmp[j];
        }
    }
}
```

#### C++

```cpp
#include <iostream>

using namespace std;

const int N = 1e6 + 10;

int n;
int nums[N];
int tmp[N];

void merge_sort(int nums[], int left, int right) {
    if (left >= right) return;
    int mid = (left + right) >> 1;
    merge_sort(nums, left, mid);
    merge_sort(nums, mid + 1, right);
    int i = left, j = mid + 1, k = 0;
    while (i <= mid && j <= right) {
        if (nums[i] <= nums[j])
            tmp[k++] = nums[i++];
        else
            tmp[k++] = nums[j++];
    }
    while (i <= mid) tmp[k++] = nums[i++];
    while (j <= right) tmp[k++] = nums[j++];
    for (i = left, j = 0; i <= right; ++i, ++j) nums[i] = tmp[j];
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%d", &nums[i]);
    merge_sort(nums, 0, n - 1);
    for (int i = 0; i < n; ++i) printf("%d ", nums[i]);
}
```

#### Go

```go
package main

import "fmt"

func mergeSort(nums []int, left, right int) {
	if left >= right {
		return
	}
	mid := (left + right) >> 1
	mergeSort(nums, left, mid)
	mergeSort(nums, mid+1, right)
	i, j := left, mid+1
	tmp := make([]int, 0)
	for i <= mid && j <= right {
		if nums[i] <= nums[j] {
			tmp = append(tmp, nums[i])
			i++
		} else {
			tmp = append(tmp, nums[j])
			j++
		}
	}
	for i <= mid {
		tmp = append(tmp, nums[i])
		i++
	}
	for j <= right {
		tmp = append(tmp, nums[j])
		j++
	}
	for i, j = left, 0; i <= right; i, j = i+1, j+1 {
		nums[i] = tmp[j]
	}
}

func main() {
	var n int
	fmt.Scanf("%d\n", &n)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &nums[i])
	}

	mergeSort(nums, 0, n-1)

	for _, v := range nums {
		fmt.Printf("%d ", v)
	}
}
```

#### Rust

```rust
use std::io;

fn merge_sort(nums: &mut Vec<i32>, left: usize, right: usize) {
    if left >= right {
        return;
    }

    let mid = left + (right - left) / 2;
    merge_sort(nums, left, mid);
    merge_sort(nums, mid + 1, right);

    let mut temp = Vec::new();
    let mut i = left;
    let mut j = mid + 1;

    while i <= mid && j <= right {
        if nums[i] < nums[j] {
            temp.push(nums[i]);
            i += 1;
        } else {
            temp.push(nums[j]);
            j += 1;
        }
    }
    while i <= mid {
        temp.push(nums[i]);
        i += 1;
    }
    while j <= right {
        temp.push(nums[j]);
        j += 1;
    }

    for i in left..=right {
        nums[i] = temp[i - left];
    }
}

fn main() -> io::Result<()> {
    let mut n = String::new();
    io::stdin().read_line(&mut n)?;
    let n = n.trim().parse::<usize>().unwrap();

    let mut nums = String::new();
    io::stdin().read_line(&mut nums)?;
    let mut nums: Vec<i32> = nums.split(' ').map(|s| s.trim().parse().unwrap()).collect();

    merge_sort(&mut nums, 0, n - 1);
    for num in nums.iter() {
        print!("{} ", num);
    }

    Ok(())
}
```

#### JavaScript

```js
var buf = '';

process.stdin.on('readable', function () {
    var chunk = process.stdin.read();
    if (chunk) buf += chunk.toString();
});

let getInputArgs = line => {
    return line
        .split(' ')
        .filter(s => s !== '')
        .map(x => parseInt(x));
};

function mergeSort(nums, left, right) {
    if (left >= right) {
        return;
    }

    const mid = (left + right) >> 1;
    mergeSort(nums, left, mid);
    mergeSort(nums, mid + 1, right);
    let i = left;
    let j = mid + 1;
    let tmp = [];
    while (i <= mid && j <= right) {
        if (nums[i] <= nums[j]) {
            tmp.push(nums[i++]);
        } else {
            tmp.push(nums[j++]);
        }
    }
    while (i <= mid) {
        tmp.push(nums[i++]);
    }
    while (j <= right) {
        tmp.push(nums[j++]);
    }
    for (i = left, j = 0; i <= right; ++i, ++j) {
        nums[i] = tmp[j];
    }
}

process.stdin.on('end', function () {
    buf.split('\n').forEach(function (line, lineIdx) {
        if (lineIdx % 2 === 1) {
            nums = getInputArgs(line);
            mergeSort(nums, 0, nums.length - 1);
            console.log(nums.join(' '));
        }
    });
});
```
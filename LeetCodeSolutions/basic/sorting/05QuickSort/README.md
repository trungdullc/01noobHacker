#### Python3

```python

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3
from typing import List

class Solution:
    """
    Done w/ recurssion
    pivot is in correct position
    all items on left are smaller all items on right are bigger
    """
    def QuickSort(self, a: List[int]) -> List[int]:
        self._quick(a, 0, len(a) - 1)       # Uses index 0 as left and last index as right
        return a

    def _quick(self, a: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        
        pivot = a[right]                    # Choose last element as pivot
        i = left                            # i will track the pivot position
        
        for j in range(left, right):        # Partition step
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        
        # Place pivot in its correct sorted spot
        a[i], a[right] = a[right], a[i]

        # Recursively sort left and right partitions
        self._quick(nums, left, i - 1)
        self._quick(nums, i + 1, right)

if __name__ == "__main__":
    sol = Solution()
    print(sol.QuickSort([2, 4, 3, 6, 1]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 2, 3, 4, 6]

real    0m0.046s
user    0m0.032s
sys     0m0.000s
```

#### Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; ++i) {
            nums[i] = sc.nextInt();
        }
        quickSort(nums, 0, n - 1);
        for (int i = 0; i < n; ++i) {
            System.out.print(nums[i] + " ");
        }
    }

    public static void quickSort(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int i = left - 1, j = right + 1;
        int x = nums[(left + right) >> 1];
        while (i < j) {
            while (nums[++i] < x)
                ;
            while (nums[--j] > x)
                ;
            if (i < j) {
                int t = nums[i];
                nums[i] = nums[j];
                nums[j] = t;
            }
        }
        quickSort(nums, left, j);
        quickSort(nums, j + 1, right);
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

void quick_sort(int nums[], int left, int right) {
    if (left >= right) return;
    int i = left - 1, j = right + 1;
    int x = nums[left + right >> 1];
    while (i < j) {
        while (nums[++i] < x)
            ;
        while (nums[--j] > x)
            ;
        if (i < j) swap(nums[i], nums[j]);
    }
    quick_sort(nums, left, j);
    quick_sort(nums, j + 1, right);
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%d", &nums[i]);
    quick_sort(nums, 0, n - 1);
    for (int i = 0; i < n; ++i) printf("%d ", nums[i]);
}
```

#### Go

```go
package main

import "fmt"

func quickSort(nums []int, left, right int) {
	if left >= right {
		return
	}
	i, j := left-1, right+1
	x := nums[(left+right)>>1]
	for i < j {
		for {
			i++
			if nums[i] >= x {
				break
			}
		}
		for {
			j--
			if nums[j] <= x {
				break
			}
		}
		if i < j {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	quickSort(nums, left, j)
	quickSort(nums, j+1, right)
}

func main() {
	var n int
	fmt.Scanf("%d\n", &n)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &nums[i])
	}

	quickSort(nums, 0, n-1)

	for _, v := range nums {
		fmt.Printf("%d ", v)
	}
}
```

#### Rust

```rust
use rand::Rng; // 0.7.2
use std::io;

fn quick_sort(nums: &mut Vec<i32>, left: usize, right: usize) {
    if left >= right {
        return;
    }

    let random_index = rand::thread_rng().gen_range(left, right + 1);
    let temp = nums[random_index];
    nums[random_index] = nums[left];
    nums[left] = temp;

    let pivot = nums[left];
    let mut i = left;
    let mut j = right;
    while i < j {
        while i < j && nums[j] >= pivot {
            j -= 1;
        }
        nums[i] = nums[j];
        while i < j && nums[i] < pivot {
            i += 1;
        }
        nums[j] = nums[i];
    }
    nums[i] = pivot;

    quick_sort(nums, left, i);
    quick_sort(nums, i + 1, right);
}

fn main() -> io::Result<()> {
    let mut n = String::new();
    io::stdin().read_line(&mut n)?;
    let n = n.trim().parse::<usize>().unwrap();

    let mut nums = String::new();
    io::stdin().read_line(&mut nums)?;
    let mut nums: Vec<i32> = nums.split(' ').map(|s| s.trim().parse().unwrap()).collect();

    quick_sort(&mut nums, 0, n - 1);
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

function quickSort(nums, left, right) {
    if (left >= right) {
        return;
    }

    let i = left - 1;
    let j = right + 1;
    let x = nums[(left + right) >> 1];
    while (i < j) {
        while (nums[++i] < x);
        while (nums[--j] > x);
        if (i < j) {
            const t = nums[i];
            nums[i] = nums[j];
            nums[j] = t;
        }
    }
    quickSort(nums, left, j);
    quickSort(nums, j + 1, right);
}

process.stdin.on('end', function () {
    buf.split('\n').forEach(function (line, lineIdx) {
        if (lineIdx % 2 === 1) {
            nums = getInputArgs(line);
            quickSort(nums, 0, nums.length - 1);
            console.log(nums.join(' '));
        }
    });
});
```
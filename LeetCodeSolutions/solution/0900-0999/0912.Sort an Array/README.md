# [912. Sort an Array](https://leetcode.com/problems/sort-an-array)

## Description

<p>Given an array of integers <code>nums</code>, sort the array in ascending order and return it.</p>

<p>You must solve the problem <strong>without using any built-in</strong> functions in <code>O(nlog(n))</code> time complexity and with the smallest space complexity possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,2,3,1]
<strong>Output:</strong> [1,2,3,5]
<strong>Explanation:</strong> After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,1,1,2,0,0]
<strong>Output:</strong> [0,0,1,1,2,5]
<strong>Explanation:</strong> Note that the values of nums are not necessairly unique.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-5 * 10<sup>4</sup> &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>

## Solutions

### Solution 1

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

class Solution:
   """
   Solution for sorting an array without built-in functions.
   """
   def sortArray(self, nums: list[int]) -> list[int]:
      """
      Sort the array in ascending order using merge sort.
      
      Args:
         nums (list[int]): Input array.
      
      Returns:
         list[int]: Sorted array.
      """
      def merge(left, right):
         result = []
         i = j = 0
         while i < len(left) and j < len(right):
            if left[i] <= right[j]:
               result.append(left[i])
               i += 1
            else:
               result.append(right[j])
               j += 1
         result.extend(left[i:])
         result.extend(right[j:])
         return result

      if len(nums) <= 1:
         return nums
      mid = len(nums) // 2
      left = self.sortArray(nums[:mid])
      right = self.sortArray(nums[mid:])
      return merge(left, right)

if __name__ == "__main__":
   sol = Solution()
   print(sol.sortArray([5,2,3,1]))
   print(sol.sortArray([5,1,1,2,0,0]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
[1, 2, 3, 5]
[0, 0, 1, 1, 2, 5]

real    0m0.021s
user    0m0.013s
sys     0m0.009s
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   # Partition function:
   #  - Chooses a pivot (median-of-three: left, mid, right)
   #  - Rearranges elements so that all values less than the pivot are to its left,
   #    and all values greater than the pivot are to its right.
   #  - Returns the final position (index) of the pivot after partitioning.
   def partition(self, nums: List[int], left: int, right: int) -> int:
      mid = (left + right) >> 1
      nums[mid], nums[left + 1] = nums[left + 1], nums[mid]

      # Median-of-three ordering
      if nums[left] > nums[right]:
         nums[left], nums[right] = nums[right], nums[left]
      if nums[left + 1] > nums[right]:
         nums[left + 1], nums[right] = nums[right], nums[left + 1]
      if nums[left] > nums[left + 1]:
         nums[left], nums[left + 1] = nums[left + 1], nums[left]

      pivot = nums[left + 1]
      i = left + 1
      j = right

      # Partition loop
      while True:
         while True:
            i += 1
            if not nums[i] < pivot:
               break
         while True:
            j -= 1
            if not nums[j] > pivot:
               break
         if i > j:
            break
         nums[i], nums[j] = nums[j], nums[i]

      nums[left + 1], nums[j] = nums[j], nums[left + 1]
      return j

   def quickSort(self, nums: List[int], left: int, right: int) -> None:
      if right <= left + 1:
         if right == left + 1 and nums[right] < nums[left]:
            nums[left], nums[right] = nums[right], nums[left]
         return

      j = self.partition(nums, left, right)
      self.quickSort(nums, left, j - 1)
      self.quickSort(nums, j + 1, right)

   def sortArray(self, nums: List[int]) -> List[int]:
      self.quickSort(nums, 0, len(nums) - 1)
      return nums

def main() -> None:
   sol = Solution()
   print(sol.sortArray([5,2,3,1]))
   print(sol.sortArray([5,1,1,2,0,0]))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
[1, 2, 3, 5]
[0, 0, 1, 1, 2, 5]
```

#### Python3

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(l, r):
            if l >= r:
                return
            x = nums[randint(l, r)]
            i, j, k = l - 1, r + 1, l
            while k < j:
                if nums[k] < x:
                    nums[i + 1], nums[k] = nums[k], nums[i + 1]
                    i, k = i + 1, k + 1
                elif nums[k] > x:
                    j -= 1
                    nums[j], nums[k] = nums[k], nums[j]
                else:
                    k = k + 1
            quick_sort(l, i)
            quick_sort(j, r)

        quick_sort(0, len(nums) - 1)
        return nums
```

#### Java

```java
class Solution {
    private int[] nums;

    public int[] sortArray(int[] nums) {
        this.nums = nums;
        quikcSort(0, nums.length - 1);
        return nums;
    }

    private void quikcSort(int l, int r) {
        if (l >= r) {
            return;
        }
        int x = nums[(l + r) >> 1];
        int i = l - 1, j = r + 1;
        while (i < j) {
            while (nums[++i] < x) {
            }
            while (nums[--j] > x) {
            }
            if (i < j) {
                int t = nums[i];
                nums[i] = nums[j];
                nums[j] = t;
            }
        }
        quikcSort(l, j);
        quikcSort(j + 1, r);
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        function<void(int, int)> quick_sort = [&](int l, int r) {
            if (l >= r) {
                return;
            }
            int i = l - 1, j = r + 1;
            int x = nums[(l + r) >> 1];
            while (i < j) {
                while (nums[++i] < x) {
                }
                while (nums[--j] > x) {
                }
                if (i < j) {
                    swap(nums[i], nums[j]);
                }
            }
            quick_sort(l, j);
            quick_sort(j + 1, r);
        };
        quick_sort(0, nums.size() - 1);
        return nums;
    }
};
```

#### Go

```go
func sortArray(nums []int) []int {
	quickSort(nums, 0, len(nums)-1)
	return nums
}

func quickSort(nums []int, l, r int) {
	if l >= r {
		return
	}
	i, j := l-1, r+1
	x := nums[(l+r)>>1]
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
	quickSort(nums, l, j)
	quickSort(nums, j+1, r)
}
```

#### TypeScript

```ts
function sortArray(nums: number[]): number[] {
    function quickSort(l: number, r: number) {
        if (l >= r) {
            return;
        }
        let i = l - 1;
        let j = r + 1;
        const x = nums[(l + r) >> 1];
        while (i < j) {
            while (nums[++i] < x);
            while (nums[--j] > x);
            if (i < j) {
                [nums[i], nums[j]] = [nums[j], nums[i]];
            }
        }
        quickSort(l, j);
        quickSort(j + 1, r);
    }
    const n = nums.length;
    quickSort(0, n - 1);
    return nums;
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    function quickSort(l, r) {
        if (l >= r) {
            return;
        }
        let i = l - 1;
        let j = r + 1;
        const x = nums[(l + r) >> 1];
        while (i < j) {
            while (nums[++i] < x);
            while (nums[--j] > x);
            if (i < j) {
                [nums[i], nums[j]] = [nums[j], nums[i]];
            }
        }
        quickSort(l, j);
        quickSort(j + 1, r);
    }
    const n = nums.length;
    quickSort(0, n - 1);
    return nums;
};
```

#### Rust

```rs
impl Solution {
    pub fn sort_array(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        Self::quick_sort(&mut nums, 0, n - 1);
        return nums;
    }

    fn quick_sort(nums: &mut Vec<i32>, left: usize, right: usize) {
        if left >= right {
            return;
        }
        let mut i = left as i32 - 1;
        let mut j = right as i32 + 1;
        let pivot = nums[left];
        while i < j {
            loop {
                i += 1;
                if nums[i as usize] >= pivot {
                    break;
                }
            }
            loop {
                j -= 1;
                if nums[j as usize] <= pivot {
                    break;
                }
            }
            if i < j {
                nums.swap(i as usize, j as usize);
            }
        }
        Self::quick_sort(nums, left, j as usize);
        Self::quick_sort(nums, j as usize + 1, right);
    }
}
```

#### Kotlin

```kotlin
class Solution {
    fun sortArray(nums: IntArray): IntArray {
        fun quickSort(left: Int, right: Int) {
            if (left >= right) {
                return
            }
            var i = left - 1
            var j = right + 1
            val pivot = nums[left]
            while (i < j) {
                while (nums[++i] < pivot) ;
                while (nums[--j] > pivot) ;
                if (i < j) {
                    val temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                }
            }
            quickSort(left, j)
            quickSort(j + 1, right)
        }
        quickSort(0, nums.size - 1)
        return nums
    }
}
```

### Solution 2

#### Python3

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(l, r):
            if l >= r:
                return
            mid = (l + r) >> 1
            merge_sort(l, mid)
            merge_sort(mid + 1, r)
            i, j = l, mid + 1
            tmp = []
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            if i <= mid:
                tmp.extend(nums[i : mid + 1])
            if j <= r:
                tmp.extend(nums[j : r + 1])
            for i in range(l, r + 1):
                nums[i] = tmp[i - l]

        merge_sort(0, len(nums) - 1)
        return nums
```

#### Java

```java
class Solution {
    private int[] nums;

    public int[] sortArray(int[] nums) {
        this.nums = nums;
        quickSort(0, nums.length - 1);
        return nums;
    }

    private void quickSort(int l, int r) {
        if (l >= r) {
            return;
        }
        int i = l - 1, j = r + 1, k = l;
        int x = nums[(l + r) >> 1];
        while (k < j) {
            if (nums[k] < x) {
                swap(++i, k++);
            } else if (nums[k] > x) {
                swap(--j, k);
            } else {
                ++k;
            }
        }
        quickSort(l, i);
        quickSort(j, r);
    }

    private void swap(int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
}
```

#### C++

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        function<void(int, int)> merge_sort = [&](int l, int r) {
            if (l >= r) {
                return;
            }
            int mid = (l + r) >> 1;
            merge_sort(l, mid);
            merge_sort(mid + 1, r);
            int i = l, j = mid + 1, k = 0;
            int tmp[r - l + 1];
            while (i <= mid && j <= r) {
                if (nums[i] <= nums[j]) {
                    tmp[k++] = nums[i++];
                } else {
                    tmp[k++] = nums[j++];
                }
            }
            while (i <= mid) {
                tmp[k++] = nums[i++];
            }
            while (j <= r) {
                tmp[k++] = nums[j++];
            }
            for (i = l; i <= r; ++i) {
                nums[i] = tmp[i - l];
            }
        };
        merge_sort(0, nums.size() - 1);
        return nums;
    }
};
```

#### Go

```go
func sortArray(nums []int) []int {
	mergeSort(nums, 0, len(nums)-1)
	return nums
}

func mergeSort(nums []int, l, r int) {
	if l >= r {
		return
	}
	mid := (l + r) >> 1
	mergeSort(nums, l, mid)
	mergeSort(nums, mid+1, r)
	i, j, k := l, mid+1, 0
	tmp := make([]int, r-l+1)
	for i <= mid && j <= r {
		if nums[i] <= nums[j] {
			tmp[k] = nums[i]
			i++
		} else {
			tmp[k] = nums[j]
			j++
		}
		k++
	}
	for ; i <= mid; i++ {
		tmp[k] = nums[i]
		k++
	}
	for ; j <= r; j++ {
		tmp[k] = nums[j]
		k++
	}
	for i = l; i <= r; i++ {
		nums[i] = tmp[i-l]
	}
}
```

#### TypeScript

```ts
function sortArray(nums: number[]): number[] {
    function mergetSort(l: number, r: number) {
        if (l >= r) {
            return;
        }
        const mid = (l + r) >> 1;
        mergetSort(l, mid);
        mergetSort(mid + 1, r);
        let [i, j, k] = [l, mid + 1, 0];
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                tmp[k++] = nums[i++];
            } else {
                tmp[k++] = nums[j++];
            }
        }
        while (i <= mid) {
            tmp[k++] = nums[i++];
        }
        while (j <= r) {
            tmp[k++] = nums[j++];
        }
        for (i = l, j = 0; i <= r; ++i, ++j) {
            nums[i] = tmp[j];
        }
    }
    const n = nums.length;
    let tmp = new Array(n).fill(0);
    mergetSort(0, n - 1);
    return nums;
}
```

#### JavaScript

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {
    function mergetSort(l, r) {
        if (l >= r) {
            return;
        }
        const mid = (l + r) >> 1;
        mergetSort(l, mid);
        mergetSort(mid + 1, r);
        let [i, j, k] = [l, mid + 1, 0];
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                tmp[k++] = nums[i++];
            } else {
                tmp[k++] = nums[j++];
            }
        }
        while (i <= mid) {
            tmp[k++] = nums[i++];
        }
        while (j <= r) {
            tmp[k++] = nums[j++];
        }
        for (i = l, j = 0; i <= r; ++i, ++j) {
            nums[i] = tmp[j];
        }
    }
    const n = nums.length;
    let tmp = new Array(n).fill(0);
    mergetSort(0, n - 1);
    return nums;
};
```

### Solution 3

#### Java

```java
class Solution {
    private int[] nums;

    public int[] sortArray(int[] nums) {
        this.nums = nums;
        mergeSort(0, nums.length - 1);
        return nums;
    }

    private void mergeSort(int l, int r) {
        if (l >= r) {
            return;
        }
        int mid = (l + r) >> 1;
        mergeSort(l, mid);
        mergeSort(mid + 1, r);
        int i = l, j = mid + 1, k = 0;
        int[] tmp = new int[r - l + 1];
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                tmp[k++] = nums[i++];
            } else {
                tmp[k++] = nums[j++];
            }
        }
        while (i <= mid) {
            tmp[k++] = nums[i++];
        }
        while (j <= r) {
            tmp[k++] = nums[j++];
        }
        for (i = l; i <= r; ++i) {
            nums[i] = tmp[i - l];
        }
    }
}
```

[Continue 0075: Sort Colors](../../0000-0099/0075.Sort%20Colors/README.md)
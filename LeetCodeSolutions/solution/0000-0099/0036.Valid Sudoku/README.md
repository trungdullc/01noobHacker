# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku) ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️

## Description

<p>Determine if a&nbsp;<code>9 x 9</code> Sudoku board&nbsp;is valid.&nbsp;Only the filled cells need to be validated&nbsp;<strong>according to the following rules</strong>:</p>

<ol>
	<li>Each row&nbsp;must contain the&nbsp;digits&nbsp;<code>1-9</code> without repetition.</li>
	<li>Each column must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
	<li>Each of the nine&nbsp;<code>3 x 3</code> sub-boxes of the grid must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.</li>
	<li>Only the filled cells need to be validated according to the mentioned&nbsp;rules.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0000-0099/0036.Valid%20Sudoku/images/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" />
<pre>
<strong>Input:</strong> board = 
[[&quot;5&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;9&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;]
,[&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;3&quot;]
,[&quot;4&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;]
,[&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;]
,[&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;8&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;.&quot;,&quot;.&quot;,&quot;5&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;9&quot;]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> board = 
[[&quot;8&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;9&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;]
,[&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;3&quot;]
,[&quot;4&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;]
,[&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;]
,[&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;8&quot;,&quot;.&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;.&quot;,&quot;.&quot;,&quot;5&quot;]
,[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;9&quot;]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being modified to <strong>8</strong>. Since there are two 8&#39;s in the top left 3x3 sub-box, it is invalid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> is a digit <code>1-9</code> or <code>&#39;.&#39;</code>.</li>
</ul>

## Solutions

### Solution 1: Traversal once

The valid sudoku satisfies the following three conditions:

-   The digits are not repeated in each row;
-   The digits are not repeated in each column;
-   The digits are not repeated in each $3 \times 3$ box.

Traverse the sudoku, for each digit, check whether the row, column and $3 \times 3$ box it is in have appeared the digit. If it is, return `false`. If the traversal is over, return `true`.

The time complexity is $O(C)$ and the space complexity is $O(C)$, where $C$ is the number of empty spaces in the sudoku. In this question, $C=81$.

#### Du Solution
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/env python3

from typing import List

class Solution:
   """
   Class to determine if a 9x9 Sudoku board is valid.

   Methods
   -------
   isValidSudoku(board: List[List[str]]) -> bool
       Returns True if the board is valid according to Sudoku rules.
   """

   def isValidSudoku(self, board: List[List[str]]) -> bool:
      """
      Check whether a 9x9 Sudoku board is valid.

      Parameters
      ----------
      board : List[List[str]]
          9x9 Sudoku board with digits '1'-'9' and '.' for empty cells.

      Returns
      -------
      bool
          True if board is valid, False otherwise.
      """
      rows = [set() for _ in range(9)]
      cols = [set() for _ in range(9)]
      boxes = [set() for _ in range(9)]

      for r in range(9):
         for c in range(9):
            val = board[r][c]
            if val == ".":
               continue
            if val in rows[r] or val in cols[c] or val in boxes[(r//3)*3 + c//3]:
               return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[(r//3)*3 + c//3].add(val)

      return True

if __name__ == "__main__":
   sol = Solution()
   print(sol.isValidSudoku([
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
   ]))
   print(sol.isValidSudoku([
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
   ]))

AsianHacker-picoctf@webshell:/tmp$ time ./pythonScript.py 
True
False

real    0m0.029s
user    0m0.012s
sys     0m0.016s
```

#### Du Solution: Python3
```python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3
from typing import List

class Solution:
   def isValidSudoku(self, board: List[List[str]]) -> bool:
      """
      Determines if a 9x9 Sudoku board is valid.
      Only filled cells (digits 1-9) are validated for rows, columns, and 3x3 boxes.

      Parameters:
         board (List[List[str]]): 9x9 Sudoku board with digits as strings and '.' for empty cells.

      Returns:
         bool: True if the board is valid, False otherwise.
      """
      rows = [set() for _ in range(9)]
      cols = [set() for _ in range(9)]
      boxes = [set() for _ in range(9)]  # 3x3 sub-boxes

      for i in range(9):
         for j in range(9):
            num = board[i][j]
            if num == '.':
               continue

            # Check row
            if num in rows[i]:
               return False
            rows[i].add(num)

            # Check column
            if num in cols[j]:
               return False
            cols[j].add(num)

            # Check box
            box_index = (i // 3) * 3 + (j // 3)
            if num in boxes[box_index]:
               return False
            boxes[box_index].add(num)

      return True

def main() -> None:
   sol = Solution()
   board1 = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
   ]
   board2 = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
   ]
   
   print(sol.isValidSudoku(board1))
   print(sol.isValidSudoku(board2))

if __name__ == "__main__":
   main()

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
True
False
```

#### Python3

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sub = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                num = int(c) - 1
                k = i // 3 * 3 + j // 3
                if row[i][num] or col[j][num] or sub[k][num]:
                    return False
                row[i][num] = True
                col[j][num] = True
                sub[k][num] = True
        return True
```

#### Java

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] row = new boolean[9][9];
        boolean[][] col = new boolean[9][9];
        boolean[][] sub = new boolean[9][9];
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char c = board[i][j];
                if (c == '.') {
                    continue;
                }
                int num = c - '0' - 1;
                int k = i / 3 * 3 + j / 3;
                if (row[i][num] || col[j][num] || sub[k][num]) {
                    return false;
                }
                row[i][num] = true;
                col[j][num] = true;
                sub[k][num] = true;
            }
        }
        return true;
    }
}
```

#### C++

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<bool>> row(9, vector<bool>(9, false));
        vector<vector<bool>> col(9, vector<bool>(9, false));
        vector<vector<bool>> sub(9, vector<bool>(9, false));
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char c = board[i][j];
                if (c == '.') continue;
                int num = c - '0' - 1;
                int k = i / 3 * 3 + j / 3;
                if (row[i][num] || col[j][num] || sub[k][num]) {
                    return false;
                }
                row[i][num] = true;
                col[j][num] = true;
                sub[k][num] = true;
            }
        }
        return true;
    }
};
```

#### Go

```go
func isValidSudoku(board [][]byte) bool {
	row, col, sub := [9][9]bool{}, [9][9]bool{}, [9][9]bool{}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			num := board[i][j] - byte('1')
			if num < 0 || num > 9 {
				continue
			}
			k := i/3*3 + j/3
			if row[i][num] || col[j][num] || sub[k][num] {
				return false
			}
			row[i][num] = true
			col[j][num] = true
			sub[k][num] = true
		}
	}
	return true
}
```

#### TypeScript

```ts
function isValidSudoku(board: string[][]): boolean {
    const row: boolean[][] = Array.from({ length: 9 }, () =>
        Array.from({ length: 9 }, () => false),
    );
    const col: boolean[][] = Array.from({ length: 9 }, () =>
        Array.from({ length: 9 }, () => false),
    );
    const sub: boolean[][] = Array.from({ length: 9 }, () =>
        Array.from({ length: 9 }, () => false),
    );
    for (let i = 0; i < 9; ++i) {
        for (let j = 0; j < 9; ++j) {
            const num = board[i][j].charCodeAt(0) - '1'.charCodeAt(0);
            if (num < 0 || num > 8) {
                continue;
            }
            const k = Math.floor(i / 3) * 3 + Math.floor(j / 3);
            if (row[i][num] || col[j][num] || sub[k][num]) {
                return false;
            }
            row[i][num] = true;
            col[j][num] = true;
            sub[k][num] = true;
        }
    }
    return true;
}
```

#### JavaScript

```js
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
    const row = [...Array(9)].map(() => Array(9).fill(false));
    const col = [...Array(9)].map(() => Array(9).fill(false));
    const sub = [...Array(9)].map(() => Array(9).fill(false));
    for (let i = 0; i < 9; ++i) {
        for (let j = 0; j < 9; ++j) {
            const num = board[i][j].charCodeAt() - '1'.charCodeAt();
            if (num < 0 || num > 8) {
                continue;
            }
            const k = Math.floor(i / 3) * 3 + Math.floor(j / 3);
            if (row[i][num] || col[j][num] || sub[k][num]) {
                return false;
            }
            row[i][num] = true;
            col[j][num] = true;
            sub[k][num] = true;
        }
    }
    return true;
};
```

#### PHP

```php
class Solution {
    /**
     * @param string[][] $board
     * @return boolean
     */

    function isValidSudoku($board) {
        $rows = [];
        $columns = [];
        $boxes = [];

        for ($i = 0; $i < 9; $i++) {
            $rows[$i] = [];
            $columns[$i] = [];
            $boxes[$i] = [];
        }

        for ($row = 0; $row < 9; $row++) {
            for ($column = 0; $column < 9; $column++) {
                $cell = $board[$row][$column];

                if ($cell != '.') {
                    if (
                        in_array($cell, $rows[$row]) ||
                        in_array($cell, $columns[$column]) ||
                        in_array($cell, $boxes[floor($row / 3) * 3 + floor($column / 3)])
                    ) {
                        return false;
                    }

                    $rows[$row][] = $cell;
                    $columns[$column][] = $cell;
                    $boxes[floor($row / 3) * 3 + floor($column / 3)][] = $cell;
                }
            }
        }
        return true;
    }
}
```

[Continue 0128: Longest Consecutive Sequence](../../0100-0199/0128.Longest%20Consecutive%20Sequence/README.md)
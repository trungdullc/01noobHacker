# Level 32

## Previous Flag
```
http://www.pythonchallenge.com/pc/rock/arecibo.html
Username: kohsamui
Password: thailand 
```

## Goal
Given Image of pixel art ok a pokemon<br>
Fill in the blanks

## What I learned
```
Nonogram (also called a Picross or griddler) puzzle

python class
```

## Side Quest
```
with open("up.txt", "w") as file:
    file.write("""## ## ##
 # ### #
  #####
   #####
#########
   ###
## ### ##
## ### ##
## ### ##
""")
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/rock/arecibo.html

View Page Source:

<html> 
<head>
  <title>etch-a-scetch</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
  <link rel="stylesheet" type="text/css" href="etch-a-scetch.css">
  <script type="text/javascript" src="etch-a-scetch.js"></script>
  <script type="text/javascript" src="pencil.js"></script>
</head>
<body>
	<!-- you are in level 32 -->
	<br><br>
	<center>
	<table id="etch-a-scetch" cellspacing="0"></table><br />
	<font color="gold">
	        Fill in the blanks <!-- for warmup.txt --> ⌨️
        </font>
	</center>
</body>
</html>

Browser: http://www.pythonchallenge.com/pc/rock/warmup.txt ⌨️
# Dimensions
9 9

# Horizontal
2 1 2
1 3 1
5

7
9
3

2 3 2
2 3 2
2 3 2

# Vertical
2 1 3
1 2 3
3

8
9
8

3
1 2 3
2 1 3

# Think: Given size 9x9
# 2 1 2 means → 2 filled, at least one blank, 1 filled, at least one blank, then 2 filled again
# Row 5 = 9 → whole row filled.
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .

Result of Puzzle:
██·██·██
·█·███·█
··█████·
···█████
█████████
···███···
██·███·██
██·███·██
██·███·██

# Do with code
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
Processing Bar: (1,4)
Processing Bar: (1,5)
Processing Bar: (1,3)
Processing Bar: (0,3)
Processing Bar: (0,2)
Processing Bar: (1,8)
Processing Bar: (1,7)
Processing Bar: (0,2)
Processing Bar: (1,1)
Processing Bar: (0,2)
Processing Bar: (1,0)
Processing Bar: (1,6)
Processing Bar: (0,8)
Processing Bar: (0,7)
Processing Bar: (0,6)
Processing Bar: (1,2)
Processing Bar: (0,5)
Processing Bar: (0,1)
Processing Bar: (1,7)
Processing Bar: (1,1)
Processing Bar: (0,0)
##  #  ##
#  ###  #
  #####  
 ####### 
#########
   ###   
## ### ##
## ### ##
## ### ##
0.019206678

# Think: Looks like an up arrow
Browser: http://www.pythonchallenge.com/pc/rock/up.txt ⌨️
# Dimensions
32 32

# Horizontal lines
3 2
8
10
3 1 1

5 2 1
5 2 1
4 1 1
15

19
6 14
6 1 12
6 1 10

7 2 1 8
6 1 1 2 1 1 1 1
5 1 4 1
5 4 1 4 1 1 1

5 1 1 8
5 2 1 8
6 1 2 1 3
6 3 2 1

6 1 5
1 6 3
2 7 2
3 3 10 4

9 12 1
22 1
21 4
1 17 1

2 8 5 1
2 2 4
5 2 1 1
5

# Vertical lines 
5
5
5
3 1

3 1
5
5
6

5 6
9 5
11 5 1
13 6 1

14 6 1
7 12 1
6 1 11 1
3 1 1 1 9 1

3 4 10
8 1 1 2 8 1
10 1 1 1 7 1
10 4 1 1 7 1

3 2 5 2 1 2 6 2
3 2 4 2 1 1 4 1
2 6 3 1 1 1 1 1
12 3 1 2 1 1 1

3 2 7 3 1 2 1 2
2 6 3 1 1 1 1
12 3 1 5
6 3 1

6 4 1
5 4
4 1 1
5

# Save the above as up.txt
# Use Nonogram Solver python script
AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import time

# Represents a single segment (continuous filled block) in a row or column
class Seg:
    def __init__(self, length):
        self.length = length             # number of filled cells in this segment
        self.placements = []             # possible starting positions for the segment

    def __repr__(self):
        return '<Seg:len=' + str(self.length) + ',placements=' + str(self.placements) + '>'

# Represents a "bar" — either a horizontal or vertical line of the nonogram
class Bar:
    def __init__(self, axis, index, segs, length):
        self.segs = segs                 # list of Seg objects in this line
        self.complete = False            # whether this line is fully solved
        self.dirty = False               # if True, needs re-evaluation
        self.axis = axis                 # 0 for horizontal, 1 for vertical
        self.index = index               # row or column index
        self.length = length             # total length of this line
        # full_space = total cells occupied by blocks + required minimum 1 space between each
        self.full_space = sum([seg.length for seg in self.segs]) + len(self.segs) - 1

    # Check if the bar is completely filled (no empty spaces)
    def is_full(self):
        return self.full_space == self.length

    def __repr__(self):
        return '<Bar:axis=' + str(self.axis) + ',index=' + str(self.index) + ',len=' + str(
            self.length) + ',full_space=' + str(
            self.full_space) + ',segs=' + str(self.segs) + ',dirty=' + str(self.dirty) + '>'

    def __lt__(self, other):
        return self.index - other.index

# Loads puzzle constraints from up.txt (nonogram file)
def load():
    with open("up.txt") as f: 👀 warmup.txt to up.txt
        lines = f.readlines()
        # Remove comments (#) and blank lines
        lines = [line.strip() for line in lines if (not line.startswith('#')) and len(line.strip()) != 0]
        # Convert each remaining line into a list of integers
        raw = [list(map(int, line.split())) for line in lines]
        # First line gives total counts — sanity check
        assert sum(raw[0]) == len(raw) - 1
        # Return two sections: horizontal clues, vertical clues
        return raw[1:raw[0][0] + 1], raw[raw[0][0] + 1:]

# Prints the solved board nicely using symbols
def print_board(board):
    m = {1: '#', 0: ' ', None: '?'}      # mapping for filled/empty/unknown
    print("\n".join([''.join([m[ele] for ele in row]) for row in board]))

# Calculates total required space for a given list of segments (including gaps)
def calc_space(segs):
    return sum([seg.length for seg in segs]) + len(segs) - 1

# Determines possible start positions for every segment in every bar
def calc_placement(bars):
    for bar in bars:
        for i in range(len(bar.segs)):
            seg = bar.segs[i]
            # Earliest possible start
            start = calc_space(bar.segs[:i]) + 1
            # Latest possible start
            end = bar.length - calc_space(bar.segs[i + 1:]) - seg.length
            seg.placements = list(range(start, end))

# Updates a cell in both horizontal and vertical boards symmetrically
def update_board(board, bar, i, value):
    if board[bar.axis][bar.index][i] == value:
        return False
    board[bar.axis][bar.index][i] = value
    board[1 - bar.axis][i][bar.index] = value
    return True

# Marks cells that must be filled based on overlapping valid segment placements
def mark_overlaps(board, bars):
    for bar in bars:
        for seg in bar.segs:
            # Overlapping region between possible placements → definitely filled
            for i in range(seg.placements[-1], seg.placements[0] + seg.length):
                if update_board(board, bar, i, 1):
                    bars[(1 - bar.axis) * h + i].dirty = True

# Checks whether a segment can start at a specific position in a line
def validate_placement(board, bar, iseg, placement):
    seg = bar.segs[iseg]

    # Can't start immediately after another filled cell
    if placement > 0 and board[bar.axis][bar.index][placement - 1] == 1:
        return False
    # Can't overlap with known empty cells
    elif 0 in board[bar.axis][bar.index][placement:placement + seg.length]:
        return False
    # Can't touch another filled cell right after the segment
    elif placement + seg.length < len(board[bar.axis][bar.index]) and board[bar.axis][bar.index][
                placement + seg.length] == 1:
        return False

    return True

# Marks allowed cells (flags) for current segment placements
def mark_flags(board, bar, tmp_placements, flags):
    prev = 0
    for i in range(len(tmp_placements)):
        seg = bar.segs[i]
        placement = tmp_placements[i]

        # Mark spaces before current segment as possible white (2)
        for j in range(prev, placement):
            flags[j] |= 2
        # Mark cells inside the segment as possible black (1)
        for j in range(placement, placement + seg.length):
            flags[j] |= 1

        end = len(board[bar.axis][0])
        # Determine where next segment begins
        if i != len(tmp_placements) - 1:
            end = tmp_placements[i + 1]

        # Mark cells between segments as possible white
        for j in range(placement + seg.length, end):
            flags[j] |= 2

        prev = placement + seg.length

# Recursive backtracking to test all valid segment placements for a line
def check_bar(board, bar, start=0, iseg=0, tmp_placements=[], flags=[]):
    if iseg == len(bar.segs):
        last_seg = bar.segs[-1]
        # If anything filled after the last segment → invalid
        if 1 in board[bar.axis][bar.index][tmp_placements[-1] + last_seg.length:]:
            return
        # Otherwise, mark valid fill/empty flags for this configuration
        mark_flags(board, bar, tmp_placements, flags)
    else:
        seg = bar.segs[iseg]
        valid_placements = []
        # Filter possible starting positions
        for placement in seg.placements:
            if validate_placement(board, bar, iseg, placement):
                valid_placements.append(placement)
        seg.placements = valid_placements

        # Try each valid position recursively
        for placement in seg.placements:
            if placement < start:
                continue
            if 1 in board[bar.axis][bar.index][start:placement]:
                continue
            tmp_placements[iseg] = placement
            check_bar(board, bar, start=placement + seg.length + 1, iseg=iseg + 1,
                      tmp_placements=tmp_placements, flags=flags)

# --- Main Execution Starts Here ---

# Load horizontal and vertical clue data from up.txt
(hlens, vlens) = load()

h = len(hlens)     # number of horizontal lines
v = len(vlens)     # number of vertical lines

bars = []

# Create Bar objects for each horizontal line
for ind in range(len(hlens)):
    segs = [Seg(i) for i in hlens[ind]]
    bars.append(Bar(0, ind, segs, h))

# Create Bar objects for each vertical line
for ind in range(len(hlens)):
    segs = [Seg(i) for i in vlens[ind]]
    bars.append(Bar(1, ind, segs, h))

# Create two mirrored boards: one horizontal and one vertical
board = [[[None] * v for i in range(h)], [[None] * v for i in range(h)]]

# Initialize all possible segment placements
calc_placement(bars)

# Pre-fill overlapping (certain) cells
mark_overlaps(board, bars)

# Iteratively process "dirty" bars until puzzle solved
while True:
    dirty_bars = [(sum([len(seg.placements) for seg in bar.segs]), bar) for bar in bars if bar.dirty]
    if len(dirty_bars) == 0:
        break
    # Choose simplest bar (fewest possibilities)
    effort, bar = min(dirty_bars)

    flags = [0] * len(board[bar.axis][0])

    print("Processing Bar: (" + str(bar.axis) + "," + str(bar.index) + ")")
    # Analyze possible placements recursively
    check_bar(board, bar, tmp_placements=[0] * len(bar.segs), flags=flags)

    # Apply deductions based on flags
    for i in range(len(flags)):
        flag = flags[i]
        if flag == 1:
            if update_board(board, bar, i, 1):
                bars[(1 - bar.axis) * h + i].dirty = True
        elif flag == 2:
            if update_board(board, bar, i, 0):
                bars[(1 - bar.axis) * h + i].dirty = True
    bar.dirty = False

# Print the final solved board
print_board(board[0])

# Print total CPU processing time
print(time.process_time())

AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
Processing Bar: (0,8)
Processing Bar: (0,7)
Processing Bar: (0,2)
Processing Bar: (1,20)
Processing Bar: (1,19)
Processing Bar: (0,9)
Processing Bar: (0,1)
Processing Bar: (1,7)
Processing Bar: (0,9)
Processing Bar: (1,31)
Processing Bar: (1,6)
Processing Bar: (1,5)
Processing Bar: (1,2)
Processing Bar: (1,1)
Processing Bar: (1,0)
Processing Bar: (0,31)
Processing Bar: (1,12)
Processing Bar: (0,24)
Processing Bar: (1,13)
Processing Bar: (0,2)
Processing Bar: (1,12)
Processing Bar: (0,1)
Processing Bar: (0,24)
Processing Bar: (1,11)
Processing Bar: (0,24)
Processing Bar: (1,9)
Processing Bar: (0,31)
Processing Bar: (1,7)
Processing Bar: (0,25)
Processing Bar: (0,10)
Processing Bar: (1,5)
Processing Bar: (1,2)
Processing Bar: (1,1)
Processing Bar: (1,0)
Processing Bar: (1,13)
Processing Bar: (1,24)
Processing Bar: (0,2)
Processing Bar: (0,1)
Processing Bar: (0,23)
Processing Bar: (1,23)
...
Processing Bar: (0,14)
Processing Bar: (1,31)
Processing Bar: (0,9)
Processing Bar: (1,17)
Processing Bar: (0,30)
Processing Bar: (0,13)
                   ### ##       
                  ########      
                 ##########     
                 ###   #  #     
                 ##### ## #     
                 ##### ## #     
                ####   #  #     
             ###############    
           ###################  
          ###### ############## 
         ######   # ############
         ######     # ##########
        #######   ##  # ########
        ###### # # ##   # # #  #
        #####   #  ####        #
        ##### #### # #### # # # 
        #####   # #   ########  
         ##### ##  #   ######## 
         ######  #  ##   # ###  
          ###### ###  ##     #  
           ######   #   #####   
#           ######  ###         
##           #######   ##       
###  ###   ########## ####      
######### ############    #     
######################    #     
 ##################### ####     
  #  #################    #     
   ##  ######## #####     #     
        ##     ##     ####      
          #####  ## #   #       
                   #####        
0.396503473

# Think: Looks like python
# Browser: http://www.pythonchallenge.com/pc/rock/python.html ⌨️
Congrats! You made it through to the smiling python. 

"Free" as in "Free speech", not as in "free... 👀

# Google: "Free" as in "Free speech", not as in "free... ⌨️
Roughly, it means that the users have the freedom to run, copy, distribute, study, change and improve the software. Thus, "free software" is a matter of liberty, not price. To understand the concept, you should think of "free" as in "free speech," not as in "free beer".
https://en.wikipedia.org/wiki/Gratis_versus_libre#:~:text=Roughly%2C%20it%20means%20that%20the,as%20in%20%22free%20beer%22

# Browser: http://www.pythonchallenge.com/pc/rock/beer.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/rock/beer.html

## Continue
[Continue](./Level33.md)
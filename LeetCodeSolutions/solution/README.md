# Asian Hacker's LeetCode Checklist
```
Competitive Programming
						Bitwise Math					Normal People
isOdd:              	x & 1 == 1						x % 2 == 1
isEven:             	(x & 1) == 0					x % 2 == 0
Multiply by 2:    		x << 1							x * 2
Divide by 2:      		x >> 1							x / 2 
Swap 2 #'s:         	a ^= b; b ^= a; a ^= b			temp = a; a = b; b = temp
is Power of 2:      	(x & (x - 1)) == 0				
Remove low bit:   		x & (x - 1)						x - 1						
Keep low bit:     		x & -x								
Set bit k:        		x | (1 << k)		Note: k is position					
Clear bit k:      		x & ~(1 << k)						
Flip/Toggle bit k:     	x ^ (1 << k)								
isCheck bit k:      	(x >> k) & 1						
x % 2^n:          		x & (2^n - 1)							

General Optimization Progression Mindset
Step	Technique						Key Question to Ask Yourself
1	    Brute Force						Can I try all possibilities first?
2	    Observations					Do I notice patterns or repeated work? Then pick from steps 3+
3	    Hash Map / FREQUENCY TABLE Set	Am I **counting** things or checking if **exists** called **frequency** or grouping?

4	Sorting → Two Pointers				Is the data sorted or can sorting make relationships clearer?
5	Binary Search / Divide & Conquer	Is the answer in a sorted space or increasing/decreasing range?
								        Asks for smallest / largest possible value
6	Sliding Window						Am I finding a longest/shortest *continuous* range or substring?
7	Prefix Sum						    Am I repeating range sum/count queries?
8	Heap / Priority Queue				Are we tracking **best** min/max?	
8	RECURSION → MEMOIZATION → DP		Do subproblems repeat? Can I store the answer and reuse it?

9	Greedy							    Can I pick the **best** possible choice at each step to reach the optimal result?
10	Graph Transversal (DFS / BFS)		Are elements connected, forming a network, map, grid, or relationship paths?
	BFS							        Shortest Path (edges same weight)
	DFS							        Flood fill / explore zones
11	Shortest PATH (Dijkstra / Bellman-Ford) Do edges have weights and I need cheapest path?
	Dijkstra						    Shortest Path (weights vary)
12	UNION-FIND (Disjoint Set)			Do I need to merge/find connected components quickly?
13	Segment Tree / Fenwick Tree (BIT)	Do I need fast range queries **and** updates on dynamic data?"
```
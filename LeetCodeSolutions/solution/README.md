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

# Side Quest: NeetCode
```
Problem Types:
								Arrays & Hashing
				Two Pointers								Stack
		Binary Search	Sliding Window	Linked List
					Trees
	Tries			Heap/Priority Queue				Backtracking
												Graphs			1-D Dynamic Programming
			Intervals	Greedy		Advanced Graphs		2-D Dynamic Programming		Bit Manipulation
																		Math & Geometry

8 Categories of Algorithms
Searching Algorithms:
	Linear Search
	Binary Search
	Breadth-First Search (BFS)
	Queue-Based
	Depth First Search (DFS)
	Recursive
	Iterative
Sorting Algorithms:
	Quick Sort
	Merge Sort
	Heap Sort
	Bubble Sort
	Insertion Sort
	Bucket Sort
String Algorithms: 
	Sliding Window (Substring, Subarray)
	Trie (Prefix Tree)
	Longest Palindromic Substring
	KMP String Patching
	Palindromes
Tree Algorithms:
	Traversal:
		Inorder
		Preorder
		Postorder Tranversal
		Level Order Traversal (BFS)
		Iterative (DFS)
	Binary Search Tree
	Algos:
		Validate BST
		Insert into BST
		Delete in BST
Graph Alogrithms:
	Basics:
		Breadth-First Search (BFS)
		Depth-First Search (DPS)
	Advanced:
		Topological Sort
		Union-Find
		Dijkstra's Algorithm
		Cycle Detection
		Minimum Spanning Tree
Dynamic Programming:
	Fibonacci Sequence
	Longest Common Subsequence (LCS)
	Longest Increasing Subsequence (LIS)
	Kadane's Algorithm
	0/1 Knapsack
	Unbound Knapsack
	Unique Paths
Greedy Algorithms:
	Kruskai's Algorithm
	Dijkstra's Algorithm
	Heap Problems
	Interval Scheduling
	Prim's Algorithm
	Activity Selection
Backtracking Algorithms
	Permutations
	Combinations
	Subsets
	N-Queens Problem
	Sudoku Solver
	Word Search
	Combination Sums (I, II, III)
```

# Side Quest: Dynamic Programming
```
What is Dynamic Programming?
	Optmizing recursion by storing results of subproblems
	
1st Solution: Recursive Backtracking
def fib(num):
	if num == 0: return 0
	elif num == 1: return 1

	return fib(num-1) + fib(num-2)

2nd Solution: Top Down Dynamic Programming (Memoization)
def fib(num):
	cache = {0:0, 1:1}

	def f(num):
		if num in cache:
			return cache[num]
		cache[num] = f(num-1) + fib(num-2)
		return cache[num]
	return f(num)

3rd Solution: Bottom-Up Dynamic Programming(Tabulation)
def fib(num):
	dp = [0, 1]

	for i in range(2, num+1):
		new = dp[i-2] + dp[i-1]
		dp.append(new)
	return dp[num]

4th Solution: Bottom-Up No Memory Dynamic Programming
def fib(num):
	if n < 2: return num

	prev, cur = 0, 1
	for i in range(2, n+1):
		prev, cur = cur, cur + prev
	return cur
```

# Side Quest: Trie
```python
What is a Trie?
	ReTRIEval
	Data Structure known as Prefix Tree
	Used for prefix matching, word searches, auto complete

#!/usr/bin/env python3
from typing import Dict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}  	# hashmap for child nodes
        self.is_end_of_word: bool = False        	# True if node represents end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  	# create new node if not exists
            node = node.children[char]
        node.is_end_of_word = True  				# mark the end of the word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  				# must be the end of a word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  								# found all characters of prefix

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   					# True
    print(trie.search("app"))     					# False
    print(trie.startsWith("app")) 					# True
    trie.insert("app")
    print(trie.search("app"))     					# True
```

# Side Quest: Dijkstra’s Algorithm
```python
What is Dijkstra's Algorithm?
	Dijkstra’s Algorithm is a greedy shortest-path algorithm used to find the minimum distance from a single source vertex to all other vertices in a weighted graph with non-negative edges. It works for both directed and undirected graphs and is widely used in routing, navigation systems, and network optimization

# Python Implementation (Adjacency List + Priority Queue)
import heapq

def dijkstra(graph, start):
	# graph: dict {node: [(neighbor, weight), ...]}
	distances = {node: float('inf') for node in graph}
	distances[start] = 0
	pq = [(0, start)] # (distance, node)

	while pq:
	current_dist, current_node = heapq.heappop(pq)

	if current_dist > distances[current_node]:
	continue # Skip outdated entry

	for neighbor, weight in graph[current_node]:
	distance = current_dist + weight
	if distance < distances[neighbor]:
	distances[neighbor] = distance
	heapq.heappush(pq, (distance, neighbor))

	return distances

if __name__ == "__main__":
	graph = {
	'A': [('B', 4), ('C', 2)],
	'B': [('C', 5), ('D', 10)],
	'C': [('E', 3)],
	'D': [('F', 11)],
	'E': [('D', 4)],
	'F': []
	}

	print(dijkstra(graph, 'A'))
```
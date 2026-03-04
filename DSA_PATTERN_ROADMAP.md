
# DSA Pattern-Based Learning Roadmap

This document outlines a **pattern-based approach to Data Structures and Algorithms (DSA)**.  
Instead of learning hundreds of random problems, we focus on **core patterns that cover ~80% of coding interview questions**.

---

# Learning Philosophy

Most DSA problems follow this thinking flow:

```

Problem
↓
Brute Force Approach
↓
Identify Pattern
↓
Choose Data Structure
↓
Apply Algorithm
↓
Analyze Time & Space Complexity

```

---

# Core DSA Patterns (80% of Interview Problems)

## 1. Hashing Pattern

### Idea
Use a **HashMap or HashSet** for fast lookups.

### When to Use
- Duplicate detection
- Frequency counting
- Complement lookup
- Membership checking

### Data Structures
- HashMap (Dictionary)
- HashSet

### Example Problems
- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Longest Consecutive Sequence

### Complexity
```

Time: O(n)
Space: O(n)

```

---

# 2. Two Pointers Pattern

### Idea
Use two indices moving toward each other or in the same direction.

### When to Use
- Sorted arrays
- Pair comparison
- Removing duplicates
- Reversing arrays

### Example Problems
- Valid Palindrome
- Remove Duplicates from Sorted Array
- Move Zeroes
- Two Sum II (Sorted)
- Container With Most Water
- 3Sum

### Complexity
```

Time: O(n)
Space: O(1)

```

---

# 3. Sliding Window Pattern

### Idea
Maintain a **window of elements** that expands or shrinks.

### When to Use
- Subarray problems
- Substring problems
- Maximum/minimum window problems

### Example Problems
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Longest Repeating Character Replacement
- Permutation in String

### Complexity
```

Time: O(n)
Space: O(1) or O(k)

```

---

# 4. Binary Search Pattern

### Idea
Divide search space in half.

### When to Use
- Sorted arrays
- Search problems
- Optimization problems

### Example Problems
- Binary Search
- Search Insert Position
- First Bad Version
- Find Peak Element
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array

### Complexity
```

Time: O(log n)
Space: O(1)

```

---

# 5. Prefix Sum Pattern

### Idea
Store cumulative sums to answer range queries quickly.

### When to Use
- Range sum queries
- Subarray sum problems
- Cumulative calculations

### Example Problems
- Running Sum of Array
- Range Sum Query
- Subarray Sum Equals K
- Continuous Subarray Sum
- Product of Array Except Self

---

# 6. Stack Pattern

### Idea
Use stack to track elements and maintain order.

### When to Use
- Parentheses validation
- Next greater element
- Expression evaluation

### Data Structure
Stack (LIFO)

### Example Problems
- Valid Parentheses
- Min Stack
- Next Greater Element
- Daily Temperatures
- Largest Rectangle in Histogram

---

# 7. Heap / Top-K Pattern

### Idea
Use **priority queue** to efficiently retrieve smallest or largest elements.

### When to Use
- Top K problems
- Scheduling problems
- Stream processing

### Data Structure
Heap / Priority Queue

### Example Problems
- Kth Largest Element
- Top K Frequent Elements
- Merge K Sorted Lists
- Find Median from Data Stream

---

# 8. Linked List Pattern

### Idea
Use pointer manipulation for efficient traversal.

### Example Problems
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Middle of Linked List
- Remove Nth Node From End

### Techniques
- Fast & Slow Pointer
- Pointer reversal

---

# 9. Tree Traversal Pattern

### Idea
Traverse hierarchical structures.

### Traversal Methods
- DFS (Depth First Search)
- BFS (Breadth First Search)

### Example Problems
- Maximum Depth of Binary Tree
- Same Tree
- Invert Binary Tree
- Level Order Traversal
- Diameter of Binary Tree
- Balanced Binary Tree
- Path Sum
- Lowest Common Ancestor

---

# 10. Dynamic Programming Pattern

### Idea
Break problems into **overlapping subproblems** and reuse results.

### Approaches
- Recursion
- Memoization
- Tabulation

### Example Problems
- Fibonacci
- Climbing Stairs
- House Robber
- Coin Change
- Longest Increasing Subsequence
- Longest Common Subsequence

---

# Recommended Learning Order

Follow this sequence to build intuition gradually.

```

1. Hashing
2. Two Pointers
3. Sliding Window
4. Binary Search
5. Prefix Sum
6. Stack
7. Heap
8. Linked List
9. Trees
10. Graphs
11. Dynamic Programming

```

---

# Weekly Practice Plan (Approx. 3 Months)

```

Week 1–2  → Hashing
Week 3–4  → Two Pointers
Week 5–6  → Sliding Window
Week 7    → Binary Search
Week 8    → Prefix Sum
Week 9    → Stack
Week 10   → Heap
Week 11   → Linked List
Week 12   → Trees + Dynamic Programming

```

---

# Key Insight

Mastering these patterns enables solving **70–80% of interview problems** efficiently.

```

Pattern Recognition > Memorizing Solutions

```

---

# Problem Solving Strategy

For every problem:

```

1. Understand the problem
2. Write brute force solution
3. Identify pattern
4. Optimize
5. Analyze complexity

```

---

# Goal

The goal is **not to memorize hundreds of problems**, but to recognize **patterns quickly and apply them effectively**.

```

Patterns → Solutions
Not
Random Problems → Confusion


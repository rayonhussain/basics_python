# Data Structures and Algorithms in Python

## Table of Contents
1. [Introduction](#introduction)
2. [Data Structures](#data-structures)
    - [Arrays](#arrays)
    - [Linked Lists](#linked-lists)
    - [Stacks](#stacks)
    - [Queues](#queues)
    - [Hash Tables](#hash-tables)
3. [Algorithms](#algorithms)
    - [Sorting](#sorting)
    - [Searching](#searching)
    - [Dynamic Programming](#dynamic-programming)
    - [Greedy Algorithms](#greedy-algorithms)
    - [Backtracking](#backtracking)
4. [Complexity Analysis](#complexity-analysis)
5. [Examples](#examples)
6. [References](#references)

## Introduction
Provide an overview of what Data Structures and Algorithms (DSA) are, and why they are important. Mention the goal of the document.

## Data Structures

### Arrays
- **Definition**: A collection of items stored at contiguous memory locations.
- **Example**:
    ```python
    arr = [1, 2, 3, 4, 5]
    print(arr)
    ```
- **Use Cases**: Storing multiple items of the same type.
- **Operations**:
    - Insertion
    - Deletion
    - Access

### Linked Lists
- **Definition**: A linear collection of data elements, called nodes, where the linear order is not given by their physical placement in memory.
- **Example**:
    ```python
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None
    ```
- **Use Cases**: Dynamic memory allocation, ease of insertion/deletion.
- **Operations**:
    - Insertion
    - Deletion
    - Traversal

### Stacks
- **Definition**: A linear data structure that follows the Last In First Out (LIFO) principle.
- **Example**:
    ```python
    stack = []
    stack.append(1)
    stack.append(2)
    stack.pop()
    ```
- **Use Cases**: Function call management, undo mechanisms in text editors.
- **Operations**:
    - Push
    - Pop
    - Peek

### Queues
- **Definition**: A linear data structure that follows the First In First Out (FIFO) principle.
- **Example**:
    ```python
    from collections import deque
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.popleft()
    ```
- **Use Cases**: Order processing, breadth-first search in graphs.
- **Operations**:
    - Enqueue
    - Dequeue
    - Front

### Hash Tables
- **Definition**: A data structure that stores items in an associative manner, using a hash function to compute an index into an array of buckets or slots.
- **Example**:
    ```python
    hash_table = {}
    hash_table["key1"] = "value1"
    ```
- **Use Cases**: Fast data retrieval.
- **Operations**:
    - Insertion
    - Deletion
    - Lookup

## Algorithms

### Sorting
- **Definition**: Algorithms to arrange data in a particular order.
- **Example**: Bubble Sort
    ```python
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    ```
- **Common Algorithms**:
    - Quick Sort
    - Merge Sort
    - Insertion Sort

### Searching
- **Definition**: Algorithms to find an item in a data structure.
- **Example**: Binary Search
    ```python
    def binary_search(arr, x):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    ```
- **Common Algorithms**:
    - Linear Search
    - Depth First Search (DFS)
    - Breadth First Search (BFS)

### Dynamic Programming
- **Definition**: A method for solving complex problems by breaking them down into simpler subproblems.
- **Example**: Fibonacci Sequence
    ```python
    def fib(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    ```

### Greedy Algorithms
- **Definition**: Algorithms that make the locally optimal choice at each stage with the hope of finding a global optimum.
- **Example**: Coin Change Problem
    ```python
    def coin_change(coins, amount):
        coins.sort(reverse=True)
        count = 0
        for coin in coins:
            count += amount // coin
            amount %= coin
        return count if amount == 0 else -1
    ```

### Backtracking
- **Definition**: A general algorithm for finding solutions to some computational problems by incrementally building candidates to the solutions.
- **Example**: N-Queens Problem
    ```python
    def solve_n_queens(n):
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    return False
            return True

        def solve(board, row):
            if row == n:
                result.append(board[:])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

        result = []
        solve([-1] * n, 0)
        return result
    ```

## Complexity Analysis
- **Time Complexity**: Measure of the amount of time an algorithm takes to complete.
    - Example: O(n), O(log n), O(n^2)
- **Space Complexity**: Measure of the amount of memory an algorithm uses.
    - Example: O(1), O(n)

## Examples
Provide practical examples and exercises for each data structure and algorithm.

## References
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [LeetCode](https://leetcode.com/)
- [Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

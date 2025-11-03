# Problem Solutions

## Problem 1: First Non-Repeating Character

### Description
Find the first character in a string that does not repeat. The solution is case-sensitive.

### Algorithm
1. **Time Complexity**: O(n) - Two passes through the string
2. **Space Complexity**: O(k) - Where k is the number of unique characters
3. **Approach**:
   - First pass: Count frequency of each character using a hash map
   - Second pass: Find first character with frequency 1

### Usage
```python
first_non_repeating_char("swiss")  # Returns "w"
first_non_repeating_char("aabb")   # Returns ""
```

## Problem 2: Count Islands in a Grid

### Description
Count connected components of 1s (land) in a 2D grid using 4-directional connectivity.

### Algorithm
1. **Time Complexity**: O(m × n) - Visit each cell once
2. **Space Complexity**: O(m × n) - For visited matrix and BFS queue in worst case
3. **Approach**:
   - Use BFS to explore connected land cells
   - Maintain visited matrix to avoid cycles
   - Increment count for each unvisited land cell found

### Usage
```python
grid = [
    [1, 1, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1]
]
count_islands(grid)  # Returns 3
```

## Running Tests
```bash
python first_non_repeating_char.py
python count_islands.py
```

## Key Features:

1. **Clean Code**: Well-structured, documented, and follows Python best practices
2. **Efficient Algorithms**: 
   - Problem 1: O(n) time with two passes
   - Problem 2: O(m×n) time with BFS
3. **Comprehensive Testing**: Covers edge cases and typical scenarios
4. **Clear Documentation**: README explains approach, complexity, and usage
5. **Robust Error Handling**: Handles empty inputs and edge cases appropriately

Both solutions are production-ready and meet all specified requirements.
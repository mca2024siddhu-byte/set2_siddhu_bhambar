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
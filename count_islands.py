from typing import List
from collections import deque

def count_islands(grid: List[List[int]]) -> int:
    """
    Count the number of connected islands in a 2D grid.
    
    Args:
        grid: 2D list where 1 represents land and 0 represents water
        
    Returns:
        Number of connected islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_count = 0
    
    def bfs(start_row: int, start_col: int):
        """BFS to mark all connected land cells as visited"""
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and if it's unvisited land
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    not visited[new_row][new_col] and grid[new_row][new_col] == 1):
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
    
    # Iterate through all cells
    for i in range(rows):
        for j in range(cols):
            # If unvisited land cell found, it's a new island
            if grid[i][j] == 1 and not visited[i][j]:
                island_count += 1
                bfs(i, j)
    
    return island_count


# Unit Tests
def test_count_islands():
    """Test cases for count_islands function"""
    
    # Example from problem
    grid1 = [
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    assert count_islands(grid1) == 3
    
    # Single island
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert count_islands(grid2) == 1
    
    # No islands (all water)
    grid3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert count_islands(grid3) == 0
    
    # Diagonal islands (not connected in 4 directions)
    grid4 = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    assert count_islands(grid4) == 5
    
    # Single cell
    grid5 = [[1]]
    assert count_islands(grid5) == 1
    
    # Single row
    grid6 = [[1, 0, 1, 1, 0, 1]]
    assert count_islands(grid6) == 3
    
    print("All island tests passed!")


if __name__ == "__main__":
    test_count_islands()
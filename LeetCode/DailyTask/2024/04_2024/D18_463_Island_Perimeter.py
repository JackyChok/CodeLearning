from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1: Expected output: 16
    print(solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    # Example 2: Expected output: 4
    print(solution.islandPerimeter([[1]]))
    # Example 3: Expected output: 4
    print(solution.islandPerimeter([[1,0]]))

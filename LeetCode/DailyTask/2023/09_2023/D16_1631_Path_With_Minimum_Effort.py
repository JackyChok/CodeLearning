import math
from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights):
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] 
        
        while minHeap:
            effort, x, y = heappop(minHeap)

            if x == rows - 1 and y == cols - 1:
                return effort
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heappush(minHeap, (new_effort, nx, ny))

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    heights1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print("Test case 1:", sol.minimumEffortPath(heights1))  # Expected output: 2
    
    # Test case 2
    heights2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print("Test case 2:", sol.minimumEffortPath(heights2))  # Expected output: 1
    
    # Test case 3
    heights3 = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print("Test case 3:", sol.minimumEffortPath(heights3))  # Expected output: 0

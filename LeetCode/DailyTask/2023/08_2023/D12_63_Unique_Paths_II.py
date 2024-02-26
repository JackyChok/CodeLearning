class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        ans = [[0] * m for _ in range(n)]
        
        for i in range(n):
            if obstacleGrid[i][0] == 0:
                ans[i][0] = 1
            else:
                break
        
        for j in range(m):
            if obstacleGrid[0][j] == 0:
                ans[0][j] = 1
            else:
                break
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        
        return ans[n-1][m-1]

def run_tests():
    sol = Solution()

    grid1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(sol.uniquePathsWithObstacles(grid1))  # Output: 2

    grid2 = [
        [0, 1],
        [0, 0]
    ]
    print(sol.uniquePathsWithObstacles(grid2))  # Output: 1

if __name__ == "__main__":
    run_tests()

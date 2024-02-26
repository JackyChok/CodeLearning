class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        dir = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]

        dp = [[[0.0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1.0

        for m in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for d in dir:
                        prevI, prevJ = i - d[0], j - d[1]
                        if 0 <= prevI < n and 0 <= prevJ < n:
                            dp[m][i][j] += dp[m - 1][prevI][prevJ] / 8.0
        print(dp)

        ans = sum(dp[k][i][j] for i in range(n) for j in range(n))
        return ans


# Test Case
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    n1, k1, row1, column1 = 3, 2, 0, 0
    print(sol.knightProbability(n1, k1, row1, column1))  # Output: 0.0625

    # Test Case 2
    n2, k2, row2, column2 = 1, 0, 0, 0
    print(sol.knightProbability(n2, k2, row2, column2))  # Output: 1.0

    # Test Case 3
    n3, k3, row3, column3 = 3, 3, 1, 1
    print(sol.knightProbability(n3, k3, row3, column3))  # Output: 0.0

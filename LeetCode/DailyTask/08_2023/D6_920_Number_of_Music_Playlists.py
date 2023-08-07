class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j-1] * (n - j + 1)) % MOD
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % MOD

        return dp[goal][n]

def run_tests():
    sol = Solution()

    # Test Case 1
    print(sol.numMusicPlaylists(3, 3, 1))  # Output: 6

    # Test Case 2
    print(sol.numMusicPlaylists(2, 3, 0))  # Output: 6

    # Test Case 3
    print(sol.numMusicPlaylists(2, 3, 1))  # Output: 2

if __name__ == "__main__":
    run_tests()

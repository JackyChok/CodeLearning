class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        # Define the constant MOD to be used for modulo operations
        MOD = 10**9 + 7
        
        # Initialize a two-dimensional array dp with all elements set to 0
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        
        # There is only one way to create an empty playlist
        dp[0][0] = 1

        # Loop through the elements of the dp array
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Calculate dp[i][j] using the formula for adding a new song to the playlist
                dp[i][j] = (dp[i-1][j-1] * (n - j + 1)) % MOD
                
                # If j is greater than k, consider the case when we can repeat songs
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % MOD

        # The value in dp[goal][n] represents the number of possible playlists
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

class Solution(object):
    def isInterleaveDP(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

    def isInterleaveDFS(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp = {}
        
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            result = False
            if i < len(s1) and s1[i] == s3[i + j]:
                result |= dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                result |= dfs(i, j + 1)
            
            dp[(i, j)] = result
            return result
        
        return dfs(0, 0)

# Test cases
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac"),
        ("aabcc", "dbbca", "aadbbbaccc"),
        ("", "", "")
    ]

    for i, (s1, s2, s3) in enumerate(test_cases):
        result_dp = solution.isInterleaveDP(s1, s2, s3)
        result_dfs = solution.isInterleaveDFS(s1, s2, s3)
        print(f"Test Case {i + 1}:")
        print("Dynamic Programming:", result_dp)
        print("DFS:", result_dfs)
        print()

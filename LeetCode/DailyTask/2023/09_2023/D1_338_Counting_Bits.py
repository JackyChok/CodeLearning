class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    n1 = 2
    result1 = solution.countBits(n1)
    print("Test Case 1: Count Bits =", result1)  # Output: [0, 1, 1]
    
    n2 = 5
    result2 = solution.countBits(n2)
    print("Test Case 2: Count Bits =", result2)  # Output: [0, 1, 1, 2, 1, 2]

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        max_length = 1

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1

            max_length = max(max_length, dp[num])

        return max_length

# Test Case 1
arr1 = [1, 2, 3, 4]
difference1 = 1
# The longest arithmetic subsequence with a difference of 1 is [1, 2, 3, 4]
# The length of the subsequence is 4
# Expected output: 4

# Test Case 2
arr2 = [1, 3, 5, 7]
difference2 = 1
# The longest arithmetic subsequence with a difference of 1 is [1]
# The length of the subsequence is 4
# Expected output: 1

# Test Case 3
arr3 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
difference3 = -2
# The longest arithmetic subsequence with a difference of -2 is [7, 5, 3, 1]
# The length of the subsequence is 4
# Expected output: 4

solution = Solution()
print(solution.longestSubsequence(arr1, difference1))
print(solution.longestSubsequence(arr2, difference2))
print(solution.longestSubsequence(arr3, difference3))

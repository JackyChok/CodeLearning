class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                diff = nums[j] - nums[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
        return max(dp.values())
    
# Test Case 1
nums = [3, 6, 9, 12]
print(Solution().longestArithSeqLength(nums))

# Test Case 2
nums = [9, 4, 7, 2, 10]
print(Solution().longestArithSeqLength(nums))

# Test Case 3
nums = [20, 1, 15, 3, 10, 5, 8]
print(Solution().longestArithSeqLength(nums))
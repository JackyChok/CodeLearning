class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i - n]

        return dp[-1]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3]
    target1 = 4
    result1 = solution.combinationSum4(nums1, target1)
    print(f"Test Case 1: {result1}")  # Expected output: 7
    
    # Test case 2
    nums2 = [9]
    target2 = 3
    result2 = solution.combinationSum4(nums2, target2)
    print(f"Test Case 2: {result2}")  # Expected output: 0

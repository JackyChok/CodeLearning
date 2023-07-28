class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        return self.score(nums, 0, n - 1, dp) >= 0

    def score(self, nums, l, r, dp):
        if dp[l][r] != -1:
            return dp[l][r]
        if l == r:
            return nums[l]
        
        left = nums[l] - self.score(nums, l + 1, r, dp)
        right = nums[r] - self.score(nums, l, r - 1, dp)
        dp[l][r] = max(left, right)
        
        return dp[l][r]


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 5, 2]
    print(sol.PredictTheWinner(nums1))  # Output: False

    # Test case 2
    nums2 = [1, 5, 233, 7]
    print(sol.PredictTheWinner(nums2))  # Output: True

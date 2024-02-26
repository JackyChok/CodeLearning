class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        maxLen = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                maxLen = max(maxLen, dp[i])
        print(dp)
        print(count)
        ans = 0
        for i in range(n):
            if dp[i] == maxLen:
                ans += count[i]

        return ans


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [1, 3, 5, 4, 7]
    print(sol.findNumberOfLIS(nums1))  # Output: 2

    # Test Case 2
    nums2 = [2, 2, 2, 2, 2]
    print(sol.findNumberOfLIS(nums2))  # Output: 5

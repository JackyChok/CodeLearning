class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_of_zeros = 1
        l = 0
        for r in range(len(nums)):
            num_of_zeros -= nums[r] == 0
            if num_of_zeros < 0:
                num_of_zeros += nums[l] == 0
                l += 1
        return r - l


# Create an instance of the Solution class
solution = Solution()

# Test case 1
nums1 = [1, 1, 0, 1]
print(solution.longestSubarray(nums1))  # Output: 3

# Test case 2
nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(solution.longestSubarray(nums2))  # Output: 5

# Test case 3
nums3 = [1, 1, 1]
print(solution.longestSubarray(nums3))  # Output: 2

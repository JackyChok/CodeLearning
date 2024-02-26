class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        cur_sum = 0
        max_window = -1
        l = 0
        
        for r in range(len(nums)):
            cur_sum += nums[r]

            while l <= r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_window = max(max_window, r - l + 1)
        
        return -1 if max_window == -1 else len(nums) - max_window

# Test Case 1
nums1 = [1, 1, 4, 2, 3]
x1 = 5
result1 = Solution().minOperations(nums1, x1)
print(result1)  # Output should be 2

# Test Case 2
nums2 = [5, 6, 7, 8, 9]
x2 = 4
result2 = Solution().minOperations(nums2, x2)
print(result2)  # Output should be -1

# Test Case 3
nums3 = [3, 2, 20, 1, 1, 3]
x3 = 10
result3 = Solution().minOperations(nums3, x3)
print(result3)  # Output should be 5

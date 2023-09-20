class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target, n = sum(nums) - x, len(nums)
        
        if target == 0:
            return n
        
        max_len = cur_sum = left = 0
        
        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len else -1

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

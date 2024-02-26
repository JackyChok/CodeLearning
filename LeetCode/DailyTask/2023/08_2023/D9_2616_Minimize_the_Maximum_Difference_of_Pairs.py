class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        l, r = 0, nums[n - 1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if self.helper(nums, mid, p) >= p:
                r = mid
            else:
                l = mid + 1
        return l
    
    def helper(self, nums, diff, p):
        i, count = 1, 0
        while i < len(nums):
            if nums[i] - nums[i - 1] <= diff:
                i += 1
                count += 1
            i += 1
        return count

# Test cases
sol = Solution()
nums1 = [10, 1, 2, 7, 1, 3]
p1 = 2
print(sol.minimizeMax(nums1, p1))  # Output: 1

nums2 = [4, 2, 1, 2]
p2 = 1
print(sol.minimizeMax(nums2, p2))  # Output: 0

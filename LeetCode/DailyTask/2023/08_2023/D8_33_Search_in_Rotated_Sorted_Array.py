class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[0]:
                if target >= nums[0] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target >= nums[m] and target <= nums[-1]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

# Test cases
sol = Solution()
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(sol.search(nums1, target1))  # Output: 4

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(sol.search(nums2, target2))  # Output: -1

nums3 = [1]
target3 = 0
print(sol.search(nums3, target3))  # Output: -1

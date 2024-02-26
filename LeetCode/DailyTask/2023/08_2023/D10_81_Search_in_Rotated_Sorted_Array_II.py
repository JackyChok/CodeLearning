class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] == target:
                return True

            while left < mid and nums[left] == nums[mid]:
                left += 1
            
            while mid < right and nums[right] == nums[mid]:
                right -= 1

            # left side id sorted
            if nums[left] <= nums[mid]:
                # target is in the first half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

# Test cases
sol = Solution()
nums1 = [2, 5, 6, 0, 0, 1, 2]
target1 = 0
print(sol.search(nums1, target1))  # Output: True

nums2 = [2, 5, 6, 0, 0, 1, 2]
target2 = 3
print(sol.search(nums2, target2))  # Output: False

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

# Test cases
sol = Solution()
print(sol.peakIndexInMountainArray([0, 1, 0]))  # Output: 1
print(sol.peakIndexInMountainArray([0, 2, 1, 0]))  # Output: 1
print(sol.peakIndexInMountainArray([0, 10, 5, 2]))  # Output: 1

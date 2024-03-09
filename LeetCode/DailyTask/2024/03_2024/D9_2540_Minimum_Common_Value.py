from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        common = float('inf')

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return common if common != float('inf') else -1

# Test cases
print(Solution().getCommon([1, 2, 3], [2, 4]))       # Output: 2
print(Solution().getCommon([1, 2, 3, 6], [2, 3, 4, 5]))  # Output: 2

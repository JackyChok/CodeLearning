from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        res = 0
        M = {}
        
        for i in range(n):
            M[nums[i]] = M.get(nums[i], 0) + 1
            
            while M[nums[i]] > k:
                M[nums[j]] -= 1
                j += 1
            
            res = max(res, i - j + 1)
        
        return res

# Test cases
solution = Solution()
print(solution.maxSubarrayLength([1,2,3,1,2,3,1,2], 2))  # Output: 5
print(solution.maxSubarrayLength([1,2,1,2,1,2,1,2], 1))  # Output: 1
print(solution.maxSubarrayLength([5,5,5,5,5,5,5], 4))    # Output: 7

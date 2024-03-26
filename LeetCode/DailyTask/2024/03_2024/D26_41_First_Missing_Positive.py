from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.firstMissingPositive([1,2,0]))  # Output: 3
    print(solution.firstMissingPositive([3,4,-1,1]))  # Output: 2
    print(solution.firstMissingPositive([7,8,9,11,12]))  # Output: 1

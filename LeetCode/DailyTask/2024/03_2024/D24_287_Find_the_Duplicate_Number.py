from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.findDuplicate([1,3,4,2,2]))  # Output: 2
    print(solution.findDuplicate([3,1,3,4,2]))  # Output: 3
    print(solution.findDuplicate([3,3,3,3,3]))  # Output: 3

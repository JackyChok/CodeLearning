class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3, 4, 2, 2]
    result1 = solution.findDuplicate(nums1)
    print(f"Test Case 1: {nums1} -> Duplicate Number: {result1}")
    
    # Test case 2
    nums2 = [3, 1, 3, 4, 2]
    result2 = solution.findDuplicate(nums2)
    print(f"Test Case 2: {nums2} -> Duplicate Number: {result2}")

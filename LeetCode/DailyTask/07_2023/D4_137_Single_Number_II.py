class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones

# Create an instance of the Solution class
solution = Solution()

# Test case 1: The single number in the list [2, 2, 3, 2] is 3
nums1 = [2, 2, 3, 2]
print(solution.singleNumber(nums1))  # Output: 3

# Test case 2: The single number in the list [0, 1, 0, 1, 0, 1, 99] is 99
nums2 = [0, 1, 0, 1, 0, 1, 99]
print(solution.singleNumber(nums2))  # Output: 99

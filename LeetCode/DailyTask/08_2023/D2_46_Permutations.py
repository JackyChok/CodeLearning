class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper([], nums, result)
        return result
    
    def helper(self, curr, nums, result):
        if len(curr) == len(nums):
            result.append(curr[:])
            return
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                self.helper(curr, nums, result)
                curr.pop()

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3]
    print("Test Case 1:", solution.permute(nums1))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    # Test Case 2
    nums2 = [0, 1]
    print("Test Case 2:", solution.permute(nums2))  # Output: [[0, 1], [1, 0]]

    # Test Case 3
    nums3 = [1]
    print("Test Case 3:", solution.permute(nums3))  # Output: [[1]]

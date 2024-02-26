class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        biggest = nums[-1]
        i = len(nums) - 2
        operations = 0
        while i >= 0:
            if nums[i] > biggest:
                denom = nums[i] // biggest
                if nums[i] % biggest > 0:
                    denom += 1
                operations += denom - 1
                biggest = nums[i] // denom
            else:
                biggest = nums[i]

            i -= 1

        return operations

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3, 9, 3]
    result1 = solution.minimumReplacement(nums1)
    print("Test Case 1: Minimum Replacement =", result1)  # Output: 1
    
    nums2 = [1, 2, 3, 4, 5]
    result2 = solution.minimumReplacement(nums2)
    print("Test Case 2: Minimum Replacement =", result2)  # Output: 0

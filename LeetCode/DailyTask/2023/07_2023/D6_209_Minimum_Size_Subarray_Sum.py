class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, total = 0 , 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res

class SolutionTest(object):
    def test_minSubArrayLen(self):
        solution = Solution()

        # Test case 1
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        expected = 2
        print(solution.minSubArrayLen(target, nums))
        assert solution.minSubArrayLen(target, nums) == expected

        # Test case 2
        target = 4
        nums = [1, 4, 4]
        expected = 1
        print(solution.minSubArrayLen(target, nums))
        assert solution.minSubArrayLen(target, nums) == expected

        # Test case 3
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = 0
        print(solution.minSubArrayLen(target, nums))
        assert solution.minSubArrayLen(target, nums) == expected

        # Additional test case
        target = 10
        nums = [3, 5, 7, 1, 1, 6, 2, 3]
        expected = 2
        print(solution.minSubArrayLen(target, nums))
        assert solution.minSubArrayLen(target, nums) == expected

        print("All test cases pass")

# Run the test cases
SolutionTest().test_minSubArrayLen()

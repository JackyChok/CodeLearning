from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        min_max_sum = 0

        for i in range(n // 2):
            min_max_sum = max(min_max_sum, nums[i] + nums[n - 1 - i])

        return min_max_sum


def test():
    sol = Solution()

    # Test Case 1
    input_nums = [3, 5, 2, 3]
    result = sol.minPairSum(input_nums)
    print(f'Test Case 1: Input: {input_nums}, Output: {result}')

    # Test Case 2
    input_nums = [3, 5, 4, 2, 4, 6]
    result = sol.minPairSum(input_nums)
    print(f'Test Case 2: Input: {input_nums}, Output: {result}')


if __name__ == "__main__":
    test()

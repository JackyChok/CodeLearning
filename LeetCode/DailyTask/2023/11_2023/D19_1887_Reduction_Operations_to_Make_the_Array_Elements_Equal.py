from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        ans = 0
        for i in range(size - 1, 0, -1):
            if nums[i - 1] != nums[i]:
                ans += size - i
        return ans


def test():
    sol = Solution()

    # Test Case 1
    input_nums = [5, 1, 3]
    result = sol.reductionOperations(input_nums)
    print(f'Test Case 1: Input: {input_nums}, Output: {result}')

    # Test Case 2
    input_nums = [1, 1, 1]
    result = sol.reductionOperations(input_nums)
    print(f'Test Case 2: Input: {input_nums}, Output: {result}')

    # Test Case 3
    input_nums = [1, 1, 2, 2, 3]
    result = sol.reductionOperations(input_nums)
    print(f'Test Case 3: Input: {input_nums}, Output: {result}')


if __name__ == "__main__":
    test()

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set()

        for binary_string in nums:
            seen.add(int(binary_string, 2))

        n = len(nums[0])

        for i in range(len(nums) + 1):
            if i not in seen:
                return bin(i)[2:].zfill(n)


def test():
    sol = Solution()

    # Test Case 1
    input_nums = ["01", "10"]
    result = sol.findDifferentBinaryString(input_nums)
    print(f'Test Case 1: Input: {input_nums}, Output: {result}')

    # Test Case 2
    input_nums = ["00", "01"]
    result = sol.findDifferentBinaryString(input_nums)
    print(f'Test Case 2: Input: {input_nums}, Output: {result}')

    # Test Case 3
    input_nums = ["111", "011", "001"]
    result = sol.findDifferentBinaryString(input_nums)
    print(f'Test Case 3: Input: {input_nums}, Output: {result}')


if __name__ == "__main__":
    test()

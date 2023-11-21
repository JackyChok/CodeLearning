from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        count = {}
        mod = 10**9 + 7
        
        for n in nums:
            rev = int(str(n)[::-1])
            cur = count.get(n - rev, 0)
            res += cur % mod
            count[n - rev] = 1 + cur

        return res % mod


def test():
    sol = Solution()

    # Test Case 1
    input_nums = [42, 11, 1, 97]
    result = sol.countNicePairs(input_nums)
    print(f'Test Case 1: Input: {input_nums}, Output: {result}')

    # Test Case 2
    input_nums = [13, 10, 35, 24, 76]
    result = sol.countNicePairs(input_nums)
    print(f'Test Case 2: Input: {input_nums}, Output: {result}')


if __name__ == "__main__":
    test()

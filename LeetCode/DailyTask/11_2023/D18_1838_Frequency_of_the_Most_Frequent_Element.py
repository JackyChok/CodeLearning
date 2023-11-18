from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = res = total = 0

        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res


def test():
    sol = Solution()

    # Test Case 1
    input_nums = [1, 2, 4]
    k = 5
    result = sol.maxFrequency(input_nums, k)
    print(f'Test Case 1: Input: {input_nums}, k: {k}, Output: {result}')

    # Test Case 2
    input_nums = [1, 4, 8, 13]
    k = 5
    result = sol.maxFrequency(input_nums, k)
    print(f'Test Case 2: Input: {input_nums}, k: {k}, Output: {result}')

    # Test Case 3
    input_nums = [3, 9, 6]
    k = 2
    result = sol.maxFrequency(input_nums, k)
    print(f'Test Case 3: Input: {input_nums}, k: {k}, Output: {result}')


if __name__ == "__main__":
    test()

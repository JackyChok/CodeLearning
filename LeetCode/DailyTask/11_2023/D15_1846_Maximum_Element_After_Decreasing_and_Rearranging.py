from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_val = 1

        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val += 1

        return max_val


def test():
    sol = Solution()

    # Test Case 1
    input_arr = [2, 2, 1, 2, 1]
    result = sol.maximumElementAfterDecrementingAndRearranging(input_arr)
    print(f'Test Case 1: Input: {input_arr}, Output: {result}')

    # Test Case 2
    input_arr = [100, 1, 1000]
    result = sol.maximumElementAfterDecrementingAndRearranging(input_arr)
    print(f'Test Case 2: Input: {input_arr}, Output: {result}')

    # Test Case 3
    input_arr = [1, 2, 3, 4, 5]
    result = sol.maximumElementAfterDecrementingAndRearranging(input_arr)
    print(f'Test Case 3: Input: {input_arr}, Output: {result}')


if __name__ == "__main__":
    test()

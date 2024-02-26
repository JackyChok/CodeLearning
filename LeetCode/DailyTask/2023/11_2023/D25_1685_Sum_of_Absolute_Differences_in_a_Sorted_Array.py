from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # Initialize an empty list to store the result
        res = []

        # Initialize variables for prefix and suffix sums
        prefix_sum = 0
        suffix_sum = sum(nums)

        # Iterate through each element in the array
        for i, num in enumerate(nums):
            # Calculate the sum of elements to the left of the current element
            left_sum = num * i - prefix_sum

            # Calculate the sum of elements to the right of the current element
            right_sum = suffix_sum - num * (len(nums) - i)

            # Calculate the total sum of absolute differences for the current element
            total_sum = left_sum + right_sum

            # Append the total sum to the result list
            res.append(total_sum)

            # Update the prefix sum and suffix sum for the next iteration
            prefix_sum += num
            suffix_sum -= num

        # Return the final result list
        return res


def test():
    sol = Solution()

    # Test Case 1
    nums1 = [2, 3, 5]
    result1 = sol.getSumAbsoluteDifferences(nums1)
    print(f'Test Case 1: Input: {nums1}, Output: {result1}')

    # Test Case 2
    nums2 = [1, 4, 6, 8, 10]
    result2 = sol.getSumAbsoluteDifferences(nums2)
    print(f'Test Case 2: Input: {nums2}, Output: {result2}')


if __name__ == "__main__":
    test()

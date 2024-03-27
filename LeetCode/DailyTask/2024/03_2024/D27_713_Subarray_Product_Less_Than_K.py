from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left, right, product, count = 0, 0, 1, 0
        n = len(nums)

        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1

        return count

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))  # Output: 8
    print(solution.numSubarrayProductLessThanK([1,2,3], 0))  # Output: 0

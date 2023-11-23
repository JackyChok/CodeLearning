from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = deque([(0, 0)])
        
        while q:
            row, col = q.popleft()
            res.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                q.append((row + 1, 0))

            if col + 1 < len(nums[row]):
                q.append((row, col + 1))

        return res


def test():
    sol = Solution()

    # Test Case 1
    input_nums1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = sol.findDiagonalOrder(input_nums1)
    print(f'Test Case 1: Input: {input_nums1}, Output: {result1}')

    # Test Case 2
    input_nums2 = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    result2 = sol.findDiagonalOrder(input_nums2)
    print(f'Test Case 2: Input: {input_nums2}, Output: {result2}')


if __name__ == "__main__":
    test()
from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = deque([(0, 0)])
        
        while q:
            row, col = q.popleft()
            res.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                q.append((row + 1, 0))

            if col + 1 < len(nums[row]):
                q.append((row, col + 1))

        return res


def test():
    sol = Solution()

    # Test Case 1
    input_nums1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = sol.findDiagonalOrder(input_nums1)
    print(f'Test Case 1: Input: {input_nums1}, Output: {result1}')

    # Test Case 2
    input_nums2 = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    result2 = sol.findDiagonalOrder(input_nums2)
    print(f'Test Case 2: Input: {input_nums2}, Output: {result2}')


if __name__ == "__main__":
    test()

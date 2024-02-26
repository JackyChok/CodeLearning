from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    n1 = 4
    left1 = [4, 3]
    right1 = [0, 1]
    result1 = solution.getLastMoment(n1, left1, right1)
    print("Result 1:", result1)

    # Test Case 2
    n2 = 7
    left2 = []
    right2 = [0, 1, 2, 3, 4, 5, 6, 7]
    result2 = solution.getLastMoment(n2, left2, right2)
    print("Result 2:", result2)

    # Test Case 3
    n3 = 7
    left3 = [0, 1, 2, 3, 4, 5, 6, 7]
    right3 = []
    result3 = solution.getLastMoment(n3, left3, right3)
    print("Result 3:", result3)

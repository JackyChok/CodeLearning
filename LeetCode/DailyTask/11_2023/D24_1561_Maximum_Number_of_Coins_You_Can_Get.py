from typing import List
from collections import deque

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)
        res = 0

        while q:
            q.pop()  # For Alice
            res += q.pop()  # For you
            q.popleft()  # For Bob
        
        return res


def test():
    sol = Solution()

    # Test Case 1
    piles1 = [2, 4, 1, 2, 7, 8]
    result1 = sol.maxCoins(piles1)
    print(f'Test Case 1: Input: {piles1}, Output: {result1}')

    # Test Case 2
    piles2 = [2, 4, 5]
    result2 = sol.maxCoins(piles2)
    print(f'Test Case 2: Input: {piles2}, Output: {result2}')

    # Test Case 3
    piles3 = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    result3 = sol.maxCoins(piles3)
    print(f'Test Case 3: Input: {piles3}, Output: {result3}')


if __name__ == "__main__":
    test()

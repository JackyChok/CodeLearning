from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        st = deque()
        st.append(deck[n - 1])
        for i in range(n - 2, -1, -1):
            st.appendleft(st.pop())
            st.appendleft(deck[i])
        revealed = []
        while st:
            revealed.append(st.popleft())
        return revealed

# Test cases
solution = Solution()
print(solution.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))  # Output: [2, 13, 3, 11, 5, 17, 7]
print(solution.deckRevealedIncreasing([1, 1000]))  # Output: [1, 1000]

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0

        for i, x in enumerate(tickets):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total

# Test cases
solution = Solution()
tickets1 = [2, 3, 2]
k1 = 2
print(solution.timeRequiredToBuy(tickets1, k1))  # Output: 6

tickets2 = [5, 1, 1, 1]
k2 = 0
print(solution.timeRequiredToBuy(tickets2, k2))  # Output: 3

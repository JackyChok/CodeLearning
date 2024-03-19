from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)

# Test cases
sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))  # Output: 8
print(sol.leastInterval(["A","C","A","B","D","B"], 1))  # Output: 6
print(sol.leastInterval(["A","A","A", "B","B","B"], 3))  # Output: 10

from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        max_freq = max(mp.values())
        count = sum(1 for freq in mp.values() if freq == max_freq)

        return count

# Test cases
print(Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]))  # Output: 2
print(Solution().maxFrequencyElements([1, 2, 3, 4, 5]))    # Output: 5

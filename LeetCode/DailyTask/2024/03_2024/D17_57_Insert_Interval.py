from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0

        # Add intervals before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)
        
        # Add remaining intervals
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged

# Test cases
sol = Solution()
print(sol.insert([[1,3],[6,9]], [2,5]))  # Output: [[1,5],[6,9]]
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # Output: [[1,2],[3,10],[12,16]]

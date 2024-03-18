from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrows = 1
        end = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > end: 
                arrows += 1  
                end = balloon[1] 
            else:
                end = min(end, balloon[1])
        
        return arrows

# Test cases
sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # Output: 2
print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))  # Output: 4
print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))  # Output: 2

import math

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if hour < len(dist) - 1:
            return -1
        
        l, r = 1, 10**7
        ans = -1
        
        while l <= r:
            m = math.ceil((l + r) / 2)            
            if self.check(dist, hour, m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return int(ans)
    
    def check(self, dist, hour, speed):
        time = 0
        i = 0
        while time <= hour and i < len(dist) - 1:
            time += math.ceil(dist[i] / speed)
            i += 1
        
        time += dist[-1] / speed
        return time <= hour


# Test cases
sol = Solution()
print(sol.minSpeedOnTime([1, 3, 2], 6))   # Output: 1
print(sol.minSpeedOnTime([1, 3, 2], 2.7)) # Output: 3
print(sol.minSpeedOnTime([1, 3, 2], 1.9)) # Output: -1

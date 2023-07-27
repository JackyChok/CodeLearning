class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        sumPower = sum(batteries)
        left, right = 1, sumPower // n
        
        while left < right:
            time = (left + right + 1) // 2
            if self.check(batteries, n, time):
                left = time
            else:
                right = time - 1
        return left
    
    def check(self, B, n, time):
        total_power = sum(min(battery, time) for battery in B)
        return total_power >= time * n

# Test cases
sol = Solution()
print(sol.maxRunTime(2, [3, 3, 3]))  # Output: 4
print(sol.maxRunTime(2, [1, 1, 1, 1]))  # Output: 2

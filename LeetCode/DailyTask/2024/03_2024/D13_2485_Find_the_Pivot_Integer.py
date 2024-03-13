from math import sqrt

class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)
        
        if x % 1 != 0:
            return -1
        else:
            return int(x)

# Test cases
sol = Solution()
print(sol.pivotInteger(8))  # Output: 6
print(sol.pivotInteger(1))  # Output: 1
print(sol.pivotInteger(4))  # Output: -1

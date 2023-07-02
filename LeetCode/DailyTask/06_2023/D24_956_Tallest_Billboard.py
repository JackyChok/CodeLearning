class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0: 0}
        for x in rods:
            for d, y in dp.copy().items():
                dp[d + x] = max(dp.get(x + d, 0), y)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
        return dp[0]

# Test Case 1
rods = [1,2,3,6]
print(Solution().tallestBillboard(rods))

# Test Case 2
rods = [1,2,3,4,5,6]
print(Solution().tallestBillboard(rods))

# Test Case 3
rods = [1,2]
print(Solution().tallestBillboard(rods))
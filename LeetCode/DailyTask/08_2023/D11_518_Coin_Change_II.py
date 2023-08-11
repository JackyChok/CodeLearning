class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]

# Test cases
sol = Solution()
amount1 = 5
coins1 = [1, 2, 5]
print(sol.change(amount1, coins1))  # Output: 4

amount2 = 3
coins2 = [2]
print(sol.change(amount2, coins2))  # Output: 0

amount3 = 10
coins3 = [10]
print(sol.change(amount3, coins3))  # Output: 1

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = float('-inf')
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell
    

# Test Case 1
prices = [1,3,2,8,4,9]
fee = 2
print(Solution().maxProfit(prices, fee))

# Test Case 2
prices = [1,3,7,5,10,3]
fee = 3
print(Solution().maxProfit(prices, fee))

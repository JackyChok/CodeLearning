class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        total_ways = 1 
        for order_number in range(2, n + 1):
            total_ways = (total_ways * (2 * order_number - 1) * order_number) % MOD
        return total_ways

if __name__ == "__main__":
    # Test case
    solution = Solution()
    n = 1  # You can change this to test different values of n
    result = solution.countOrders(n)
    print(f"Number of possible orders for n={n} is {result}")

    n = 2  # You can change this to test different values of n
    result = solution.countOrders(n)
    print(f"Number of possible orders for n={n} is {result}")

    n = 3  # You can change this to test different values of n
    result = solution.countOrders(n)
    print(f"Number of possible orders for n={n} is {result}")

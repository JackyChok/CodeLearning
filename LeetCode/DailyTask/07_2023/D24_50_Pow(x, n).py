class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def bs(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = bs(x, n // 2)
            res = res * res

            if n % 2:
                return res * x
            else:
                return res

        res = bs(x, abs(n))

        if n >= 0:
            return res
        return 1 / res


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    x1, n1 = 2.00000, 10
    result1 = solution.myPow(x1, n1)
    print("Test case 1:", result1)

    # Test case 2
    x2, n2 = 2.10000, 3
    result2 = solution.myPow(x2, n2)
    print("Test case 2:", result2)

    # Test case 3
    x3, n3 = 2.00000, -2
    result3 = solution.myPow(x3, n3)
    print("Test case 3:", result3)

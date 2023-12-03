class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)


def test():
    sol = Solution()

    # Test Case 1
    input1 = 3
    result1 = sol.minimumOneBitOperations(input1)
    print(f'Test Case 1: Input: {input1}, Output: {result1}')

    # Test Case 2
    input2 = 6
    result2 = sol.minimumOneBitOperations(input2)
    print(f'Test Case 2: Input: {input2}, Output: {result2}')


if __name__ == "__main__":
    test()

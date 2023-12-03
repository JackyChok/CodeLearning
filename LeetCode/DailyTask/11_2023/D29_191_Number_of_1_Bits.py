class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1:
                res += 1

        return res


def test():
    sol = Solution()

    # Test Case 1
    input1 = 0b00000000000000000000000000001011
    result1 = sol.hammingWeight(input1)
    print(f'Test Case 1: Input: {bin(input1)}, Output: {result1}')

    # Test Case 2
    input2 = 0b00000000000000000000000010000000
    result2 = sol.hammingWeight(input2)
    print(f'Test Case 2: Input: {bin(input2)}, Output: {result2}')

    # Test Case 3
    input3 = 0b11111111111111111111111111111101
    result3 = sol.hammingWeight(input3)
    print(f'Test Case 3: Input: {bin(input3)}, Output: {result3}')


if __name__ == "__main__":
    test()

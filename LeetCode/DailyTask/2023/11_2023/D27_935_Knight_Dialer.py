class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        mod = 10**9 + 7
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        dp = [1] * 10  # ways to land on i-th digit
        for _ in range(n - 1):
            next_dp = [0] * 10
            for i in range(10):
                for j in jumps[i]:
                    next_dp[j] = (next_dp[j] + dp[i]) % mod
            dp = next_dp
        
        res = 0
        for num in dp:
            res = (res + num) % mod
        return res


def test():
    sol = Solution()

    # Test Case 1
    result1 = sol.knightDialer(1)
    print(f'Test Case 1: Input: 1, Output: {result1}')

    # Test Case 2
    result2 = sol.knightDialer(2)
    print(f'Test Case 2: Input: 2, Output: {result2}')

    # Test Case 3
    result3 = sol.knightDialer(3131)
    print(f'Test Case 3: Input: 3131, Output: {result3}')


if __name__ == "__main__":
    test()

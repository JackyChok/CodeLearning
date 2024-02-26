class Solution:
    def countHomogenous(self, s: str) -> int:
        left = 0
        res = 0

        for right in range(len(s)):
            if s[left] == s[right]:
                res += right - left + 1
            else:
                res += 1
                left = right

        return res % (10**9 + 7)


def run_test():
    sol = Solution()

    # Test Case 1
    s1 = "abbcccaa"
    result1 = sol.countHomogenous(s1)
    print(f'Test Case 1: "{s1}" -> {result1}')

    # Test Case 2
    s2 = "xy"
    result2 = sol.countHomogenous(s2)
    print(f'Test Case 2: "{s2}" -> {result2}')

    # Test Case 3
    s3 = "zzzzz"
    result3 = sol.countHomogenous(s3)
    print(f'Test Case 3: "{s3}" -> {result3}')


if __name__ == "__main__":
    run_test()

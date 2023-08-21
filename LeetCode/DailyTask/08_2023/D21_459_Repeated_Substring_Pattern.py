class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = ["abab", "aba", "abcabcabcabc"]
    
    for test_case in test_cases:
        result = solution.repeatedSubstringPattern(test_case)
        print(f"Input: {test_case}\nOutput: {result}\n")

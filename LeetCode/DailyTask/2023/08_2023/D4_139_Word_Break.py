class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i - len(w)] and s[:i].endswith(w):
                    dp[i] = True
                    break
        return dp[-1]


def run_test_cases():
    s1, wordDict1 = "leetcode", ["leet", "code"]
    s2, wordDict2 = "applepenapple", ["apple", "pen"]
    s3, wordDict3 = "catsandog", ["cats", "dog", "sand", "and", "cat"]

    sol = Solution()
    
    output1 = sol.wordBreak(s1, wordDict1)
    output2 = sol.wordBreak(s2, wordDict2)
    output3 = sol.wordBreak(s3, wordDict3)

    print(f"Test Case 1: {output1}")  # Expected Output: True
    print(f"Test Case 2: {output2}")  # Expected Output: True
    print(f"Test Case 3: {output3}")  # Expected Output: False


if __name__ == "__main__":
    run_test_cases()

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        dp = {}
        max_chain = 0
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
                    print(dp)
            max_chain = max(max_chain, dp[word])
        return max_chain

# Test cases
if __name__ == "__main__":
    solution = Solution()

    words1 = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(solution.longestStrChain(words1))  # Expected output: 4

    words2 = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    print(solution.longestStrChain(words2))  # Expected output: 5

    words3 = ["abcd", "dbqca"]
    print(solution.longestStrChain(words3))  # Expected output: 1

# Define the TrieNode and Trie classes
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

# Define the Solution class with the minExtraChar method
class Solution(object):
    def minExtraChar(self, s, dictionary):
        dp = {len(s): 0}
        trie = Trie(dictionary).root

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)  # skip curr char
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    s1 = "leetscode"
    dictionary1 = ["leet", "code", "leetcode"]
    result1 = solution.minExtraChar(s1, dictionary1)
    print(f"Result 1: {result1}")  # Expected output: 1

    s2 = "sayhelloworld"
    dictionary2 = ["hello", "world"]
    result2 = solution.minExtraChar(s2, dictionary2)
    print(f"Result 2: {result2}")  # Expected output: 3

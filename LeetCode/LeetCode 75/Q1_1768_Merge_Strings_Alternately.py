class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
            i += 1
        return merged

# Test Case 1: word1 and word2 have equal lengths
word1 = "abc"
word2 = "pqr"
# Expected output: "apbqcr"
print(Solution().mergeAlternately(word1, word2))

# Test Case 2: word1 is shorter than word2
word1 = "ab"
word2 = "pqrs"
# Expected output: "apbqrs"
print(Solution().mergeAlternately(word1, word2))

# Test Case 3: word1 is longer than word2
word1 = "abcd"
word2 = "pq"
# Expected output: "apbqcd"
print(Solution().mergeAlternately(word1, word2))

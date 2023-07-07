import unittest

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        max_freq = i = 0

        d = {'T': 0, 'F': 0}

        for j in range(len(answerKey)):
            d[answerKey[j]] += 1
            max_freq = max(max_freq, d[answerKey[j]])
            if j - i + 1 > max_freq + k:
                d[answerKey[i]] -= 1
                i += 1
        return len(answerKey) - i
    

# Create an instance of the Solution class
solution = Solution()

# Test case 1
answerKey = "TTFF"
k = 2
print(solution.maxConsecutiveAnswers(answerKey, k))  # Output: 4

# Test case 2
answerKey = "TFFT"
k = 1
print(solution.maxConsecutiveAnswers(answerKey, k))  # Output: 3

# Test case 3
answerKey = "TTFTTFTT"
k = 1
print(solution.maxConsecutiveAnswers(answerKey, k))  # Output: 5
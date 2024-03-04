from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        max_score = 0
        left = 0
        right = n - 1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score

# Test cases
print(Solution().bagOfTokensScore([100], 50))                 # Output: 0
print(Solution().bagOfTokensScore([200, 100], 150))           # Output: 1
print(Solution().bagOfTokensScore([100, 200, 300, 400], 200)) # Output: 2

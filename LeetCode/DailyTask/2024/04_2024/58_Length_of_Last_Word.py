class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        
        if not words:
            return 0
        
        return len(words[-1])

# Test cases
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))               # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))     # Output: 6

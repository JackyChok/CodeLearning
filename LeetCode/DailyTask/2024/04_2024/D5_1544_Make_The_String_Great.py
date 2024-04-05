class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

# Test cases
sol = Solution()
print(sol.makeGood("leEeetcode"))  # Output: "leetcode"
print(sol.makeGood("abBAcC"))      # Output: ""
print(sol.makeGood("s"))            # Output: "s"

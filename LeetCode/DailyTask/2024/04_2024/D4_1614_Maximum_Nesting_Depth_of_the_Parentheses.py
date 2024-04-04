class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_num = 0
        for i in s:
            if i == "(":
                count += 1
                if max_num < count:
                    max_num = count
            elif i == ")":
                count -= 1
        return max_num

# Test cases
sol = Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3
print(sol.maxDepth("(1)+((2))+(((3)))"))    # Output: 3

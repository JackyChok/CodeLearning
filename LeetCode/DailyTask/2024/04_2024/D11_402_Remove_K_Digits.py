from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining k digits from the end of the stack
        stack = stack[:-k] if k > 0 else stack
        
        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Handle edge case where result might be empty
        return result if result else '0'

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeKdigits("1432219", 3))  # Output: "1219"
    print(solution.removeKdigits("10200", 1))    # Output: "200"
    print(solution.removeKdigits("10", 2))        # Output: "0"

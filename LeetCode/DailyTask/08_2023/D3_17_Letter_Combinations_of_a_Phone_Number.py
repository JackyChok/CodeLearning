class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        dial = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        def helper(comb, index, digits):
            if index == len(digits):
                ans.append(comb)
                return
            
            letters = dial[int(digits[index])]
            for char in letters:
                helper(comb + char, index + 1, digits)
        
        if len(digits) == 0:
            return ans
        
        helper("", 0, digits)
        return ans

# Test cases
if __name__ == "__main__":
    sol = Solution()

    digits1 = "23"
    print(f"Input: {digits1}, Output: {sol.letterCombinations(digits1)}")

    digits2 = ""
    print(f"Input: {digits2}, Output: {sol.letterCombinations(digits2)}")

    digits3 = "2"
    print(f"Input: {digits3}, Output: {sol.letterCombinations(digits3)}")

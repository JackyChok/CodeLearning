class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        uniq = set(s)
        
        for c in uniq:
            start = s.find(c)  # search a character from the beginning
            end = s.rfind(c)  # search a character from the last index
            
            if start < end:
                res += len(set(s[start+1:end]))
        
        return res


def test():
    sol = Solution()

    # Test Case 1
    input_str = "aabca"
    result = sol.countPalindromicSubsequence(input_str)
    print(f'Test Case 1: Input: "{input_str}", Output: {result}')

    # Test Case 2
    input_str = "adc"
    result = sol.countPalindromicSubsequence(input_str)
    print(f'Test Case 2: Input: "{input_str}", Output: {result}')

    # Test Case 3
    input_str = "bbcbaba"
    result = sol.countPalindromicSubsequence(input_str)
    print(f'Test Case 3: Input: "{input_str}", Output: {result}')


if __name__ == "__main__":
    test()

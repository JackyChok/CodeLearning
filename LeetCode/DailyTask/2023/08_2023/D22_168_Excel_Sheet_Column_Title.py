class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            c = chr(ord('A') + (columnNumber - 1) % 26)
            result = c + result
            columnNumber = (columnNumber - 1) // 26
        return result

if __name__ == "__main__":
    solution = Solution()
    
    test_case = 1
    result = solution.convertToTitle(test_case)
    print(f"Input: {test_case}\nOutput: {result}\n")

    test_case = 28
    result = solution.convertToTitle(test_case)
    print(f"Input: {test_case}\nOutput: {result}\n")

    test_case = 701
    result = solution.convertToTitle(test_case)
    print(f"Input: {test_case}\nOutput: {result}\n")

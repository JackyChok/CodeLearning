class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count("1")
        zeros_count = len(s) - ones_count

        return "1" * (ones_count - 1) + "0" * zeros_count + "1"

# Test cases
print(Solution().maximumOddBinaryNumber("010"))   # Output: "011"
print(Solution().maximumOddBinaryNumber("0101"))  # Output: "0111"

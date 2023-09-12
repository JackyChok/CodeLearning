from collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = Counter(s)

        uniq_set = set()
        count = 0

        for freq in chars.values():
            while freq > 0 and freq in uniq_set:
                freq -= 1
                count += 1
            
            uniq_set.add(freq)

        return count

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "aab"
    result1 = solution.minDeletions(s1)
    print(result1)  # Output should be 0

    # Test case 2
    s2 = "aaabbbcc"
    result2 = solution.minDeletions(s2)
    print(result2)  # Output should be 2

    # Test case 3
    s3 = "ceabaacb"
    result3 = solution.minDeletions(s3)
    print(result3)  # Output should be 2

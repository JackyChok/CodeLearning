class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_idx = t_idx = 0

        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1

        return s_idx == len(s)

def test_isSubsequence():
    solution = Solution()

    # Test case 1: s is a subsequence of t
    s1 = "abc"
    t1 = "ahbgdc"
    result1 = solution.isSubsequence(s1, t1)
    print(f"Test Case 1 - Result: {result1}, Expected: True")

    # Test case 2: s is not a subsequence of t
    s2 = "axc"
    t2 = "ahbgdc"
    result2 = solution.isSubsequence(s2, t2)
    print(f"Test Case 2 - Result: {result2}, Expected: False")

if __name__ == '__main__':
    test_isSubsequence()

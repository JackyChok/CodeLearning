from collections import defaultdict

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = defaultdict(int)
        
        def printer(i, j):
            if i > j:
                return 0
            if (i, j) in visited:
                return visited[(i, j)]
            res = 1 + printer(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, printer(i, k - 1) + printer(k + 1, j))
            visited[(i, j)] = res
            return res
        
        return printer(0, len(s) - 1)

# Test cases
solution = Solution()
print(solution.strangePrinter("aaabbb"))  # Output: 2
print(solution.strangePrinter("aba"))  # Output: 2

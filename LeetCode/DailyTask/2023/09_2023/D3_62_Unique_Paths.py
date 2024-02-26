class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.uniquePaths(3, 7)
    print("Test Case 1: Expected Result: 28, Actual Result:", result1)

    # Test case 2
    result2 = solution.uniquePaths(3, 2)
    print("Test Case 2: Expected Result: 3, Actual Result:", result2)

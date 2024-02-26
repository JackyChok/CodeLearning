from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])

        # Calculate heights for each column
        for i in range(1, row):
            for j in range(col):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        res = 0
        for i in range(row):
            # Sort the heights in ascending order
            matrix[i].sort(reverse=True)

            # Iterate through the sorted heights
            for j in range(col):
                height = matrix[i][j]
                width = j + 1
                res = max(res, height * width)

        return res


def test():
    sol = Solution()

    # Test Case 1
    matrix1 = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
    result1 = sol.largestSubmatrix(matrix1)
    print(f'Test Case 1: Input: {matrix1}, Output: {result1}')

    # Test Case 2
    matrix2 = [[1, 0, 1, 0, 1]]
    result2 = sol.largestSubmatrix(matrix2)
    print(f'Test Case 2: Input: {matrix2}, Output: {result2}')

    # Test Case 3
    matrix3 = [[1, 1, 0], [1, 0, 1]]
    result3 = sol.largestSubmatrix(matrix3)
    print(f'Test Case 3: Input: {matrix3}, Output: {result3}')


if __name__ == "__main__":
    test()

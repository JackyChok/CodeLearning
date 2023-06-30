class Solution(object):
    # Binary Search + BFS
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        left, right = 1, len(cells)
        res = -1

        while left <= right:
            mid = (left + right) // 2

            if self.is_possible(mid, row, col, cells):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res

    def is_possible(self, mid, n, m, cells):
        grid = [[0] * m for _ in range(n)]

        for i in range(mid):
            row, col = cells[i]
            grid[row - 1][col - 1] = 1

        visited = set()
        stack = [(0, col) for col in range(m) if grid[0][col] == 0]

        while stack:
            row, col = stack.pop()

            if row == n - 1:
                return True

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dx, col + dy

                if (
                    0 <= new_row < n
                    and 0 <= new_col < m
                    and grid[new_row][new_col] == 0
                ):
                    stack.append((new_row, new_col))

        return False


solution = Solution() 

# Test Case 1
row = 2
col = 2
cells = [[1, 1], [2, 1], [1, 2], [2, 2]]
output_1 = solution.latestDayToCross(row, col, cells)
print(output_1)  # Output: 2

# Test Case 2
row = 2
col = 2
cells = [[1, 1], [1, 2], [2, 1], [2, 2]]
output_2 = solution.latestDayToCross(row, col, cells)
print(output_2)  # Output: 1

# Test Case 3
row = 3
col = 3
cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
output_3 = solution.latestDayToCross(row, col, cells)
print(output_3)  # Output: 3
from collections import deque, defaultdict

class Solution(object):
    # Modified DFS
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y, m, n, totalKeys = -1, -1, len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    x, y = i, j
                if 'a' <= c <= 'f':
                    totalKeys += 1

        start = (0, x, y)
        queue = deque([start])
        visited = defaultdict(bool)
        visited[start] = True

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                keys, i, j = queue.popleft()
                if keys == (1 << totalKeys) - 1:
                    return step

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    newKeys = keys
                    if 0 <= ni < m and 0 <= nj < n:
                        c = grid[ni][nj]
                        if c == '#':
                            continue
                        if 'a' <= c <= 'f':
                            newKeys |= 1 << (ord(c) - ord('a'))
                        if 'A' <= c <= 'F' and not (keys >> (ord(c) - ord('A')) & 1):
                            continue
                        if not visited[(newKeys, ni, nj)]:
                            visited[(newKeys, ni, nj)] = True
                            queue.append((newKeys, ni, nj))
            step += 1
        return -1


solution = Solution()

# Test Case 1
grid_1 = ["@.a..","###.#","b.A.B"]
output_1 = solution.shortestPathAllKeys(grid_1)
print(output_1)  # Output: 8

# Test Case 2
grid_2 = ["@..aA","..B#.","....b"]
output_2 = solution.shortestPathAllKeys(grid_2)
print(output_2)  # Output: 6

# Test Case 3
grid_3 = ["@Aa"]
output_3 = solution.shortestPathAllKeys(grid_3)
print(output_3)  # Output: -1


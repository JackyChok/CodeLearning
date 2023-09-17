from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))
        
        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    graph1 = [[1, 2, 3], [0], [0], [0]]
    result1 = solution.shortestPathLength(graph1)
    print(result1)  # Output should be 4

    # Test case 2
    graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    result2 = solution.shortestPathLength(graph2)
    print(result2)  # Output should be 4

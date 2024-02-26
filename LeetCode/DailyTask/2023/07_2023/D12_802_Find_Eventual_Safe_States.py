class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        visited = [False] * n
        unsafe = [0] * n

        for i in range(n):
            if unsafe[i] == 0:
                visited[i] = True
                self.dfs(i, visited, graph, unsafe)
                visited[i] = False

        result = []
        for i in range(len(unsafe)):
            if unsafe[i] == 1:
                result.append(i)
        return result

    def dfs(self, node, visited, graph, unsafe):
        isSafe = True
        for neighbor in graph[node]:
            if visited[neighbor] or unsafe[neighbor] == 2:
                isSafe = False
                break
            if unsafe[neighbor] == 1:
                continue
            visited[neighbor] = True
            if not self.dfs(neighbor, visited, graph, unsafe):
                isSafe = False
            visited[neighbor] = False
        unsafe[node] = 1 if isSafe else 2
        return isSafe


# Create an instance of the Solution class
solution = Solution()

# Test case 1
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(solution.eventualSafeNodes(graph))  # Output: [2, 4, 5, 6]

# Test case 2
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(solution.eventualSafeNodes(graph))  # Output: [4]

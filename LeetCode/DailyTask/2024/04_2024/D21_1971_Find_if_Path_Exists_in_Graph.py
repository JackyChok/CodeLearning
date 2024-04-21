from typing import List
import collections

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = collections.deque([source])
        visited = set([source])
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False

# Test cases
def run_test_cases():
    solution = Solution()
    print(solution.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
    print(solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))

if __name__ == "__main__":
    run_test_cases()

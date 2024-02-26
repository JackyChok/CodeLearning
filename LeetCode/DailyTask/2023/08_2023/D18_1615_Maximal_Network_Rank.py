import collections
import itertools

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # T: O(N^2)
        # S: O(N^2)
        graph = collections.defaultdict(set)

        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        res = 0

        for city1, city2 in itertools.combinations(graph.keys(), 2):
            has_connection = 1 if city1 in graph[city2] else 0

            city1_connections = len(graph[city1])
            city2_connections = len(graph[city2])

            res = max(res, city1_connections + city2_connections - has_connection)
        
        return res

# Test cases
solution = Solution()

print(solution.maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]]))  # Output: 4
print(solution.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))  # Output: 5
print(solution.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))  # Output: 5

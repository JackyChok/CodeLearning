from typing import List
import collections
import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq = [(-1, start)]
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end:
                return prob * -1
            for neigh, edgeProb in adj[cur]:
                if neigh not in visit:
                    heapq.heappush(pq, (prob * edgeProb, neigh))
        return 0


solution = Solution()

# Test Case 1
n_1 = 3
edges_1 = [[0, 1], [1, 2], [0, 2]]
succProb_1 = [0.5, 0.5, 0.2]
start_1 = 0
end_1 = 2
output_1 = solution.maxProbability(n_1, edges_1, succProb_1, start_1, end_1)
print(output_1)  # Output: 0.25

# Test Case 2
n_2 = 3
edges_2 = [[0, 1], [1, 2], [0, 2]]
succProb_2 = [0.5, 0.5, 0.3]
start_2 = 0
end_2 = 2
output_2 = solution.maxProbability(n_2, edges_2, succProb_2, start_2, end_2)
print(output_2)  # Output: 0.3

# Test Case 3
n_3 = 3
edges_3 = [[0, 1]]
succProb_3 = [0.5]
start_3 = 0
end_3 = 2
output_3 = solution.maxProbability(n_3, edges_3, succProb_3, start_3, end_3)
print(output_3)  # Output: 0


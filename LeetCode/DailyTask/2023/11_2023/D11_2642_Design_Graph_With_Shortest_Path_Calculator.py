import heapq
from typing import List

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = {i: [] for i in range(n)}
        for edge in edges:
            self.adj_list[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.adj_list[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        dist = {i: float('inf') for i in range(len(self.adj_list))}
        dist[node1] = 0

        while heap:
            (d, node) = heapq.heappop(heap)
            if node == node2:
                return d
            if d > dist[node]:
                continue
            for neighbor, weight in self.adj_list[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        return -1


def run_test():
    # Test Case
    graph = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    result1 = graph.shortestPath(3, 2)
    print(f'Test Case 1: Shortest path from node 3 to 2 is {result1}')

    result2 = graph.shortestPath(0, 3)
    print(f'Test Case 2: Shortest path from node 0 to 3 is {result2}')

    graph.addEdge([1, 3, 4])
    result3 = graph.shortestPath(0, 3)
    print(f'Test Case 3: After adding edge [1, 3, 4], the shortest path from node 0 to 3 is {result3}')


if __name__ == "__main__":
    run_test()

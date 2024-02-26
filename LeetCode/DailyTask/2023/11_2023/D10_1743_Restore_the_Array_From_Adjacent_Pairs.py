from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Create a graph to represent adjacent pairs
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize the result list
        res = []

        # Find the starting node with only one neighbor
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                res = [node, neighbors[0]]
                break

        # Continue building the array until its length matches the number of pairs
        while len(res) < len(adjacentPairs) + 1:
            # Get the last two elements in the result array
            last, prev = res[-1], res[-2]

            # Find the candidates for the next element
            candidates = graph[last]

            # Choose the candidate that is not the previous element
            next_element = candidates[0] if candidates[0] != prev else candidates[1]

            # Append the next element to the result array
            res.append(next_element)

        return res


def run_test():
    sol = Solution()

    # Test Case 1
    pairs1 = [[2,1],[3,4],[3,2]]
    result1 = sol.restoreArray(pairs1)
    print(f'Test Case 1: {pairs1} -> {result1}')

    # Test Case 2
    pairs2 = [[4,-2],[1,4],[-3,1]]
    result2 = sol.restoreArray(pairs2)
    print(f'Test Case 2: {pairs2} -> {result2}')

    # Test Case 3
    pairs3 = [[100000,-100000]]
    result3 = sol.restoreArray(pairs3)
    print(f'Test Case 3: {pairs3} -> {result3}')


if __name__ == "__main__":
    run_test()

import heapq

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        for i, row in enumerate(mat):
            strength = sum(row)
            heapq.heappush(heap, (-strength, -i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [-i for _, i in sorted(heap, reverse=True)]

# Test Case 1
mat1 = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
k1 = 3
result1 = Solution().kWeakestRows(mat1, k1)
print(result1)  # Output should be [2, 0, 3]

# Test Case 2
mat2 = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
k2 = 2
result2 = Solution().kWeakestRows(mat2, k2)
print(result2)  # Output should be [0, 2]

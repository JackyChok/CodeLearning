import itertools

class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        for k in range(len(requests), 0, -1):
            for c in itertools.combinations(range(len(requests)), k):
                degree = [0] * n
                for i in c:
                    degree[requests[i][0]] -= 1
                    degree[requests[i][1]] += 1
                if not any(degree):
                    return k
        return 0

# Create an instance of the Solution class
solution = Solution()

# Test Case 1
n = 5
requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
print(solution.maximumRequests(n, requests))  # Output: 5

# Test Case 2
n = 3
requests = [[0, 0], [1, 2], [2, 1]]
print(solution.maximumRequests(n, requests))  # Output: 3

# Test Case 3
n = 4
requests = [[0, 3], [3, 1], [1, 2], [2, 0]]
print(solution.maximumRequests(n, requests))  # Output: 4

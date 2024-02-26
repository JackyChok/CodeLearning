class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights)
        pairs = [0] * (n - 1)
        for i in range(1, n):
            pairs[i - 1] = weights[i] + weights[i - 1]
        pairs.sort()

        min_sum = 0
        max_sum = 0
        for i in range(k - 1):
            min_sum += pairs[i]
            max_sum += pairs[n - i - 2]

        return max_sum - min_sum



# Create an instance of the Solution class
solution = Solution()

# Test case 1
weights = [1, 3, 5, 1]
k = 2
print(solution.putMarbles(weights, k))  # Output: 4

# Test case 2
weights = [1, 3]
k = 2
print(solution.putMarbles(weights, k))  # Output: 0

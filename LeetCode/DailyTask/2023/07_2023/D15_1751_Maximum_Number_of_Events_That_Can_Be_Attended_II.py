class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x: x[0])
        n = len(events)
        
        dp = [[-1] * n for _ in range(k + 1)]
        
        def dfs(index, count):
            if count == 0 or index == n:
                return 0
            if dp[count][index] != -1:
                return dp[count][index]
            
            dp[count][index] = max(events[index][2] + dfs(binarySearch(events[index][1]), count - 1), dfs(index + 1, count))
            
            return dp[count][index]
        
        def binarySearch(target):
            left, right = 0, n - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left
        
        return dfs(0, k)

# Test Case 1
events1 = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
k1 = 2
# Available events: [[1, 2, 4], [2, 3, 1], [3, 4, 3]]
# Maximize the total value with at most 2 events
# Selecting events [1, 2, 4] and [3, 4, 3] gives a total value of 7
# Expected output: 7

# Test Case 2
events2 = [[1, 2, 4], [3, 4, 3], [2, 3, 10]]
k2 = 2
# Available events: [[1, 2, 4], [2, 3, 10], [3, 4, 3]]
# Maximize the total value with at most 2 events
# Selecting events [2, 3, 10] gives a total value of 10
# Expected output: 10

# Test Case 3
events3 = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
k3 = 3
# Available events: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
# Maximize the total value with at most 3 events
# Selecting events [2, 2, 2], [3, 3, 3], and [4, 4, 4] gives a total value of 9
# Expected output: 9

solution = Solution()
print(solution.maxValue(events1, k1))
print(solution.maxValue(events2, k2))
print(solution.maxValue(events3, k3))

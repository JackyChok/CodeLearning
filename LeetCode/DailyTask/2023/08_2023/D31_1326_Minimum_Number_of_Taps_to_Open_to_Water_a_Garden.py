class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        max_range = [0] * (n + 1)

        for i in range(len(ranges)):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_range[left] = max(max_range[left], right)
        
        end = farthest = taps = 0
        i = 0

        while end < n:
            while i <= end:
                farthest = max(farthest, max_range[i])
                i += 1
            
            if farthest <= end:
                return -1
            
            end = farthest
            taps += 1
        
        return taps
    
# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    n1 = 5
    ranges1 = [3,4,1,1,0,0]
    result1 = solution.minTaps(n1, ranges1)
    print("Test Case 1: Tap =", result1)  # Output: 1
    
    n2 = 3
    ranges2 = [0,0,0,0]
    result2 = solution.minTaps(n2, ranges2)
    print("Test Case 2: Tap =", result2)  # Output: -1

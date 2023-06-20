class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Sliding Window Method
        avgs = [-1]*len(nums)

        left, currWinSum, diameter = 0, 0, 2*k+1
        for right in range(len(nums)):
            currWinSum += nums[right]
            if (right-left+1 >= diameter):
                avgs[k+left] = currWinSum//diameter
                currWinSum -= nums[left]
                left += 1
        return avgs
    
# Test Case 1
nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
print(Solution().getAverages(nums, k))

# Test Case 2
nums = [100000]
k = 0
print(Solution().getAverages(nums, k))

# Test Case 3
nums = [8]
k = 100000
print(Solution().getAverages(nums, k))
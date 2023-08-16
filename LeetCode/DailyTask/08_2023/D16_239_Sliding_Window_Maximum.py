import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_list = []
        
        #base_case
        if len(nums) == 0:
            return max_list
        if k == 0:
            return nums
        
        #create deque
        d = collections.deque()
        
        
        # Iterating k-sized window-wise from left to right
        l = 0
        for r in range(len(nums)):
            
            #STEP1 : Pop all elements lower than current element in deque
            while d and nums[d[-1]] < nums[r]:     
                    d.pop()
            
            #STEP2 : Push current element to deque
            d.append(r)
        
            #STEP3 : If left-most element in deque is outside window - Remove it!
            if l > d[0]:
                d.popleft()
                
            #STEP4 : In last step before changing window, add left most element to output list and shift the window to right
            if r+1 >= k : 
                max_list.append(nums[d[0]])
                l += 1
        
        return max_list

# Test Case
solution = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = solution.maxSlidingWindow(nums, k)
print(result)  # Output: [3, 3, 5, 5, 6, 7]


nums = [1]
k = 1
result = solution.maxSlidingWindow(nums, k)
print(result)  # Output: [1]

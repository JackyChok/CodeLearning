class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def sum_cost(l):
            total_cost = 0
            for i, x in enumerate(nums):
                total_cost += abs(l-x) * cost[i]
            return total_cost

        left = min(nums)
        right = max(nums) + 1
        mid = (left+right)//2

        while left < right:
            if sum_cost(mid) < sum_cost(mid+1):
                right = mid
            else:
                left = mid + 1
            mid = (left+right)//2
        return sum_cost(left)

# Test Case 1
nums = [1, 3, 5, 2]
cost = [2, 3, 1, 14]
print(Solution().minCost(nums, cost))

# Test Case 2
nums = [2, 2, 2, 2, 2]
cost = [4, 2, 8, 1, 3]
print(Solution().minCost(nums, cost))

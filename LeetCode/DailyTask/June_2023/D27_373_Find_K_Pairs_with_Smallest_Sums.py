import heapq;

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        res = []
        if not nums1 or not nums2:
            return res
        # add init pairs (sum, nums1[i], nums2[0], ids of nums2)
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, [nums1[i]+nums2[0], nums1[i], nums2[0], 0])  # 0 is the index of nums2

        for i in range(min(k, len(nums1)*len(nums2))):
            cur = heapq.heappop(heap)
            res.append([cur[1], cur[2]])
            
            if cur[3] < len(nums2)-1:  # cur[3] is the idx of nums2: still at least one elem after num2 in array nums2
                idx = cur[3] + 1
                heapq.heappush(heap, [cur[1]+nums2[idx], cur[1], nums2[idx], idx])
                
        return res
    
solution = Solution()

# Test Case 1
nums1_1 = [1, 7, 11]
nums2_1 = [2, 4, 6]
k_1 = 3
output_1 = solution.kSmallestPairs(nums1_1, nums2_1, k_1)
print(output_1)  # Output: [[1, 2], [1, 4], [1, 6]]

# Test Case 2
nums1_2 = [1, 1, 2]
nums2_2 = [1, 2, 3]
k_2 = 2
output_2 = solution.kSmallestPairs(nums1_2, nums2_2, k_2)
print(output_2)  # Output: [[1, 1], [1, 2]]

# Test Case 3
nums1_3 = [1, 2]
nums2_3 = [3]
k_3 = 3
output_3 = solution.kSmallestPairs(nums1_3, nums2_3, k_3)
print(output_3)  # Output: [[1, 3], [2, 3]]

import heapq;

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        n = len(costs)
        cand_heap = [] # Heap of candidates; hp elem (cost, inx)
        
        # remaining elems bounds
        left_bound, right_bound = candidates, n-candidates-1
        
        # add left candidates
        for i in range(candidates):
            heapq.heappush(cand_heap, (costs[i], i))
        
        # add right candidates, (exclude already taken from left)
        for i in reversed(range(n-candidates, n)):
            if i < left_bound:
                break
            heapq.heappush(cand_heap, (costs[i], i))
        
        total_cost = 0
        for _ in range(k):
            cost, inx = heapq.heappop(cand_heap)
            total_cost += cost
            if left_bound <= right_bound: # if there are remaining elements
                if inx < left_bound: # if cur elem was from left, replenish from left
                    heapq.heappush(cand_heap, (costs[left_bound], left_bound))
                    left_bound += 1
                elif inx > right_bound: # if cur elem was from right, replenish from right
                    heapq.heappush(cand_heap, (costs[right_bound], right_bound))
                    right_bound -= 1
        return total_cost   
    
# Test Case 1
costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
print(Solution().totalCost(costs, k, candidates))

# Test Case 2
costs = [1, 2, 4, 1]
k = 3
candidates = 3
print(Solution().totalCost(costs, k, candidates))    
class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        min_unfairness = float('inf')
        dist = [0] * k

        def backtrack(i, min_unfairness, dist):
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(dist))
                return min_unfairness
            
            if min_unfairness <= max(dist):
                return min_unfairness

            for j in range(k):
                dist[j] += cookies[i]
                min_unfairness = backtrack(i+1, min_unfairness, dist)
                dist[j] -= cookies[i]
        
            return min_unfairness
        
        return backtrack(0, min_unfairness, dist)


# Test Case 1
cookies = [8,15,10,20,8]
k = 2
print(Solution().distributeCookies(cookies, k)) # Output: 31

# Test Case 2
cookies = [6,1,3,2,2,4,1,2]
k = 3
print(Solution().distributeCookies(cookies, k)) # Output: 7
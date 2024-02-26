class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.helper(1, n, k, [], ans)
        return ans
    
    def helper(self, start, n, k, sub, ans):
        if k == 0:
            ans.append(sub[:])
            return
        for i in range(start, n - k + 2):
            sub.append(i)
            self.helper(i + 1, n, k - 1, sub, ans)
            sub.pop()

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1, k1 = 4, 2
    print(solution.combine(n1, k1))
    # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    # Test Case 2
    n2, k2 = 1, 1
    print(solution.combine(n2, k2))
    # Output: [[1]]

    # Test Case 3
    n3, k3 = 0, 0
    print(solution.combine(n3, k3))
    # Output: [[]]

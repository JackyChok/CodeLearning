# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = { 0 : [], 1 : [TreeNode()] } # map n : list of FBT

        # ret the list of fbt with n nodes
        def backtrack(n):
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n): # 0 - (n-1)
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res
        return backtrack(n)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def allPossibleFBT(self, n):
        dp = {0: [], 1: [TreeNode()]}  # map n : list of FBT

        # ret the list of fbt with n nodes
        def backtrack(n):
            if n in dp:
                return dp[n]

            res = []
            for l in range(n):  # 0 - (n-1)
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res
        # Answer
        # return backtrack(n)
        return [self.tree_to_list(tree) for tree in backtrack(n)]

    # Helper function to convert TreeNode to list representation
    def tree_to_list(self, root):
        if not root:
            return None
        return [root.val, self.tree_to_list(root.left), self.tree_to_list(root.right)]

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    n1 = 7
    result1 = solution.allPossibleFBT(n1)
    print("Test case 1:")
    for tree in result1:
        print(tree)
    
    #Answer
    [0, [0, None, None], [0, [0, None, None], [0, [0, None, None], [0, None, None]]]]
    [0, [0, None, None], [0, [0, [0, None, None], [0, None, None]], [0, None, None]]]
    [0, [0, [0, None, None], [0, None, None]], [0, [0, None, None], [0, None, None]]]
    [0, [0, [0, None, None], [0, [0, None, None], [0, None, None]]], [0, None, None]]
    [0, [0, [0, [0, None, None], [0, None, None]], [0, None, None]], [0, None, None]]

    # Test case 2
    n2 = 3
    result2 = solution.allPossibleFBT(n2)
    print("Test case 2:")
    for tree in result2:
        print(tree)
    
    # Answer
    [0, [0, None, None], [0, None, None]]

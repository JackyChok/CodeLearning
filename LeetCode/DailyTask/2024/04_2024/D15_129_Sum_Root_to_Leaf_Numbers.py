from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur):
            if not root: return 0
            # Calculate the current number by multiplying the current number by 10 and adding the value of the current node
            cur = cur * 10 + root.val
            # If the current node is a leaf, return the current number
            if not root.left and not root.right:
                return cur
            # Recursively calculate the sum of root-to-leaf numbers for the left and right subtrees
            return dfs(root.left, cur) + dfs(root.right, cur)
        
        # Start the DFS traversal from the root with an initial current number of 0
        return dfs(root, 0)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1: Expected output: 25 (12 + 13)
    print(solution.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
    # Example 2: Expected output: 1026 (495 + 491 + 40)
    print(solution.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))

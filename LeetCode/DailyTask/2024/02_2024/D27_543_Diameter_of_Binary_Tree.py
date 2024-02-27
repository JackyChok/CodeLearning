# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            diameter[0] = max(diameter[0], left + right)
            
            return max(left, right) + 1
        
        helper(root)
        return diameter[0]

# Test cases
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root2 = TreeNode(1)
root2.left = TreeNode(2)

print(Solution().diameterOfBinaryTree(root1))  # Output: 3
print(Solution().diameterOfBinaryTree(root2))  # Output: 1

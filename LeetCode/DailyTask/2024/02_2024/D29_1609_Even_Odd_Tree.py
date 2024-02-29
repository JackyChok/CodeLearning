# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, 0))

        while q:
            prev = None
            for _ in range(len(q)):
                node, level = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev and prev >= node.val:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                    if prev and prev <= node.val:
                        return False
                
                prev = node.val

                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))

        return True

# Test cases
root1 = TreeNode(1)
root1.left = TreeNode(10)
root1.right = TreeNode(4)
root1.left.left = TreeNode(3)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(9)
root1.right.left.left = TreeNode(8)
root1.right.left.right = TreeNode(6)
root1.right.right.left = TreeNode(2)

root2 = TreeNode(5)
root2.left = TreeNode(4)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(7)

root3 = TreeNode(5)
root3.left = TreeNode(9)
root3.right = TreeNode(1)
root3.left.left = TreeNode(3)
root3.left.right = TreeNode(5)
root3.right.right = TreeNode(7)

print(Solution().isEvenOddTree(root1))  # Output: True
print(Solution().isEvenOddTree(root2))  # Output: False
print(Solution().isEvenOddTree(root3))  # Output: False

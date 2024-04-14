from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Initialize a deque (double-ended queue) for BFS traversal and a variable for the sum
        q, ans = deque([(root, False)]), 0
        # Continue BFS until the queue is empty
        while q:
            # Pop the leftmost node from the queue and check if it's a left leaf
            cur, isLeft = q.popleft()
            # If the current node is a left leaf, add its value to the sum
            if not cur.left and not cur.right and isLeft:
                ans = ans + cur.val
            # Add the right child to the queue if it exists
            if cur.right:
                q.append((cur.right, False))
            # Add the left child to the queue if it exists, marking it as a left child
            if cur.left: 
                q.append((cur.left, True))
        # Return the sum of left leaves
        return ans

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1: Expected output: 24 (9 + 15)
    print(solution.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    # Example 2: Expected output: 0 (no left leaves)
    print(solution.sumOfLeftLeaves(TreeNode(1)))

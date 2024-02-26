import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # DFS
    def minDepth_DFS(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth_DFS(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth_DFS(root.right)
        return 1 + min(self.minDepth_DFS(root.left), self.minDepth_DFS(root.right))

    # BFS
    def minDepth_BFS(self, root):
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))

# Create an instance of the Solution class
solution = Solution()

# Test case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.minDepth_DFS(root))  # Output: 2
print(solution.minDepth_BFS(root))  # Output: 2

# Test case 2
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print(solution.minDepth_DFS(root))  # Output: 5
print(solution.minDepth_BFS(root))  # Output: 5

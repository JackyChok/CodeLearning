# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root):
        counts = {}
        max_count = 0
        modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            nonlocal max_count, modes

            counts[node.val] = 1 + counts.get(node.val, 0)
            
            if counts[node.val] > max_count:
                max_count = counts[node.val]
                modes = [node.val]
            elif counts[node.val] == max_count:
                modes.append(node.val)

            inorder(node.right)

        inorder(root)

        return modes

# Test case
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    solution = Solution()
    result = solution.findMode(root)
    print("Result 1:", result)

    root = TreeNode(0)

    solution = Solution()
    result = solution.findMode(root)
    print("Result 2:", result)

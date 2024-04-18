# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def add(self, root, val, depth, curr):
        if not root:
            return None

        if curr == depth - 1:
            # Save the current left and right children
            lTemp = root.left
            rTemp = root.right

            # Create new nodes with value val and connect them to the current node
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = lTemp
            root.right.right = rTemp

            return root

        # Recursively add nodes at the specified depth
        root.left = self.add(root.left, val, depth, curr + 1)
        root.right = self.add(root.right, val, depth, curr + 1)

        return root

    def addOneRow(self, root, val, depth):
        if depth == 1:
            # If depth is 1, add a new root with the existing tree as its left child
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        # Call the add method to add nodes at the specified depth
        return self.add(root, val, depth, 1)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1: Expected output: [4,1,1,2,null,null,6,3,1,5]
    print(solution.addOneRow(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5))), 1, 2))
    # Example 2: Expected output: [4,2,null,3,1]
    print(solution.addOneRow(TreeNode(4, TreeNode(2, None, TreeNode(3)), None), 1, 3))

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Helper function to perform DFS
        def dfs(node, path, smallest):
            if not node:
                return
            
            # Append current node's character to the path
            path.append(chr(node.val + ord('a')))
            
            # If it's a leaf node, reverse the path and compare
            if not node.left and not node.right:
                current_string = ''.join(path[::-1])  # reverse path to get string
                smallest[0] = min(smallest[0], current_string)
            
            # Recursively traverse left and right subtrees
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)
            
            # Backtrack: remove the current node's character from the path
            path.pop()
        
        # Initialize smallest string as a large value
        smallest = [chr(ord('z') + 1)]  # Store smallest string found
        
        # Start DFS from the root with an empty path
        dfs(root, [], smallest)
        
        return smallest[0]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1: Expected output: "dba"
    print(solution.smallestFromLeaf(TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))))
    # Example 2: Expected output: "adz"
    print(solution.smallestFromLeaf(TreeNode(25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(0, TreeNode(3), TreeNode(2)))))
    # Example 3: Expected output: "abc"
    print(solution.smallestFromLeaf(TreeNode(2, TreeNode(2, None, TreeNode(1)), TreeNode(1, None, TreeNode(0)))))

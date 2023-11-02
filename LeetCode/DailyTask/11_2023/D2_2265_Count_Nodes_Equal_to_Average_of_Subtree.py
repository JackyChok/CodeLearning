# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def postorder(node):
            if not node:
                return (0, 0)  # sum, number of nodes

            left = postorder(node.left)
            right = postorder(node.right)

            nonlocal res

            total_sum = left[0] + right[0] + node.val
            total_count = 1 + left[1] + right[1]
            res += (node.val == total_sum // total_count)

            return (total_sum, total_count)

        postorder(root)

        return res

def test_averageOfSubtree():
    solution = Solution()

    # Example 1:
    # Create the tree [4,8,5,0,1,null,6]
    root1 = TreeNode(4)
    root1.left = TreeNode(8)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(1)
    root1.right.right = TreeNode(6)
    # The expected result is 5
    result1 = solution.averageOfSubtree(root1)
    print("Result for Example 1:", result1)

    # Example 2:
    # Create a single-node tree [1]
    root2 = TreeNode(1)
    # The expected result is 1 as the only node is its own average.
    result2 = solution.averageOfSubtree(root2)
    print("Result for Example 2:", result2)

    # Add more test cases as needed

if __name__ == "__main__":
    test_averageOfSubtree()

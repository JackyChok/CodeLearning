# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        graph = {}
        self.buildGraph(root, None, graph)

        queue = [(target, 0)]
        visited = set([target])
        res = []

        while queue:
            node, dist = queue.pop(0)

            if dist == k:
                res.append(node.val)

            if dist > k:
                break

            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, dist + 1))
        
        return res

    def buildGraph(self, node, parent, graph):
        if not node:
            return

        if node not in graph:
            graph[node] = []
        
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        
        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)


# Create an instance of the Solution class
solution = Solution()

# Test case 1
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
target = root.left
k = 2
print(solution.distanceK(root, target, k))  # Output: [7, 4, 1]

# Test case 2
root = TreeNode(1)
target = root
k = 1
print(solution.distanceK(root, target, k))  # Output: []


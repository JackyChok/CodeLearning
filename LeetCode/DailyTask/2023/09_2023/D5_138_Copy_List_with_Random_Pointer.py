# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]

def convertToLists(head):
    result = []
    cur = head
    while cur:
        next_index = None if cur.next is None else cur.next.val
        random_index = None if cur.random is None else cur.random.val
        result.append([cur.val, next_index, random_index])
        cur = cur.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    result1 = solution.copyRandomList(node1)
    result_list1 = convertToLists(result1)

    # Test case 2
    node6 = Node(1)
    node7 = Node(2)

    node6.next = node7
    node6.random = node7
    node7.random = node7

    result2 = solution.copyRandomList(node6)
    result_list2 = convertToLists(result2)

    # Test case 3
    node8 = Node(3)
    node9 = Node(3)
    node10 = Node(3)

    node8.next = node9
    node9.next = node10

    result3 = solution.copyRandomList(node8)
    result_list3 = convertToLists(result3)

    # Print results
    print("Test Case 1: Result", result_list1)
    print("Test Case 2: Result", result_list2)
    print("Test Case 3: Result", result_list3)

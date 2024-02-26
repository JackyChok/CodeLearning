# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False

# Test cases
def test_hasCycle():
    # Test case 1: Cycle exists
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create a cycle
    solution = Solution()
    assert solution.hasCycle(node1) == True

    # Test case 2: No cycle
    node5 = ListNode(1)
    node6 = ListNode(2)
    node5.next = node6
    assert solution.hasCycle(node5) == False

    # Test case 3: Single node (no cycle)
    node7 = ListNode(1)
    assert solution.hasCycle(node7) == False

    # Test case 4: Single node (cycle)
    node8 = ListNode(1)
    node8.next = node8  # Create a cycle
    assert solution.hasCycle(node8) == True

if __name__ == "__main__":
    test_hasCycle()
    print("All test cases passed.")

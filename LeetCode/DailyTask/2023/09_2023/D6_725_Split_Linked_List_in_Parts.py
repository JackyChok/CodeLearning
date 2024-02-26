# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1
        
        base_len, remainder = length // k, length % k
        curr = head
        res = []
        for i in range(k):
            res.append(curr)

            for j in range(base_len - 1 + (1 if remainder else 0)):
                if not curr: break
                curr = curr.next
            remainder -= (1 if remainder else 0)
            if curr:
                curr.next, curr = None, curr.next
        
        return res

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    k1 = 5
    result1 = solution.splitListToParts(node1, k1)

    # Test case 2
    node4 = ListNode(1)
    node5 = ListNode(2)
    node6 = ListNode(3)
    node7 = ListNode(4)
    node8 = ListNode(5)
    node9 = ListNode(6)
    node10 = ListNode(7)
    node11 = ListNode(8)
    node12 = ListNode(9)
    node13 = ListNode(10)
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    node10.next = node11
    node11.next = node12
    node12.next = node13

    k2 = 3
    result2 = solution.splitListToParts(node4, k2)

    # Print results
    print("Test Case 1: Result")
    for part in result1:
        curr = part
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    print("Test Case 2: Result")
    for part in result2:
        curr = part
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

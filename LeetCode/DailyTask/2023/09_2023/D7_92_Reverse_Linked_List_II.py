# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    left1 = 2
    right1 = 4
    result1 = solution.reverseBetween(node1, left1, right1)

    # Test case 2
    node6 = ListNode(5)
    left2 = 1
    right2 = 1
    result2 = solution.reverseBetween(node6, left2, right2)

    # Test case 3
    node7 = ListNode(1)
    left3 = 1
    right3 = 1
    result3 = solution.reverseBetween(node7, left3, right3)

    # Print results
    print("Test Case 1: Result")
    curr = result1
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

    print("Test Case 2: Result")
    curr = result2
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

    print("Test Case 3: Result")
    curr = result3
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

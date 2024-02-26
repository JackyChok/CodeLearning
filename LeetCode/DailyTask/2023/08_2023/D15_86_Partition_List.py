# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        slist, blist = ListNode(), ListNode()
        small, big = slist, blist # dummy lists

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next

        small.next = blist.next
        big.next = None # prevent linked list circle

        return slist.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

def run_tests():
    sol = Solution()

    # Test case 1
    head1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    x1 = 3
    result1 = sol.partition(head1, x1)
    print_linked_list(result1)  # Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None

    # Test case 2
    head2 = ListNode(2, ListNode(1))
    x2 = 2
    result2 = sol.partition(head2, x2)
    print_linked_list(result2)  # Output: 1 -> 2 -> None

if __name__ == "__main__":
    run_tests()

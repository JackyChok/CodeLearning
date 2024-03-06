from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

# Test cases
def create_linked_list(lst, pos):
    dummy = ListNode(0)
    curr = dummy
    cycle_node = None
    for i, val in enumerate(lst):
        curr.next = ListNode(val)
        curr = curr.next
        if i == pos:
            cycle_node = curr
    if pos != -1:
        curr.next = cycle_node
    return dummy.next

head1 = create_linked_list([3, 2, 0, -4], 1)
head2 = create_linked_list([1, 2], 0)
head3 = create_linked_list([1], -1)

print(Solution().hasCycle(head1))  # Output: True
print(Solution().hasCycle(head2))  # Output: True
print(Solution().hasCycle(head3))  # Output: False

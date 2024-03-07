from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Test cases
def create_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

head1 = create_linked_list([1, 2, 3, 4, 5])
head2 = create_linked_list([1, 2, 3, 4, 5, 6])

print(Solution().middleNode(head1).val)  # Output: 3
print(Solution().middleNode(head2).val)  # Output: 4

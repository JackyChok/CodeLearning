# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr, length = head, 0
        while ptr:
            ptr, length = ptr.next, length + 1
        if length == n: 
            return head.next
        ptr = head
        for i in range(1, length - n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head

# Test cases
def list_to_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

head1 = list_to_linked_list([1, 2, 3, 4, 5])
head2 = list_to_linked_list([1])
head3 = list_to_linked_list([1, 2])

result1 = Solution().removeNthFromEnd(head1, 2)
result2 = Solution().removeNthFromEnd(head2, 1)
result3 = Solution().removeNthFromEnd(head3, 1)

print(linked_list_to_list(result1))  # Output: [1, 2, 3, 5]
print(linked_list_to_list(result2))  # Output: []
print(linked_list_to_list(result3))  # Output: [1]

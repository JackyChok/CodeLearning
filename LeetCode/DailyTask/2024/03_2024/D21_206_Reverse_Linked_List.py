from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev

# Helper function to print the linked list
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Test cases
sol = Solution()

# Example 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reversed_head = sol.reverseList(head)
print_list(reversed_head)  # Output: 5 4 3 2 1

# Example 2
head = ListNode(1)
head.next = ListNode(2)

reversed_head = sol.reverseList(head)
print_list(reversed_head)  # Output: 2 1

# Example 3
head = None

reversed_head = sol.reverseList(head)
print_list(reversed_head)  # Output: (empty)

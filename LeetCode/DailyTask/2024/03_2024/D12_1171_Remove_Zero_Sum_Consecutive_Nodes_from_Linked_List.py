# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next

        return dummy.next

# Helper function to create linked list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Test cases
head1 = create_linked_list([1, 2, -3, 3, 1])
head2 = create_linked_list([1, 2, 3, -3, 4])
head3 = create_linked_list([1, 2, 3, -3, -2])

sol = Solution()
result1 = sol.removeZeroSumSublists(head1)  # Output: 3 -> 1
result2 = sol.removeZeroSumSublists(head2)  # Output: 1 -> 2 -> 4
result3 = sol.removeZeroSumSublists(head3)  # Output: 1 -> 2 -> 3 -> -3 -> -2

# Function to convert linked list to list for display
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Display results
print(linked_list_to_list(result1))
print(linked_list_to_list(result2))
print(linked_list_to_list(result3))

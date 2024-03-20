# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        
        qtr = ptr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        
        return list1

# Test cases
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Example 1
list1 = ListNode(10)
list1.next = ListNode(1)
list1.next.next = ListNode(13)
list1.next.next.next = ListNode(6)
list1.next.next.next.next = ListNode(9)
list1.next.next.next.next.next = ListNode(5)

list2 = ListNode(1000000)
list2.next = ListNode(1000001)
list2.next.next = ListNode(1000002)

sol = Solution()
result = sol.mergeInBetween(list1, 3, 4, list2)
print_list(result)  # Output: 10 1 13 1000000 1000001 1000002 6 9 5

# Example 2
list1 = ListNode(0)
list1.next = ListNode(1)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(4)
list1.next.next.next.next.next = ListNode(5)
list1.next.next.next.next.next.next = ListNode(6)

list2 = ListNode(1000000)
list2.next = ListNode(1000001)
list2.next.next = ListNode(1000002)
list2.next.next.next = ListNode(1000003)
list2.next.next.next.next = ListNode(1000004)

result = sol.mergeInBetween(list1, 2, 5, list2)
print_list(result)  # Output: 0 1 1000000 1000001 1000002 1000003 1000004 6

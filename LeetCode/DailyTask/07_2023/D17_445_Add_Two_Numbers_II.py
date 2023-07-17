# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        res = None

        while stack1 or stack2 or carry:
            sum_ = carry

            if stack1:
                sum_ += stack1.pop()
            if stack2:
                sum_ += stack2.pop()

            node = ListNode(sum_ % 10)
            node.next = res
            res = node

            carry = sum_ // 10

        return res


# Test Cases
# Test Case 1
l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
# Expected output: ListNode(7 -> 8 -> 0 -> 7)
current = result
while current:
    print(current.val, end=" ")
    current = current.next
print()

# Test Case 2
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
# Expected output: ListNode(7 -> 0 -> 8)
current = result
while current:
    print(current.val, end=" ")
    current = current.next
print()

# Test Case 3
l1 = ListNode(0)

l2 = ListNode(0)

result = Solution().addTwoNumbers(l1, l2)
# Expected output: ListNode(0)
current = result
while current:
    print(current.val, end=" ")
    current = current.next
print()

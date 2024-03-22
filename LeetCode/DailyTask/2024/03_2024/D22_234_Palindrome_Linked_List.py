from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def check(head):
            if head is None:
                return True
            res = check(head.next) and (self.temp.val == head.val)
            self.temp = self.temp.next
            return res
        
        self.temp = head
        return check(head)

# Test the solution
def main():
    # Create a linked list: 1 -> 2 -> 2 -> 1
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Check if the linked list is a palindrome
    solution = Solution()
    result = solution.isPalindrome(node1)
    print(f"Is the linked list a palindrome? {result}")

if __name__ == "__main__":
    main()

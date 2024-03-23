from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr, Iter = [], head
        while Iter:
            arr.append(Iter)
            Iter = Iter.next
        
        L, R = 1, len(arr)-1
        for i in range(len(arr)):
            if i & 1:
                head.next = arr[L]
                L += 1
            else:
                head.next = arr[R]
                R -= 1
            head = head.next
        head.next = None

# Test the solution
def main():
    # Create a linked list: 1 -> 2 -> 3 -> 4
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Reorder the linked list
    solution = Solution()
    solution.reorderList(node1)

    # Print the reordered linked list
    while node1:
        print(node1.val, end=" -> ")
        node1 = node1.next
    print("None")

if __name__ == "__main__":
    main()

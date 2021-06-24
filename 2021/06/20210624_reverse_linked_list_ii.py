"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Init
        left_prev = None
        cur = head
        left_ptr = cur
        count = 1

        # Locate the left position, where start to reverse.
        while count < left:
            left_prev = cur
            cur = cur.next
            count += 1
        left_ptr = cur

        # Reverse the linked list til the right position.
        prev = None
        while count <= right:
            curr = cur
            cur = cur.next
            curr.next = prev
            prev = curr
            count += 1

        # Linked the all linked list.
        if left_prev:
            left_prev.next = prev
        left_ptr.next = cur

        # Return the head of the reversed linked list.
        if left_prev:
            return head
        else:
            return prev


if __name__ == '__main__':
    solution = Solution()

    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head = solution.reverseBetween(head, 2, 4)

    while head:
        print(head.val)
        head = head.next

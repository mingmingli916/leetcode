"""
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base case
        if head is None:
            return head

        # compute the length of the list
        length = 0
        cur = head
        tail = None
        while cur:
            length += 1
            tail = cur
            cur = cur.next

        # compute the real rotate times
        k = k % length
        # compute the times to iterate
        k = (length - k) % length

        if k == 0:
            return head

        # find the new head and new tail
        new_head = head
        new_tail = tail
        for _ in range(k):
            new_tail = new_head
            new_head = new_head.next

        # link
        new_tail.next = None
        tail.next = head

        return new_head

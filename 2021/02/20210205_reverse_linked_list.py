# coding=utf8
"""
@project: leetcode
@file: 20210205_reverse_linked_list
@author: mike
@time: 2021/2/5
 
@function:

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(prev, head):
            # base case
            if not head or not head.next:
                return head

            cur = head
            head = helper(head, head.next)
            cur.next.next = cur
            cur.next = prev

            return head

        return helper(None, head)

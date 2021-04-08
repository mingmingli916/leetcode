#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210209_merge_two_sorted_lists
@author: mike
@time: 2021/2/9
 
@function:
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.



Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            head = l1
            tail = l1
            l1 = l1.next
        else:
            head = l2
            tail = l2
            l2 = l2.next

        def helper(l1, l2, tail, head):
            # Base case
            if l1 is None:
                tail.next = l2
                return head
            if l2 is None:
                tail.next = l1
                return head

            # Recursion relationship
            if l1.val <= l2.va:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
                return helper(l1, l2, tail, head)
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
                return helper(l1, l2, tail, head)

        return helper(l1, l2, tail, head)

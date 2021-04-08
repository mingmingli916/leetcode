# coding=utf8
"""
@project: leetcode
@file: 20210204_swap_nodes_in_pairs
@author: mike
@time: 2021/2/4
 
@function:

Swap Nodes in Pairs

Solution
Given a linked list, swap every two adjacent nodes and return its head.



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

Follow up:
Can you solve the problem without modifying the values in the list's nodes?
(i.e., Only nodes themselves may be changed.)
 """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        if not (head and head.next):
            return head

        tmp = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(tmp)
        return head

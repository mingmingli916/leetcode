"""
  Binary Tree Level Order Traversal

Solution
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List
import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder_queue(self, root: TreeNode) -> List[List[int]]:
        # base case
        if root is None:
            return None

        # init
        # outer list and queue
        lst = []
        que = queue.Queue()
        # put the root node into the queue
        q = queue.Queue()
        q.put(root)
        que.put(q)

        # traverse
        while not que.empty():
            q = que.get()
            # inner lst and queue
            inner_lst = []
            inner_q = queue.Queue()

            while not q.empty():
                node = q.get()
                inner_lst.append(node.val)
                if node.left:
                    inner_q.put(node.left)
                if node.right:
                    inner_q.put(node.right)

            lst.append(inner_lst)
            if not inner_q.empty():
                que.put(inner_q)

        return lst

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # base case
        if root is None:
            return None

        lst = []

        def helper(node, level):
            if len(lst) == level:
                lst.append([])

            lst[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return lst

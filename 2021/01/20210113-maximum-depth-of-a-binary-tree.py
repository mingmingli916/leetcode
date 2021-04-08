"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self):
    #     self.answer = 0
    #
    # def maxDepth(self, root: TreeNode) -> int:
    #     self.answer = 0
    #     self.maxHelper(root, 1)
    #     return self.answer
    #
    # def maxHelper(self, node: TreeNode, depth: int):
    #     if node is None:
    #         return 0
    #     if node.left is None and node.right is None:
    #         self.answer = max(self.answer, depth)
    #     self.maxHelper(node.left, depth + 1)
    #     self.maxHelper(node.right, depth + 1)
    def maxDepth(self, root: TreeNode) -> int:
        # base case
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

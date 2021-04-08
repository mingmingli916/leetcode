"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        length = len(preorder)
        index = 0
        # construct a map to reduce search time
        inorder_indices = {inorder[i]: i for i in range(length)}

        def build_helper(start, end):
            # base case
            if start > end:
                return None

            nonlocal index

            # root node
            root_val = preorder[index]
            root = TreeNode(root_val)

            # recursive call
            index += 1
            inorder_index = inorder_indices[root_val]
            root.left = build_helper(start, inorder_index - 1)
            root.right = build_helper(inorder_index + 1, end)

            return root

        return build_helper(0, length - 1)

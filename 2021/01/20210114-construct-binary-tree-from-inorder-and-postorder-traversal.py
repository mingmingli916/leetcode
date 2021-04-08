"""
Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTreeCopy(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        root_val = postorder[-1]
        left_inorder = inorder[:inorder.index(root_val)]
        right_inorder = inorder[inorder.index(root_val):]
        right_inorder = right_inorder[1:]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]
        root = TreeNode(root_val)
        root.left = self.buildTreeCopy(left_inorder, left_postorder)
        root.right = self.buildTreeCopy(right_inorder, right_postorder)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        length = len(inorder)
        index = length - 1
        # to reduce search time
        inorder_indices = {inorder[i]: i for i in range(length)}

        def buildTreeHelper(start, end):
            nonlocal index
            if start > end:
                return None

            # construct the root node
            root_val = postorder[index]
            node = TreeNode(root_val)
            # induce the global index
            index -= 1

            # construct the child nodes
            inorder_index = inorder_indices[root_val]
            node.right = buildTreeHelper(inorder_index + 1, end)
            node.left = buildTreeHelper(start, inorder_index - 1)

            return node

        return buildTreeHelper(0, length - 1)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    root = sol.buildTree(inorder, postorder)
    print(root)

# note:
# 1. Use hash map to reduce the search time
# 2. Use index to reduce the list copy time

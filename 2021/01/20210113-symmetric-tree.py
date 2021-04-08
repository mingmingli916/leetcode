"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.answer = True

    def isSymmetric(self, root: TreeNode) -> bool:
        # base case
        if root is None:
            return True

        self.answer = True
        self.isSymmetricHelper(root, root)
        return self.answer

    def isSymmetricHelper(self, l: TreeNode, r: TreeNode):
        if l.left and r.right:
            self.answer = self.answer and (l.left.val == r.right.val)
        elif l.left:
            self.answer = False
        elif r.right:
            self.answer = False

        if self.answer is False:
            return

        if l.left and r.right:
            self.isSymmetricHelper(l.left, r.right)
        if l.right and r.left:
            self.isSymmetricHelper(l.right, r.left)

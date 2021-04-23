"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.check_depth(root) == -1:
            return False
        return True

    def check_depth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left = self.check_depth(node.left)
        # No more checking is needed
        if left == -1:
            return -1
        right = self.check_depth(node.right)
        # No more checking is needed
        if right == -1:
            return -1
        dif = abs(left - right)
        # No more checking is needed
        if dif > 1:
            return -1
        return 1 + max(left, right)

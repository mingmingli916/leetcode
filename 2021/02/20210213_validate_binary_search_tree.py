#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210213_validate_binary_search_tree
@author: mike
@time: 2021/2/13
 
@function:
Validate Binary Search Tree

Solution
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NotValidBSTError(Exception): pass


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def divide_and_conquer(root):
            # Base case
            if root is None:
                return True, None, None

            left_bool, left_min, left_max = divide_and_conquer(root.left)
            right_bool, right_min, right_max = divide_and_conquer(root.right)
            return merge(root, left_bool, left_min, left_max, right_bool, right_min, right_max)

        def merge(root, left_bool, left_min, left_max, right_bool, right_min, right_max):
            if not (left_bool and right_bool):
                raise NotValidBSTError

            if left_max and left_max >= root.val:
                raise NotValidBSTError
            if right_min and right_min <= root.val:
                raise NotValidBSTError

            if left_min is None and right_max is None:
                return True, root.val, root.val
            elif left_min is None:
                return True, root.val, right_max
            elif right_max is None:
                return True, left_min, root.val
            else:
                return True, left_min, right_max

        try:
            divide_and_conquer(root)
            return True
        except NotValidBSTError:
            return False

    def isValidBST2(self, root: TreeNode) -> bool:
        def helper(root, minimum, maximum):
            # Base case
            if not root:
                return True

            if root.val >= maximum or root.val <= minimum:
                return False

            return helper(root.left, minimum, root.val) and helper(root.right, root.val, maximum)

        return helper(root, -float('inf'), float('inf'))


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    result = solution.isValidBST2(root)
    print(result)

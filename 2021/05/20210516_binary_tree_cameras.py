"""
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.



Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    The answer is wrong.
    """

    def minCameraCover(self, root: TreeNode) -> int:
        def helper(node: TreeNode, minimum: List[int]):
            if node is None:
                return

            if node.val == 1:
                minimum[0] += 1
                if node.left:
                    node.left.val = -1
                if node.right:
                    node.right.val = -1

            if node.val == -1:
                if node.left:
                    node.left.val = 1
                if node.right:
                    node.right.val = 1

            helper(node.left, minimum)
            helper(node.right, minimum)

        minimum1 = [0]
        root.val = 1
        helper(root, minimum1)

        minimum2 = [0]
        root.val = -1
        helper(root, minimum2)
        return min(minimum1[0], minimum2[0])


class Solution2:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        We do not install camera on the leaf node, so place camera from bottom.
        -1 represent do not install camera on the node.
        1 represent there is a camera on the node.
        0 represent the node is in the camera field.
        """
        def dfs(node):
            l = r = 0
            # This is the leaf node.
            if node.left is None and node.right is None:
                return -1

            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)

            # If there is no camera on the left or right child node.
            # Install a camera on the current node.
            if l == -1 or r == -1:
                self.count += 1
                return 1

            # There left and right child nodes are in camera field.
            if l == 0 and r == 0:
                return -1

            # There is a camera on the left or right child node.
            # There is no need to install a camera on the current node.
            if l == 1 or r == 1:
                return 0

        self.count = 0
        cameras = dfs(root)

        if cameras == -1:
            self.count += 1
        return self.count


if __name__ == '__main__':
    solution = Solution2()

    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(0)

    minimum = solution.minCameraCover(root)
    print(minimum)

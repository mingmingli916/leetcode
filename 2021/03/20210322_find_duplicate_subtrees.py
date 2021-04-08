"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.



Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""
from typing import List
import collections
import ast


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # Base case
        if not root:
            return '[]'

        # init
        lst = [root.val]
        q = collections.deque([root])

        while q:
            cur = q.popleft()  # current

            # If there is a node in the right
            # the null is needed
            lst.append(None)
            if cur.left:
                q.append(cur.left)
                lst[-1] = cur.left.val

            # If there are node lower level
            # the null is needed
            lst.append(None)
            if cur.right:
                q.append(cur.right)
                lst[-1] = cur.right.val

        # remove the unnecessary null
        while lst and lst[-1] is None:
            lst.pop()

        return str(lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # Base case
        if data == str([]):
            return None

        # init
        lst = ast.literal_eval(data)
        root = TreeNode(lst.pop(0))
        q = collections.deque([root])

        while q:
            cur = q.popleft()
            # There is no need to process None node
            if cur is None:
                continue

            # When there is not elements in lst
            # the node is the leaf node in tree
            # the loop stop
            try:
                val = lst.pop(0)
                # set the left attribute if necessary
                if val is not None:
                    node = TreeNode(val)
                    cur.left = node
                    q.append(node)

                # set the right attribute if necessary
                val = lst.pop(0)
                if val is not None:
                    node = TreeNode(val)
                    cur.right = node
                    q.append(node)

            except Exception:
                break

        return root


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def helper(root, d, dp):
            if root is None:
                return

            key = tuple(self.inorder_traversal(root, dp))
            d[key].append(root)

            helper(root.left, d, dp)
            helper(root.right, d, dp)

        d = collections.defaultdict(list)
        dp = {}
        helper(root, d, dp)

        result = []
        for key in d:
            if len(d[key]) != 1:
                result.append(d[key][0])
        return result

    def inorder_traversal(self, root, dp) -> str:
        # base case
        if root in dp:
            return dp[root]

        if root is None:
            return [None]

        lst = []
        lst.append(root.val)
        lst.extend(self.inorder_traversal(root.left, dp))
        lst.extend(self.inorder_traversal(root.right, dp))

        dp[root] = lst

        return lst

    def findDuplicateSubtrees2(self, root: TreeNode) -> List[TreeNode]:
        dups = []
        d = collections.defaultdict(list)
        self.hash_subtree(root, d, dups)
        return dups

    def hash_subtree(self, node, d, dup):
        left, right = 'null', 'null'
        if node.left:
            left = self.hash_subtree(node.left, d, dup)
        if node.right:
            right = self.hash_subtree(node.right, d, dup)

        node_hash = f'{node.val}-{left}-{right}'

        d[node_hash].append(node)
        if len(d[node_hash]) ==2:
            dup.append(d[node_hash][0])

        return node_hash


if __name__ == '__main__':
    codec = Codec()

    solution = Solution()

    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2

    node3 = TreeNode(4)
    node1.left = node3

    node4 = TreeNode(2)
    node2.left = node4

    node5 = TreeNode(4)
    node2.right = node5

    node6 = TreeNode(4)
    node4.left = node6

    # root = codec.deserialize(str([0, 0, 0, 0, None, None, 0, None, None, None, 0]))

    result = solution.findDuplicateSubtrees2(root)
    print(result)

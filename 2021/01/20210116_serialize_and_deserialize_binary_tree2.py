# coding=utf8
"""
@project: leetcode
@file: 20210116_serialize_and_deserialize_binary_tree
@author: mike
@time: 2021/1/16
 
@function:
"""

"""
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
"""
import collections
import ast


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


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


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    root.right = node1
    node1.left = node2
    node2.left = node4
    node1.right = node3
    node3.left = node5
    node3.right = node6

    ser = Codec()
    deser = Codec()
    lst = ser.serialize(root)

    print(lst)
    ans = deser.deserialize(lst)
    print(ser.serialize(ans))

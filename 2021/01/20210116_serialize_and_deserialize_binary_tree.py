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
import queue
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
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # Base case
        if root is None:
            return str([])

        # init
        lst = []
        qq = queue.Queue()
        q = queue.Queue()
        q.put(root)
        qq.put(q)

        while not qq.empty():
            q = qq.get()
            tmp = queue.Queue()
            while not q.empty():
                node = q.get()
                if node is None:
                    lst.append(None)
                else:
                    lst.append(node.val)
                    tmp.put(node.left)
                    tmp.put(node.right)
            if not tmp.empty():
                qq.put(tmp)

        # remove unnecessary None
        while lst[-1] is None:
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

        level = [root]
        while True:
            tmp_level = []
            try:
                for i in range(len(level)):
                    if lst[2 * i] is not None:
                        node = TreeNode(lst[2 * i])
                        level[i].left = node
                        tmp_level.append(node)
                    if lst[2 * i + 1] is not None:
                        node = TreeNode(lst[2 * i + 1])
                        level[i].right = node
                        tmp_level.append(node)
            except Exception:
                break
            lst = lst[2 * len(level):]
            level = tmp_level

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

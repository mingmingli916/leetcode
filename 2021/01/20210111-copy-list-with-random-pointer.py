"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1)
where random pointer points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.


Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return str(self.val)


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # base case
        if head is None:
            return head

        # copy the interweave the list
        cur = head
        while cur:
            # copy the current node
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = cur.next.next

        # correct the random attribute in new nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # split the interweave list
        # init
        new_head = head.next
        new_cur = head.next
        cur = head

        while cur:
            # build the old list
            cur.next = cur.next.next
            cur = cur.next

            # build the new list
            if new_cur.next:
                new_cur.next = new_cur.next.next
                new_cur = new_cur.next

        return new_head


if __name__ == '__main__':
    head = Node(3)
    node2 = Node(3)
    node3 = Node(3)
    head.next = node2
    node2.next = node3

    node2.random = head

    cur = head
    while cur:
        print('[{},{}]'.format(cur.val, cur.random))
        cur = cur.next

    sol = Solution()
    result = sol.copyRandomList(head)
    while result:
        print('[{},{}]'.format(result.val, result.random))
        result = result.next

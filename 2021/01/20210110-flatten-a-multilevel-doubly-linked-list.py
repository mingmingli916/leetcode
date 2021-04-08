"""
You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure,
as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.



Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []

Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""


# Definition for a Node.

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        lst = []
        cur = self
        while cur:
            lst.append(cur.val)
            cur = cur.next
        return str(lst)


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        cur = head
        while cur:
            if cur.child:
                # recursive call
                child_head = self.flatten(cur.child)

                # init the pointer
                child_tail = child_head
                child_cur = child_head

                # locate child tail
                while child_cur:
                    child_tail = child_cur
                    child_cur = child_cur.next

                # break and connect
                child_tail.next = cur.next
                child_head.prev = cur
                if cur.next:
                    cur.next.prev = child_tail
                cur.next = child_head
                cur.child = None

                # check the next node
                cur = child_tail.next

            else:
                cur = cur.next

        return head


if __name__ == '__main__':
    head = Node(1)
    node2 = Node(2)
    head.next = node2
    node3 = Node(3)
    head.child = node3
    node4 = Node(4)
    node3.next = node4

    solution = Solution()
    result = solution.flatten(head)
    print(result)

# Simplify the problem into sub problems.
# divide and conquer.
# Do not combine all the code into a whole.
# At first, there is infinite loop in my solution.
# I break the problem into sub problem: locate the node and the insert the node.
# After that, the dug disappears and the code became neat.



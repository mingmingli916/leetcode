"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place.
The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # In this case, the linked list does not need change
        if head is None or head.next is None or head.next.next is None:
            return head

        cnode = head.next.next  # current node
        # even queue
        even_p = head.next
        even_last = head.next
        even_last.next = None
        # odd queue
        odd_p = head
        odd_last = head
        odd_last.next = None
        # to determine the odd or even node
        count = 3

        while cnode:
            tmp = cnode
            cnode = cnode.next
            tmp.next = None
            if count % 2 == 0:
                even_last.next = tmp
                even_last = tmp
            else:
                odd_last.next = tmp
                odd_last = tmp

            count += 1

        odd_last.next = even_p
        return odd_p

    def oddEvenList2(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even, even_start = head.next, head.next

        while odd.next and odd.next.next:
            odd.next = even.next
            even.next = odd.next.next

            odd = odd.next
            even = even.next

        odd.next = even_start

        return head


if __name__ == '__main__':
    lst = ListNode(1)
    node2 = ListNode(2)
    lst.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5

    solution = Solution()
    solution.oddEvenList(lst)

    while lst:
        print(lst)
        lst = lst.next

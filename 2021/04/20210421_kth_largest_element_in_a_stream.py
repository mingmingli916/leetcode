"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None, cnt=1):
        self.val = val
        self.left = left
        self.right = right
        self.cnt = cnt

    def __str__(self):
        d = {
            'val': self.val,
            'cnt': self.cnt
        }
        return str(d)


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.root = None
        for num in nums:
            self.root = self.insert(self.root, num)

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)

        def helper(node, k):
            right_cnt = 0
            if node.right is not None:
                right_cnt = node.right.cnt

            kth = right_cnt + 1

            if kth == k:
                return node.val
            elif kth > k:
                return helper(node.right, k)
            else:
                return helper(node.left, k - kth)

        return helper(self.root, self.k)

    def insert(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            left_bst = self.insert(root.left, val)
            root.left = left_bst
        else:
            right_bst = self.insert(root.right, val)
            root.right = right_bst

        root.cnt += 1
        return root


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == '__main__':
    solution = KthLargest(3, [4, 5, 8, 2])
    for i in [3, 5, 10, 9, 4]:
        print(solution.add(i))

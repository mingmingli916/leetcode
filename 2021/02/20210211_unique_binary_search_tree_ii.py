#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210211_unique_binary_search_tree_ii
@author: mike
@time: 2021/2/11
 
@function:
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.



Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 8
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start, end, dp):
            if start > end:
                return [None]
            if (start, end) in dp:
                return dp[start, end]
            res = []
            for rootval in range(start, end + 1):
                left_tree = helper(start, rootval - 1, dp)
                right_tree = helper(rootval + 1, end, dp)
                for i in left_tree:
                    for j in right_tree:
                        root = TreeNode(rootval)
                        root.left = i
                        root.right = j
                        res.append(root)
            dp[start, end] = res
            return res

        return helper(1, n, {})


if __name__ == '__main__':
    import datetime

    n = 4
    solution = Solution()
    start = datetime.datetime.now()
    solution.generateTrees(n)
    end = datetime.datetime.now()
    print(end - start)

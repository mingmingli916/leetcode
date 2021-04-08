# coding=utf8
"""
@project: leetcode
@file: 20210206_pascal_triangle_ii
@author: mike
@time: 2021/2/6
 
@function:
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?



Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst = []
        d = {}

        def helper(i, j):
            # base case
            if j == 0 or i == j:
                return 1
            # memorize
            if (i, j) in d:
                return d[(i, j)]
            d[(i, j)] = helper(i - 1, j - 1) + helper(i - 1, j)
            return d[(i, j)]

        for i in range(rowIndex + 1):
            lst.append(helper(rowIndex, i))
        return lst


class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex + 1):
            ans.append(ans[-1] * (rowIndex - i + 1) // i)
        return ans

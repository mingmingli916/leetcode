#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210305_pascal_triangle
@author: mike
@time: 2021/3/5
 
@function:
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        for i in range(2, numRows):
            lst = []
            last_lst = result[-1]
            for i in range(len(last_lst) - 1):
                lst.append(last_lst[i] + last_lst[i + 1])
            lst.insert(0, 1)
            lst.append(1)
            result.append(lst)

        return result


if __name__ == '__main__':
    solution = Solution()

    numRows = 5
    expect = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    result = solution.generate(numRows)
    print(result == expect)
    print(result)

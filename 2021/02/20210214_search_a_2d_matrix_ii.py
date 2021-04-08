#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210214_search_a_2d_matrix_ii
@author: mike
@time: 2021/2/14
 
@function:
Write an efficient algorithm that searches for a target value in an m x n integer matrix.
The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""
from typing import List
import bisect
import numpy as np


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = np.array(matrix)

        # Base case
        m = len(matrix)
        if m == 0:
            return False
        if m == 1:
            return target in matrix[0]
        n = len(matrix[0])
        if n == 0:
            return False
        if n == 1:
            return target in matrix[:, 0]

        mid_column = n // 2
        frontier = bisect.bisect_left(matrix[:, mid_column], target)
        if frontier == m:
            frontier = m - 1
        if target in matrix[frontier] or target in matrix[:, mid_column]:
            return True

        if frontier == m - 1 or mid_column == 0:
            bottom_left = []
        else:
            bottom_left = matrix[frontier + 1:, :mid_column]
        if frontier == 0 or mid_column == n - 1:
            top_right = []
        else:
            top_right = matrix[:frontier, mid_column + 1:]
        return (self.searchMatrix(bottom_left, target) or
                self.searchMatrix(top_right, target))

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            if matrix[row][col] < target:
                row += 1
        return False


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 100
    matrix = [[1, 4], [2, 5]]
    target = 2
    matrix = [[-1, 1]]
    target = 3

    result = solution.searchMatrix2(matrix, target)
    print(result)

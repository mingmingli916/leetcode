# coding=utf8
"""
@project: leetcode
@file: 20210203_01_matrix
@author: mike
@time: 2021/2/2
 
@function:
"""
'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''
from typing import List
import collections


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # base case
        if not matrix or not matrix[0]:
            return matrix

        # init
        columns = len(matrix)
        rows = len(matrix[0])
        queue = collections.deque()
        visited = set()
        for column in range(columns):
            for row in range(rows):
                if matrix[column][row] == 0:
                    queue.append((column, row))
                    visited.add((column, row))

        # BFS
        distance = 0
        while queue:
            distance += 1
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for c, r in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nc = cur[0] + c
                    nr = cur[1] + r
                    if 0 <= nc <= columns - 1 and 0 <= nr <= rows - 1 and (nc, nr) not in visited:
                        matrix[nc][nr] = distance
                        visited.add((nc, nr))
                        queue.append((nc, nr))

        return matrix


if __name__ == '__main__':
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [0, 0, 0]]
    matrix = [[0, 0, 0],
              [0, 1, 0],
              [1, 1, 1]]
    solution = Solution()
    solution.updateMatrix(matrix)
    print(matrix)

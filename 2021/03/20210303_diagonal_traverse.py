#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210303_diagonal_traverse
@author: mike
@time: 2021/3/3
 
@function:
Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

The total number of elements of the given matrix will not exceed 10,000.
"""
from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        dictionary = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dictionary[i + j].append(matrix[i][j])
        print(dictionary)

        maximum = len(dictionary)
        result = []
        for i in range(maximum):
            if i % 2 == 0:
                result.extend(list(reversed(dictionary[i])))
            else:
                result.extend(dictionary[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = solution.findDiagonalOrder(matrix)
    print(result)

# Two manners to solve the problem:
# 1. based on the procedure
# 2. based on overview properties

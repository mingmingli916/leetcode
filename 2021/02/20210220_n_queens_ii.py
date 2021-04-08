#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210220_n_queens_ii
@author: mike
@time: 2021/2/20
 
@function:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.



Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        placed = []

        def backtrack_nqueen(row, count):
            nonlocal n
            nonlocal placed
            for col in range(n):
                if is_not_under_attack(row, col):
                    placed.append((row, col))
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack_nqueen(row + 1, count)
                    placed.remove((row, col))
            return count

        def is_not_under_attack(row, col):
            nonlocal placed
            for r, c in placed:
                if r == row or c == col or abs(r - row) == abs(c - col):
                    return False
            return True

        return backtrack_nqueen(0, 0)


if __name__ == '__main__':
    solution = Solution()

    for i in range(1, 10):
        print(i, solution.totalNQueens(i))
    # n = solution.totalNQueens(4)
    # print(n)

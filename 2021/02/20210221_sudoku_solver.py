#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210221_sudoku_solver
@author: mike
@time: 2021/2/21
 
@function:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.



Example 1:


Input: board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
Output: [
["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:




Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        unknown = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    unknown.append((i, j))

        def backtrack():
            if find_solution():
                return True
            x, y = unknown[-1]

            for candidate in '123456789':
                if is_valid(x, y, candidate):
                    place(x, y, candidate)
                    if backtrack():
                        return True
                    remove(x, y)
            return False

        def find_solution():
            if not unknown:
                return True
            return False

        def is_valid(x, y, candidate):
            # row
            for i in range(len(board[x])):
                if board[i][y] == candidate:
                    return False
            # col
            for j in range(len(board)):
                if board[x][j] == candidate:
                    return False
            # square
            x = x // 3 * 3
            y = y // 3 * 3
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] == candidate:
                        return False
            return True

        def place(x, y, candidate):
            board[x][y] = candidate
            unknown.remove((x, y))

        def remove(x, y):
            unknown.append((x, y))
            board[x][y] = '.'

        backtrack()


if __name__ == '__main__':
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
              ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
              ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
              ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
              ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    solution.solveSudoku(board)
    print(result == board)
    for i in range(len(board)):
        print(board[i])
        print(result[i])
        print(board[i] == result[i])
        print('-' * 100)

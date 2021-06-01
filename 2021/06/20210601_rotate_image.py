"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]


Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

"""
from typing import List


class Solution:
    """
    Suppose the point to rotate round is (x0, y0).
    The point to rotate is (x, y).
    The angle is ß.
    The target point is (x', y').

    x' = x0 + (x - x0)·cosß - (y - y0)·sinß
    y' = y0 + (y - y0)·cosß + (x - x0)·sinß

    In this situation, ß is -90˚, so
    x' = x0 + (y - y0)
    y' = y0 - (x - x0)
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        x0 = (rows - 1) / 2
        y0 = (cols - 1) / 2

        for x in range(cols // 2 + 1):
            for y in range(x, cols - x - 1):
                tmp = matrix[x][y]
                tmp_x, tmp_y = x, y
                for _ in range(4):
                    target_x = int(x0 + tmp_y - y0)
                    target_y = int(y0 - tmp_x + x0)
                    matrix[target_x][target_y], tmp = tmp, matrix[target_x][target_y]
                    tmp_x, tmp_y = target_x, target_y


class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    for i in matrix:
        print(i)
    print('=' * 10)

    solution.rotate(matrix)

    for i in expected:
        print(i)
    print('=' * 10)
    for i in matrix:
        print(i)

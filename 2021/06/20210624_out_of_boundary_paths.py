"""
There is an m x n grid with a ball.
The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent four cells in the grid
(possibly out of the grid crossing the grid boundary).
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn,
return the number of paths to move the ball out of the grid boundary.
Since the answer can be very large, return it modulo 10^9 + 7.



Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6


Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12


Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow <= m
0 <= startColumn <= n

Hide Hint #1
WIll traversing every path is fesaible?
There are many possible paths for a small matrix.
Try to optimize it.

Hide Hint #2
Can we use some space to store the number of paths and updating them after every move?

Hide Hint #3
One obvious thing: ball will go out of boundary only by crossing it.
Also, there is only one possible way ball can go out of boundary from boundary cell except corner cells.
From corner cell ball can go out in two different ways.
Can you use this thing to solve the problem?
"""
import numpy as np


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = np.zeros((maxMove + 1, m, n), dtype=int)

        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    up = 1 if i == 0 else dp[k - 1][i - 1][j]
                    down = 1 if i == m - 1 else dp[k - 1][i + 1][j]
                    left = 1 if j == 0 else dp[k - 1][i][j - 1]
                    right = 1 if j == n - 1 else dp[k - 1][i][j + 1]
                    dp[k][i][j] = (up + down + left + right) % (10 ** 9 + 7)
        return dp[maxMove][startRow][startColumn]


if __name__ == '__main__':
    solution = Solution()

    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0

    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1

    ans = solution.findPaths(m, n, maxMove, startRow, startColumn)
    print(ans)

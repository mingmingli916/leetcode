# coding=utf8
"""
@project: leetcode
@file: 20210120_perfect_squares
@author: mike
@time: 2021/1/20
 
@function:
"""
"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
"""

import collections
import math


class Solution:
    def numSquares(self, n: int) -> int:
        queue = collections.deque()
        step = 0
        queue.append(n)

        while queue:
            step += 1
            size = len(queue)
            # iterate all the squares as one step loop
            for _ in range(size):
                square = 1
                num = queue.popleft()
                # account for all the sub squares
                while square ** 2 <= num:
                    dif = num - square ** 2
                    if dif == 0:
                        return step
                    queue.append(dif)
                    square += 1
        return step


class Solution2:
    def numSquares(self, n: int) -> int:
        root = int(math.sqrt(n))
        if root * root == n:
            return 1

        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        root = int(math.sqrt(n))
        for i in range(1, root + 1):
            dif = n - i * i
            tmp = int(math.sqrt(dif))
            if tmp * tmp == dif:
                return 2
        return 3


if __name__ == '__main__':
    n = 20
    sol = Solution2()
    result = sol.numSquares(n)
    print(result)

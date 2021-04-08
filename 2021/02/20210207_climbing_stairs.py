#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210207_climbing_stairs
@author: mike
@time: 2021/2/7
 
@function:

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(n):
            if n in cache:
                return cache[n]
            if n < 3:
                result = n
            else:
                result = helper(n - 1) + helper(n - 2)
            cache[n] = result
            return result

        return helper(n)

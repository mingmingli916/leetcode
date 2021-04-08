#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210224_generate_parentheses
@author: mike
@time: 2021/2/24
 
@function:
Generate Parentheses

Solution
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        num_open = num_close = 0

        def backtrack(cur, num_open, num_close):
            if num_close == n:
                result.append(cur)
                return
            if num_open < n:
                backtrack(cur + '(', num_open + 1, num_close)
            if num_close < num_open:
                backtrack(cur + ')', num_open, num_close + 1)

        backtrack('', num_open, num_close)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.generateParenthesis(3)
    print(result)

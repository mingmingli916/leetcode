# coding=utf8
"""
@project: leetcode
@file: 20210122_valid_parentheses
@author: mike
@time: 2021/1/22
 
@function:
"""
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        se = {'(', '[', '{'}

        for c in s:
            if c in se:
                stack.append(c)
            else:
                if not stack or stack[-1] != d[c]:
                    return False
                stack.pop()

        return not stack


if __name__ == '__main__':
    s = '()'
    sol = Solution()
    result = sol.isValid(s)
    print(result)

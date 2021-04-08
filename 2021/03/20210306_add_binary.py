#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210306_add_binary
@author: mike
@time: 2021/3/6
 
@function:
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        min_len = min(len(a), len(b))
        carry = 0

        for i in range(-1, -min_len - 1, -1):
            digit = int(a[i]) + int(b[i]) + carry
            carry = digit // 2
            digit = digit % 2
            answer.append(str(digit))

        if len(a) > len(b):
            c = a[:-min_len]
        else:
            c = b[:-min_len]

        for i in range(-1, -len(c) - 1, -1):
            digit = int(c[i]) + carry
            carry = digit // 2
            digit = digit % 2
            answer.append(str(digit))

        if carry:
            answer.append(str(carry))

        return ''.join(answer[::-1])


if __name__ == '__main__':
    solution = Solution()

    a = "11"
    b = "1"

    a = "1010"
    b = "1011"

    answer = solution.addBinary(a, b)
    print(answer)

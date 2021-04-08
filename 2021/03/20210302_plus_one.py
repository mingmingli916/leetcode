#!/usr/bin/env python3
"""
@project: leetcode
@file: plus_one
@author: mike
@time: 2021/3/2
 
@function:
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed_digits = list(reversed(digits))
        digit = reversed_digits[0] + 1
        carry = digit // 10
        reversed_digits[0] = digit % 10

        cur = 1
        while carry and cur < len(reversed_digits):
            digit = reversed_digits[cur] + carry
            carry = digit // 10
            reversed_digits[cur] = digit % 10
            cur += 1

        if carry:
            reversed_digits.append(1)

        return list(reversed(reversed_digits))


if __name__ == '__main__':
    solution = Solution()
    digits = [1, 2, 3]
    digits = [9, 9]
    result = solution.plusOne(digits)
    print(result)

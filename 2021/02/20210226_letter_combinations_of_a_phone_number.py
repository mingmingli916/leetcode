#!/usr/bin/env python3
"""
@project: leetcode
@file: 2021_letter_combinations_of_a_phone_number
@author: mike
@time: 2021/2/26
 
@function:
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

2=abc
3=def
4=ghi
5=jkl
6=mno
7=pqrs
8=tuv
9=wxyz


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        directory = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        anses = []

        def backtrack(ans, digits):
            # Basec case
            if digits == '':
                anses.append(ans)
                return

            digit = digits[0]
            for c in directory[digit]:
                backtrack(ans + c, digits[1:])

        backtrack('', digits)
        return anses


if __name__ == '__main__':
    solution = Solution()

    digits = ''

    result = solution.letterCombinations(digits)
    print(result)

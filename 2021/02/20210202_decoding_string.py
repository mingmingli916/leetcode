# coding=utf8
"""
@project: leetcode
@file: 20210202_decoding_string
@author: mike
@time: 2021/2/1
 
@function:
"""
'''
Decode String

Solution
Given an encoded string, return its decoded string.

The encoding rule is: 
k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and 
that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

import string


class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s, li):
            # li imitate pointer
            res = ''
            length = len(s)
            while li[0] < length and s[li[0]] != ']':
                if not s[li[0]].isdigit():
                    res += s[li[0]]
                    li[0] += 1
                else:
                    num = 0
                    while li[0] < length and s[li[0]].isdigit():
                        num = num * 10 + int(s[li[0]])
                        li[0] += 1
                    li[0] += 1  # skip '['
                    tmp = helper(s, li)
                    li[0] += 1  # skip ']'

                    res += tmp * num

            return res

        return helper(s, [0])


if __name__ == '__main__':
    s = '3[a2[c]]'
    s = "3[a]2[bc]"

    solution = Solution()
    result = solution.decodeString(s)
    print(result)

# coding=utf8
"""
@project: leetcode
@file: 20210204_reverse_string
@author: mike
@time: 2021/2/4


Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Hide Hint #1  
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(s, start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]  # swap
            helper(s, start + 1, end - 1)

        helper(s, 0, len(s) - 1)


if __name__ == '__main__':
    s = list('ab')
    print(s)
    solution = Solution()
    solution.reverseString(s)
    print(s)

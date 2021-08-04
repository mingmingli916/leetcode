#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210306_longest_common_prefix
@author: mike
@time: 2021/3/6
 
@function:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

from typing import List


class ExceedError(Exception):
    pass


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        shortest = '?' * 201
        for i in strs:
            if len(i) < len(shortest):
                shortest = i

        i = 0
        try:
            while i < len(shortest):
                lcp = shortest[:i + 1]
                for j in strs:
                    if not j.startswith(lcp):
                        raise ExceedError()
                i += 1
        except ExceedError:
            return shortest[:i]

        return shortest[:i + 1]


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        shortest = min(strs, key=lambda i: len(i))

        i = 0
        while i < len(shortest):
            lcp = shortest[:i + 1]
            for j in strs:
                if not j.startswith(lcp):
                    return shortest[:i]
            i += 1

        return shortest


if __name__ == '__main__':
    solution = Solution2()

    strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    strs = ["c", "cracecar", "car"]

    result = solution.longestCommonPrefix(strs)
    print(result)

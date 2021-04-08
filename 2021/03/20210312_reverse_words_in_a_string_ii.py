#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210312_reverse_words_in_a_string_ii
@author: mike
@time: 2021/3/12
 
@function:
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"


Constraints:

1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        return ' '.join(s_list)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"

    solution = Solution()

    s = solution.reverseWords(s)
    print(s)

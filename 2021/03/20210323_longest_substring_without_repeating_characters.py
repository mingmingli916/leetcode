"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        i = 0
        maximum = 0

        while i < len(s):
            if s[i] in d:
                if len(d) > maximum:
                    maximum = len(d)
                i = d[s[i]] + 1
                d = dict()
            else:
                d[s[i]] = i
                i += 1

        if len(d) > maximum:
            maximum = len(d)

        return maximum

    def lengthOfLongestSubstrings(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[char] = i
        return max_length


if __name__ == '__main__':
    solution = Solution()

    s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    # s = ""
    # s = " "
    # s = "dvdf"

    result = solution.lengthOfLongestSubstring(s)
    print(result)

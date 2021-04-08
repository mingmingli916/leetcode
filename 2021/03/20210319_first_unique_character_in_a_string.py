"""
Given a string, find the first non-repeating character in it and return its index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.
"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        default_dict = collections.defaultdict(int)
        for c in s:
            default_dict[c] += 1

        for i, c in enumerate(s):
            if default_dict[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()

    s = 'leetcode'
    s = "loveleetcode"

    result = solution.firstUniqChar(s)
    print(result)

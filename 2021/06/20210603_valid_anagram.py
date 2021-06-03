"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        if len(counter_s.keys()) != len(counter_t.keys()):
            return False
        for k in counter_s:
            if counter_s[k] != counter_t[k]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()

    s = "anagram"
    t = "nagaram"

    ans = solution.isAnagram(s, t)
    print(ans)

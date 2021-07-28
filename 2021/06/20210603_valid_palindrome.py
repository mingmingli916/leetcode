"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''.join([c.lower() for c in s if c.isalnum()])
        return self.is_palindrome(alphanumeric)

    def is_palindrome(self, s: str):
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(filter(str.isalnum, s)).lower()
        return clean_s == clean_s[::-1]


if __name__ == '__main__':
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    s = "race a car"

    ans = solution.isPalindrome(s)
    print(ans)

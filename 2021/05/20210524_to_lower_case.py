"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"


Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.

Hide Hint #1
Most languages support lowercase conversion for a string data type. However,
that is certainly not the purpose of the problem.
Think about how the implementation of the lowercase function call can be done easily.

Hide Hint #2
Think ASCII!

Hide Hint #3
Think about the different capital letters and their ASCII codes and how that relates to their lowercase counterparts.
Does there seem to be any pattern there? Any mathematical relationship that we can use?

"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for c in s:
            if c < 'A' or c > 'Z':
                ans.append(c)
            else:
                ans.append(chr(ord(c) + 32))

        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution()
    s = "LOVELY&"
    ans = solution.toLowerCase(s)
    print(ans)

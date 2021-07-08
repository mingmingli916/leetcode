"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false


Constraints:

-2^31 <= n <= 2^31 - 1


Follow up: Could you solve it without loops/recursion?
"""

s = {1, 3, 9, 2187, 27, 6561, 59049, 43046721, 129140163, 387420489, 81, 1594323, 729, 19683, 14348907, 531441, 243,
     4782969, 177147}


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n in s

"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-2^31 <= x <= 2^31 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        x_lst = list(str(x))
        if x_lst[0] == '-':
            nums = x_lst[1:]
            nums.reverse()
            x_lst = ['-'] + nums
        else:
            x_lst.reverse()
        reversed_x = int(''.join(x_lst))
        if reversed_x > 2 ** 31 - 1 or reversed_x < -2 ** 31:
            return 0
        return reversed_x


class Solution2:
    def reverse(self, x: int) -> int:
        strx = str(x)

        if x >= 0:
            revstrx = int(strx[::-1])

        else:
            temp = strx[1:]
            revstrx = int(temp[::-1])
            revstrx = -1 * revstrx

        if revstrx >= 2 ** 31 - 1 or revstrx <= -2 ** 31:
            return 0
        else:
            return revstrx


if __name__ == '__main__':
    solution = Solution()
    # x = -123
    x = -321
    ans = solution.reverse(x)
    print(ans)

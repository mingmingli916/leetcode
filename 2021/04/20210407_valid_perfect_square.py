"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Base case.
        if num == 1:
            return True

        left, right = 1, num
        while right - left > 1:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid
            else:
                right = mid
        return False


if __name__ == '__main__':
    solution = Solution()
    ans = solution.isPerfectSquare(10000)
    print(ans)

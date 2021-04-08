#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210208_pow_n
@author: mike
@time: 2021/2/8
 
@function:
Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^(-2) = (1/2)^2 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        # how to divide
        result = self.myPow(x, n // 2)
        return result * result * (x if n % 2 else 1)


if __name__ == '__main__':
    solution = Solution()

    # for x, n in ((2.0, 10), (2.1, 3), (2, -2), (0.00001, 2147483647), (-2.0, 2)):
    #     print(solution.myPow(x, n))
    # result = solution.myPow(-2.0, 2)
    # result = solution.myPow(2., 10)
    result = solution.myPow(0.99999, 948688)
    print(result)

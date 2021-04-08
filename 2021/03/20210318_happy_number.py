"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 2^31 - 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Algorithm:
            Compute the square of the nums in n and sum them up to get square_sum.
            If square_sum == 1, return True.
            If square_sum is in check set, this square_sum will result in loop, so return False.
            If square_sum not in check set, recursively call isHappy.
        """
        def helper(n, check):
            ss = self.square_sum(n)
            if ss == 1:
                return True
            if ss in check:
                return False
            check.add(n)
            return helper(ss, check)

        check = set()
        return helper(n, check)

    def square_sum(self, n: int) -> int:
        answer = 0
        while n != 0:
            remainder = n % 10
            answer += remainder ** 2
            n = n // 10
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))
    print(solution.square_sum(100))

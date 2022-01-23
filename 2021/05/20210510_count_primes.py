"""
Count the number of prime numbers less than a non-negative number, n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0


Constraints:

0 <= n <= 5 * 10^6
"""

import math


class Solution1:
    """
    Time complexity: O(n^2)
    """

    def countPrimes(self, n: int) -> int:
        lst = []
        for i in range(2, n):
            if self.is_prime(i):
                lst.append(i)

        return len(lst)

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False

        for i in range(2, n - 1):
            if n % i == 0:
                return False

        return True


class Solution2:
    def countPrimes(self, n: int) -> int:
        lst = []
        for i in range(2, n):
            if self.is_prime(i):
                lst.append(i)
        return len(lst)

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False

        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True


class Solution3:
    def countPrimes(self, n: int) -> int:
        lst = []
        for i in range(2, n):
            if self.is_prime(i):
                lst.append(i)
        return len(lst)

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False

        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


class Solution4:
    def countPrimes(self, n: int) -> int:
        set_ = set(range(2, n))
        i = 2
        while i * i < n:
            if not self.is_prime(i):
                i += 1
                continue

            j = i * i
            while j < n:
                if j in set_:
                    set_.remove(j)
                j += i
            i += 1
        return len(set_)

    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False

        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


class Solution5:
    def countPrimes(self, n: int) -> int:
        lst = [False] * n
        for i in range(2, n):
            lst[i] = True
        i = 2
        while i * i < n:
            if not lst[i]:
                continue
            j = i * i
            while j < n:
                lst[j] = False
                j += i

            i += 1
        count = 0
        i = 2
        while i < n:
            if lst[i]:
                count += 1
            i += 1
        return count


if __name__ == '__main__':
    solution = Solution5()
    res = solution.countPrimes(1000)
    print(res)

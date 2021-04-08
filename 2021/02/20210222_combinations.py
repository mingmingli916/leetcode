#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210222_combinations
@author: mike
@time: 2021/2/22
 
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n_lst = []
        for i in range(1, n + 1):
            n_lst.append(i)
        result = []

        def backtrack(start, depth, cur, result):
            # find the solution
            if depth == k:  # end condition
                result.append(cur[::])
                return

            # iterate all possible candidates
            for i in range(start, n):
                # generate the next solution from cur
                cur.append(n_lst[i])
                # move to the next solution
                backtrack(i + 1, depth + 1, cur, result)

                # backtrack to previous partial state
                cur.pop()

        backtrack(0, 0, [], result)
        return result

    def combine2(self, n: int, k: int) -> List[List[int]]:
        inp = [i + 1 for i in range(n)]
        print(inp)
        ans = list(combinations(inp, k))
        return ans


def C_n_k(a, n, k, start, depth, curr, ans):
    # find the solution
    if depth == k:  # end condition
        ans.append(curr[::])
        return

    # iterate all possible candidates
    for i in range(start, n):
        # generate the next solution from curr
        curr.append(a[i])
        # move to the next solution
        C_n_k(a, n, k, i + 1, depth + 1, curr, ans)

        # backtrack to previous partial state
        curr.pop()
    return


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    n = len(a)
    k = 2
    ans = []
    C_n_k(a, n, k, 0, 0, [], ans)
    print(ans)

    print('=' * 100)
    solution = Solution()
    result = solution.combine(4, 2)
    print(result)

    result = solution.combine2(4, 2)
    print(result)

"""
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from typing import List
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        ab_map = collections.defaultdict(int)
        for a in A:
            for b in B:
                ab_map[a + b] += 1
        for c in C:
            for d in D:
                ans += ab_map[-c - d]
        return ans


if __name__ == '__main__':
    solution = Solution()

    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]

    result = solution.fourSumCount(A, B, C, D)
    print(result)

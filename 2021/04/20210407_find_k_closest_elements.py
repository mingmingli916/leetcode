"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
"""

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = k
        high = len(arr)

        while low < high:
            mid = (low + high) // 2

            if (arr[mid] - x) >= (x - arr[mid - k]):
                high = mid
            else:
                low = mid + 1
        return arr[low - k: high]


if __name__ == '__main__':
    solution = Solution()

    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3

    x = -1

    x = 5

    arr = [1, 1, 2, 2, 3, 3, 4, 4]
    k = 3

    ans = solution.findClosestElements(arr, k, x)
    print(ans)

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6


Follow up: The overall run time complexity should be O(log (m+n)).
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth(nums1, nums2, k):
            # Base case
            if not nums1:
                return nums2[k - 1]
            if not nums2:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])

            i = min(len(nums1), k // 2)
            j = min(len(nums2), k // 2)
            if nums1[i - 1] > nums2[j - 1]:
                return find_kth(nums1, nums2[j:], k - j)
            else:
                return find_kth(nums1[i:], nums2, k - i)
            return 0

        m = len(nums1)
        n = len(nums2)
        return (find_kth(nums1, nums2, (m + n + 1) // 2) + find_kth(nums1, nums2, (m + n + 2) // 2)) / 2


if __name__ == '__main__':
    solution = Solution()

    nums1 = [1, 2]
    nums2 = [3, 4]

    nums1 = [1]
    nums2 = []

    median = solution.findMedianSortedArrays(nums1, nums2)
    print(median)

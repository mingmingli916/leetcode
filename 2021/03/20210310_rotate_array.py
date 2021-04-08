#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210310_rotate_array
@author: mike
@time: 2021/3/10
 
@function:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums.reverse()
        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        for i in range((length - k) // 2):
            nums[k + i], nums[length - 1 - i] = nums[length - 1 - i], nums[k + i]


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # nums = [-1, -100, 3, 99]
    # k = 2
    # nums = [-1]
    # k = 2

    solution.rotate(nums, k)
    print(nums)

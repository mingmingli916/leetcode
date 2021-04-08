#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210309_minimum_size_subarray_sum
@author: mike
@time: 2021/3/9
 
@function:
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which
the sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialization
        length = len(nums)
        sum_ = 0
        minimum = length + 1

        # Two pointers
        start = 0
        end = 0

        while end < length:
            # Keep adding elements
            while sum_ < target and end < length:
                sum_ += nums[end]
                end += 1

            while sum_ >= target and start < length:
                if end - start < minimum:
                    minimum = end - start

                # Remove start element to try smaller length
                sum_ -= nums[start]
                start += 1

        if minimum == length + 1:
            return 0
        return minimum


if __name__ == '__main__':
    solution = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    # target = 4
    # nums = [1, 4, 4]
    # target = 11
    # nums = [1, 1, 1, 1, 1, 1, 1, 1]
    answer = solution.minSubArrayLen(target, nums)
    print(answer)

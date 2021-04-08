#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210212_sort_an_array
@author: mike
@time: 2021/2/12
 
@function:
Given an array of integers nums, sort the array in ascending order.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case
        if len(nums) <= 1:
            return nums

        midpoint = len(nums) // 2
        left_list = self.sortArray(nums[:midpoint])
        right_list = self.sortArray(nums[midpoint:])
        return self.merge(left_list, right_list)

    def merge(self, left_list, right_list):
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])
        return ret

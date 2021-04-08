#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210226_permutations
@author: mike
@time: 2021/2/26
 
@function:
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        indexes = list(range(length))
        result = []

        def backtrack(permutation, indexes):
            # Base case
            if len(permutation) == length:
                result.append(permutation)
                return
            for i in indexes:
                indexes_copy = indexes[:]
                permutation_copy = permutation[:]
                indexes_copy.remove(i)
                permutation_copy.append(nums[i])
                backtrack(permutation_copy, indexes_copy)

        backtrack([], indexes)
        return result


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3]

    result = solution.permute(nums)
    print(result)

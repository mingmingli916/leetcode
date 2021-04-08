# coding=utf8
"""
@project: leetcode
@file: 20210127_target_sum
@author: mike
@time: 2021/1/27
 
@function:
"""
"""
Target Sum

Solution
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. 
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
from typing import List
import numpy as np


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        count = 0

        def helper(nums, S):
            nonlocal count
            if len(nums) > 1:
                helper(nums[1:], S + nums[0])
                helper(nums[1:], S - nums[0])
            else:
                if nums[0] == S:
                    count += 1
                if nums[0] == -S:
                    count += 1

        helper(nums, S)
        return count


class Solution2:
    # todo
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)  # sum
        # all of nums's elements is non-negative
        # if S is greater than s
        # the target can be reached
        if S < -s or S > s:
            return 0

        dp = np.zeros((len(nums) + 1, s * 2 + 1), dtype=int)
        dp[0][s] = 1
        for i in range(1, len(nums) + 1):
            for j in range(s * 2 + 1):
                if j + nums[i - 1] < s * 2 + 1:
                    dp[i][j] = dp[i][j] + dp[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][s + S]


class Solution3:
    # todo
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if s < S or (s + S) % 2:
            return 0
        a = (s + S) // 2
        dp = [0] * (a + 1)
        dp[0] = 1
        for n in nums:
            for i in range(a, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[-1]


if __name__ == '__main__':
    nums = [35, 25, 24, 23, 2, 47, 39, 22, 3, 7, 11, 26, 6, 30, 5, 34, 10, 43, 41, 28]
    S = 49
    s = Solution3()
    count = s.findTargetSumWays(nums, S)
    print(count)

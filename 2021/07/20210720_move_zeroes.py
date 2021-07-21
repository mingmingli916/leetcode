"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer] = nums[i]
                pointer += 1

        nums[pointer:] = [0] * (len(nums) - pointer)


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    nums = [0]
    s.moveZeroes(nums)
    print(nums)

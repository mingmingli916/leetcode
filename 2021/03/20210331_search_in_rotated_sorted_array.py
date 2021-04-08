"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function,
nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4


Follow up: Can you achieve this in O(log n) time complexity?
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        left_ans = self.binary_search(nums[:pivot + 1], target)
        right_ans = self.binary_search(nums[pivot + 1:], target)
        if left_ans > -1:
            return left_ans
        if right_ans > -1:
            return pivot + right_ans + 1
        return -1

    def find_pivot(self, nums):
        left, right = 0, len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        return left

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [5, 6, 7, 0, 1, 2, 3]
    target = 0
    # pivot = solution.find_pivot(nums)
    # print(pivot)
    ans = solution.search(nums, target)
    print(ans)

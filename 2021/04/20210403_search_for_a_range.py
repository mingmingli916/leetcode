"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            if not nums:
                return -1
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if nums[left] != target:
                return -1
            else:
                return left

        left_bound = find_left()
        if left_bound == -1:
            return [-1, -1]

        def find_right():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return right

        right_bound = find_right()
        return [left_bound, right_bound]


if __name__ == '__main__':
    solution = Solution()

    nums = []
    target = 0

    nums = [1]
    target = 2

    nums = [2, 2, 2]
    target = 3

    nums = [5, 7, 7, 8, 8, 10]
    target = 9

    ans = solution.searchRange(nums, target)
    print(ans)

# Don't be restricted by the template.
# At first, I want to solve the problem in one binary search.
# It takes me a long time to solve it like that manner.
# At last, I divide the problem and solve it with two binary search.

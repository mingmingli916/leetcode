"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 10^4
-9999 <= nums[i], target <= 9999
All the integers in nums are unique.
nums is sorted in an ascending order.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int):
        def helper(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return helper(mid + 1, right)
            else:
                return helper(left, mid - 1)

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    nums = [1]
    target = 1

    answer = solution.search(nums, target)
    print(answer)

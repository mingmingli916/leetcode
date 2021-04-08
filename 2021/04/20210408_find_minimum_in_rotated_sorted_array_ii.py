"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.



Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.


Follow up:
This is the same as Find Minimum in Rotated Sorted Array but with duplicates.
Would allow duplicates affect the run-time complexity?
How and why?
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(left, right):
            if left >= right:
                return nums[left]

            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                return helper(left, mid)
            elif nums[mid] > nums[right]:
                return helper(mid + 1, right)
            else:
                return min(helper(left, mid), helper(mid + 1, right))

        return helper(0, len(nums) - 1)

    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[right]


if __name__ == '__main__':
    solution = Solution()

    nums = [3, 3, 1, 3]
    nums = [1, 3, 5]
    nums = [2, 2, 2, 0, 1]
    nums = [3, 1, 3, 3]

    ans = solution.findMin(nums)
    print(ans)

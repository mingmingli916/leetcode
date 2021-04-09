"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1


Constraints:

2 <= n <= 3 * 10^4
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return right


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 3, 4, 2, 2]
    nums = [3, 1, 3, 4, 2]

    ans = solution.findDuplicate(nums)
    print(ans)

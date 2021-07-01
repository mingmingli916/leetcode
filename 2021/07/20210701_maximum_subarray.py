"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5


Follow up:
If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.

"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_cross_subarray(low, mid, high):
            left_sum = right_sum = -float('inf')
            sum_ = 0
            for i in range(mid, low - 1, -1):
                sum_ += nums[i]
                if sum_ > left_sum:
                    left_sum = sum_
            sum_ = 0
            for i in range(mid + 1, high + 1):
                sum_ += nums[i]
                if sum_ > right_sum:
                    right_sum = sum_
            return left_sum + right_sum

        def max_sum_subarray(low, high):
            if low == high:
                return nums[high]

            mid = (low + high) // 2
            left_sum = max_sum_subarray(low, mid)
            right_sum = max_sum_subarray(mid + 1, high)
            mid_sum = max_cross_subarray(low, mid, high)

            return max(left_sum, right_sum, mid_sum)

        return max_sum_subarray(0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6

    ans = solution.maxSubArray(nums)
    print(ans)

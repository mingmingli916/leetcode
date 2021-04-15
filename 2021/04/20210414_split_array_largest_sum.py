"""
Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(mid):
            """
            To check if mid can be maximum subarray sum.

            :param mid:
            :return:
            """
            count = 0
            sum_ = 0
            for i in range(len(nums)):
                if nums[i] > mid:
                    return False
                # Increase sum of current subarray.
                sum_ += nums[i]

                # If the sum is greater than mid, increase count.
                if sum_ > mid:
                    count += 1
                    sum_ = nums[i]
            count += 1

            if count <= m:
                return True
            return False

        start = max(nums)
        end = sum(nums)

        # Store possible maximum subarray sum.
        answer = 0
        while start <= end:
            mid = (start + end) // 2
            # If mid is possible solution.
            if check(mid):
                answer = mid
                end = mid - 1
            else:
                start = mid + 1
        return answer


if __name__ == '__main__':
    solution = Solution()

    nums = [7, 2, 5, 10, 8]
    m = 2

    ans = solution.splitArray(nums, m)
    print(ans)

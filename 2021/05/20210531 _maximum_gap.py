"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.



Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.


Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^9

"""
from typing import List
import math


class Solution1:
    """
    This solution does not meet the requirement.
    The time complexity is O(nlgn).
    """

    def maximumGap(self, nums: List[int]) -> int:
        # Base case.
        if len(nums) <= 1:
            return 0

        nums.sort()
        maximum = 0
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - pre > maximum:
                maximum = nums[i] - pre
            pre = nums[i]
        return maximum


class Solution2:
    """
    As far as I know,
    There are several sort algorithm run in O(n) time,
    but the nums array does not meet the requirement.
    So use one sort algorithm run in O(n) plus an iterative operation does not work.
    (Pigeonhole Principle).
    """

    def maximumGap(self, nums: List[int]) -> int:
        # Base case.
        if len(nums) <= 1:
            return 0

        # Find the maximum and minimum num in nums.
        max_num, min_num = 0, 10 ** 9
        for num in nums:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

        # Divide the interval [min_num, max_num] into n-1 buckets of equal size.
        delta = (max_num - min_num) / (len(nums) - 1)

        # Use min bucket array and max bucket array to store min and max values.
        # Avoiding nested array.
        min_buckets = [max_num] * (len(nums) - 1)
        max_buckets = [min_num] * (len(nums) - 1)

        # Fill the bucket arrays.
        for num in nums:
            if num == min_num or num == max_num:
                continue

            index = math.floor((num - min_num) / delta)
            min_buckets[index] = min(min_buckets[index], num)
            max_buckets[index] = max(max_buckets[index], num)

        # Find the maximum gap.
        prev = min_num
        max_gap = 0
        for i in range(len(min_buckets)):
            # Empty bucket.
            if min_buckets[i] == max_num:
                continue

            max_gap = max(max_gap, min_buckets[i] - prev)
            prev = max_buckets[i]
        max_gap = max(max_gap, max_num - prev)

        return max_gap


if __name__ == '__main__':
    solution = Solution2()
    nums = [3, 6, 9, 1]
    ans = solution.maximumGap(nums)
    print(ans)

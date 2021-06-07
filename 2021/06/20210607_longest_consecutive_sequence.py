"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List
from collections import defaultdict


class Solution:
    """
    使用set来使查找的复杂度为O(1).
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        s = set(nums)
        for num in nums:
            if num not in s:
                continue
            s.remove(num)
            prev = num - 1
            next_ = num + 1
            while prev in s:
                s.remove(prev)
                prev -= 1
            while next_ in s:
                s.remove(next_)
                next_ += 1
            result = max(result, next_ - prev - 1)
        return result


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:
                start = num
                while start in nums:
                    start += 1
                res = max(res, start - num)
        return res


if __name__ == '__main__':
    solution = Solution()

    nums = [100, 4, 200, 1, 3, 2]
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    ans = solution.longestConsecutive(nums)
    print(ans)

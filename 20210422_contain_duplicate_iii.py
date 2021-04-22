"""
Given an integer array nums and two integers k and t,
return true if there are two distinct indices i and j in the array
such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


Constraints:

0 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^4
0 <= t <= 2^31 - 1

Hide Hint #1
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.

Hide Hint #2
Use already existing state to evaluate next state -
Like, a set of k sorted numbers are only needed to be tracked.
When we are processing the next number in array, then we can utilize the existing sorted state and
it is not necessary to sort next overlapping set of k numbers again.

"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) < 2 or k <= 0 or t < 0:
            return False

        width = t + 1
        bucket = dict()

        for i, num in enumerate(nums):
            id = self.get_id(num, width)
            if id in bucket:
                return True
            if id - 1 in bucket and abs(num - bucket[id - 1]) <= t:
                return True
            if id + 1 in bucket and abs(num - bucket[id + 1]) <= t:
                return True
            bucket[id] = num

            if i >= k:  # This ensure the requirement: abs(i - j) <= k
                del bucket[self.get_id(nums[i - k], width)]
        return False

    def get_id(self, num, width) -> int:
        if num >= 0:
            return num // width
        else:
            return num // width - 1


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3, 1]
    k = 3
    t = 0

    nums = [1, 0, 1, 1]
    k = 1
    t = 2

    nums = [1, 5, 9, 12, 13, 15]
    k = 3
    t = 3

    ans = solution.containsNearbyAlmostDuplicate(nums, k, t)
    print(ans)

"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.



Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16


Constraints:

n == nums.length
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Let's consider a possible scenario in which we've decided
        that our target value is x which would take ans number of moves to complete.
        What would happen to ans if we increased x by 1?
        If we did, each element that is below the new x would have to spend another move to get up to x,
        but every element that is above the new x would have to spend one less move to get down to x.

        This means that x should naturally move up if there are more elements above x than below.
        It also means the inverse, that x should move down if there are more elements below x than above.
        The natural outcome of this is that x will settle at a spot
        where there are the same number of elements on either side, which is the median value of nums.
        """
        nums.sort()
        ans = 0
        median = nums[len(nums) // 2]
        for num in nums:
            ans += abs(num - median)
        return ans


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3]
    nums = [1, 10, 2, 9, 100]
    ans = solution.minMoves2(nums)
    print(ans)

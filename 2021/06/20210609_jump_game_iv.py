"""
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0.
In one move, you can jump at most k steps forward without going outside the boundaries of the array.
That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1).
Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.



Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0


Constraints:

 1 <= nums.length, k <= 10^5
-10^4 <= nums[i] <= 10^4

Hide Hint #1
Let dp[i] be "the maximum score to reach the end starting at index i".
The answer for dp[i] is nums[i] + max{dp[i+j]} for 1 <= j <= k.
That gives an O(n*k) solution.

Hide Hint #2
Instead of checking every j for every i,
keep track of the largest dp[i] values in a heap and calculate dp[i] from right to left.
When the largest value in the heap is out of bounds of the current index, remove it and keep checking.
"""
from typing import List
from collections import deque


class Solution:
    """
    When k is large, the time complexity exceed the time list.
    """

    def maxResult(self, nums: List[int], k: int) -> int:
        # Init the dynamic programming cache.
        dp = {len(nums) - 1: nums[len(nums) - 1]}
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = nums[i] + max(dp.values())
            if len(dp) > k:
                del dp[i + k]
        return dp[0]


class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque([n - 1])
        for i in range(n - 2, -1, -1):
            if deq[0] - i > k:
                deq.popleft()
            nums[i] += nums[deq[0]]
            while len(deq) and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
        return nums[0]


if __name__ == '__main__':
    solution = Solution2()

    nums = [1, -1, -2, 4, -7, 3]
    k = 2
    # nums = [10, -5, -2, 4, 0, 3]
    # k = 3
    # nums = [1, -5, -20, 4, -1, 3, -6, -3]
    # k = 2
    nums = [1, -5, -20, 4, -1, 3, -6, -3]
    k = 2

    ans = solution.maxResult(nums, k)
    print(ans)

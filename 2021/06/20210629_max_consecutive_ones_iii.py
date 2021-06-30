"""
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length

   Hide Hint #1
One thing's for sure, we will only flip a zero if it extends an existing window of 1s.
Otherwise, there's no point in doing it, right? Think Sliding Window!
   Hide Hint #2
Since we know this problem can be solved using the sliding window construct,
we might as well focus in that direction for hints.
Basically, in a given window, we can never have > K zeros, right?
   Hide Hint #3
We don't have a fixed size window in this case.
The window size can grow and shrink depending upon the number of zeros we have
(we don't actually have to flip the zeros here!).
   Hide Hint #4
The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.
"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Special case.
        if k == 0 and sum(nums) == 0:
            return 0

        maximum = 0
        zero_in_window = []
        start = 0
        end = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_in_window.append(i)

            if len(zero_in_window) > k:
                if end - start + 1 > maximum:
                    maximum = end - start + 1
                start = zero_in_window[0] + 1
                zero_in_window.pop(0)

            end = i

        if end - start + 1 > maximum:
            maximum = end - start + 1
        return maximum


class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Move right edge to expand sliding window and move left edge when k < 0
        start = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
        return end - start + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]  # 6
    k = 2
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]  # 10
    k = 3
    nums = [1]  # 1
    k = 1
    nums = [0, 0, 0, 0]  # 0
    k = 0
    ans = solution.longestOnes(nums, k)
    print(ans)

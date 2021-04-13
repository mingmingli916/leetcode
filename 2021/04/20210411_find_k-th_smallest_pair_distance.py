"""
Given an integer array, return the k-th smallest distance among all the pairs.
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.

Hide Hint #1
Binary search for the answer. How can you check how many pairs have distance <= X?
"""
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = 0
            start = 0
            # Use window to count the number of distance that is smaller or equal to the mid
            for i in range(length):
                while start < length and nums[i] - nums[start] > mid:
                    start += 1
                count += i - start
            # To locate the distance.
            if count < k:
                left = mid + 1
            else:
                right = mid
        return right

    def smallestDistancePairs2(self, nums: List[int], k: int) -> int:
        nums.sort()


    def Cn2(self, n):
        return n * (n - 1) // 2


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 3, 1]
    k = 3

    ans = solution.smallestDistancePair(nums, k)
    print(ans)

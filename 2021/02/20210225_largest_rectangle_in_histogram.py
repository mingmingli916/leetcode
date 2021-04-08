#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210225_largest_rectangle_in_histogram
@author: mike
@time: 2021/2/25
 
@function:
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10


Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""
from typing import List


class Solution:
    def largestRectangleArea2(self, heights: List[int]) -> int:
        def helper(heights, idx, prev_max):
            # Base case
            if idx == 0:
                return prev_max

            for i in range(idx, -1, -1):
                area = min(heights[i:idx + 1]) * len(heights[i:idx + 1])
                if area > prev_max:
                    prev_max = area

            return helper(heights, idx - 1, prev_max)

        return helper(heights, len(heights) - 1, heights[0])

    # def largestRectangleArea3(self, heights: List[int]) -> int:
    #     if len(heights) == 1:
    #         return heights[0]
    #
    #     mid_index = len(heights) // 2
    #     left_lst = heights[:mid_index]
    #     right_lst = heights[mid_index:]
    #     left_max = self.largestRectangleArea(left_lst)
    #     right_max = self.largestRectangleArea(right_lst)
    #     return self.merge(left_lst, right_lst, left_max, right_max)
    #
    # def merge(self, left_lst, right_lst, left_max, right_max):
    #     cur_max = max(left_max, right_max)
    #     for i in range(len(left_lst) - 1, -1, -1):
    #         for j in range(len(right_lst)):
    #             new_lst = left_lst[i:] + right_lst[:j + 1]
    #             area = min(new_lst) * len(new_lst)
    #             if area > cur_max:
    #                 cur_max = area
    #     return cur_max

    def largestRectangleArea4(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        min_index = self.find_min(heights)
        left_lst = heights[:min_index]
        right_lst = heights[min_index + 1:]
        left_max = self.largestRectangleArea(left_lst)
        right_max = self.largestRectangleArea(right_lst)
        return self.merge(left_lst, right_lst, left_max, right_max, heights[min_index])

    def merge(self, left_lst, right_lst, left_max, right_max, minimum):
        cur_max = max(left_max, right_max)
        new_lst = left_lst + right_lst
        area = minimum * (len(new_lst) + 1)
        return max(area, cur_max)

    def find_min(self, lst):
        minimum = min(lst)
        count = (lst.count(minimum) + 1) // 2
        index = -1
        for i in range(count):
            index = lst.index(minimum, index + 1)
        return index

    def largestRectangleArea_iterate(self, histogram: List[int]) -> int:
        stack = list()
        max_area = 0
        index = 0

        while index < len(histogram):
            if (not stack) or histogram[stack[-1]] <= histogram[index]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(area, max_area)
        while stack:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(area, max_area)
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans


if __name__ == '__main__':
    solution = Solution()

    test_list = [
        [2, 1, 5, 6, 2, 3],
        [2, 4],
        [2, 1, 5, 6, 2, 3, 8, 9, 2, 5, 3, 5, 3],
        [1, 1],
        [1] * 100000
    ]
    for heights in test_list:
        print(solution.largestRectangleArea4(heights))

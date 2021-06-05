"""
Given a rectangular cake with height h and width w, and
two arrays of integers horizontalCuts and verticalCuts where
horizontalCuts[i] is the distance from the top of the rectangular cake
to the ith horizontal cut and similarly,
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position
provided in the arrays horizontalCuts and verticalCuts.
Since the answer can be a huge number, return this modulo 10^9 + 7.



Example 1:



Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts.
After you cut the cake, the green piece of cake has the maximum area.
Example 2:



Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts.
After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9


Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.

Hide Hint #1
Sort the arrays, then compute the maximum difference between
two consecutive elements for horizontal cuts and vertical cuts.
Hide Hint #2
The answer is the product of these maximum values in horizontal cuts and vertical cuts.
"""
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        h_cuts = sorted(horizontalCuts)
        v_cuts = sorted(verticalCuts)
        h_max = 0
        v_max = 0
        for i in range(1, len(h_cuts)):
            distance = h_cuts[i] - h_cuts[i - 1]
            if distance > h_max:
                h_max = distance
        for i in range(1, len(v_cuts)):
            distance = v_cuts[i] - v_cuts[i - 1]
            if distance > v_max:
                v_max = distance

        return h_max * v_max % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()

    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]

    # h = 5
    # w = 4
    # horizontalCuts = [3, 1]
    # verticalCuts = [1]

    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]

    ans = solution.maxArea(h, w, horizontalCuts, verticalCuts)
    print(ans)

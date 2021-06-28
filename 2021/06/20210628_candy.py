"""
There are n children standing in a line.
Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4

"""
from typing import List


class Solution:
    """
    There is a bug in the edge condition.
    I add a set to solve this bug.
    But this solution is ugly.
    This is the wrong solution.
    """

    def candy(self, ratings: List[int]) -> int:
        # Iterate the list, imagine all difference is 1.
        candies = [0] * len(ratings)
        for i in range(1, len(candies)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            elif ratings[i] < ratings[i - 1]:
                candies[i] = candies[i - 1] - 1

        print(candies)

        # Change all the negative candies into at lest 1.
        visited = set()
        while min(candies) < 1:
            i = candies.index(min(candies))
            dif = 1 - candies[i]
            candies[i] += dif
            i_left, i_right = i, i
            visited.add(i)

            while i_left - 1 not in visited and i_left > 0 and candies[i_left - 1] - (candies[i_left] - dif) == 1:
                candies[i_left - 1] += dif
                i_left -= 1
                visited.add(i_left)
            while i_right + 1 not in visited and i_right < len(ratings) - 1 and \
                    candies[i_right + 1] - (candies[i_right] - dif) == 1:
                candies[i_right + 1] += dif
                i_right += 1
                visited.add(i_right)
            print(candies)

        if len(candies) > 2 and candies[-1] < candies[-2]:
            candies[-1] = 1

        return sum(candies)


class Solution2:

    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candies = [1] * length
        for i in range(length - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
        for i in range(length - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
        return sum(candies)


if __name__ == '__main__':
    solution = Solution2()
    ratings = [1, 0, 10, 7, 7, 2, 5]
    ratings = [1, 0, 2]
    ratings = [1, 2, 2]
    ratings = [29, 51, 87, 87, 72, 12]  # 12
    # ratings = [1, 3, 4, 5, 2]  # 11
    # ratings = [5, 1, 1, 1, 10, 2, 1, 1, 1, 3]  # 15
    ans = solution.candy(ratings)
    print(ans)

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

"""
from typing import List


class Solution:
    """
    There is a bug for this input: prices = [2, 1, 2, 1, 0, 1, 2]
    """

    def maxProfit(self, prices: List[int]) -> int:
        # Base case.
        if len(prices) == 1:
            return 0

        diffs = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        print(diffs)

        max_profit = 0
        accu = 0
        for i in diffs:
            if i < 0:
                if max_profit <= 0:
                    continue
                else:
                    accu += i
            else:
                accu += i

            if accu > 0:
                max_profit += accu
                accu = 0
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


if __name__ == '__main__':
    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]
    prices = [2, 1, 2, 1, 0, 1, 2]

    ans = solution.maxProfit(prices)
    print(ans)

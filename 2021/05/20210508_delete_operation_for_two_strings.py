"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.



Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4


Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    """
    The essence is the longest common subsequence.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return l1 + l2 - 2 * dp[l1][l2]

    def minDistance2(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        if l1 < l2:
            word1, word2, l1, l2 = word2, word1, l2, l1
        dp_last, dp_cur = [0] * (l2 + 1), [0] * (l2 + 1)
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp_cur[j + 1] = dp_last[j] + 1
                else:
                    dp_cur[j + 1] = max(dp_cur[j], dp_last[j + 1])
            dp_last, dp_cur = dp_cur, dp_last
        return l1 + l2 - 2 * dp_last[l2]


if __name__ == '__main__':
    solution = Solution()

    word1 = 'sea'
    word2 = 'eat'

    word1 = 'leetcode'
    word2 = 'etco'

    l = solution.minDistance2(word1, word2)
    print(l)

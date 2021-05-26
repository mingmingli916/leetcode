"""
Given an array of strings words, return the smallest string that contains each string in words as a substring.
If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.



Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"


Constraints:

1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List
from functools import lru_cache
from itertools import permutations


class Solution:
    """
    This greedy algorithm is wrong.
    """

    def shortestSuperstring(self, words: List[str]) -> str:
        while len(words) != 1:
            maximum = -1
            cat = ''
            l, r = 0, 0
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    max_tmp, cat_tmp = self.find_overlapping_pair(words[i], words[j])
                    if maximum < max_tmp:
                        maximum = max_tmp
                        cat = cat_tmp
                        l = i
                        r = j
            # There are no overlapping
            if maximum == -1:
                words = [''.join(words)]
                break
            else:
                words.pop(l)
                words.pop(r - 1)
                words.append(cat)
        return words[0]

    def find_overlapping_pair(self, s1: str, s2: str):
        maximum = -1  # Maximum overlapping length.
        cat = ''  # Store the concatenated string.

        # Check if the suffix of `s1` matches with the prefix of `s2`.
        for i in range(1, min(len(s1), len(s2))):
            if s1[:i] == s2[-i:]:
                if maximum < i:
                    maximum = i
                    cat = s2 + s1[i:]

        for i in range(1, min(len(s1), len(s2))):
            if s1[-i:] == s2[:i]:
                if maximum < i:
                    maximum = i
                    cat = s1 + s2[i:]
        return maximum, cat


class Solution2:
    # TODO NP-Hard
    def shortestSuperstring(self, words: List[str]) -> str:
        @lru_cache(None)
        def connect(w1, w2):
            return [w2[i:] for i in range(len(w1) + 1) if w1[-i:] == w2[:i] or not i][-1]

        length = len(words)
        dp = [[(float("inf"), "")] * length for _ in range(1 << length)]
        for i in range(length):
            dp[1 << i][i] = (len(words[i]), words[i])

        for mask in range(1 << length):
            n_z_bits = [i for i in range(length) if mask & 1 << i]

            for i, k in permutations(n_z_bits, 2):
                cand = dp[mask ^ 1 << i][k][1] + connect(words[k], words[i])
                dp[mask][i] = min(dp[mask][i], (len(cand), cand))

        return min(dp[-1])[1]


class Solution3:
    # TODO how?
    def shortestSuperstring(self, words: List[str]) -> str:
        def st(B, ans):
            if len(B) == 0:
                return ans
            if not B[0] in ans:
                return min(st(B[1:], ans + [B[0]]), st(B[1:], [B[0]] + ans), key=lambda x: len(x))
            else:
                return st(B[1:], ans)

        if len(words) == 1:
            return words

        B = sorted(words, key=lambda s: len(s))
        ans = [B[0]]

        return st(B, ans)


if __name__ == '__main__':
    solution = Solution2()
    words = ["alex", "loves", "leetcode"]
    expected = "alexlovesleetcode"
    # words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
    # expected = "gctaagttcatgcatc"
    words = ["abcdef", "efde", "defab"]
    expected = "efdefabcdef"
    ans = solution.shortestSuperstring(words)
    print(ans)
    print(len(ans) == len(expected))

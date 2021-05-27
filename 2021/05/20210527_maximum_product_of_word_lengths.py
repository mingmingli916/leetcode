"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. If no such two words exist, return 0.



Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.

"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = sorted(words, key=len, reverse=True)
        print(words)
        maximum = 0
        for i in range(len(words) - 1):
            for j in range(1, len(words)):
                if not (set(words[i]) & set(words[j])):
                    if maximum < len(words[i]) * len(words[j]):
                        maximum = len(words[i]) * len(words[j])
                    else:
                        break
            if maximum >= len(words[i]) ** 2:
                break
        return maximum


class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        # Number operation is faster
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask_bit = 1 << ord(c) - ord('a')
                mask |= mask_bit
                print(bin(mask))
            d[mask] = max(d.get(mask, 0), len(w))
        return max((d[i] * d[j] for i in d for j in d if i & j == 0), default=0)


if __name__ == '__main__':
    solution = Solution2()

    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    # words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    # words = ["a", "aa", "aaa", "aaaa"]

    ans = solution.maxProduct(words)
    print(ans)

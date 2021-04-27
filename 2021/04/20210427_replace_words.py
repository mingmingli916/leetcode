"""
In English, we have a concept called root, which can be followed by some other word to form another longer word -
let's call this word successor. For example, when the root "an" is followed by the successor word "other",
we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
replace all the successors in the sentence with the root forming it.
If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.



Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
Example 3:

Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"
Example 4:

Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 5:

Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"


Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Each two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""
from typing import List
import collections


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Keep the shorter prefix
        dictionary = sorted(dictionary, key=lambda x: len(x), reverse=True)
        i = 0
        while i < len(dictionary) - 1:
            j = i + 1
            while j < len(dictionary):
                if dictionary[i].startswith(dictionary[j]):
                    del dictionary[i]
                    i -= 1
                    break
                j += 1
            i += 1

        words = sentence.split()
        for i, word in enumerate(words):
            for prefix in dictionary:
                if word.startswith(prefix):
                    words[i] = prefix
                    break

        return ' '.join(words)

    def replaceWords2(self, dictionary: List[str], sentence: str) -> str:
        res = []
        d = collections.defaultdict(list)
        for w in dictionary:
            d[w[0]].append(w)
        for k in d:
            d[k].sort(key=len)

        for word in sentence.split():
            if word[0] in d:
                for dword in d[word[0]]:
                    if word.startswith(dword):
                        word = dword
                        break
            res.append(word)

        return " ".join(res)


if __name__ == '__main__':
    dictionary = ["catt", "cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    expected = "the cat was rat by the bat"

    # dictionary = ["a", "aa", "aaa", "aaaa"]
    # sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    # expected = "a a a a a a a a bbb baba a"

    solution = Solution()
    ans = solution.replaceWords2(dictionary, sentence)
    print(ans)
    print(ans == expected)

"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list,
so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""
from typing import List
import collections


def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-1])


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_end_index = -1
        # Store all words that are palindrome from this node to end of word.
        self.palindromes_below = []


class Trie:
    """
    It is built with each input word in reverse.
    It has index of each word in the input array as the 'end' indicator.

    Suppose we are trying to find all words that can match an input word, A.
    We have two cases:
    1. The matching word is shorter than or the same size as A.
    2. The matching word is longer than A.
    """
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word, index):
        cur = self.root
        for i, c in enumerate(reversed(word)):
            if is_palindrome(word[:len(word) - i]):
                cur.palindromes_below.append(index)
            cur = cur.children[c]
        cur.word_end_index = index

    def get_palindromes_for_word(self, word):
        """
        Takes a word and its index in the word array and return the index
        of every word that could be appended to it to form a palindrome.
        """
        output = []
        cur = self.root
        while word:
            if cur.word_end_index >= 0:
                """
                Any word endings below the current node indicate words of the form: ca ___ ac. 
                So, if any of these have a palindrome in the blank space, 
                then they can be concatenated to “ac” to form a palindrome. 
                We need to search for any word ending below the current node 
                that are palindromes from the current node down.

                Rather than searching for every query, we can create the list of all palindromes below the current node
                as we build the trie (while adding, if the rest of the letters in the word form a palindrome, 
                add it to a list of all “palindromes below this node” stored in the node).
                """
                if is_palindrome(word):
                    output.append(cur.word_end_index)
            if word[0] not in cur.children:
                return output
            cur = cur.children[word[0]]
            word = word[1:]

        if cur.word_end_index >= 0:
            output.append(cur.word_end_index)
        output.extend(cur.palindromes_below)
        return output


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.add_word(word, i)

        output = []
        for i, word in enumerate(words):
            candidates = trie.get_palindromes_for_word(word)
            output.extend([[i, j] for j in candidates if i != j])
        return output


if __name__ == '__main__':
    solution = Solution()

    words = ["abcd", "dcba", "lls", "s", "sssll"]
    words = ["bat", "tab", "cat"]

    output = solution.palindromePairs(words)
    print(output)

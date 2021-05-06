"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.



Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
    words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 10^4
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.

Hide Hint #1
    You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
Hide Hint #2
    If the current candidate does not exist in all words' prefix, you could stop backtracking immediately.
    What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not?
    How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem:
    Implement Trie (Prefix Tree) first.

"""
from typing import List
from functools import lru_cache


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word


class Solution:
    def __init__(self):
        self.res = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])

        @lru_cache(100000)
        def dfs(i: int, j: int, node: TrieNode):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            c = board[i][j]
            if c == '#' or c not in node.children:
                return
            node = node.children[c]
            if node.word is not None:  # found a word
                self.res.append(node.word)
                node.word = None  # remove the duplicate

            board[i][j] = '#'
            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)
            board[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
        return self.res


if __name__ == '__main__':
    board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    words = ["oa", "oaa"]

    # board = [["a", "a"]]
    # words = ["a"]

    solution = Solution()
    res = solution.findWords(board, words)
    print(res)

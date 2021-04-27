"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary()
    Initializes the object.
void addWord(word)
    Adds word to the data structure, it can be matched later.
bool search(word)
    Returns true if there is any string in the data structure that matches word or false otherwise.
    word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""


class TrieNode:
    def __init__(self, children=None, is_word=False):
        self.children = children if children else {}
        self.is_word = is_word


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def helper(node, word):
            cur = node
            for i, c in enumerate(word):
                if c == '.':
                    result = False
                    for child in cur.children.values():
                        child_result = helper(child, word[i + 1:])
                        result = result or child_result
                    return result

                if c not in cur.children:
                    return False
                cur = cur.children[c]

            if cur.is_word is True:
                return True
            else:
                return False

        return helper(self.root, word)


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad") is False)  # return False
    print(wordDictionary.search("bad") is True)  # return True
    print(wordDictionary.search(".ad") is True)  # return True
    print(wordDictionary.search("b..") is True)  # return True

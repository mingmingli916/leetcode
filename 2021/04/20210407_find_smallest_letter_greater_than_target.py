"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        next_letter = self._next_letter(target)
        if next_letter == 'a':
            if letters[0] == 'a':
                return 'a'
            else:
                return self.nextGreatestLetter(letters, 'b')

        if next_letter == 'z':
            if letters[-1] == 'z':
                return 'z'
            else:
                return self.nextGreatestLetter(letters, 'a')

        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == next_letter:
                return next_letter
            elif ord(letters[mid]) < ord(next_letter):
                left = mid + 1
            else:
                right = mid - 1

        return self.nextGreatestLetter(letters, next_letter)

    def _next_letter(self, letter: str):
        if ord(letter) == 122:
            return 'a'
        else:
            return chr(ord(letter) + 1)

    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:
                right = mid - 1

        # `target` is smaller than all letters.
        if left < 0:
            return letters[0]
        # `target` is greater smaller than all letters.
        if right == len(letters) - 1:
            return letters[0]

        return letters[right + 1]


if __name__ == '__main__':
    solution = Solution()

    letters = ["c", "f", "j"]
    target = 'a'  # c
    target = 'c'  # f
    target = 'd'  # f
    target = 'g'  # j
    target = 'j'  # c
    target = 'k'  # c

    ans = solution.nextGreatestLetter(letters, target)
    print(ans)

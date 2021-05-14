"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".
Then, we removed all commas, decimal points, and spaces, and ended up with the string s.
Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes,
so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01",
or any other number that can be represented with less digits.
Also, a decimal point within a number never occurs without at least one digit occuring before it,
so we never started with numbers like ".1".

The final answer list can be returned in any order.
Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: s = "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: s = "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: s = "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.


Note:

4 <= s.length <= 12.
s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.

"""
from typing import List


class Solution:
    """
    This is a wrong solution.
    It can not match the situation:
    s = "(00011)"
    """

    def ambiguousCoordinates(self, s: str) -> List[str]:
        digits = s[1:-1]
        print(digits)

        ans = []
        for i in range(1, len(digits)):
            l = digits[:i]
            r = digits[i:]

            if self.start_with_zero(l) or self.start_with_zero(r):
                continue
            ans.append(f'({l}, {r})')

            if len(l) > 1:
                for j in range(1, len(l)):
                    ll = l[:j]
                    lr = l[j:]
                    if lr.endswith('0'):
                        continue
                    ans.append(f'({ll}.{lr}, {r})')
            if len(r) > 1:
                for j in range(1, len(r)):
                    rl = r[:j]
                    rr = r[j:]
                    if rr.endswith('0'):
                        continue
                    ans.append(f'({l}, {rl}.{rr})')

            if self.start_with_zero(l) or self.start_with_zero(r):
                continue
            ans.append(f'({l}, {r})')
        print(ans)

    def start_with_zero(self, s: str) -> bool:
        if s.startswith('0') and len(s) > 1:
            return True


class Solution2:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        digits = s[1:-1]
        print(digits)

        ans = []
        for i in range(1, len(digits)):
            l = digits[:i]
            r = digits[i:]

            ll = self.generate(l)
            rr = self.generate(r)

            for li in ll:
                for ri in rr:
                    ans.append(f'({li}, {ri})')
        return ans

    def valid_integer(self, s: str) -> bool:
        if s.startswith('0') and len(s) > 1:
            return False
        return True

    def generate(self, s: str) -> List[str]:
        if len(s) <= 1:
            return [s]

        ans = []
        if self.valid_integer(s):
            ans.append(s)

        for i in range(1, len(s)):
            l = s[:i]
            r = s[i:]
            if not self.valid_integer(l) or r.endswith('0'):
                continue
            ans.append(f'{l}.{r}')
        return ans


if __name__ == '__main__':
    solution = Solution2()

    s = "(123)"
    s = "(00011)"
    s = "(0123)"
    s = "(100)"

    ans = solution.ambiguousCoordinates(s)
    print(ans)

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.



Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1


Constraints:

0 <= x, y <= 2^31 - 1
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        z_str = bin(z)[2:]
        count = 0
        for c in z_str:
            if c == '1':
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(4, 1))
    print(s.hammingDistance(3, 1))
    print(s.hammingDistance(0, 0))

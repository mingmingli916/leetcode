"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?



Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127


Constraints:

1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 2^31 - 1
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}

    def __str__(self):
        return str(self.children.keys())


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        word = f'{str(bin(num))[2:]:>031}'
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)

        maximum = ['0']
        self.find_max_pair(self.root, self.root, '', maximum)
        return self.str2num(maximum[0])

    def find_max_pair(self, left_node, right_node, prefix, maximum):
        # Left and right have same length.
        # Base case.
        if len(left_node.children) == 0:
            return

        left_keys = sorted(left_node.children.keys())
        right_keys = sorted(right_node.children.keys(), reverse=True)
        for i in left_keys:
            for j in right_keys:
                if i != j:
                    prefix_buf = prefix + '1'
                else:
                    prefix_buf = prefix + '0'

                current_num = self.str2num(prefix_buf)
                max_num = self.str2num(maximum[0][:len(prefix_buf)])
                if current_num > max_num:
                    maximum[0] = prefix_buf
                    self.find_max_pair(left_node.children[i], right_node.children[j], prefix_buf, maximum)
                elif current_num == max_num:
                    self.find_max_pair(left_node.children[i], right_node.children[j], prefix_buf, maximum)

    # def find_max_pair(self, left_node, right_node, index, mask):
    #     # Left and right have same length.
    #     # Base case.
    #     if len(left_node.children) == 0:
    #         return
    # # There is a bug in this part.
    # # If there is only one child, then is should process on over.
    # # But the higher position is not meet.
    # # It set the lower to True, it produce a logical bug.
    # for i in left_node.children:
    #     for j in right_node.children:
    #         if i != j:
    #             mask[index] = True
    #             self.find_max_pair(left_node.children[i], right_node.children[j], index + 1, mask)
    #
    #         else:
    #             if len(left_node.children) == len(right_node.children) == 1:
    #                 if mask[index] is True:
    #                     return
    #                 else:
    #                     self.find_max_pair(left_node.children[i], right_node.children[j], index + 1, mask)

    def str2num(self, str_):
        return int('0b' + str_, 2)


# There is a bug in this part.
# If there is only one child, then is should process on over.
# But the higher position is not meet.
# It set the lower to True, it produce a logical bug.

if __name__ == '__main__':
    nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]  # 127
    # nums = [3, 10, 5, 25, 2, 8]  # 28
    # nums = [32, 18, 33, 42, 29, 20, 26, 36, 15, 46]  # expected: 62
    # nums = [0]  # 0
    # nums = [12, 86, 52, 58, 13, 63, 64, 18, 40, 73, 44, 94]  # 127
    nums = [89, 102, 183, 233, 175, 87, 497, 350, 348, 191, 136, 497, 166, 420, 279, 212, 269, 125, 262, 74]
    solution = Solution()
    ans = solution.findMaximumXOR(nums)
    print(ans)

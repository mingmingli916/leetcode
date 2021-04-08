#!/usr/bin/env python3
"""
@project: leetcode
@file: 20210315_design_hashset
@author: mike
@time: 2021/3/15
 
@function:
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.


Follow up: Could you solve the problem without using the built-in HashSet library?
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [set() for i in range(10000)]

    def add(self, key: int) -> None:
        self.array[self.hash(key)].add(key)

    def remove(self, key: int) -> None:
        set_ = self.array[self.hash(key)]
        if key in set_:
            set_.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.array[self.hash(key)]

    def hash(self, key: int):
        return key % 10000

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

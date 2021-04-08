"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap(): initializes the object with an empty map.
void put(int key, int value): inserts a (key, value) pair into the HashMap.
    If the key already exists in the map, update the corresponding value.
int get(int key): returns the value to which the specified key is mapped,
    or -1 if this map contains no mapping for the key.
void remove(key): removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.


Follow up: Please do not use the built-in HashMap library.
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.buckets = [-1] * self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.hash(key)
        bucket = self.buckets[idx]
        if bucket == -1:
            self.buckets[idx] = [[key, value]]
            return

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self.buckets[self.hash(key)]
        if bucket == -1:
            return -1

        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.buckets[self.hash(key)]
        if bucket == -1:
            return

        i = 0
        while i < len(bucket):
            if bucket[i][0] == key:
                break

        if i != len(bucket):
            del bucket[i]

    def hash(self, key: int) -> int:
        return key % self.capacity


if __name__ == '__main__':
    myHashMap = MyHashMap();
    myHashMap.put(1, 1)  # The map is now [[1,1]]
    myHashMap.put(2, 2)  # The map is now [[1,1], [2,2]]
    myHashMap.get(1)  # return 1, The map is now [[1,1], [2,2]]
    myHashMap.get(3)  # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    myHashMap.put(2, 1)  # The map is now [[1,1], [2,1]] (i.e., update the existing value)
    myHashMap.get(2)  # return 1, The map is now [[1,1], [2,1]]
    myHashMap.remove(2)  # remove the mapping for 2, The map is now [[1,1]]
    myHashMap.get(2)  # return -1 (i.e., not found), The map is now [[1,1]]

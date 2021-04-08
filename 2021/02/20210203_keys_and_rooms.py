# coding=utf8
"""
@project: leetcode
@file: 20210203_keys_and_rooms
@author: mike
@time: 2021/2/3
 
@function:
"""
"""
There are N rooms and you start in room 0.  
Each room has a distinct number in 0, 1, 2, ..., N-1, and 
each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and 
each key rooms[i][j] is an integer in [0, 1, ..., N-1] 
where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 1 <= rooms.length <= 1000
        # 0 <= rooms[i].length <= 1000
        # There is no need to consider None case

        visited = set()

        def helper(rooms, room, visited):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    helper(rooms, key, visited)

        helper(rooms, 0, visited)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    rooms = [[1], [2], [3], []]
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    solution = Solution()
    result = solution.canVisitAllRooms(rooms)
    print(result)

# coding=utf8
"""
@project: leetcode
@file: 20210117_design_circle_queue
@author: mike
@time: 2021/1/17
 
@function:
"""

"""
Design your implementation of the circular queue. The circular queue 
is a linear data structure in which the operations are performed 
based on FIFO (First In First Out) principle and the last position 
is connected back to the first position to make a circle. It is also 
called "Ring Buffer".

One of the benefits of the circular queue is that we can make use
 of the spaces in front of the queue. In a normal queue, once the 
 queue becomes full, we cannot insert the next element even if there 
 is a space in front of the queue. But using the circular queue, we 
 can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
 

Follow up: Could you solve the problem without using the built-in queue? 
"""


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.head = 0
        self.tail = -1
        self.size = 0
        self.lst = [0] * self.k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False

        self.tail = (self.tail + 1) % self.k
        self.lst[self.tail] = value
        self.size += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return False

        value = self.lst[self.head]
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.lst[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.lst[self.tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.size == self.k:
            return True
        else:
            return False


if __name__ == '__main__':

    # Your MyCircularQueue object will be instantiated and called as such:
    k = 3
    lst = []

    obj = MyCircularQueue(k)

    for i in range(1, 5):
        param_1 = obj.enQueue(i)
        lst.append(param_1)

    param_2 = obj.Rear()
    lst.append(param_2)
    param_3 = obj.isFull()
    lst.append(param_3)
    param_4 = obj.deQueue()
    lst.append(param_4)
    param_5 = obj.enQueue(4)
    lst.append(param_5)
    param_6 = obj.Rear()
    lst.append(param_6)

    print(lst)

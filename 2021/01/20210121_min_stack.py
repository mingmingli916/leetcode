# coding=utf8
"""
@project: leetcode
@file: 20210121_min_stack
@author: mike
@time: 2021/1/21
 
@function:
"""

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # for normal stack operation
        self.stack = []
        # for storing minimum values
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # when x is smaller than minimum
        # push x into min_stack
        if self.min_stack:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        # if x is the minimum
        # remove minimum in min_stack
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
